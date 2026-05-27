#https://help.alibre.com/articles/#!alibre-help-v23/profile-and-sweep-path
# create the part and get the yz plane
MyPart = Part('Test')
YZPlane = MyPart.GetPlane('YZ-Plane')
# create the route for the pipe
PipeRoute = MyPart.Add3DSketch('Pipe Route')
PipeRoute.AddBspline([0, 0, 0,    5, 0, 0,    10, 5, 5,    15, 10, 5,    15, 15, 15])
# create the pipe profile as a circle on the yz plane
StartProfile = MyPart.AddSketch('Start Profile', YZPlane)
StartProfile.AddCircle(0, 0, 5, False)