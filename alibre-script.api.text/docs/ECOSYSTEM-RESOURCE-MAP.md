# Ecosystem Resource Map

This repository sits inside a larger Alibre Script workspace. Use the sibling
folders together, but give each folder a clear job.

## Recommended Trust Order

1. `alibre-script.api.text/alibre.script.api3.csv`
   - Best compact source of truth for API member names, overloads, and summaries.
2. `alibre-script.api.text/alibre.script.api2.csv`
   - Broader fallback when `api3` is missing a member.
3. `Alibre-Script.Reflected/sources/`
   - Per-class reflected text files. Good for class-level lookup and parameter names.
4. `Alibre-Script.Reflected/output/`
   - Generated Python-like classes. Good for browsing methods by class.
5. `../alibre-script-examples/` and `../alibre-script-library-examples/`
   - Working style references and complete script patterns.
6. `Alibre-Script-Stub-Files/`
   - Editor autocomplete and mock/reference material. Useful, but not authoritative.
7. `Alibre-Script-Code-Assistant/`
   - AI-generated example seeds. Validate carefully before reuse.

## Folder Roles

### `Alibre-Script-Code-Assistant/`

Contains scripts from the custom GPT. Use this as a prompt/example corpus for
common requests such as plates, bolts, holes, helices, flanges, and dialog-driven
scripts.

Do not treat these scripts as proven API usage. Some generated examples may use
ambiguous terms like radius/diameter or less stable feature references. Validate
against the API CSV and the official example scripts.

Useful searches:

```powershell
rg -n "CurrentPart|Part\(|AddSketch|AddExtrude|OptionsDialog|WindowsInputTypes" ..\Alibre-Script-Code-Assistant
```

### `Alibre-Script-Stub-Files/`

Contains `.py`, `.pyi`, and mock files for working outside Alibre Design.
Use these for:

- editor autocomplete
- quick symbol search
- draft static analysis
- seeing friendlier parameter names in some mock files

Caveat: Python does not support true overloaded methods by repeating the same
`def` name. These files are reference aids, not executable truth. Confirm
overloads in `alibre.script.api3.csv` or `alibre.script.api2.csv`.

Useful files:

- `AlibreScriptAPI_Mock.py`: Python 2.7-style mock/reference with readable parameter names.
- `mock_api.py`: generated mock with many signatures.
- `alibre_script_api_docs.pyi`: type-stub style reference.
- `alibre_script_api_python27_docs.py`: Python 2.7-oriented docs.

Useful searches:

```powershell
rg -n "def AddPlane|def AddAxis|def AddSketch|class Part|class Windows" ..\Alibre-Script-Stub-Files
```

### `Alibre-Script.Reflected/`

Contains reflected output from `AlibreScriptAddOn.dll`.
Use it when you need class-specific context or parameter names beyond the CSV.

Best folders:

- `sources/`: per-class reflected text files.
- `output/`: generated Python-like classes.
- `generate.py`: generator script that created the reflected output.
- `test.packages/`: packaging experiments for local imports.

Useful searches:

```powershell
rg -n "AddPlane|AddAxis|AddPoint" ..\Alibre-Script.Reflected\sources ..\Alibre-Script.Reflected\output
rg -n "class Part|class Plane|class Axis|class Windows" ..\Alibre-Script.Reflected\output
```

## Practical LLM Workflow

For a new Alibre Script request:

1. Read `llms.txt` and `AGENTS.md`.
2. Search `alibre.script.api3.csv` for exact API calls.
3. Search `Alibre-Script.Reflected/sources/` for class-specific parameter names.
4. Search official examples for working usage.
5. Search Code Assistant examples only for task shape or prompt ideas.
6. Produce IronPython 2.7-compatible script.
7. Note any UI operation that had to be represented with lower-level geometry.

## Practical Agent Workflow

Use this retrieval bundle when the task involves reference geometry:

```powershell
rg -n "AddPlane|AddAxis|AddPoint|GetPlane|GetAxis" `
  .\alibre.script.api3.csv `
  ..\Alibre-Script.Reflected\sources `
  ..\Alibre-Script.Reflected\output `
  ..\alibre-script-examples `
  ..\alibre-script-library-examples
```

Use this retrieval bundle when the task involves sketches/features:

```powershell
rg -n "AddSketch|AddRectangle|AddCircle|AddLine|AddExtrude|AddRevolve|AddLoft|AddSweep" `
  .\alibre.script.api3.csv `
  ..\Alibre-Script.Reflected\sources `
  ..\Alibre-Script.Reflected\output `
  ..\alibre-script-examples `
  ..\alibre-script-library-examples
```

Use this retrieval bundle when the task involves dialogs:

```powershell
rg -n "WindowsInputTypes|OptionsDialog|UtilityDialog|Options.append" `
  .\alibre.script.api3.csv `
  ..\Alibre-Script.Reflected\sources `
  ..\Alibre-Script-Stub-Files `
  ..\alibre-script-examples `
  ..\alibre-script-library-examples
```

## Editor Setup Idea

For VS Code or another editor, use the stub files for completion while keeping
the API CSV open for confirmation:

1. Open the workspace root `D:\05-26-2026\AlibreScript`.
2. Keep `alibre-script.api.text/llms.txt` and `AGENTS.md` in context.
3. Add `Alibre-Script-Stub-Files/` and `Alibre-Script.Reflected/output/` to the
   editor search scope.
4. Use generated stubs for autocomplete hints only.
5. Run final scripts inside Alibre Script, not against the mocks.

## Prompt Pattern

```text
Use the Alibre Script workspace at D:\05-26-2026\AlibreScript.
Trust alibre-script.api.text/alibre.script.api3.csv first.
Use Alibre-Script.Reflected/sources for class-specific parameter context.
Use Alibre-Script-Stub-Files only for autocomplete/reference.
Use Alibre-Script-Code-Assistant examples only as unverified seeds.

Write IronPython 2.7-compatible Alibre Script for:
[task]

Return the complete script and list the API calls used.
```
