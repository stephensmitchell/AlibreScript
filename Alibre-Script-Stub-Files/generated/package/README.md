# Alibre Script type stubs

Editor autocomplete and type hints for the Alibre Script API.

Generated from `AlibreScriptAddOn` 6.1.0.0 and the matching `AlibreScriptAPI.xml`, both read from an
installed Alibre Design. Return types, property types and parameter names come
from assembly reflection; summaries and parameter descriptions come from the
XML documentation.

## Use

Point the language server at the directory containing the package:

```json
{
  "python.analysis.extraPaths": ["path/to/generated/package"]
}
```

Then, for editor support only:

```python
from AlibreScript import *
```

## Authoring only

Alibre Script runs on IronPython 2.7.10 inside Alibre Design, which supplies the
real API as built-in globals. Never import this package inside a live Alibre
script. The runtime `__init__.py` raises on every call by design; it exists so
the import resolves outside Alibre, not so the API works there.

## Regenerating

Do not hand-edit. From `alibre-script.api.text`:

```
python tools/extract_api.py tools/api_model.json
python tools/generate_stubs.py
```

The first step needs Alibre Design installed and pythonnet available. The second
reads only the committed `api_model.json`, so routine regeneration works on any
machine.
