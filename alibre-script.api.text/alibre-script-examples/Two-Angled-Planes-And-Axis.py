# Creates the reference geometry shown in the tree:
#   16 degree plane
#   Axis<2>
#   30 degree plane

from math import sin, cos, radians

P = CurrentPart()

Angle16 = 16.0
Angle30 = -30.0
AxisLength = 100.0

XYPlane = P.GetPlane('XY-Plane')
YZPlane = P.GetPlane('YZ-Plane')
XAxis = P.GetAxis('X-Axis')

# Create the first angled plane.
# This makes "16 degree" from XY-Plane, rotated about X-Axis.
Plane16 = P.AddPlane('16 degree', XYPlane, XAxis, Angle16)

# Create Axis<2>, equivalent to selecting Origin and the 16 degree plane.
# The script API does not expose that exact UI input pair, so this creates
# the same axis using two points: origin and a point along Plane16's normal.
Angle16Rad = radians(Angle16)
AxisStart = [0.0, 0.0, 0.0]
AxisEnd = [0.0, -sin(Angle16Rad) * AxisLength, cos(Angle16Rad) * AxisLength]
Axis2 = P.AddAxis('Axis<2>', AxisStart, AxisEnd)

# Create the second angled plane.
# This matches the dialog inputs: YZ-Plane, Axis<2>, -30 degrees.
Plane30 = P.AddPlane('30 degree', YZPlane, Axis2, Angle30)
