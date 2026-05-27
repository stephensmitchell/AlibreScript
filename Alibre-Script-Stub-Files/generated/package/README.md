# alibrescript-ide-stubs

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

Full usage and publishing notes:

```text
..\..\..\alibre-script.api.text\docs\PACKAGE-USAGE.md
```
