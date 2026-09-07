"""Render Alibre Script stubs from the reflected API model.

Input:  api_model.json, produced by extract_api.py against an installed
        Alibre Design (AlibreScriptAddOn.dll + AlibreScriptAPI.xml).
Output: ../Alibre-Script-Stub-Files/generated-v2/

Why this exists alongside generate_stubs.py: the CSV that generator reads is a
lossy export of AlibreScriptAPI.xml. It carries summaries but no return types,
no property types and no parameter names, so half the API ends up as `Any` and
return types come from a hand-maintained lookup keyed by bare method name.
Reflection supplies all three exactly.

    python tools/generate_stubs.py
"""
from __future__ import print_function

import json
import os
import re
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
API_TEXT_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
WORKSPACE = os.path.abspath(os.path.join(API_TEXT_DIR, os.pardir))
MODEL = os.path.join(HERE, "api_model.json")
OUTPUT_DIR = os.path.join(WORKSPACE, "Alibre-Script-Stub-Files", "generated")
PACKAGE_MODULE_DIR = os.path.join(OUTPUT_DIR, "package", "AlibreScript")

BUILTIN = {"Any", "List", "Dict", "None", "bool", "int", "float", "str", "object"}

# Alibre Script injects these; they belong at module scope, not on a class.
GLOBALS_PY = [
    ("ScriptFileName", "str", "Full path of the running script."),
    ("ScriptFolder", "str", "Folder containing the running script."),
]
GLOBAL_FUNCS = [
    ("CurrentPart", "Part", "The part in the active window."),
    ("CurrentAssembly", "Assembly", "The assembly in the active window."),
    ("CurrentParts", "List[Part]", "Every open part."),
    ("CurrentAssemblies", "List[Assembly]", "Every open assembly."),
]

PY_KEYWORDS = {
    "None", "True", "False", "class", "def", "from", "import", "lambda",
    "global", "pass", "return", "yield", "in", "is", "not", "and", "or",
}

README_TEMPLATE = """# Alibre Script type stubs

Editor autocomplete and type hints for the Alibre Script API.

Generated from `%s` %s and the matching `AlibreScriptAPI.xml`, both read from an
installed Alibre Design. Return types, property types and parameter names come
from assembly reflection; summaries and parameter descriptions come from the
XML documentation.

## Use

Point the language server at the directory containing the package:

```json
{
  "python.analysis.extraPaths": ["path/to/generated/package"]
}
```

Then, for editor support only:

```python
from AlibreScript import *
```

## Authoring only

Alibre Script runs on IronPython 2.7.10 inside Alibre Design, which supplies the
real API as built-in globals. Never import this package inside a live Alibre
script. The runtime `__init__.py` raises on every call by design; it exists so
the import resolves outside Alibre, not so the API works there.

## Regenerating

Do not hand-edit. From `alibre-script.api.text`:

```
python tools/extract_api.py tools/api_model.json
python tools/generate_stubs.py
```

The first step needs Alibre Design installed and pythonnet available. The second
reads only the committed `api_model.json`, so routine regeneration works on any
machine.
"""

SETUP_TEMPLATE = """from setuptools import setup

setup(
    name="alibrescript-ide-stubs",
    version="%s",
    description="Editor type stubs for the Alibre Script API",
    packages=["AlibreScript"],
    package_data={"AlibreScript": ["py.typed", "__init__.pyi"]},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
)
"""


def load_model(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def documented_member_count(cls):
    n = sum(1 for v in cls["properties"].values() if v.get("doc"))
    n += sum(1 for v in cls["fields"].values() if v.get("doc"))
    n += sum(1 for ov in cls["methods"].values() for o in ov if o.get("doc"))
    return n


def referenced_types(cls):
    """Every API type named anywhere in this class's signatures."""
    out = set()

    def add(ann):
        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", ann or ""):
            if tok not in BUILTIN:
                out.add(tok)

    for p in cls["properties"].values():
        add(p["type"])
    for f in cls["fields"].values():
        add(f["type"])
    for overloads in cls["methods"].values():
        for o in overloads:
            add(o["ret"])
            for prm in o["params"]:
                add(prm["type"])
    return out


def select_classes(classes):
    """Documented classes, plus everything their signatures can reach.

    Filtering on documentation alone drops the enums callers need most
    (Part.EndCondition, WindowsInputTypes) because Alibre documents members
    rather than types. Filtering on nothing ships ASDictionary, CSharpUtilities
    and a dozen event-handler delegates into autocomplete.
    """
    keep = {name for name, c in classes.items() if documented_member_count(c) > 0}

    # Enums carry no documentation and no signature ever names them: Windows
    # .OptionsDialog takes a plain List[Any], so nothing points at
    # WindowsInputTypes even though seven of Alibre's own examples use it.
    # Callers reach for these by name, so keep every one.
    for name, c in classes.items():
        if c.get("is_enum"):
            keep.add(name)

    # Nested enums and constant holders hang off a kept owner.
    for name in list(classes):
        owner = name.split(".")[0]
        if "." in name and owner in keep:
            keep.add(name)

    # Close over referenced types until nothing new appears.
    changed = True
    while changed:
        changed = False
        for name in list(keep):
            for ref in referenced_types(classes[name]):
                base = ref.split(".")[0]
                for cand in (ref, base):
                    if cand in classes and cand not in keep:
                        keep.add(cand)
                        changed = True
    return keep


def doc_literal(text, indent):
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    text = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    if text.endswith('"'):
        text += " "
    return ['%s"""%s"""' % (indent, text)]


def method_doc(entry):
    """Summary, parameter descriptions and the returns note, as one docstring."""
    parts = []
    summary = re.sub(r"\s+", " ", entry.get("doc") or "").strip()
    if summary:
        parts.append(summary)
    documented = [p for p in entry["params"] if p.get("doc")]
    if documented:
        parts.append("")
        parts.append("Args:")
        for p in documented:
            parts.append("    %s: %s" % (p["name"], re.sub(r"\s+", " ", p["doc"]).strip()))
    rdoc = re.sub(r"\s+", " ", entry.get("returns_doc") or "").strip()
    if rdoc:
        parts.append("")
        parts.append("Returns:")
        parts.append("    %s" % rdoc)
    return parts


def render_doc_block(lines, indent):
    if not lines:
        return []
    if len(lines) == 1:
        return doc_literal(lines[0], indent)
    out = ['%s"""%s' % (indent, lines[0].replace("\\", "\\\\").replace('"""', "'''"))]
    for l in lines[1:]:
        out.append((indent + l).rstrip() if l else "")
    out.append('%s"""' % indent)
    return out


def param_type(ann):
    """Annotation for a parameter, allowing None where .NET allows null.

    Every AlibreScript.API type is a .NET reference type, and the assembly
    carries no nullable-reference annotations. Alibre's own examples pass None
    for the reference slots they are not using:

        AddExtrudeBoss('Cyl', S, L, False, EndCondition.MidPlane,
                       None, 0, DirectionType.Normal, None, 0, False)

    Declaring those required makes working scripts fail to type-check.
    Primitives stay strict: passing None for a name or a depth is a real error.
    """
    if ann in ALL_CLASSES or ann.split(".")[0] in ALL_CLASSES:
        return "Optional[%s]" % ann
    return ann


def render_params(params, used):
    """Parameter list, giving .NET optional parameters a stub default.

    Windows.OptionsDialog(Title, Inputs, InputAreaWidth) declares the width
    optional, so Alibre's own scripts call it with two arguments. Python needs
    every later parameter to carry a default once one does.
    """
    out = []
    seen_default = False
    for i, p in enumerate(params):
        if p.get("optional"):
            seen_default = True
        suffix = " = ..." if seen_default else ""
        out.append(", %s: %s%s" % (safe_param(p["name"], used, i), param_type(p["type"]), suffix))
    return "".join(out)


def safe_param(name, used, index):
    name = name or "arg%d" % index
    name = re.sub(r"\W", "_", name)
    if not name or name[0].isdigit():
        name = "arg%d" % index
    if name in PY_KEYWORDS:
        name += "_"
    base = name
    n = 2
    while name in used:
        name = "%s%d" % (base, n)
        n += 1
    used.add(name)
    return name


def render_class(name, cls, keep):
    bases = [b for b in cls.get("implements", []) if b in keep and b != name]
    header = "class %s:" % name.split(".")[-1]
    if bases:
        header = "class %s(%s):" % (name.split(".")[-1], ", ".join(sorted(bases)))
    lines = [header]
    body = []
    body.extend(doc_literal(cls.get("doc", ""), "    "))

    for nested in sorted(k for k in keep if k.startswith(name + ".")):
        if nested.count(".") != name.count(".") + 1:
            continue
        for l in render_class(nested, ALL_CLASSES[nested], keep):
            body.append("    " + l if l else "")

    for fname in sorted(cls["fields"]):
        # value__ is the .NET enum backing field. Nothing calls it, and it
        # clutters every enum's completion list.
        if fname == "value__":
            continue
        f = cls["fields"][fname]
        ident = fname + "_" if fname in PY_KEYWORDS else fname
        body.append("    %s: %s" % (ident, f["type"]))
        body.extend(doc_literal(f.get("doc", ""), "    "))

    for pname in sorted(cls["properties"]):
        p = cls["properties"][pname]
        ident = pname + "_" if pname in PY_KEYWORDS else pname
        body.append("    %s: %s" % (ident, p["type"]))
        doc = p.get("doc", "")
        if p.get("readonly") and doc:
            doc += " (read-only)"
        body.extend(doc_literal(doc, "    "))

    for ctor in cls.get("constructors", []) or []:
        pass  # constructors rendered below with overloads

    ctors = cls.get("constructors") or []
    if ctors:
        multiple = len(ctors) > 1
        for c in ctors:
            if multiple:
                body.append("    @overload")
            used = {"self"}
            params = "".join(
                ", %s: %s" % (safe_param(p["name"], used, i), param_type(p["type"]))
                for i, p in enumerate(c["params"])
            )
            sig = "    def __init__(self%s) -> None:" % params
            doc = render_doc_block(method_doc({"doc": c.get("doc", ""), "params": c["params"], "returns_doc": ""}), "        ")
            if doc:
                body.append(sig)
                body.extend(doc)
                body.append("        ...")
            else:
                body.append(sig + " ...")

    for mname in sorted(cls["methods"]):
        overloads = cls["methods"][mname]
        multiple = len(overloads) > 1
        ident = mname + "_" if mname in PY_KEYWORDS else mname
        for entry in overloads:
            if multiple:
                body.append("    @overload")
            if entry.get("static"):
                body.append("    @staticmethod")
            used = set() if entry.get("static") else {"self"}
            params = render_params(entry["params"], used)
            head = "" if entry.get("static") else "self"
            if head and params:
                arglist = head + params
            elif head:
                arglist = head
            else:
                arglist = params.lstrip(", ")
            sig = "    def %s(%s) -> %s:" % (ident, arglist, entry["ret"])
            doc = render_doc_block(method_doc(entry), "        ")
            if doc:
                body.append(sig)
                body.extend(doc)
                body.append("        ...")
            else:
                body.append(sig + " ...")

    if not body:
        body.append("    pass")
    lines.extend(body)
    lines.append("")
    return lines


def order(keep):
    """Interfaces first: a class lists them as bases, so they must exist already."""
    priority = ["Part", "Assembly", "Sketch", "Sketch3D", "Plane", "Axis", "Point",
                "Face", "Edge", "Vertex", "Feature", "Configuration", "Parameter", "Windows"]
    top = sorted(k for k in keep if "." not in k)
    interfaces = [n for n in top if re.match(r"^I[A-Z]", n)]
    rest = [n for n in top if n not in interfaces]
    return interfaces + [n for n in priority if n in rest] + [n for n in rest if n not in priority]


def main():
    global ALL_CLASSES
    if not os.path.isfile(MODEL):
        sys.exit("Missing %s - run extract_api.py first." % MODEL)
    model = load_model(MODEL)
    ALL_CLASSES = model["classes"]
    keep = select_classes(ALL_CLASSES)

    src = model["source"]
    lines = [
        "# Generated type stubs for the Alibre Script API.",
        "# Source: %s %s + AlibreScriptAPI.xml" % (src["assembly"], src["assembly_version"]),
        "# Do not hand-edit: regenerate with tools/generate_stubs_from_model.py.",
        "from typing import Any, Dict, List, Optional, overload",
        "",
    ]
    for name, ann, doc in GLOBALS_PY:
        lines.append("%s: %s" % (name, ann))
        lines.extend(doc_literal(doc, ""))
    lines.append("")

    for name in order(keep):
        lines.extend(render_class(name, ALL_CLASSES[name], keep))

    for fname, ret, doc in GLOBAL_FUNCS:
        lines.append("def %s() -> %s:" % (fname, ret))
        lines.extend(doc_literal(doc, "    "))
        lines.append("    ...")
        lines.append("")

    pyi = "\n".join(lines)

    for d in [OUTPUT_DIR, PACKAGE_MODULE_DIR]:
        if not os.path.isdir(d):
            os.makedirs(d)

    runtime = [
        "# Runtime companion to __init__.pyi, IronPython 2.7.10 compatible.",
        "# Authoring aid only: Alibre Script supplies the real API as built-in",
        "# globals. Every member here raises if called outside Alibre Design.",
        "",
        "",
        "def _unavailable(name):",
        "    raise NotImplementedError(",
        "        name + ' is only available inside Alibre Design.'",
        "        ' These stubs exist for editor autocomplete.')",
        "",
        "",
    ]
    for name, _ann, _doc in GLOBALS_PY:
        runtime.append("%s = ''" % name)
    runtime.append("")

    def emit_runtime_class(full, indent=""):
        cls = ALL_CLASSES[full]
        short = full.split(".")[-1]
        out = ["%sclass %s(object):" % (indent, short)]
        inner = []
        for nested in sorted(k for k in keep if k.startswith(full + ".")):
            if nested.count(".") != full.count(".") + 1:
                continue
            inner.extend(emit_runtime_class(nested, indent + "    "))
        for fname in sorted(cls["fields"]):
            ident = fname + "_" if fname in PY_KEYWORDS else fname
            inner.append("%s    %s = None" % (indent, ident))
        for pname in sorted(cls["properties"]):
            ident = pname + "_" if pname in PY_KEYWORDS else pname
            inner.append("%s    %s = None" % (indent, ident))
        for mname in sorted(cls["methods"]):
            ident = mname + "_" if mname in PY_KEYWORDS else mname
            inner.append(
                "%s    def %s(self, *args, **kwargs): _unavailable('%s.%s')"
                % (indent, ident, short, mname)
            )
        if not inner:
            inner.append("%s    pass" % indent)
        out.extend(inner)
        out.append("")
        return out

    for name in order(keep):
        runtime.extend(emit_runtime_class(name))

    for fname, _ret, _doc in GLOBAL_FUNCS:
        runtime.append("def %s(*args, **kwargs): _unavailable('%s')" % (fname, fname))
    runtime.append("")
    py = "\n".join(runtime)

    def write(path, text):
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    write(os.path.join(PACKAGE_MODULE_DIR, "__init__.pyi"), pyi)
    write(os.path.join(PACKAGE_MODULE_DIR, "__init__.py"), py)
    write(os.path.join(PACKAGE_MODULE_DIR, "py.typed"), "")

    # Flat copies, for anyone pointing an editor at the directory rather than
    # installing the package. Written from the same strings so they cannot drift.
    write(os.path.join(OUTPUT_DIR, "AlibreScript.pyi"), pyi)
    write(os.path.join(OUTPUT_DIR, "AlibreScript.py"), py)

    version = src["assembly_version"]
    write(os.path.join(OUTPUT_DIR, "README.md"), README_TEMPLATE % (src["assembly"], version))
    package_dir = os.path.dirname(PACKAGE_MODULE_DIR)
    write(os.path.join(package_dir, "README.md"), README_TEMPLATE % (src["assembly"], version))
    write(os.path.join(package_dir, "setup.py"), SETUP_TEMPLATE % version)
    write(os.path.join(package_dir, "MANIFEST.in"),
          "include README.md\ninclude AlibreScript/py.typed\ninclude AlibreScript/__init__.pyi\n")

    print("source     :", src["assembly"], src["assembly_version"])
    print("classes    :", len(keep), "of", len(ALL_CLASSES), "reflected")
    print("output     :", OUTPUT_DIR)


if __name__ == "__main__":
    main()
