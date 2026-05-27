#https://help.alibre.com/articles/#!alibre-help-v23/everyone-loves-a-slinky
# Everyone Loves a Slinky
# Adapted from:
# http://forum.alibre.com/viewtopic.php?f=9&amp;t=5752&amp;p=30750&amp;hilit=Spring#p30750
import sys
import math
# create dialog window
Win = Windows()
Options = []
Options.append(['Angle Increment', WindowsInputTypes.Real, 0.05])
Options.append(['Loop Scale', WindowsInputTypes.Real, 0.8])
Options.append(['Height Scale', WindowsInputTypes.Real, 1.0])
Options.append(['Major Helix Width Scale', WindowsInputTypes.Real, 2.0])
Options.append(['Turn Density', WindowsInputTypes.Integer, 25])
# show dialog window and get values
Values = Win.OptionsDialog('Everyone Loves a Slinky', Options)
if Values == None:
  sys.exit('User cancelled')
AngleIncrement = Values[0]
LoopScale = Values[1]
HeightScale = Values[2]
WidthScale = Values[3]
TurnDensity = Values[4]
print 'Angle Increment = %f' % AngleIncrement
print 'Loop Scale = %f' % LoopScale
print 'Height Scale = %f' % HeightScale
print 'Width Scale = %f' % WidthScale
print 'Turn Density = %d' % TurnDensity
# create list of points for 3d sketch
Points = []
Angle = 0.0
for Pass in range(0, 437):
  X = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.cos(Angle)
  Y = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.sin(Angle)
  Z = HeightScale * Angle + LoopScale * math.sin(Angle * TurnDensity)
  Points.extend([X, Y, Z])
  Angle += AngleIncrement
# create part and add 3d sketch
Slinky = Part('Slinky')
Path = Slinky.Add3DSketch('Path')
Path.AddBspline(Points)
