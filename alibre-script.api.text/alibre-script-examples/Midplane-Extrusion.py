#https://help.alibre.com/articles/#!alibre-help-v23/midplane-extrusion
# create the part and then a sketch containing a circle
P = Part('Test')
S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
S.AddCircle(0, 0, 9, False)
# how far we will extrude from mid-plane
ExtrudeLength = 10
# extrude it
P.AddExtrudeBoss('Cyl', S, ExtrudeLength, False, Part.EndCondition.MidPlane, None, 0, Part.DirectionType.Normal, None, 0, False)