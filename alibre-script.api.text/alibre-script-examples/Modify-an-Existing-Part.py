#https://help.alibre.com/articles/#!alibre-help-v23/modify-an-existing-part
# demonstrates opening an existing part and adding a 3d sketch to it
# load P:\work\TestPart.AD_PRT
MyPart = Part(r'C:\Users\<username>\Desktop\ScriptDir', 'New')
# create a 3D sketch
Route = MyPart.Add3DSketch('Route')
Route.AddBspline([0, 0, 0,    5, 0, 0,    10, 5, 5,    15, 10, 5,    15, 15, 15])
