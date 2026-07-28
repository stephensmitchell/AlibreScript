#https://help.alibre.com/articles/#!alibre-help-v23/import-points-from-a-csv-file-rotate-them-and-connect-into-a-polyline
# imports a set of 2D points from a csv file, rotates them and then
# adds them to a 2D sketch with lines connecting the points
# specify which libraries we are going to use
import csv
import math
# configuration
angle = 45
rotationpoint = [15.0, 0.0]
# file to import, replace with your own example
csvfile = r'C:\temp\sample.csv'
# rotates a point around another point
# passed is the angle, the point to rotate and the origin of the rotation
# copied from http://ubuntuforums.org/showthread.php?t=975315&amp;p=8618044#post8618044
def rotate2d(degrees,point,origin):
  x = point[0] - origin[0]
  yorz = point[1] - origin[1]
  newx = (x*math.cos(math.radians(degrees))) - (yorz*math.sin(math.radians(degrees)))
  newyorz = (x*math.sin(math.radians(degrees))) + (yorz*math.cos(math.radians(degrees)))
  newx += origin[0]
  newyorz += origin[1] 
  return newx,newyorz
# list of points, empty for now
# points will be stored as [x1,y1, x2,y2, ... ,xn,yn]
points = []
# open csv file
f = open(csvfile)
# create csv reader and read in lines
reader = csv.reader(f)
for row in reader:
  # column 0 contains x, column 1 contains y
  x = float(row[0])
  y = float(row[1])
  # rotate point and add to list of points
  points.extend(rotate2d(angle, [x, y], rotationpoint))
# finished with csv file
f.close()
# show number of points found
print 'Found %d points' % (len(points) / 2)
# create part
MyPart = Part('My Part')
# add sketch on XY plane
PointSketch = MyPart.AddSketch('Point Sketch', MyPart.GetPlane('XY-Plane'))
# add points with lines connecting them
PointSketch.AddLines(points, False)