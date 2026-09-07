import math
from AlibreScript import *
part = Part('a_new_sk')
sketch3D = part.Add3DSketch('My3DSketch')
if sketch3D is None:
    raise Exception("Failed to create 3D sketch.")
sketch3D.StartEditing()
# Define start and end points of the line
startPoint = [0, 0, 0]  # Replace x1, y1, z1 with your start point coordinates
endPoint = [10, 10, 10]    # Replace x2, y2, z2 with your end point coordinates
# Add the line to the sketch
sketch3D.AddLine(startPoint, endPoint)
sketch3D.StopEditing()
print("Line added to 3D sketch successfully.")