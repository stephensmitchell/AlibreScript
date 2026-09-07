#https://help.alibre.com/articles/#!alibre-help-v23/polygon-incircle
import math
# diameter of circle that fits inside polygon
Diameter = 100
# number of sides
Sides = 6
# calculate exterior diameter of polygon
EDia = Diameter / math.cos(math.pi / Sides)
# create part, create polygon sketch, extrude
P = Part('Hex')
S = P.AddSketch('Hexagon', P.GetPlane('XY-Plane'))
S.AddPolygon(0, 0, EDia, Sides, False)
P.AddExtrudeBoss('Hex Head', S, 10, False)