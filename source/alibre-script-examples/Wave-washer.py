#https://help.alibre.com/articles/#!alibre-help-v23/wave-washer
import math
from math import *
# radius
R = 100.0
# amplitude
A = 10.0
# number of waves (must be a whole number)
B = 4
# width
Width = 10
# thickness
Thickness = 5
Win = Windows()
Options = []
Options.append(['Radius', WindowsInputTypes.Real, R])
Options.append(['Amplitude', WindowsInputTypes.Real, A])
Options.append(['Number of Waves', WindowsInputTypes.Integer, B])
Options.append(['Width', WindowsInputTypes.Real, Width])
Options.append(['Thickness', WindowsInputTypes.Real, Thickness])
Values = Win.OptionsDialog('Wave Washer Generator', Options)
if Values == None:
  sys.exit()
R = Values[0]
A = Values[1]
B = Values[2]
Width = Values[3]
Thickness = Values[4]
# path accuracy = lower number = more points calculated
t_step = 0.1
# complete circle = PI x 2
t_max = 3.141592 * 2
# keep track of the total points we have calculated
TotalPoints = 0
# calculate points for 3D sketch
PathPoints = []
t = 0
while True:
  X = R * sin(t)
  Y = R * cos(t)
  Z = A * sin(B * t)
  PathPoints.extend([X, Y, Z])
  if TotalPoints == 0:
    P1 = [X, Y, Z]
  elif TotalPoints == 1:
    P2 = [X, Y, Z]
  t = t + t_step
  TotalPoints = TotalPoints + 1
  if t >= t_max:
    break
# close path
PathPoints.extend([PathPoints[0], PathPoints[1], PathPoints[2]])
# create part and add 3d sketch
P = Part('Wave Washer')
Path = P.Add3DSketch('Path')
Path.AddBspline(PathPoints)
# calculate normal vector for the plane at the start of the path
normal_vector = [P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]]
# create plane at the start of the path
Plane = P.AddPlane('Start Plane', normal_vector, P1)
CrossSection = P.AddSketch('Cross Section', Plane)
Origin = CrossSection.GlobaltoPoint(P1[0], P1[1], P1[2])
CrossSection.AddRectangle(Origin[0] - (Thickness / 2.0), Origin[1] - (Width / 2.0), Origin[0] + (Thickness / 2.0), Origin[1] + (Width / 2.0), False)
P.AddSweepBoss('Washer', CrossSection, Path, False, Part.EndCondition.EntirePath, None, 0, 0, False)
