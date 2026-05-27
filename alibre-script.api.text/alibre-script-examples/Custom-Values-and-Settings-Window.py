#https://help.alibre.com/articles/#!alibre-help-v23/custom-values-and-settings-window
# create windows object
Win = Windows()
# construct list of items for the window
Options = []
# ask user for text
Options.append(['Name of the item', WindowsInputTypes.String, 'Baz'])
# ask user for a floating point (real) value
Options.append(['Scale', WindowsInputTypes.Real, 1.234])
# checkbox
Options.append(['Enabled', WindowsInputTypes.Boolean, True])
# ask user for an integer
Options.append(['Count', WindowsInputTypes.Integer, 123456])
# show window and output results
# if user closes window or clicks on Cancel button then Values will be set to 'None'
Values = Win.OptionsDialog('Test', Options)
print Values