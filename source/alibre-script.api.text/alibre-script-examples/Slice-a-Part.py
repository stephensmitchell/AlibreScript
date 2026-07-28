#https://help.alibre.com/articles/#!alibre-help-v23/slice-a-part
# open part, replace with your own path
P = Part(r'C:\Users\Brian\Desktop\ScriptDir', 'New2')
# get bounding box of part - eight points, one for each corner
# of the bounding box
Bounds = P.GetBoundingBox()
# get the plane that the part will be sliced on
SlicePlane = P.GetPlane('Slice')
# create a sketch on the slicing plane
S = P.AddSketch('SliceSketch', SlicePlane)
# empty list
Proj = []
# for each corner of the part bounding box, map that 3D point into
# a 2D point on the sketch
# this doesn't create the points in the sketch, but is only a mathematical
# operation
for i in range(0, 8):
  Proj.append(S.GlobaltoPoint(Bounds[i][0], Bounds[i][1], Bounds[i][2]))
# go through the eight 2D points and find the maximum and minimum
# X and Y values
MaxX = Proj[0][0]
for i in range (0, 8):
  if Proj[i][0] >= MaxX :
    MaxX = Proj[i][0]
MaxY = Proj[0][1]
for i in range (0, 8):
  if Proj[i][1] >= MaxY :
    MaxY = Proj[i][1]
MinX = Proj[0][0]
for i in range (0, 8):
  if Proj[i][0] < MinX :
    MinX = Proj[i][0]
MinY = Proj[0][1]
for i in range (0, 8):
  if Proj[i][1] < MinY :
    MinY = Proj[i][1]
# draw a rectangle on the sketch which will cover the entire part when viewed
# perpendicular to the slicing plane
S.AddRectangle(MinX, MinY, MaxX, MaxY, False)
# cut the part using the rectangle
P.AddExtrudeCut('Cut', S, 100, False)