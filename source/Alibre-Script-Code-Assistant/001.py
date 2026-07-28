from AlibreScript import *
def create_base_plate_with_holes():
    # Initialize a part session
    part = CurrentPart()
    # Define dimensions for the base plate and holes
    plate_length = 100.0  # Length of the base plate
    plate_width = 50.0    # Width of the base plate
    plate_thickness = 5.0 # Thickness of the base plate
    hole_diameter = 5.0   # Diameter of the holes
    hole_offset = 10.0    # Offset of the holes from the edges
    # Create a base plate
    base_sketch = part.AddSketch('BasePlateSketch', part.XYPlane)
    base_sketch.AddRectangle(-plate_width / 2, -plate_length / 2, plate_width / 2, plate_length / 2, False)
    part.AddExtrudeBoss('BasePlate', base_sketch, plate_thickness, False, part.EndCondition.ToDepth, None, 0, part.DirectionType.Normal, None, 0, False)
    # Create holes
    for x in [-plate_width / 2 + hole_offset, plate_width / 2 - hole_offset]:
        for y in [-plate_length / 2 + hole_offset, plate_length / 2 - hole_offset]:
            hole_sketch = part.AddSketch('HoleSketch', part.XYPlane)
            hole_sketch.AddCircle(x, y, hole_diameter / 2, False)
            part.AddExtrudeCut('ThroughHole', hole_sketch, 0, False, part.EndCondition.ThroughAll, None, 0, part.DirectionType.Normal, None, 0, False)
    # Save the part
    #part.Save()
# Run the function to create a simple base plate with four holes
create_base_plate_with_holes()