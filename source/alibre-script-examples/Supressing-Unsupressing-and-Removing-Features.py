#https://help.alibre.com/articles/#!alibre-help-v23/supressing-unsupressing-and-removing-features
# create a part
P = Part('Example Part')
# create a cube
CubeSketch = P.AddSketch('CubeProfile', P.GetPlane('XY-Plane'))
CubeSketch.AddRectangle(0, 0, 10, 10, False)
CubeFeature = P.AddExtrudeBoss('Cube', CubeSketch, 10, True)
# cut a hole in the cube
HoleSketch = P.AddSketch('HoleProfile', P.GetPlane('XY-Plane'))
HoleSketch.AddRectangle(2, 2, 8, 8, False)
HoleFeature = P.AddExtrudeCut('Hole', HoleSketch, 10, True)
# suppress the cube using the name of the feature
P.SuppressFeature('Cube')
# unsuppress the cube using the feature object
P.UnsuppressFeature(CubeFeature)
# remove the hole using the name of the feature
P.RemoveFeature('Hole')
# remove the hole sketch using the sketch object
P.RemoveSketch(HoleSketch)