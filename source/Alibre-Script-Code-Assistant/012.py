import sys
import math
Win = Windows()
Options = []
Options.append(['Angle Increment', WindowsInputTypes.Real, 0.05])
Options.append(['Radius', WindowsInputTypes.Real, 1.0])
Options.append(['Height Increment', WindowsInputTypes.Real, 0.1])
Options.append(['Turns', WindowsInputTypes.Integer, 20])
Values = Win.OptionsDialog('Helix Parameters', Options)
if Values is None:
  sys.exit('User cancelled')
AngleIncrement = Values[0]
Radius = Values[1]
HeightIncrement = Values[2]
Turns = Values[3]
Points = []
Angle = 0.0
Height = 0.0
TotalAngle = 2 * math.pi * Turns
while Angle <= TotalAngle:
    X = Radius * math.cos(Angle)
    Y = Radius * math.sin(Angle)
    Z = Height
    Points.extend([X, Y, Z])
    Angle += AngleIncrement
    Height += HeightIncrement * AngleIncrement / (2 * math.pi) 
HelixPart = Part('Helix')
Path = HelixPart.Add3DSketch('Path')
Path.AddBspline(Points)