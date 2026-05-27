# Gear Generator Script
# Used as a demonstration of how to create a custom utility
# for use with Alibre Design
Units.Current = UnitTypes.Millimeters
# default settings
NumberofTeeth = 20
PitchDiameter = 30
PressureAngle = 20
Thickness = 3
Win = Windows()
ScriptName = 'Gear Generator'
# create dialog window and show to user
Options = []
Options.append([None, WindowsInputTypes.Image, 'GearGenerator.png', 170])
Options.append(['Number of Teeth', WindowsInputTypes.Integer, NumberofTeeth])
Options.append(['Pitch Diameter (mm)', WindowsInputTypes.Real, PitchDiameter])
Options.append(['Pressure Angle', WindowsInputTypes.Real, PressureAngle])
Options.append(['Thickness (mm)', WindowsInputTypes.Real, Thickness])
Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
  sys.exit()
print "Working..."
# get user inputs
NumberofTeeth = Values[1]
PitchDiameter = Values[2]
PressureAngle = Values[3]
Thickness = Values[4]
# get current part
MyPart = CurrentPart()
# get the plane to create the gear on
GearPlane = MyPart.XYPlane
# create the sketch then extrude it
ProfileSketch = MyPart.AddGearNP("Profile", NumberofTeeth, PitchDiameter, PressureAngle, 0, 0, False, GearPlane)
Gear = MyPart.AddExtrudeBoss("Gear", ProfileSketch, Thickness, False)
print "Done"
