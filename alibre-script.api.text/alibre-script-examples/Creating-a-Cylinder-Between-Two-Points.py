#https://help.alibre.com/articles/#!alibre-help-v23/creating-a-cylinder-between-two-points
# creates a cylinder between two arbitrary points
from math import sqrt
# ends of cylinder are centered on these points
cyl_p1 = [1, 5, 2]
cyl_p2 = [10, 14, 8]
# diameter of cylinder
diameter = 6
# get length of cynlinder using euclidean distance
length = sqrt((cyl_p2[0] - cyl_p1[0])**2 + (cyl_p2[1] - cyl_p1[1])**2 + (cyl_p2[2] - cyl_p1[2])**2)
# calculate normal vector for the plane at the first end of the cylinder
normal_vector = [cyl_p2[0] - cyl_p1[0], cyl_p2[1] - cyl_p1[1], cyl_p2[2] - cyl_p1[2]]
# create part
P = Part('Cylinder')
# create plane for one end of the cylinder
cyl_plane = P.AddPlane('Cyl Start Plane', normal_vector, cyl_p1)
P.AddAxis('Cylinder Axis', cyl_p1, cyl_p2)
# draw a circle on the plane
S = P.AddSketch('Cylinder End', cyl_plane)
[cx, cy] = S.GlobaltoPoint(cyl_p1[0], cyl_p1[1], cyl_p1[2])
S.AddCircle(cx, cy, diameter, False)
# extrude into a cylinder
P.AddExtrudeBoss('Cylinder', S, length, False)