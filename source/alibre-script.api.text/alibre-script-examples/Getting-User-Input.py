#https://help.alibre.com/articles/#!alibre-help-v23/getting-user-input
# Demonstrates requesting values from the user then creating a part
# with those values
print 'Input width in mm and press Enter'
Width = float(Read())
if Width < 0.1:
  sys.exit('Width must be at least 0.1 mm')
print 'Input height in mm and press Enter'
Height = float(Read())
if Height < 0.1:
  sys.exit('Height must be at least 0.1 mm')
print 'Input depth in mm and press Enter'
Depth = float(Read())
if Depth < 0.1:
  sys.exit('Depth must be at least 0.1 mm')
print 'Creating a box measuring %f mm x %f mm x %f mm...' % (Width, Height, Depth)
MyPart = Part('My Part')
Profile = MyPart.AddSketch('Profile', MyPart.GetPlane('XY-Plane'))
Profile.AddRectangle(0, 0, Width, Height, False)
MyPart.AddExtrudeBoss('Box', Profile, Depth, False)