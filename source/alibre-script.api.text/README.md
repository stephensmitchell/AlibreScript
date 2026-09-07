# Alibre Script API Text

This repository contains local text and CSV references for the Alibre Script
IronPython 2.7 API, plus example scripts.

## LLM And Agent Resources

- `llms.txt`: compact entry point for LLM retrieval.
- `AGENTS.md`: rules and workflow guidance for coding agents.
- `docs/API-QUICK-REFERENCE.md`: curated method signatures and common patterns.
- `docs/AGENT-WORKFLOWS.md`: repeatable workflows for script generation and debugging.
- `docs/PROMPT-TEMPLATES.md`: copy-ready prompts for Alibre Script tasks.
- `docs/ECOSYSTEM-RESOURCE-MAP.md`: how to use sibling reflected, stub, and Code Assistant folders.
- `docs/STUB-REVIEW.md`: current correctness review and regeneration plan for stub files.
- `docs/PACKAGE-USAGE.md`: manual IDE install, GitHub install, and optional PyPI packaging workflow.
- `tools/audit_stubs.py`: read-only audit tool for checking stubs against the API CSV.
- `tools/generate_stubs.py`: generator for clean IronPython-compatible runtime stubs and `.pyi` editor stubs.

## Source References

- `alibre.script.api3.csv`: compact API reference.
- `alibre.script.api2.csv`: broader API reference.
- `alibre.script.api.txt`: text API reference.
- `../alibre-script-examples/`: small example scripts.
- `../alibre-script-library-examples/`: larger utility examples.
