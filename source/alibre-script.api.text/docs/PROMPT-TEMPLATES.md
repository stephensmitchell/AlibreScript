# Prompt Templates

These prompts are designed for LLMs working with this repository.

## Create Script From UI Inputs

```text
You are writing Alibre Script for IronPython 2.7.
Use the API dumps in this repo as source of truth.

Task:
Create an Alibre Script that performs this manual UI operation:
- Type:
- Inputs, in order:
- Numeric values:
- Label:

Requirements:
- Use CurrentPart() for active-part work, or CurrentAssembly() for active-assembly work.
- Use ScriptFileName/ScriptFolder if the script needs its saved location.
- Use CurrentParts()/CurrentAssemblies() only when the task needs all open documents.
- Use Python 2 compatible syntax.
- Verify method names and argument order against the API dumps.
- If an exact UI input combination is not exposed, construct equivalent geometry with exposed overloads and explain the equivalence.
- Return the complete script.
```

## Create Reference Geometry

```text
Create an Alibre Script reference-geometry script for IronPython 2.7.

Geometry needed:
- Base datums:
- Planes:
- Axes:
- Points:
- Angle signs:
- Labels in feature tree:

Use:
- P = CurrentPart()
- A = CurrentAssembly() only for assembly context
- ScriptFileName and ScriptFolder only for saved-script path context
- AddPlane/AddAxis/AddPoint overloads from alibre.script.api3.csv
- Existing examples for style

Return:
- Full script
- Short note on datum assumptions
```

## Build A Part Feature

```text
Write an Alibre Script that creates this part feature.

Part context:
- Active part or new part:
- Units:
- Base plane/face:
- Sketch geometry:
- Feature type:
- Depth/angle/end condition:

Constraints:
- IronPython 2.7 syntax only
- Put dimensions at top
- Avoid generated Face<n> references unless unavoidable
- Use simple API overloads where possible
```

## Diagnose A Failing Script

```text
Debug this Alibre Script.

Error message:

Script:

Please:
- Identify likely API signature mismatches.
- Identify Python 2 compatibility problems.
- Compare calls to alibre.script.api3.csv and examples.
- Return a corrected full script and explain only the necessary changes.
```

## Expand The Knowledge Base

```text
Improve this Alibre Script reference repo for LLM/agent use.

Goal:
- Add concise, retrieval-friendly documentation.
- Do not rewrite API dumps.
- Prefer examples and method maps.
- Keep files ASCII and small enough to embed in prompts.

Deliverables:
- Update llms.txt if new resources are added.
- Add or update docs under docs/.
- Add example scripts only when they demonstrate a reusable pattern.
```
