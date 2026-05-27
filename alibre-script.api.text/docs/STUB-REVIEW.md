# Stub Review

The existing stub folders can be improved using the API CSV and reflected
content. Current status: useful reference material, but not yet reliable as
drop-in editor/runtime stubs.

## Audit Command

From `alibre-script.api.text`:

```powershell
python tools/audit_stubs.py
```

## Findings

### `Alibre-Script-Stub-Files/`

Syntax check results from the current files:

- `alibre_script_api.py`: invalid Python. It uses .NET type names such as
  `AlibreX.IADAssemblySession` as parameter names.
- `alibre_script_api_python27_docs.py`: invalid Python because generated
  docstrings can contain unescaped quotes.
- `alibre_script_api_docs.pyi`: invalid stub syntax in several signatures where
  dotted .NET type names are used as parameter names.
- `alibre_script_api_advanced_docs.pyi`: invalid stub syntax/docstring output.
- `AlibreScriptAPI_Mock.py`: invalid Python because constructors were emitted as
  `def #ctor(...)`.
- `mock_api.py`: invalid Python around malformed array-type parameters such as
  `Object[]}`.
- `mock_api (Original).py`: invalid Python because constructors were emitted as
  `def #ctor(...)`.
- `main.py`: syntactically valid, but only a small smoke-test file.

These files remain useful for text search, but should not be treated as correct
Python stubs.

### `Alibre-Script.Reflected/output/`

The reflected `.py` files parse successfully and currently cover the method
groups and arities from `alibre.script.api3.csv`.

The main issue is overloaded methods. Normal Python does not keep multiple
methods with the same name in a class; later definitions replace earlier ones at
runtime. For example, `Part.AddPlane`, `Part.AddAxis`, `Part.AddPoint`, and many
sketch methods are emitted multiple times.

This means reflected output is good for browsing and extraction, but should be
converted to `.pyi` with `@overload` for editor use.

## Recommended Regeneration Strategy

Create a new generated package, separate from the current experimental files:

```text
Alibre-Script-Stub-Files/
  generated/
    AlibreScript.pyi
    AlibreScript.py
    README.md
```

Generate `AlibreScript.pyi` from:

1. `alibre-script.api.text/alibre.script.api3.csv` for authoritative public API
   members and summaries.
2. `Alibre-Script.Reflected/sources/` for friendlier parameter names.
3. `Alibre-Script.Reflected/output/` as a coverage cross-check.

Rules for the generator:

- Emit one class per API class.
- Emit overloaded methods with `@overload` in `.pyi`.
- Emit only one runtime method per name in `.py`, using `*args, **kwargs`.
- Translate `#ctor` to `__init__`.
- Drop invalid .NET parameter names from signatures.
- Sanitize parameter names to valid Python identifiers.
- Map simple types:
  - `System.String` -> `str`
  - `System.Double` -> `float`
  - `System.Int32` -> `int`
  - `System.Boolean` -> `bool`
  - `System.Byte` -> `int`
  - `IronPython.Runtime.List` -> `list`
  - unknown Alibre/.NET types -> `Any` or quoted class names
- Preserve docstrings from the CSV, with quotes escaped.
- Represent enum-like values such as `WindowsInputTypes` as classes/constants,
  not functions.

## Correctness Checklist

Before using regenerated stubs:

- `python -m py_compile generated/AlibreScript.py` passes.
- `python -m ast` or `python tools/audit_stubs.py` reports no syntax failures.
- `@overload` appears before repeated signatures in `.pyi`.
- `Part.AddPlane`, `Part.AddAxis`, `Sketch.AddCircle`, and `Windows.OptionsDialog`
  signatures match the API CSV.
- `AddCircle` documentation says diameter where the API says diameter.
- No generated signature contains `System.String` or `AlibreScript.API.Part` as a
  parameter name.

## Practical Use Today

Use the regenerated files:

- `../Alibre-Script-Stub-Files/generated/AlibreScript.py`
- `../Alibre-Script-Stub-Files/generated/AlibreScript.pyi`

Generation and validation:

```powershell
python tools/generate_stubs.py
python tools/audit_stubs.py
```

The generated `AlibreScript.py` file is intentionally IronPython 2.7.10
compatible. The generated `AlibreScript.pyi` file is for editors/type checkers
only and should not be copied into Alibre Script.

For script correctness:

- Use `alibre.script.api2.csv` as the broad source of truth.
- Use `alibre.script.api3.csv` as the compact quick reference.
- Use `Alibre-Script.Reflected/sources/` for parameter names.
- Use `Alibre-Script.Reflected/output/` for class browsing.
- Use legacy stub files only as search/autocomplete aids.
- Validate generated scripts inside Alibre Script.
