# sketch copier
# Demonstrates copying a sketch inside a part
Win = Windows()
ScriptName = 'Sketch Copier'
# create dialog window and show to user
Options = []
Options.append([None, WindowsInputTypes.Image, 'SketchCopier.png', 170])
Options.append(['Source Sketch', WindowsInputTypes.Sketch, None])
Options.append(['Destination Plane', WindowsInputTypes.Plane, None])
Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
  sys.exit()
# get user inputs
SourceSketch = Values[1]
DestPlane = Values[2]
MyPart = CurrentPart()
DestSketch = MyPart.AddSketch("Copy of " + SourceSketch.Name, DestPlane)
DestSketch.CopyFrom(SourceSketch)
