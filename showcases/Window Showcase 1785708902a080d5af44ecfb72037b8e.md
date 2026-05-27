# Window Showcase

ID: A7246742B-14
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 11, 2025 9:10 AM
AI summary: Demonstrates various dialog windows in Alibre Script, including info, error, question, options, utility, open file, save file, and folder selection dialogs, with user interaction and callbacks.

```python
def windows_showcase():
    """
    Demonstrates multiple dialog windows using the Windows object.
    1) InfoDialog
    2) ErrorDialog
    3) QuestionDialog
    4) OptionsDialog
    5) UtilityDialog
    6) OpenFileDialog
    7) SaveFileDialog
    8) SelectFolderDialog
    """
    import sys

    # Create a Windows object for dialogs
    Win = Windows()
    
    # 1) Show an info dialog
    Win.InfoDialog("This is an information message.", "Information")
    
    # 2) Show an error dialog
    Win.ErrorDialog("Uh oh, something happened!", "Error")
    
    # 3) Show a question dialog (returns True for 'yes', False for 'no')
    user_chose_yes = Win.QuestionDialog("Do you want to proceed?", "Question")
    if user_chose_yes:
        print("User clicked Yes.")
    else:
        print("User clicked No.")
    
    # 4) Show an OptionsDialog for multiple inputs
    #    Each item is [Name, WindowsInputTypes, DefaultValue, ...]
    opts = []
    opts.append(["Name", WindowsInputTypes.String, "Unnamed"])
    opts.append(["Thickness (mm)", WindowsInputTypes.Real, 5.0])
    opts.append(["IncludeHoles?", WindowsInputTypes.Boolean, True])
    opts.append(["Quantity", WindowsInputTypes.Integer, 10])
    opts.append(["Material", WindowsInputTypes.StringList, ["Plastic", "Steel", "Aluminum"], "Steel"])
    
    user_values = Win.OptionsDialog("Enter Values", opts)
    if user_values is None:
        print("User canceled the OptionsDialog.")
    else:
        print("User values from OptionsDialog: {}".format(user_values))
    
    # 5) Show a UtilityDialog that remains open, with a single real input
    #    We'll create a function callback that is invoked each time the user 
    #    changes input or presses the action button.
    def on_apply_clicked(vals):
        print("Action button clicked, user entries: {}".format(vals))

    def input_changed_callback(index, value):
        print("Input at index {} changed to: {}".format(index, value))
    
    # The UtilityDialog inputs: 
    #   e.g. [ ["NameOfInput", WindowsInputTypes.Real, 1.234], ...]
    utility_inputs = [
        ["Angle", WindowsInputTypes.Real, 45.0],
        ["CheckBox", WindowsInputTypes.Boolean, True],
    ]
    
    # Show the dialog
    # Parameters: Title, ActionButtonText, ActionButtonCallback, 
    #             InputChangedCallback, InputsList, InputAreaWidth=200
    Win.UtilityDialog(
        "UtilityDialog Showcase", 
        "Apply", 
        on_apply_clicked,
        input_changed_callback,
        utility_inputs,
        250   # width of input area
    )
    # The script continues after the user closes the UtilityDialog.
    
    # 6) Prompt user to open a file. 
    file_path = Win.OpenFileDialog("Select a file", "All Files|*.*", ".txt")
    if file_path:
        print("File chosen: {}".format(file_path))
    else:
        print("User canceled open file dialog.")
    
    # 7) Prompt user to save a file
    save_path = Win.SaveFileDialog("Save your file", "Text Files|*.txt|All Files|*.*", ".txt")
    if save_path:
        print("File to save: {}".format(save_path))
    else:
        print("User canceled save file dialog.")
    
    # 8) Prompt user to select a folder
    folder_path = Win.SelectFolderDialog("", "Choose a folder for something")
    if folder_path:
        print("Folder chosen: {}".format(folder_path))
    else:
        print("User canceled folder selection.")

    print("Finished the Windows showcase.")

# To run directly in AlibreScript, just call:
# windows_showcase()

```