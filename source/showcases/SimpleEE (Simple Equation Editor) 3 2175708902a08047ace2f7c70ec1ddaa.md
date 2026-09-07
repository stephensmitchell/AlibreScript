# SimpleEE (Simple Equation Editor) 3

ID: A7246742B-33
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: June 18, 2025 9:41 PM
AI summary: Dynamic Equation Editor in Python for Alibre Script. Updates parameter equations and values in real time, handles invalid inputs, and provides an interface for input changes.

```python
#===========================================================
#  Dynamic Equation Editor – refresh-enabled version
#===========================================================

import sys
TargetPart = CurrentPart()
Units.Current = UnitTypes.Inches
if TargetPart is None:
    sys.exit("No current part window found. Please open a part and try again.")

AllParams = TargetPart.Parameters
if len(AllParams) == 0:
    sys.exit("The current part has no parameters defined.")

DialogInputs   = []
ParamIndexMap  = []

for p in AllParams:
    DialogInputs.append([
        p.Name,
        WindowsInputTypes.String,
        p.Equation.strip() if p.Equation else str(p.Value)
    ])
    ParamIndexMap.append(p)

# ---------- helpers ----------------------------------------------------------
_prog_update = False          # prevents infinite callback recursion

def RefreshDialog(exclude=None):
    """Push the latest equation/value of every parameter into its textbox."""
    global _prog_update
    _prog_update = True
    for i, prm in enumerate(ParamIndexMap):
        if i == exclude:       # leave the box the user is typing in untouched
            continue
        txt = prm.Equation.strip() if prm.Equation else str(prm.Value)
        Win.SetInputValue(i, txt)    # << the magic sync call
    _prog_update = False
# -----------------------------------------------------------------------------

def InputChangedCallback(InputIndex, NewValue):
    if _prog_update:           # ignore programmatic updates
        return

    prm  = ParamIndexMap[InputIndex]
    text = NewValue.strip()

    try:                       # 1) try equation
        prm.Equation = text
    except:
        try:                   # 2) try numeric literal
            prm.Equation = ""
            prm.Value    = float(text)
        except:
            Win.ErrorDialog("Invalid expression or number: '%s'" % text,
                            "Parameter Update Error")
            RefreshDialog(exclude=InputIndex)   # roll back visible value
            return

    TargetPart.Regenerate()
    RefreshDialog(exclude=InputIndex)           # show new driven values

def ActionButtonCallback(vals):
    TargetPart.Regenerate()
    RefreshDialog()                              # full refresh

Win = Windows()
Win.UtilityDialog(
    "SimpleEE",
    "Regenerate",
    ActionButtonCallback,
    InputChangedCallback,
    DialogInputs,
    500
)

```