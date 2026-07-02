# SimpleEE (Simple Equation Editor) 2

ID: A7246742B-24
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: February 7, 2025 11:02 PM
AI summary: A Python script for a Simple Equation Editor. Users set a part's parameters in inches by choosing from size options in a dialog. The script updates each parameter's equation or numeric value in real time and reports errors for invalid inputs.

```python
def main():
    TargetPart = CurrentPart()
    Units.Current = UnitTypes.Inches
    if TargetPart is None:
        sys.exit("No current part window found. Please open a part and try again.")

    all_params = TargetPart.Parameters
    if len(all_params) == 0:
        sys.exit("The current part has no parameters defined.")

    # -------------------------------------------------
    # 1) Updated list of desired sizes
    # -------------------------------------------------
    size_options = [
        "0.13",
        "0.25",
        "0.38",
        "0.50",
        "0.63",
        "0.75",
        "0.88",
        "1.00",
        "1.13",
        "1.25",
        "1.38",
        "1.50",
        "1.63",
        "1.75",
        "1.88",
        "2.00",
        "2.13",
        "2.25",
        "2.38",
        "2.50",
        "2.63",
        "2.75",
        "2.88",
        "3.00",
        "3.13",
        "3.25",
        "3.38",
        "3.50",
        "3.63",
        "3.75",
        "3.88",
        "4.00",
        "4.13",
        "4.25",
        "4.38",
        "4.50",
        "4.63",
        "4.75",
        "4.88",
        "5.00",
        "5.13",
        "5.25",
        "5.38",
        "5.50",
        "5.63",
        "5.75",
        "5.88",
        "6.00",
        "6.13",
        "6.25",
        "6.38",
        "6.50",
        "6.63",
        "6.75",
        "6.88",
        "7.00",
        "7.13",
        "7.25",
        "7.38",
        "7.50",
        "7.63",
        "7.75",
        "7.88",
        "8.00",
        "8.13",
        "8.25",
        "8.38",
        "8.50",
        "8.63",
        "8.75",
        "8.88",
        "9.00",
        "9.13",
        "9.25",
        "9.38",
        "9.50",
        "9.63",
        "9.75",
        "9.88",
        "10.00",
        "10.13",
        "10.25",
        "10.38",
        "10.50",
        "10.63",
        "10.75",
        "10.88",
        "11.00"
    ]

    dialog_inputs = []
    param_index_map = []

    # -------------------------------------------------
    # Build the dialog inputs for each parameter
    # -------------------------------------------------
    for param in all_params:
        # Figure out the parameter's current text (equation or numeric)
        try:
            if param.Equation and len(param.Equation.strip()) > 0:
                default_text = param.Equation.strip()
            else:
                default_text = str(param.Value)
        except:
            # Skip weird/invalid parameters
            continue

        # Make a copy of size_options (so we don't mutate the original)
        custom_list = size_options[:]

        # Ensure the parameter's current value is in the list
        if default_text not in custom_list:
            custom_list.append(default_text)

        # Find the default index
        default_index = custom_list.index(default_text)

        # Append [Name, WindowsInputTypes.StringList, list_of_strings, default_index]
        dialog_inputs.append([
            param.Name,
            WindowsInputTypes.StringList,
            custom_list,
            default_index
        ])
        param_index_map.append(param)

    if not dialog_inputs:
        sys.exit("No valid parameters found.")

    # -------------------------------------------------
    # Real-time "changed" callback
    # -------------------------------------------------
    def input_changed_callback(input_index, new_value):
        changed_param = param_index_map[input_index]

        # Retrieve the list of choices for this input row (3rd item)
        choice_list = dialog_inputs[input_index][2]

        # Determine if new_value is an integer (index) or already a string
        if isinstance(new_value, int):
            # new_value is an index
            if new_value < 0 or new_value >= len(choice_list):
                Win.ErrorDialog("Index out of range: {}".format(new_value),
                                "Parameter Update Error")
                return
            text = choice_list[new_value].strip()
        else:
            # new_value is likely a string
            text = str(new_value).strip()

        # First, try to assign as an Equation
        try:
            changed_param.Equation = text
        except:
            # Fallback: numeric
            try:
                numeric_val = float(text)
                changed_param.Equation = ""
                changed_param.Value = numeric_val
            except:
                Win.ErrorDialog(
                    "Could not set parameter '{}' to '{}'.\n"
                    "Neither a valid equation nor a valid number."
                    .format(changed_param.Name, text),
                    "Parameter Update Error"
                )
                return

        # Regenerate the part
        try:
            TargetPart.Regenerate()
        except:
            Win.ErrorDialog(
                "Error regenerating part after setting '{}'."
                .format(changed_param.Name),
                "Regeneration Error"
            )

    # -------------------------------------------------
    # "Regenerate" button callback
    # -------------------------------------------------
    def action_button_callback(values_list):
        try:
            TargetPart.Regenerate()
        except:
            Win.ErrorDialog("Error regenerating part on final apply.",
                            "Regeneration Error")

    # -------------------------------------------------
    # Show the dialog
    # -------------------------------------------------
    Win = Windows()
    Win.UtilityDialog(
        "SimpleEE 2",
        "Regenerate",
        action_button_callback,
        input_changed_callback,
        dialog_inputs,
        500
    )

# Finally, call main()
main()

```

![SimpleEE 2.gif](SimpleEE_2.gif)