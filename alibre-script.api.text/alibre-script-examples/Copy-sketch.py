#https://help.alibre.com/articles/#!alibre-help-v23/copy-sketch
MyPart = Part('MyPart')
Sketch1 = MyPart.AddSketch('Sketch1', MyPart.GetPlane('XY-Plane'))
Sketch1.AddLines([0, 10, 0, 0, 10, 0, 10, 10], False)
Sketch1.AddArcCenterStartAngle(5, 10, 10, 10, 180, False)
Sketch2 = MyPart.AddSketch('Sketch2', MyPart.GetPlane('YZ-Plane'))
Sketch2.CopyFrom(Sketch1)
