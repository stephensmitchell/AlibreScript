# Generated Alibre Script Stubs

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
python tools\generate_stubs.py
```

Install locally for an IDE:

```powershell
pip install -e package
```

Packaging and PyPI notes are documented in:

```text
..\..\alibre-script.api.text\docs\PACKAGE-USAGE.md
```

Do not install or import this package inside the Alibre Script add-on. Inside
Alibre Design, use the real built-in Alibre Script API.
