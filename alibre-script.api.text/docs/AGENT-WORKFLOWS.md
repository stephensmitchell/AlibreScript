# Agent Workflows

## Generate A New Alibre Script

1. Restate the target geometry in terms of datums, sketches, features, and dimensions.
2. Search the API dump for each needed method.
3. Search examples for the closest working script.
4. Choose `CurrentPart()` for active-part scripts, `CurrentAssembly()` for active-assembly scripts, `CurrentParts()`/`CurrentAssemblies()` for open-document enumeration, or `Part('Name')` for generated demo parts.
5. Put editable dimensions and angles at the top.
6. Create reference geometry before sketches and features.
7. Avoid generated face names unless there is no stable alternative.
8. Add short comments for geometry transforms, axis directions, and API workarounds.

## Convert A Manual UI Operation To Script

Capture the UI inputs as:

- feature type
- selected references in order
- numeric values with signs
- feature label

Then map them to API calls. If the exact input combination is not exposed,
construct equivalent geometry with available overloads.

Example: UI axis from `Origin` and `16 degree` plane.

- No `AddAxis(name, point, plane)` overload is listed.
- Use `AddAxis(name, pointA, pointB)`.
- Let `pointA` be origin.
- Let `pointB` be any point along the target plane normal.

## Debug A Script That Fails In Alibre

Check these first:

- Python 3 syntax accidentally used in IronPython 2.7.
- Wrong method overload or argument order.
- Passing a name string where an API object is required.
- Angle sign reversed.
- Plane/axis selected in the wrong order.
- Face names changed because feature creation order changed.
- A method exists in one API dump but not in the installed Alibre version.

## Retrieval Checklist

Use these searches before editing:

```powershell
rg -n "MethodName" alibre.script.api3.csv alibre.script.api2.csv alibre.script.api.txt
rg -n "MethodName" ..\alibre-script-examples ..\alibre-script-library-examples
```

For reference geometry:

```powershell
rg -n "AddPlane|AddAxis|AddPoint|GetPlane|GetAxis" alibre.script.api3.csv ..\alibre-script-examples
```

For sketches and features:

```powershell
rg -n "AddSketch|AddRectangle|AddCircle|AddExtrude|AddRevolve|AddLoft|AddSweep" alibre.script.api3.csv ..\alibre-script-examples
```

For dialogs:

```powershell
rg -n "WindowsInputTypes|OptionsDialog|UtilityDialog|Options.append" ..\alibre-script-examples ..\alibre-script-library-examples
```

## Output Format For Agents

When answering with a script:

- Give the full script first.
- Then list the exact API calls used.
- Mention any assumptions about datum orientation or angle sign.
- Mention whether it modifies the active part or creates a new part.

When editing this repo:

- Keep generated helper docs small enough for retrieval.
- Add examples with descriptive filenames.
- Update `llms.txt` when adding important new resources.
