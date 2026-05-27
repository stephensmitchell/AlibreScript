# SimpleEE (Simple Equation Editor)

ID: A7246742B-23
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: February 7, 2025 11:01 PM
AI summary: A dynamic equation editor for Alibre Script allows users to edit parameters in real-time within an active part window, handling equations and numeric values while regenerating the part upon changes.

```python
#===========================================================
# AlibreScript: Dynamic Equation Editor (using CurrentPart)
#===========================================================
#
# Provides a simple “equation editor” style UI for the currently
# active/open part window.  Lists all parameters, lets the
# user edit each parameter’s equation (or numeric value),
# and regenerates in real time upon each edit.
#
# NOTES / LIMITATIONS:
#  1) Must have a part window active so that CurrentPart() is valid.
#  2) If a parameter has no equation, we display its numeric value
#     as a string. Otherwise, we display its .Equation text.
#  3) When user changes the text, we first try assigning
#     param.Equation = newText. If it fails, we next try numeric .Value.
#  4) A more robust script might handle invalid expressions more gracefully.
#  5) This script is entirely “flat”: no class or advanced function usage,
#     except the minimal callback functions for the dialog events.
#  6) Requires AlibreScript with Windows() / UtilityDialog capabilities
#
#===========================================================

# Step 1: Get the current part
TargetPart = CurrentPart()
Units.Current = UnitTypes.Inches
if TargetPart is None:
    sys.exit("No current part window found. Please open a part and try again.")

# Step 2: Gather all parameters
AllParams = TargetPart.Parameters
if len(AllParams) == 0:
    sys.exit("The current part has no parameters defined.")

# Step 3: Build input lines for the UtilityDialog
DialogInputs = []
ParamIndexMap = []  # store index -> parameter

for idx, param in enumerate(AllParams):
    if param.Equation and len(param.Equation.strip()) > 0:
        defaultText = param.Equation
    else:
        defaultText = str(param.Value)

    DialogInputs.append([param.Name, WindowsInputTypes.String, defaultText])
    ParamIndexMap.append(param)

# Step 4: Define the realtime input-changed callback
def InputChangedCallback(InputIndex, NewValue):
    changedParam = ParamIndexMap[InputIndex]
    text = NewValue.strip()

    # Try setting the equation
    try:
        changedParam.Equation = text
    except:
        # If that fails, try numeric
        try:
            numericVal = float(text)
            changedParam.Equation = ""
            changedParam.Value = numericVal
        except:
            Win.ErrorDialog("Invalid expression or number: '%s'" % text,
                            "Parameter Update Error")
            return

    # Regenerate part
    TargetPart.Regenerate()

# Step 5: Action button callback
def ActionButtonCallback(ValuesList):
    # Apply all values before closing
    TargetPart.Regenerate()

# Step 6: Show the UtilityDialog
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

![SimpleEE.gif](SimpleEE.gif)