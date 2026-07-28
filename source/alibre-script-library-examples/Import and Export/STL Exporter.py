# exports rotated STLs with a specific face on the bottom
ScriptName = 'STL Exporter'
Win = Windows()
# called when an input changes in the dialog window
def InputChanged(Index, Value):
  # use custom settings changed
  if Index == Index_UseCustom:
    UpdateUserInterface()
# updates the user interface based on the current selections made
def UpdateUserInterface():
  UseCustom = Win.GetInputValue(Index_UseCustom)
  if UseCustom == True:
    Win.EnableInput(Index_MaxCellSize)
    Win.EnableInput(Index_NormalDeviation)
    Win.EnableInput(Index_SurfaceDeviation)
  else:
    Win.DisableInput(Index_MaxCellSize)
    Win.DisableInput(Index_NormalDeviation)
    Win.DisableInput(Index_SurfaceDeviation)
# get current settings, if any
CurrentSettings = CurrentPart().GetUserData('alibre.stlexporter.settings')
if CurrentSettings == None:
  CurrentSettings = {}
# define options to show in dialog window
Options = []
Options.append(['File Name', WindowsInputTypes.SaveFile, CurrentSettings['FileName'] if 'FileName' in CurrentSettings else None])
Index_FileName = 0
Options.append(['Bottom Face', WindowsInputTypes.Face, CurrentPart().GetFace(CurrentSettings['BottomFace']) if 'BottomFace' in CurrentSettings else None])
Index_BottomFace = 1
Options.append(['Force STL units to millimeters', WindowsInputTypes.Boolean, CurrentSettings['ForceMM'] if 'ForceMM' in CurrentSettings else True])
Index_ForceMM = 2
Options.append(['Use Custom Settings', WindowsInputTypes.Boolean, CurrentSettings['UseCustom'] if 'UseCustom' in CurrentSettings else False])
Index_UseCustom = 3
Options.append(['Custom Normal Deviation', WindowsInputTypes.Real, CurrentSettings['NormalDev'] if 'NormalDev' in CurrentSettings else 10])
Index_NormalDeviation = 4
Options.append([None, WindowsInputTypes.Image, 'NormalDeviation.jpg', 170])
Options.append(['Custom Surface Deviation', WindowsInputTypes.Real, CurrentSettings['SurfaceDev'] if 'SurfaceDev' in CurrentSettings else 0])
Index_SurfaceDeviation = 6
Options.append([None, WindowsInputTypes.Image, 'SurfaceDeviation.jpg', 170])
Options.append(['Custom Max Cell Size', WindowsInputTypes.Real, CurrentSettings['MaxCellSize'] if 'MaxCellSize' in CurrentSettings else 0])
Index_MaxCellSize = 8
Options.append([None, WindowsInputTypes.Image, 'MaxCellSize.jpg', 170])
# show dialog to user, get inputs
Values = Win.OptionsDialog(ScriptName, Options, 170, InputChanged, UpdateUserInterface)
if Values == None:
  sys.exit()
# get the inputs
BottomFace = Values[Index_BottomFace]
CurrentSettings['BottomFace'] = BottomFace.Name
CurrentSettings['FileName'] = Values[Index_FileName]
CurrentSettings['ForceMM'] = Values[Index_ForceMM]
CurrentSettings['UseCustom'] = Values[Index_UseCustom]
CurrentSettings['MaxCellSize'] = Values[Index_MaxCellSize]
CurrentSettings['NormalDev'] = Values[Index_NormalDeviation]
CurrentSettings['SurfaceDev'] = Values[Index_SurfaceDeviation]
# update settings on part
CurrentPart().SetUserData('alibre.stlexporter.settings', CurrentSettings)
if CurrentSettings['FileName'] == "":
  Win.ErrorDialog('No filename entered', ScriptName)
  sys.exit()
if BottomFace == None:
  Win.ErrorDialog('No bottom face selected', ScriptName)
  sys.exit()
# export rotated stl
MyPart = CurrentPart()
MyPart.ExportRotatedSTL(CurrentSettings['FileName'], BottomFace,
  CurrentSettings['ForceMM'], CurrentSettings['UseCustom'], CurrentSettings['MaxCellSize'],
  CurrentSettings['NormalDev'], CurrentSettings['SurfaceDev'])
Win.InfoDialog('Export completed', ScriptName)
