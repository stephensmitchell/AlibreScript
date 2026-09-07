#https://help.alibre.com/articles/#!alibre-help-v23/triangle
# Create triangle with angles 90, 15, 75
import math
# set up parameters
Theta = 15.0
Adjacent = 100.0
# calculate side
Opposite = Adjacent * math.tan(math.radians(Theta))
# generate three vertices of triangle
P1_X = 0
P1_Y = 0
P2_X = Adjacent
P2_Y = 0
P3_X = Adjacent
P3_Y = Opposite
# create part and sketch
P = Part('Foo')
S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
# draw it
S.AddLine(P1_X, P1_Y, P2_X, P2_Y, False)
S.AddLine(P2_X, P2_Y, P3_X, P3_Y, False)
S.AddLine(P3_X, P3_Y, P1_X, P1_Y, False)