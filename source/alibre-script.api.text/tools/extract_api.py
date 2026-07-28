"""Extract a complete Alibre Script API model from the installed Alibre Design.

Joins two sources on the .NET XML documentation ID:

  AlibreScriptAddOn.dll  -> exact return types, property types, parameter
                            names and types (reflection; the only source that
                            has types at all)
  AlibreScriptAPI.xml    -> summaries, per-parameter descriptions, returns
                            prose (the only source that has documentation)

Emits one JSON file that a stub generator can consume without Alibre installed.

Usage:
    python extract_api.py <output.json> [--alibre-root "<Alibre install>\\Program"]

Without --alibre-root the newest installed Alibre Design is used, and the
ALIBRE_PROGRAM_DIR environment variable overrides the search.
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

import clr  # noqa: F401
from System import AppDomain, ResolveEventHandler
from System.Reflection import Assembly, BindingFlags

PUBLIC = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly
API_NS = 'AlibreScript.API.'

PRIMITIVES = {
    'System.Void': 'None',
    'System.String': 'str',
    'System.Double': 'float',
    'System.Single': 'float',
    'System.Int32': 'int',
    'System.Int64': 'int',
    'System.Int16': 'int',
    'System.Boolean': 'bool',
    'System.Byte': 'int',
    'System.Object': 'Any',
    'IronPython.Runtime.List': 'List[Any]',
    'IronPython.Runtime.PythonDictionary': 'Dict[Any, Any]',
    'IronPython.Runtime.PythonTuple': 'Any',
}


def install_resolver(root):
    search = [os.path.join(root, 'Addons', 'AlibreScript'), root]

    def _resolve(sender, args):
        name = args.Name.split(',')[0]
        for d in search:
            for ext in ('.dll', '.exe'):
                cand = os.path.join(d, name + ext)
                if os.path.isfile(cand):
                    try:
                        return Assembly.LoadFrom(cand)
                    except Exception:
                        pass
        return None

    AppDomain.CurrentDomain.AssemblyResolve += ResolveEventHandler(_resolve)


def py_type(t):
    """.NET Type -> the annotation a stub should use."""
    if t is None:
        return 'Any'
    if t.IsByRef:
        t = t.GetElementType()
    if t.IsArray:
        return 'List[%s]' % py_type(t.GetElementType())
    full = t.FullName or t.Name
    full = full.split('[[')[0]
    if full in PRIMITIVES:
        return PRIMITIVES[full]
    if full.startswith(API_NS):
        return full[len(API_NS):].replace('+', '.')
    if t.IsEnum:
        return 'Any'
    return 'Any'


def doc_id_type(t):
    """.NET Type -> the spelling used inside an XML documentation ID."""
    if t is None:
        return ''
    if t.IsByRef:
        t = t.GetElementType()
    if t.IsArray:
        return doc_id_type(t.GetElementType()) + '[]'
    full = t.FullName or t.Name
    return full.split('[[')[0].replace('+', '.')


def member_key(cls, name, params):
    if not params:
        return '%s%s.%s' % (API_NS, cls, name)
    return '%s%s.%s(%s)' % (API_NS, cls, name, ','.join(params))


def clean(node):
    if node is None:
        return ''
    return re.sub(r'\s+', ' ', ''.join(node.itertext())).strip()


def parse_xml(path):
    docs = {}
    if not os.path.isfile(path):
        return docs
    root = ET.parse(path).getroot()
    for m in root.findall('./members/member'):
        raw = m.get('name') or ''
        if len(raw) < 3 or raw[1] != ':':
            continue
        kind, ident = raw[0], raw[2:]
        docs[ident] = {
            'kind': kind,
            'summary': clean(m.find('summary')),
            'returns': clean(m.find('returns')),
            'params': {p.get('name'): clean(p) for p in m.findall('param')},
        }
    return docs


def index_by_name(docs):
    """Group documented members by their un-parenthesised name.

    The assembly exposes overloads the XML never documents (Part.GetPlane takes
    an IADDesignPlane as well as a string, but only the string form is written
    up). Falling back to a sibling overload's summary beats emitting nothing.
    """
    out = {}
    for ident, d in docs.items():
        out.setdefault(ident.split('(')[0], []).append(d)
    return out


def newest_alibre_root():
    override = os.environ.get('ALIBRE_PROGRAM_DIR')
    if override and os.path.isdir(override):
        return override
    base = os.environ.get('ProgramFiles', r'C:\Program Files')
    found = []
    for name in os.listdir(base):
        if not name.upper().startswith('ALIBRE DESIGN') or 'BETA' in name.upper():
            continue
        program = os.path.join(base, name, 'Program')
        if os.path.isfile(os.path.join(program, 'AlibreX.dll')):
            found.append(program)
    return sorted(found)[-1] if found else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('output')
    ap.add_argument('--alibre-root', default=None)
    args = ap.parse_args()

    root = args.alibre_root or newest_alibre_root()
    if not root:
        raise SystemExit('No Alibre Design installation found. Pass --alibre-root.')
    dll = os.path.join(root, 'Addons', 'AlibreScript', 'AlibreScriptAddOn.dll')
    xml = os.path.join(root, 'Addons', 'AlibreScript', 'AlibreScriptAPI.xml')
    if not os.path.isfile(dll):
        sys.exit('Not found: %s' % dll)

    install_resolver(root)
    asm = Assembly.LoadFrom(dll)
    docs = parse_xml(xml)
    docs_by_name = index_by_name(docs)

    try:
        types = [t for t in asm.GetTypes() if t is not None]
    except Exception as exc:
        types = [t for t in getattr(exc, 'Types', []) if t is not None]

    model = {
        'source': {
            'assembly': asm.GetName().Name,
            'assembly_version': str(asm.GetName().Version),
            'xml_members': len(docs),
        },
        'classes': {},
    }
    matched = unmatched = inherited = 0

    for t in sorted(types, key=lambda x: x.FullName or ''):
        full = t.FullName or ''
        if not full.startswith(API_NS):
            continue
        if not (t.IsPublic or t.IsNestedPublic):
            continue
        cls = full[len(API_NS):].replace('+', '.')
        entry = model['classes'].setdefault(
            cls, {'doc': '', 'properties': {}, 'fields': {}, 'methods': {}, 'is_enum': bool(t.IsEnum)}
        )
        entry['doc'] = docs.get(full, {}).get('summary', '')
        entry['documented'] = full in docs

        # Method signatures are written in terms of interfaces (AddSketch takes
        # an ISketchSurface, and Plane implements it). Without these the stub
        # declares both as unrelated classes and every real call fails to check.
        implements = []
        for i in t.GetInterfaces():
            iname = i.FullName or ''
            if iname.startswith(API_NS):
                implements.append(iname[len(API_NS):].replace('+', '.'))
        base = t.BaseType.FullName if t.BaseType else None
        if base and base.startswith(API_NS):
            implements.insert(0, base[len(API_NS):].replace('+', '.'))
        entry['implements'] = sorted(set(implements))

        for p in t.GetProperties(PUBLIC):
            d = docs.get('%s.%s' % (full, p.Name), {})
            entry['properties'][p.Name] = {
                'type': py_type(p.PropertyType),
                'doc': d.get('summary', ''),
                'readonly': not p.CanWrite,
            }

        for f in t.GetFields(PUBLIC):
            d = docs.get('%s.%s' % (full, f.Name), {})
            entry['fields'][f.Name] = {'type': py_type(f.FieldType), 'doc': d.get('summary', '')}

        for m in t.GetMethods(PUBLIC):
            if m.IsSpecialName:
                continue
            prms = list(m.GetParameters())
            key = member_key(cls, m.Name, [doc_id_type(p.ParameterType) for p in prms])
            d = docs.get(key)
            doc_source = 'exact'
            if d:
                matched += 1
            else:
                siblings = docs_by_name.get(key.split('(')[0])
                if siblings:
                    d = siblings[0]
                    doc_source = 'sibling-overload'
                    inherited += 1
                else:
                    d = {}
                    doc_source = 'none'
                    unmatched += 1
            entry['methods'].setdefault(m.Name, []).append({
                'ret': py_type(m.ReturnType),
                'doc': d.get('summary', ''),
                'returns_doc': d.get('returns', ''),
                'doc_source': doc_source,
                'static': bool(m.IsStatic),
                'params': [
                    {
                        'name': p.Name,
                        'type': py_type(p.ParameterType),
                        'doc': (d.get('params') or {}).get(p.Name, ''),
                        'optional': bool(p.IsOptional),
                    }
                    for p in prms
                ],
            })

        for ctor in t.GetConstructors(PUBLIC):
            prms = list(ctor.GetParameters())
            key = member_key(cls, '#ctor', [doc_id_type(p.ParameterType) for p in prms])
            d = docs.get(key, {})
            entry.setdefault('constructors', []).append({
                'doc': d.get('summary', ''),
                'params': [
                    {
                        'name': p.Name,
                        'type': py_type(p.ParameterType),
                        'doc': (d.get('params') or {}).get(p.Name, ''),
                    }
                    for p in prms
                ],
            })

    model['source']['xml_matched_methods'] = matched
    model['source']['xml_unmatched_methods'] = unmatched
    model['source']['xml_sibling_methods'] = inherited

    with open(args.output, 'w', encoding='utf-8') as fh:
        json.dump(model, fh, indent=1, sort_keys=True)

    classes = model['classes']
    print('assembly        :', model['source']['assembly'], model['source']['assembly_version'])
    print('classes         :', len(classes))
    print('methods         :', sum(len(v) for c in classes.values() for v in c['methods'].values()))
    print('properties      :', sum(len(c['properties']) for c in classes.values()))
    print('fields          :', sum(len(c['fields']) for c in classes.values()))
    print('xml exact match :', matched)
    print('xml via sibling :', inherited)
    print('no doc at all   :', unmatched)
    print('documented cls  :', sum(1 for c in classes.values() if c.get('documented')), 'of', len(classes))
    print('wrote           :', args.output)


if __name__ == '__main__':
    main()
