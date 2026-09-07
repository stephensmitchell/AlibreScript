#https://help.alibre.com/articles/#!alibre-help-v23/create-reference-planes-axes-and-points
# demonstrates creating reference geometry
# create a new part and get the xy plane
MyPart = Part('My Part')
XYPlane = MyPart.GetPlane('XY-Plane')
# create planes 100mm above and below the xy plane
TopPlane = MyPart.AddPlane('Top Plane', XYPlane, 100.0)
BottomPlane = MyPart.AddPlane('Bottom Plane', XYPlane, -100.0)
# add reference points to bottom plane
Ref1 = MyPart.AddPoint('Ref 1', 50.0, 50.0, -100.0)
Ref2 = MyPart.AddPoint('Ref 2', 50.0, -50.0, -100.0)
Ref3 = MyPart.AddPoint('Ref 3', -50.0, -50.0, -100.0)
Ref4 = MyPart.AddPoint('Ref 4', -50.0, 50.0, -100.0)
# add reference axes from points on bottom plane to center of top plane
Axis1 = MyPart.AddAxis('Axis 1', [50.0, 50.0, -100.0], [0.0, 0.0, 100.0])
Axis2 = MyPart.AddAxis('Axis 2', [50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
Axis3 = MyPart.AddAxis('Axis 3', [-50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
Axis4 = MyPart.AddAxis('Axis 4', [-50.0, 50.0, -100.0], [0.0, 0.0, 100.0])