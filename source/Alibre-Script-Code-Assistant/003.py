import math
from AlibreScript import *
# Initialize the part session
part = CurrentPart()
# Define the dimensions of the bolt
hex_head_diameter = 10  # Diameter of the hex head
hex_head_height = 5     # Height of the hex head
shaft_diameter = 5      # Diameter of the shaft
shaft_length = 20       # Length of the shaft
# Create a hexagon sketch for the bolt head
hex_sketch = part.AddSketch("HexHeadSketch", part.XYPlane)
for i in range(6):
    angle1 = math.radians(60 * i)
    angle2 = math.radians(60 * (i + 1))
    x1 = hex_head_diameter / 2 * math.cos(angle1)
    y1 = hex_head_diameter / 2 * math.sin(angle1)
    x2 = hex_head_diameter / 2 * math.cos(angle2)
    y2 = hex_head_diameter / 2 * math.sin(angle2)
    hex_sketch.AddLine([x1, y1], [x2, y2], False)
# Extrude the hex head
hex_head = part.AddExtrudeBoss("HexHead", hex_sketch, hex_head_height, False)
# Create a circle sketch for the shaft
shaft_sketch = part.AddSketch("ShaftSketch", part.XYPlane)
shaft_sketch.AddCircle(0, 0, shaft_diameter / 2, False)
# Extrude the shaft
shaft = part.AddExtrudeBoss("Shaft", shaft_sketch, shaft_length, False)
# Regenerate the part to update the view
part.Regenerate()
