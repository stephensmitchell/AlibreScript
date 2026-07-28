import math
from AlibreScript import *
# Initialize the part session
part = CurrentPart()
# Flange dimensions (in mm)
flangeDiameter = 565  # Flange outer diameter
flangeThickness = 30   # Flange thickness
pipeDiameter = 254     # 10 inches converted to mm for pipe
boltHoleDiameter = 40  # Bolt hole diameter
boltCircleDiameter = 175  # Bolt circle diameter
numberOfBoltHoles = 12
# Create main flange disc
flangeSketch = part.AddSketch('FlangeBase', part.XYPlane)
flangeSketch.StartEditing()
flangeSketch.AddCircle(0, 0, flangeDiameter / 2, False)  # Center at (0,0)
flangeSketch.StopEditing()
flange = part.AddExtrudeBoss('FlangeDisc', flangeSketch, flangeThickness, False)
# Create bolt holes
for i in range(numberOfBoltHoles):
    angle = 2 * math.pi * i / numberOfBoltHoles
    x = boltCircleDiameter / 2 * math.cos(angle)
    y = boltCircleDiameter / 2 * math.sin(angle)
    boltHoleSketch = part.AddSketch('BoltHole', part.XYPlane)
    boltHoleSketch.StartEditing()
    boltHoleSketch.AddCircle(x, y, boltHoleDiameter / 2, False)
    boltHoleSketch.StopEditing()
    part.AddExtrudeCut('BoltHoleCut', boltHoleSketch, flangeThickness, False)
# Create center pipe hole
centerHoleSketch = part.AddSketch('CenterPipeHole', part.XYPlane)
centerHoleSketch.StartEditing()
centerHoleSketch.AddCircle(0, 0, pipeDiameter / 2, False)
centerHoleSketch.StopEditing()
part.AddExtrudeCut('CenterHoleCut', centerHoleSketch, flangeThickness, False)
print("10-inch pipe flange model created.")