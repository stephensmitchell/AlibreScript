# Agent Guide

This repository is a compact local knowledge base for Alibre Script and its
IronPython 2.7 API. Treat the API dumps as source of truth and the example
folders as executable style references.

## Project Map

- `alibre.script.api3.csv`: preferred compact API reference.
- `alibre.script.api2.csv`: broader CSV reference; useful if `api3` is missing a member.
- `alibre.script.api.txt`: XML-doc style API reference with member prefixes.
- `../alibre-script-examples/`: small scripts that show common part, sketch, plane, axis, and feature workflows.
- `../alibre-script-library-examples/`: larger utility scripts with dialogs, selection inputs, exports, and reusable workflows.
- `docs/API-QUICK-REFERENCE.md`: curated signatures and patterns for common agent tasks.
- `docs/AGENT-WORKFLOWS.md`: task decomposition and validation checklist.
- `docs/PROMPT-TEMPLATES.md`: prompts that help an LLM produce Alibre Script reliably.
- `docs/ECOSYSTEM-RESOURCE-MAP.md`: explains how to use sibling reflected, stub, and Code Assistant folders.
- `docs/STUB-REVIEW.md`: stub correctness findings and regeneration rules.
- `docs/PACKAGE-USAGE.md`: packaging and IDE installation workflow for generated stubs.
- `tools/generate_stubs.py`: generates the clean stub package under `../Alibre-Script-Stub-Files/generated/`.

## Coding Rules

- Target Alibre Script running on IronPython 2.7.
- Use Python 2 compatible syntax: no f-strings, no type annotations, no pathlib.
- `ScriptFileName` and `ScriptFolder` are built-in globals in Alibre Script.
- Prefer `CurrentPart()` when modifying the active open part.
- Prefer `CurrentAssembly()` when modifying the active open assembly.
- Use `CurrentParts()` and `CurrentAssemblies()` when enumerating open documents.
- Prefer `Part('Name')` only when intentionally creating a new part.
- Use exact API signatures from the CSV/text dumps before inventing a call.
- Keep scripts short and parameterized at the top.
- Use lists like `[x, y, z]` for 3D points and vectors.
- Use degrees for Alibre angle arguments unless an example proves otherwise.
- Avoid relying on generated face names such as `Face<5>` unless the script creates the feature immediately before using that face.
- For UI-like operations that are not exposed directly by the API, reproduce the geometry with exposed lower-level calls and comment the equivalence.
- Treat sibling stubs and Code Assistant examples as aids, not authority. Confirm signatures in the API CSV files.
- Run `python tools/audit_stubs.py` before relying on generated stubs.
- Keep generated `AlibreScript.py` IronPython 2.7.10 compatible. Put typing-only syntax in `AlibreScript.pyi`, not the runtime `.py`.

## Search Strategy

Use `rg` first:

```powershell
rg -n "AddPlane|AddAxis|AddPoint" alibre.script.api3.csv alibre.script.api2.csv alibre.script.api.txt
rg -n "AddPlane|AddAxis" ..\alibre-script-examples ..\alibre-script-library-examples
```

For a new task:

1. Search the API dump for the needed method.
2. Search examples for the same method.
3. Copy the local style and argument order.
4. Add a small script under `../alibre-script-examples/` or a reusable script under `../alibre-script-library-examples/`.
5. Include comments only where the geometry or API workaround is non-obvious.

## Validation

This repo cannot fully execute Alibre Script without Alibre Design. Validate by:

- Checking syntax for Python 2 compatibility.
- Verifying every Alibre method exists in the API dump.
- Verifying argument order against examples.
- Running the script manually in Alibre Script when CAD behavior matters.
