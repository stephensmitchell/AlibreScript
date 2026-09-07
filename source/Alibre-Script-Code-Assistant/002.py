from AlibreScript import *
import math
# Function to add a hole
def add_hole(sketch, x, y, diameter):
    # Create a circle for the hole
    sketch.AddCircle(x, y, diameter / 2, False)
# Main Script
def main():
    # Create a new part
    part = CurrentPart()
    # Add a sketch for the circular plate
    sketch = part.AddSketch("PlateSketch", part.XYPlane)
    # Draw the main circle (plate) - 20 inch diameter
    plate_diameter = 20
    sketch.AddCircle(0, 0, plate_diameter / 2, False)
    # Hole dimensions
    hole_diameter = 2
    offset_distance = 2
    # Calculate hole positions and add holes
    # Assuming the holes are equally spaced around the plate
    for i in range(4):
        angle = math.radians(90 * i)
        x = offset_distance * math.cos(angle)
        y = offset_distance * math.sin(angle)
        add_hole(sketch, x, y, hole_diameter)
    # Extrude the sketch to create the plate - Assuming 0.25 inch thickness
    thickness = 0.25
    part.AddExtrudeBoss("Plate", sketch, thickness, False)
    # Save the part
    #part.SaveAs("/path/to/save/location", "CircularPlate")
main()
