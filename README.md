# Alibre Script examples, demos and experiments.

Examples, demos, experiments, API references, and stub files for working with Alibre Script outside and inside Alibre Design.

This project is focused on Alibre Script and IronPython 2.7.10 compatibility.

## Table Of Contents

- [What Is Here](#what-is-here)
- [Quick Start](#quick-start)
- [LLM And Agent Resources](#llm-and-agent-resources)
- [Key Files](#key-files)
- [Key Folders](#key-folders)
- [VS Code Type Checking](#vs-code-type-checking)
- [Alibre Script API Verification](#alibre-script-api-verification)
- [Notes](#notes)
- [License](#license)

## What Is Here

This repository collects:

- Alibre Script examples and showcases.
- Generated Python stubs for editor autocomplete and Pylance/Pyright checking.
- API text and CSV exports.
- A self-contained runtime verifier for the real Alibre Script environment.
- VS Code settings for local script development.

## Quick Start

Open this folder in VS Code:

```text
\AlibreScript
```

Use `main.py` for local script experiments.

Use `alibre_script_all_types_main.py` inside Alibre Script to verify the real API environment.

## LLM And Agent Resources

Use these files when working with LLMs, coding agents, or prompt-driven Alibre Script generation:

| Resource | Purpose |
| --- | --- |
| `alibre-script.api.text/llms.txt` | Short LLM entry point with primary resources, runtime assumptions, retrieval queries, and common examples. |
| `alibre-script.api.text/AGENTS.md` | Agent guide with coding rules, search strategy, and validation workflow. |
| `alibre-script.api.text/docs/API-QUICK-REFERENCE.md` | Curated API signatures and common usage patterns. |
| `alibre-script.api.text/docs/AGENT-WORKFLOWS.md` | Repeatable workflows for agent-assisted script generation. |
| `alibre-script.api.text/docs/PROMPT-TEMPLATES.md` | Copy-ready prompts for Alibre Script tasks. |
| `alibre-script.api.text/docs/ECOSYSTEM-RESOURCE-MAP.md` | Map of how the examples, reflected output, stubs, and assistant content fit together. |
| `alibre-script.api.text/docs/STUB-REVIEW.md` | Stub correctness notes and regeneration strategy. |
| `alibre-script.api.text/docs/PACKAGE-USAGE.md` | How to use the generated stubs in IDEs or package workflows. |

## Key Files

| File | Purpose |
| --- | --- |
| `alibre_script_all_types_main.py` | Self-contained verifier for Alibre Script types, globals, parameters, sketches, and 3D sketches. |
| `main.py` | Local test script for VS Code and Pylance/Pyright. |
| `pyrightconfig.json` | Points Pyright at the generated Alibre Script stubs. |
| `Alibre-Script.code-workspace` | VS Code workspace file. |
| `alibre-script.api.text/llms.txt` | LLM-friendly entry point for this API reference. |
| `alibre-script.api.text/AGENTS.md` | Coding-agent instructions for this repo. |
| `.gitignore` | Ignores caches, local output, logs, and editor noise. |

## Key Folders

| Folder | Purpose |
| --- | --- |
| `Alibre-Script-Stub-Files/` | Generated and source stub files for editor support. |
| `Alibre-Script-Stub-Files/generated/package/AlibreScript/` | Main importable stub package used by VS Code. |
| `alibre-script.api.text/` | API text, CSV exports, LLM/agent docs, examples, and stub generator tools. |
| `alibre-script.api.text/docs/` | LLM and agent workflow docs. |
| `alibre-script-examples/` | Example scripts from Alibre Script documentation. |
| `alibre-script-library-examples/` | Larger library-style examples. |
| `showcases/` | Markdown demos and testbed notes. |
| `Alibre-Script-Code-Assistant/` | Assistant-oriented examples and support content. |
| `Alibre-Script.Reflected/` | Reflected API source material. |

## VS Code Type Checking

The generated stub package is used for local editor support:

```text
Alibre-Script-Stub-Files/generated/package
```

Important Alibre Script globals are supported by the stubs and verifier, including:

```python
CurrentPart()
CurrentAssembly()
CurrentParts()
CurrentAssemblies()
ScriptFileName
ScriptFolder
```

VS Code should use `pyrightconfig.json` and `.vscode/settings.json` to find the stubs.

## Alibre Script API Verification

Run this file from the Alibre Script add-on or console:

```text
alibre_script_all_types_main.py
```

The verifier checks:

- Built-in Alibre Script globals.
- Top-level API types.
- Nested types and constants.
- Current part read/create APIs.
- 2D sketch creation.
- 3D sketch creation through a new `Part(...)`.
- Parameter creation and updates.

A clean run ends with:

```text
== Verification Summary ==
Errors: 0
Missing: 0
RESULT PASS
```

## Notes

- Alibre Script uses IronPython 2.7.10, so scripts should stay Python 2.7 compatible.
- The local CPython fallback behavior in `alibre_script_all_types_main.py` is for syntax and editor checks only.
- Real API behavior must be verified inside Alibre Script.

## License

See [LICENSE](LICENSE).

Alibre, Alibre Design, and Alibre Script names and related materials belong to their respective owners.
