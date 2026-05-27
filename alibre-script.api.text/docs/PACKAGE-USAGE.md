# Package Usage

The generated package is for IDE authoring support outside Alibre Design.

Generated package path:

```text
D:\05-26-2026\AlibreScript\Alibre-Script-Stub-Files\generated\package
```

Import name:

```python
from AlibreScript import *
```

Distribution name:

```text
alibrescript-ide-stubs
```

## Important Boundary

Do not install or import this package inside the Alibre Script add-on. Alibre
Design already provides the real API in its IronPython 2.7.10 runtime.

The generated package is only for:

- VS Code autocomplete
- IDE symbol resolution
- external linting/static inspection
- lightweight mock imports outside Alibre

## Files

- `AlibreScript/__init__.py`
  - IronPython 2.7.10-compatible runtime mock.
  - No type annotations, no f-strings, no Python 3-only syntax.
- `AlibreScript/__init__.pyi`
  - Editor/type-checking stub with overloads.
  - Not intended for Alibre Script execution.
- `setup.py`
  - Python packaging entry point.
- `MANIFEST.in`
  - Includes the `.pyi` and `py.typed` files.

## Manual IDE Use Without Installing

Add this folder to your IDE search path:

```text
D:\05-26-2026\AlibreScript\Alibre-Script-Stub-Files\generated\package
```

VS Code example:

```json
{
  "python.analysis.extraPaths": [
    "D:/05-26-2026/AlibreScript/Alibre-Script-Stub-Files/generated/package"
  ]
}
```

## Local Editable Install

Install into the Python environment used by your IDE:

```powershell
cd D:\05-26-2026\AlibreScript\Alibre-Script-Stub-Files\generated\package
pip install -e .
```

This is usually the best workflow while the stubs are changing.

## Install From GitHub

After this repository is pushed to GitHub, install the IDE package directly from
the package subdirectory:

```powershell
pip install "git+https://github.com/stephensmitchell/AlibreScript.git#egg=alibrescript-ide-stubs&subdirectory=Alibre-Script-Stub-Files/generated/package"
```

This installs the authoring-only `AlibreScript` module for external IDEs. Do not
use this install inside the Alibre Script add-on.

This is not a GitHub Packages registry publish. It is a normal Git repository
install using `pip` and the package metadata under
`Alibre-Script-Stub-Files/generated/package`.

GitHub Packages does not currently provide a PyPI-compatible Python package
registry. Use PyPI/TestPyPI for a real Python package registry, or keep using the
GitHub repository URL above for private/local IDE installs.

## Local Wheel Or Source Distribution

From the package folder:

```powershell
python setup.py sdist bdist_wheel
```

If `bdist_wheel` is not available:

```powershell
pip install wheel
python setup.py sdist bdist_wheel
```

Install the built wheel manually:

```powershell
pip install dist\alibrescript_ide_stubs-0.1.0-py2.py3-none-any.whl
```

## Publish To PyPI

Publishing should be done from a normal Python environment outside Alibre, not
from the Alibre Script console.

Recommended flow:

```powershell
cd D:\05-26-2026\AlibreScript\Alibre-Script-Stub-Files\generated\package
python setup.py sdist bdist_wheel
twine check dist\*
twine upload dist\*
```

Use TestPyPI first for a dry run:

```powershell
twine upload --repository testpypi dist\*
```

Before public publishing:

- Confirm the package name is available.
- Confirm the project license and Alibre trademark/disclaimer text are acceptable.
- Make clear that the package is unofficial and authoring-only.
- Keep the runtime mock compatible with IronPython 2.7.10.

## Regenerate And Validate

From `alibre-script.api.text`:

```powershell
python tools\generate_stubs.py
python tools\audit_stubs.py
```
