#https://help.alibre.com/articles/#!alibre-help-v23/drop-down-lists
import glob
import os
import re
# default diameter to show
DefaultDiameter = 'M6'
# called when an input changes in the dialog window
def InputChanged(Index, Value):
  # size changed
  if Index == 0:
    Size = DiameterNames[Value]
    print Size
# called when user confirms selections
def SelectionMade(Values):
  # get values
  Size = DiameterNames[Values[0]]
  print Size
# get access to windows functionality
Win = Windows()
# list of diameters to choose from
DiameterNames = ['M6', 'M8', 'M10', 'M12']
# create dialog window
Options = []
Options.append(['Size', WindowsInputTypes.StringList, DiameterNames, DefaultDiameter])
# show dialog window to user
DialogWidth = 400
Win.UtilityDialog('Test', 'Apply', SelectionMade, InputChanged, Options, DialogWidth)