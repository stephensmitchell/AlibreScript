Python stub files for using Alibre Script outside of Alibre Design.

## Recommended Files

Use the generated stubs first:

- `generated/AlibreScript.py`: IronPython 2.7.10-compatible runtime mock for imports outside Alibre Design.
- `generated/AlibreScript.pyi`: editor/static-analysis stub with overload signatures.
- `generated/README.md`: generation notes.
- `generated/package/`: installable package for external IDEs and VS Code.

The older files in this folder are kept as historical/reference material. They
have known syntax and overload issues and should not be treated as authoritative.

Regenerate from `../alibre-script.api.text`:

```powershell
python tools\generate_stubs.py
python tools\audit_stubs.py
```
