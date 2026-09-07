import math
from AlibreScript import *
# Initialize the part session
part = CurrentPart()
# Nut dimensions (in mm)
threadDiameter = 10  # M10 thread
pitch = 1.5          # Typical pitch for M10
acrossFlats = 17     # Width across flats for M10
thickness = 8        # Nut thickness for M10
cornerRadius = 1     # Corner radius
# Number of sides for the hexagon
numSides = 6
# Create the base hexagonal profile
hexSketch = part.AddSketch('HexBase', part.XYPlane)
hexSketch.StartEditing()
# Calculate vertices for the hexagon
vertices = []
for i in range(numSides + 1):  # +1 to close the hexagon
    angle = 2 * math.pi * i / numSides
    x = acrossFlats / (2 * math.cos(math.pi / numSides)) * math.cos(angle)
    y = acrossFlats / (2 * math.cos(math.pi / numSides)) * math.sin(angle)
    vertices.append([x, y])
# Add lines to create the hexagon
for i in range(numSides):
    startX, startY = vertices[i]
    endX, endY = vertices[i + 1]
    hexSketch.AddLine(startX, startY, endX, endY, False)  # Adding line using coordinates
hexSketch.StopEditing()
# Extrude the hexagon to form the nut body
nutBody = part.AddExtrudeBoss('NutBody', hexSketch, thickness, False)
# Create internal thread hole
threadHoleSketch = part.AddSketch('ThreadHole', part.XYPlane)
threadHoleSketch.StartEditing()
threadHoleSketch.AddCircle(0, 0, threadDiameter / 2, False)
threadHoleSketch.StopEditing()
part.AddExtrudeCut('ThreadHoleCut', threadHoleSketch, thickness, False)
print("M10 hex nut model created.")