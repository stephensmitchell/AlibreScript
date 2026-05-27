#https://help.alibre.com/articles/#!alibre-help-v23/bolt-creator
MyPart = Part('My Part')
XYPlane = MyPart.GetPlane('XY-Plane')
HeadSketch = MyPart.AddSketch('Head', XYPlane)
HeadSketch.AddCircle(0, 0, 10, False)
BoltHead = MyPart.AddExtrudeBoss('Bolt Head', HeadSketch, 5, False)
HeadBottomPlane = MyPart.AddPlane('Head Bottom', XYPlane, 5)
ShoulderSketch = MyPart.AddSketch('Shoulder', HeadBottomPlane)
ShoulderSketch.AddCircle(0, 0, 5, False)
BoltShoulder = MyPart.AddExtrudeBoss('Bolt Shoulder', ShoulderSketch, 20, False)
HexSketch = MyPart.AddSketch('Hex', XYPlane)
HexSketch.AddPolygon(0, 0, 5, 6, False)
HexRecess = MyPart.AddExtrudeCut('Hex Recess', HexSketch, 3, False)
# save and export, replace paths with your own
#Remove the "#" from the lines below to make them active
#MyPart.Save('C:\Users\YourUserName\Desktop')
#MyPart.ExportSTL('C:\Users\YourUserName\Desktop\My Part.stl')
#MyPart.Close()
