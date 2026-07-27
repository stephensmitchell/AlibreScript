"""Generate clean Alibre Script stubs from local API/reference data.

Run from `alibre-script.api.text`:

    python tools/generate_stubs.py

Inputs:
    - alibre.script.api2.csv
    - ../Alibre-Script.Reflected/sources/*.txt

Outputs:
    - ../Alibre-Script-Stub-Files/generated/AlibreScript.pyi
    - ../Alibre-Script-Stub-Files/generated/AlibreScript.py
    - ../Alibre-Script-Stub-Files/generated/README.md

The `.pyi` file preserves overloads for editor/static tooling. The `.py` file
uses one runtime method per name with `*args, **kwargs`, which avoids Python's
normal "last overload wins" behavior.
"""

from __future__ import print_function

import csv
import os
import re
from collections import defaultdict


HERE = os.path.abspath(os.path.dirname(__file__))
API_TEXT_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
WORKSPACE = os.path.abspath(os.path.join(API_TEXT_DIR, os.pardir))
API_CSV = os.path.join(API_TEXT_DIR, "alibre.script.api2.csv")
REFLECTED_SOURCES = os.path.join(WORKSPACE, "Alibre-Script.Reflected", "sources")
OUTPUT_DIR = os.path.join(WORKSPACE, "Alibre-Script-Stub-Files", "generated")
PACKAGE_DIR = os.path.join(OUTPUT_DIR, "package")
PACKAGE_MODULE_DIR = os.path.join(PACKAGE_DIR, "AlibreScript")


TYPE_MAP = {
    "System.String": "str",
    "System.Double": "float",
    "System.Int32": "int",
    "System.Boolean": "bool",
    "System.Byte": "int",
    "System.Object": "Any",
    "IronPython.Runtime.List": "List[Any]",
    "IronPython.Runtime.PythonDictionary": "Dict[Any, Any]",
    "Microsoft.CodeAnalysis.Scripting.Script{System.Object[]}": "Any",
}


TYPE_PREFIXES = [
    "AssembledSubAssembly",
    "ISelectableGeometry",
    "IADDesignPlane",
    "IADDesignAxis",
    "IADPoint",
    "IADGeometryFactory",
    "ConstraintBoundsType",
    "GuideCurveTypes",
    "ParameterTypes",
    "ParameterUnits",
    "PythonDictionary",
    "ISketchFigure3D",
    "ISketchSurface",
    "EndCondition",
    "DirectionType",
    "IConstrainable",
    "CircularArc3D",
    "EllipticalArc",
    "PolylinePoint3D",
    "SketchPoint3D",
    "ICrossSection",
    "IChamferable",
    "ISketchFigure",
    "ISweepPath",
    "IFilletable",
    "PolylinePoint",
    "GlobalParameters",
    "Configuration",
    "CircularArc",
    "Polyline3D",
    "Sketch3D",
    "Bspline3D",
    "UnitTypes",
    "LockTypes",
    "IAssembled",
    "IInstance",
    "Assembly",
    "Feature",
    "Material",
    "Parameter",
    "Polyline",
    "SketchPoint",
    "Boolean",
    "Double",
    "String",
    "Object",
    "Int32",
    "Byte",
    "List`1",
    "List",
    "IPlane",
    "IAxis",
    "IPoint",
    "Vertex",
    "Sketch",
    "Bspline",
    "Circle",
    "Ellipse",
    "Line3D",
    "Line",
    "Plane",
    "Point",
    "Axis",
    "Face",
    "Edge",
    "Part",
]


STATIC_CONSTANTS = {
    "WindowsInputTypes": [
        "Boolean",
        "Edge",
        "Face",
        "File",
        "Folder",
        "Image",
        "Integer",
        "Part",
        "Plane",
        "Real",
        "SaveFile",
        "Sketch",
        "Sketch3D",
        "String",
        "StringList",
    ],
    "UnitTypes": ["Millimeters", "Inches", "Centimeters"],
    "ParameterTypes": ["Distance", "Angle", "Count"],
    "ParameterUnits": [
        "Unitless",
        "Millimeters",
        "Centimeters",
        "Inches",
        "Degrees",
    ],
    "GuideCurveTypes": ["Global", "Local"],
    "LockTypes": ["SuppressNewFeatures", "LockColorProperties"],
    "Part.EndCondition": ["ToDepth", "ThroughAll", "MidPlane", "EntirePath"],
    "Part.DirectionType": ["Normal"],
    "Part.FileTypes": [
        "GeomagicDesignPart",
        "AlibreDesignPart",
        "STEP",
        "IGES",
        "ThreeDM",
        "SAT",
        "STL_in",
        "STL_cm",
        "STL_mm",
    ],
    "Sketch.Constraints": [
        "Coincident",
        "Collinear",
        "Equal",
        "Horizontal",
        "Parallel",
        "Perpendicular",
        "Tangent",
        "Vertical",
    ],
    # These nested enum types exist in Alibre Script build 347013, but the
    # member constants were not exposed as Python attributes in runtime testing.
    "Assembly.ConstraintBoundsType": [],
    "CircularArc.ArcType": [],
    "CircularArc3D.ArcType": [],
}


RETURN_TYPES = {
    "Add3DSketch": "Sketch3D",
    "AddAxis": "Axis",
    "AddChamfer": "Feature",
    "AddChamferAngle": "Feature",
    "AddConfiguration": "Configuration",
    "AddExtrudeBoss": "Feature",
    "AddExtrudeCut": "Feature",
    "AddFeature": "Feature",
    "AddFillet": "Feature",
    "AddGear": "GearSketch",
    "AddGearDN": "GearSketch",
    "AddGearDP": "GearSketch",
    "AddGearNP": "GearSketch",
    "AddLoftBoss": "Feature",
    "AddLoftCut": "Feature",
    "AddPlane": "Plane",
    "AddPoint": "Point",
    "AddPointFromCircularEdge": "Point",
    "AddPointFromToroidalFace": "Point",
    "AddPoints": "List[Point]",
    "AddRevolveBoss": "Feature",
    "AddRevolveCut": "Feature",
    "AddSketch": "Sketch",
    "AddSweepBoss": "Feature",
    "AddSweepCut": "Feature",
    "AddVertexChamfer": "Feature",
    "Close": "None",
    "ErrorDialog": "None",
    "Get3DSketch": "Sketch3D",
    "GetActiveConfiguration": "Configuration",
    "GetAxis": "Axis",
    "GetBoundingBox": "List[Any]",
    "GetConfiguration": "Configuration",
    "GetCustomProperty": "Any",
    "GetEdge": "Edge",
    "GetEdges": "List[Edge]",
    "GetFace": "Face",
    "GetFaces": "List[Face]",
    "GetFeature": "Feature",
    "GetParameter": "Parameter",
    "GetPart": "Part",
    "GetPlane": "Plane",
    "GetPoint": "Point",
    "GetSketch": "Sketch",
    "GetUserData": "Any",
    "GetVertex": "Vertex",
    "GetVertices": "List[Vertex]",
    "Hide": "None",
    "InfoDialog": "None",
    "IsOpen": "bool",
    "OpenFileDialog": "str",
    "QuestionDialog": "bool",
    "Regenerate": "None",
    "RemoveFeature": "None",
    "RemovePlane": "None",
    "RemovePoint": "None",
    "RemoveSketch": "None",
    "ResumeUpdating": "None",
    "Save": "None",
    "SaveAs": "None",
    "SaveFileDialog": "str",
    "Select": "None",
    "SelectFolderDialog": "str",
    "SetColor": "None",
    "SetCustomProperty": "None",
    "SetUserData": "None",
    "Show": "None",
    "SuppressFeature": "None",
    "UnsuppressFeature": "None",
}


def read_csv_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def split_args(args):
    args = args.strip()
    if not args:
        return []
    return [arg.strip() for arg in args.split(",") if arg.strip()]


def api_type_to_hint(api_type):
    api_type = api_type.strip()
    if api_type in TYPE_MAP:
        return TYPE_MAP[api_type]
    if api_type.startswith("AlibreScript.API."):
        name = api_type[len("AlibreScript.API.") :]
        return name
    if api_type.startswith("System."):
        return "Any"
    if api_type.startswith("IronPython.Runtime."):
        return "Any"
    return "Any"


def api_type_key(api_type):
    api_type = api_type.strip()
    if api_type.startswith("AlibreScript.API."):
        return api_type[len("AlibreScript.API.") :].split(".")[-1]
    if api_type.startswith("System."):
        return api_type[len("System.") :]
    if api_type == "IronPython.Runtime.List":
        return "List"
    if api_type == "IronPython.Runtime.PythonDictionary":
        return "PythonDictionary"
    if api_type.startswith("Microsoft.CodeAnalysis.Scripting."):
        return "Object"
    return re.sub(r"[^0-9A-Za-z_]", "", api_type) or "Any"


def reflected_type_key(token):
    token = token.strip()
    token = token.replace("&", "")
    token = token.replace("[]", "")
    token = token.replace("`1", "")
    for prefix in sorted(TYPE_PREFIXES, key=len, reverse=True):
        if token == prefix or token.startswith(prefix):
            return prefix.replace("List`1", "List")
    return "Any"


def strip_type_prefix(token):
    token = token.strip()
    token = token.replace("&", "")
    token = token.replace("[]", "")
    token = token.replace("`1", "")
    for prefix in sorted(TYPE_PREFIXES, key=len, reverse=True):
        if token.startswith(prefix) and len(token) > len(prefix):
            return token[len(prefix) :]
    return token


def camel_to_snake(name):
    name = re.sub(r"[^0-9A-Za-z_]", "_", name)
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"_+", "_", name).strip("_").lower()
    if not name:
        name = "value"
    if name[0].isdigit():
        name = "arg_" + name
    if name in {"class", "def", "from", "import", "None", "True", "False", "pass"}:
        name = name + "_"
    return name


def fallback_name(api_type, index):
    api_type = api_type.replace("AlibreScript.API.", "")
    api_type = api_type.replace("IronPython.Runtime.", "")
    api_type = api_type.replace("System.", "")
    api_type = api_type.replace("Microsoft.CodeAnalysis.Scripting.", "")
    api_type = re.sub(r"[^0-9A-Za-z_]", "_", api_type)
    name = camel_to_snake(api_type)
    if name in {"string", "double", "int32", "boolean", "byte", "object"}:
        name = "value"
    return name or "arg{0}".format(index + 1)


def unique_names(names):
    counts = defaultdict(int)
    result = []
    for name in names:
        counts[name] += 1
        if counts[name] == 1:
            result.append(name)
        else:
            result.append("{0}_{1}".format(name, counts[name]))
    return result


def reflected_param_names():
    result = defaultdict(lambda: defaultdict(dict))
    if not os.path.isdir(REFLECTED_SOURCES):
        return result

    method_re = re.compile(r"^Method->([A-Za-z0-9_]+)\((.*)\)")
    for name in os.listdir(REFLECTED_SOURCES):
        if not name.endswith(".txt"):
            continue
        class_name = name[len("AlibreScript.API.") : -len(".txt")]
        path = os.path.join(REFLECTED_SOURCES, name)
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                match = method_re.match(line.strip())
                if not match:
                    continue
                method_name, arg_text = match.groups()
                tokens = split_args(arg_text)
                names = [camel_to_snake(strip_type_prefix(token)) for token in tokens]
                key = tuple(reflected_type_key(token) for token in tokens)
                result[class_name][method_name][key] = unique_names(names)
    return result


def parse_api(rows):
    classes = defaultdict(
        lambda: {
            "methods": defaultdict(list),
            "constructors": [],
            "properties": {},
            "fields": {},
            "nested_types": {},
            "doc": "",
        }
    )
    top_types = {}

    method_re = re.compile(r"^(?:M:)?AlibreScript\.API\.([A-Za-z0-9_]+)\.([A-Za-z0-9_#]+)\((.*)\)$")
    no_arg_method_re = re.compile(r"^(?:M:)?AlibreScript\.API\.([A-Za-z0-9_]+)\.([A-Za-z0-9_#]+)$")
    prop_re = re.compile(r"^P:AlibreScript\.API\.([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)$")
    field_re = re.compile(r"^F:AlibreScript\.API\.([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)$")
    type_re = re.compile(r"^T:AlibreScript\.API\.([A-Za-z0-9_.]+)$")

    for row in rows:
        member = (row.get("Member Name") or "").strip()
        summary = (row.get("Summary") or "").strip()

        match = method_re.match(member)
        if match:
            class_name, method_name, arg_text = match.groups()
            args = split_args(arg_text)
            entry = {"api_args": args, "summary": summary}
            if method_name == "#ctor":
                classes[class_name]["constructors"].append(entry)
            else:
                classes[class_name]["methods"][method_name].append(entry)
            continue

        match = no_arg_method_re.match(member)
        if match:
            class_name, method_name = match.groups()
            entry = {"api_args": [], "summary": summary}
            if method_name == "#ctor":
                classes[class_name]["constructors"].append(entry)
            else:
                classes[class_name]["methods"][method_name].append(entry)
            continue

        match = prop_re.match(member)
        if match:
            class_name, prop_name = match.groups()
            classes[class_name]["properties"][prop_name] = summary
            continue

        match = field_re.match(member)
        if match:
            class_name, field_name = match.groups()
            classes[class_name]["fields"][field_name] = summary
            continue

        match = type_re.match(member)
        if match:
            type_name = match.group(1)
            if "." in type_name:
                parent, nested = type_name.split(".", 1)
                classes[parent]["nested_types"][nested] = summary
            else:
                top_types[type_name] = summary
                classes[type_name]["doc"] = summary
            continue

    return classes, top_types


def param_names_for(class_name, method_name, api_args, reflected_names):
    method_reflections = reflected_names.get(class_name, {}).get(method_name, {})
    key = tuple(api_type_key(arg) for arg in api_args)
    reflected = method_reflections.get(key)
    if reflected:
        return reflected
    same_arity = [
        names for reflected_key, names in method_reflections.items() if len(reflected_key) == len(api_args)
    ]
    if len(same_arity) == 1:
        return same_arity[0]
    return unique_names([fallback_name(arg, index) for index, arg in enumerate(api_args)])


def signature_params(class_name, method_name, entry, reflected_names):
    names = param_names_for(class_name, method_name, entry["api_args"], reflected_names)
    params = []
    for name, api_type in zip(names, entry["api_args"]):
        params.append("{0}: {1}".format(name, api_type_to_hint(api_type)))
    return ", ".join(params)


def method_return_type(method_name):
    return RETURN_TYPES.get(method_name, "Any")


def clean_doc(text):
    text = re.sub(r"\s+", " ", text or "").strip()
    return text.replace('"""', '\\"\\"\\"')


def class_order(classes):
    priority = [
        "Part",
        "Assembly",
        "AssembledPart",
        "AssembledSubAssembly",
        "Sketch",
        "Sketch3D",
        "Plane",
        "Axis",
        "Point",
        "Face",
        "Edge",
        "Vertex",
        "Feature",
        "Windows",
    ]
    names = sorted(classes.keys())
    return [name for name in priority if name in classes] + [
        name for name in names if name not in priority
    ]


def render_constant_class(name, constants, indent=""):
    lines = [indent + "class {0}:".format(name)]
    if constants:
        for index, constant in enumerate(constants, 1):
            safe = "None_" if constant == "None" else constant
            lines.append(indent + "    {0}: Any".format(safe))
    else:
        lines.append(indent + "    pass")
    return lines


def render_pyi(classes, top_types, reflected_names):
    lines = [
        "# Generated by alibre-script.api.text/tools/generate_stubs.py",
        "# Source of truth: alibre.script.api2.csv; parameter names from Alibre-Script.Reflected/sources.",
        "from typing import Any, Dict, List, overload",
        "",
        "ScriptFileName: str",
        "ScriptFolder: str",
        "",
    ]

    all_top_types = sorted(set(top_types) | {key for key in STATIC_CONSTANTS if "." not in key})
    for type_name in all_top_types:
        if type_name in classes:
            continue
        lines.extend(render_constant_class(type_name, STATIC_CONSTANTS.get(type_name, [])))
        lines.append("")

    for class_name in class_order(classes):
        info = classes[class_name]
        lines.append("class {0}:".format(class_name))
        body = []
        doc = clean_doc(info.get("doc", ""))
        if doc:
            body.append('    """{0}"""'.format(doc))

        for constant in STATIC_CONSTANTS.get(class_name, []):
            safe = "None_" if constant == "None" else constant
            body.append("    {0}: Any".format(safe))

        for nested_name, nested_doc in sorted(info["nested_types"].items()):
            constants = STATIC_CONSTANTS.get("{0}.{1}".format(class_name, nested_name), [])
            body.extend(render_constant_class(nested_name, constants, indent="    "))

        if class_name in {"Part", "Assembly", "Sketch", "CircularArc", "CircularArc3D"}:
            for nested_name in sorted(
                name.split(".", 1)[1]
                for name in STATIC_CONSTANTS
                if name.startswith(class_name + ".")
            ):
                if nested_name not in info["nested_types"]:
                    constants = STATIC_CONSTANTS.get("{0}.{1}".format(class_name, nested_name), [])
                    body.extend(render_constant_class(nested_name, constants, indent="    "))

        for prop_name in sorted(info["properties"]):
            body.append("    {0}: Any".format(prop_name))
        for field_name in sorted(info["fields"]):
            if field_name.startswith("_"):
                continue
            body.append("    {0}: Any".format(field_name))

        constructors = info["constructors"] or [{"api_args": [], "summary": ""}]
        if len(constructors) > 1:
            for entry in constructors:
                body.append("    @overload")
                params = signature_params(class_name, "__init__", entry, reflected_names)
                body.append("    def __init__(self{0}) -> None: ...".format(", " + params if params else ""))
        else:
            entry = constructors[0]
            params = signature_params(class_name, "__init__", entry, reflected_names)
            body.append("    def __init__(self{0}) -> None: ...".format(", " + params if params else ""))

        for method_name in sorted(info["methods"]):
            overloads = info["methods"][method_name]
            if len(overloads) > 1:
                for entry in overloads:
                    body.append("    @overload")
                    params = signature_params(class_name, method_name, entry, reflected_names)
                    body.append(
                        "    def {0}(self{1}) -> {2}: ...".format(
                            method_name,
                            ", " + params if params else "",
                            method_return_type(method_name),
                        )
                    )
            else:
                entry = overloads[0]
                params = signature_params(class_name, method_name, entry, reflected_names)
                body.append(
                    "    def {0}(self{1}) -> {2}: ...".format(
                        method_name,
                        ", " + params if params else "",
                        method_return_type(method_name),
                    )
                )

        if not body:
            body.append("    pass")
        lines.extend(body)
        lines.append("")

    lines.extend(
        [
            "def CurrentPart() -> Part: ...",
            "def CurrentAssembly() -> Assembly: ...",
            "def CurrentParts() -> List[Part]: ...",
            "def CurrentAssemblies() -> List[Assembly]: ...",
            "",
        ]
    )
    return "\n".join(lines)


def render_py(classes, top_types):
    lines = [
        "# Generated by alibre-script.api.text/tools/generate_stubs.py",
        "# Minimal runtime mock for editor imports outside Alibre Design.",
        "",
        "ScriptFileName = ''",
        "ScriptFolder = ''",
        "",
        "class _StubBase(object):",
        "    def __init__(self, *args, **kwargs):",
        "        pass",
        "",
    ]

    def add_constant_class(name, constants, indent=""):
        lines.append(indent + "class {0}(object):".format(name))
        if constants:
            for index, constant in enumerate(constants, 1):
                safe = "None_" if constant == "None" else constant
                lines.append(indent + "    {0} = {1}".format(safe, index))
        else:
            lines.append(indent + "    pass")

    all_top_types = sorted(set(top_types) | {key for key in STATIC_CONSTANTS if "." not in key})
    for type_name in all_top_types:
        if type_name in classes:
            continue
        add_constant_class(type_name, STATIC_CONSTANTS.get(type_name, []))
        lines.append("")

    for class_name in class_order(classes):
        info = classes[class_name]
        lines.append("class {0}(_StubBase):".format(class_name))
        body_count = 0

        for index, constant in enumerate(STATIC_CONSTANTS.get(class_name, []), 1):
            safe = "None_" if constant == "None" else constant
            lines.append("    {0} = {1}".format(safe, index))
            body_count += 1

        nested_names = set(info["nested_types"])
        nested_names.update(
            name.split(".", 1)[1]
            for name in STATIC_CONSTANTS
            if name.startswith(class_name + ".")
        )
        for nested_name in sorted(nested_names):
            add_constant_class(
                nested_name,
                STATIC_CONSTANTS.get("{0}.{1}".format(class_name, nested_name), []),
                indent="    ",
            )
            body_count += 1

        for prop_name in sorted(info["properties"]):
            lines.append("    {0} = None".format(prop_name))
            body_count += 1
        for field_name in sorted(info["fields"]):
            if field_name.startswith("_"):
                continue
            lines.append("    {0} = None".format(field_name))
            body_count += 1

        method_names = set(info["methods"])
        if info["constructors"]:
            lines.append("    def __init__(self, *args, **kwargs):")
            lines.append("        pass")
            body_count += 1

        for method_name in sorted(method_names):
            lines.append("    def {0}(self, *args, **kwargs):".format(method_name))
            lines.append("        return None")
            body_count += 1

        if body_count == 0:
            lines.append("    pass")
        lines.append("")

    lines.extend(
        [
            "def CurrentPart():",
            "    return Part()",
            "",
            "def CurrentAssembly():",
            "    return Assembly()",
            "",
            "def CurrentParts():",
            "    return [Part()]",
            "",
            "def CurrentAssemblies():",
            "    return [Assembly()]",
            "",
        ]
    )
    return "\n".join(lines)


def render_readme():
    return """# Generated Alibre Script Stubs

Generated from:

- `../alibre-script.api.text/alibre.script.api2.csv`
- `../Alibre-Script.Reflected/sources/`

Files:

- `AlibreScript.pyi`: editor/static-analysis stub with `@overload` signatures.
- `AlibreScript.py`: IronPython 2.7.10-compatible runtime mock for imports
  outside Alibre Design. It intentionally has no type annotations, no f-strings,
  and no Python 3-only syntax.
- `package/`: installable IDE package. It exposes the same mock as
  `import AlibreScript`.

These files are for authoring support only. Alibre Script still runs inside
Alibre Design/IronPython 2.7.10, and CAD behavior must be verified there.

The generated `AlibreScript` module includes common Alibre Script globals:
`ScriptFileName`, `ScriptFolder`, `CurrentPart()`, `CurrentAssembly()`,
`CurrentParts()`, and `CurrentAssemblies()`.

Do not copy `.pyi` syntax into Alibre Script. The `.pyi` file is only for
editors and language servers.

Regenerate from `alibre-script.api.text`:

```powershell
python tools\\generate_stubs.py
```

Install locally for an IDE:

```powershell
pip install -e package
```

Packaging and PyPI notes are documented in:

```text
..\\..\\alibre-script.api.text\\docs\\PACKAGE-USAGE.md
```

Do not install or import this package inside the Alibre Script add-on. Inside
Alibre Design, use the real built-in Alibre Script API.
"""


def render_package_readme():
    return """# alibrescript-ide-stubs

Authoring-only stubs for Alibre Script.

This package installs an `AlibreScript` module so external IDEs can resolve
imports such as:

```python
from AlibreScript import *
```

The runtime `AlibreScript/__init__.py` is intentionally compatible with
IronPython 2.7.10. The companion `AlibreScript/__init__.pyi` is for editors and
language servers only.

This package is not the real Alibre Script API and should not be imported inside
Alibre Design. Alibre Design provides the real API at script runtime.

Included Alibre Script globals: `ScriptFileName`, `ScriptFolder`,
`CurrentPart()`, `CurrentAssembly()`, `CurrentParts()`, and
`CurrentAssemblies()`.

Local install:

```powershell
pip install -e .
```

GitHub install after the repository is pushed:

```powershell
pip install "git+https://github.com/stephensmitchell/AlibreScript.git#egg=alibrescript-ide-stubs&subdirectory=Alibre-Script-Stub-Files/generated/package"
```

This is a Git repository install, not a GitHub Packages registry publish.
GitHub Packages does not currently provide a PyPI-compatible Python package
registry. Use PyPI/TestPyPI for a real Python package registry.

Full usage and publishing notes:

```text
..\\..\\..\\alibre-script.api.text\\docs\\PACKAGE-USAGE.md
```
"""


def render_setup_py():
    return '''from setuptools import setup


def readme():
    try:
        with open("README.md", "r") as f:
            return f.read()
    except IOError:
        return ""


setup(
    name="alibrescript-ide-stubs",
    version="0.1.0",
    description="Authoring-only IDE stubs for Alibre Script IronPython 2.7.10",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Alibre Script API Text contributors",
    url="https://github.com/stephensmitchell/AlibreScript",
    project_urls={"Source": "https://github.com/stephensmitchell/AlibreScript"},
    license="MIT",
    packages=["AlibreScript"],
    package_data={"AlibreScript": ["__init__.pyi", "py.typed"]},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Stubs Only",
    ],
)
'''


def render_manifest():
    return """include README.md
recursive-include AlibreScript *.pyi py.typed
"""


def write_file(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        if not text.endswith("\n"):
            f.write("\n")


def main():
    rows = read_csv_rows(API_CSV)
    classes, top_types = parse_api(rows)
    reflected_names = reflected_param_names()

    for directory in [OUTPUT_DIR, PACKAGE_DIR, PACKAGE_MODULE_DIR]:
        if not os.path.isdir(directory):
            os.makedirs(directory)

    pyi = render_pyi(classes, top_types, reflected_names)
    py = render_py(classes, top_types)
    readme = render_readme()

    write_file(os.path.join(OUTPUT_DIR, "AlibreScript.pyi"), pyi)
    write_file(os.path.join(OUTPUT_DIR, "AlibreScript.py"), py)
    write_file(os.path.join(OUTPUT_DIR, "README.md"), readme)
    write_file(os.path.join(PACKAGE_MODULE_DIR, "__init__.py"), py)
    write_file(os.path.join(PACKAGE_MODULE_DIR, "__init__.pyi"), pyi)
    write_file(os.path.join(PACKAGE_MODULE_DIR, "py.typed"), "")
    write_file(os.path.join(PACKAGE_DIR, "README.md"), render_package_readme())
    write_file(os.path.join(PACKAGE_DIR, "setup.py"), render_setup_py())
    write_file(os.path.join(PACKAGE_DIR, "MANIFEST.in"), render_manifest())

    print("Generated stubs in:", OUTPUT_DIR)
    print("Generated package in:", PACKAGE_DIR)
    print("Classes:", len(classes))
    print("Top-level types:", len(top_types))


if __name__ == "__main__":
    main()
