import sys
import math
Win = Windows()
Options = []
Options.append(['Radius', WindowsInputTypes.Real, 10.0])
Options.append(['Pitch', WindowsInputTypes.Real, 5.0])
Options.append(['Turns', WindowsInputTypes.Integer, 10])
Options.append(['Angle Increment', WindowsInputTypes.Real, 0.1])
Values = Win.OptionsDialog('Helix Parameters', Options)
if Values == None:
    sys.exit('User cancelled')
Radius = Values[0]
Pitch = Values[1]
Turns = Values[2]
AngleIncrement = Values[3]
print('Radius = %f' % Radius)
print('Pitch = %f' % Pitch)
print('Turns = %d' % Turns)
print('Angle Increment = %f' % AngleIncrement)
Points = []
Angle = 0.0
HeightIncrement = Pitch / (2 * math.pi / AngleIncrement)
for Pass in range(int(Turns * (2 * math.pi / AngleIncrement))):
    X = Radius * math.cos(Angle)
    Y = Radius * math.sin(Angle)
    Z = Pass * HeightIncrement
    Points.extend([X, Y, Z])
    Angle += AngleIncrement
Helix = CurrentPart()
Path = Helix.Add3DSketch('Path')
Path.AddBspline(Points)