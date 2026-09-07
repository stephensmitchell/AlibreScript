# Plane at Sketch Point

ID: A7246742B-12
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 11, 2025 8:49 AM
AI summary: Creates a 50×50×10 block, adds a sketch with a point at (25, 25), converts it to 3D coordinates, and adds a reference plane at that location with a specified normal vector.

```python
def create_plane_at_sketch_point():
    """
    1. Creates a part with a 50×50×10 block.
    2. Adds a sketch on the top face and places a point at (25, 25).
    3. Converts that point's 2D location into 3D global coordinates.
    4. Creates a reference plane at that 3D location, 
       using a chosen normal vector (e.g. [0,0,1]) for orientation.
    """
    # 1) Create the part
    part_obj = Part("PlaneAtPointPart")

    # 2) Create a base rectangle on the XY-plane (50×50)
    xy_plane = part_obj.GetPlane("XY-Plane")
    base_sketch = part_obj.AddSketch("BaseSketch", xy_plane)
    base_sketch.AddRectangle(0, 0, 50, 50, False)

    # 3) Extrude 10 mm
    part_obj.AddExtrudeBoss("BaseExtrusion", base_sketch, 10, False)

    # 4) Identify the top face created by the extrusion 
    #    (commonly "Face<5>" or similar).
    top_face = part_obj.GetFace("Face<5>")

    # 5) Add a sketch on that top face
    point_sketch = part_obj.AddSketch("PointSketch", top_face)

    # 6) Place a point at (25, 25) in the local 2D coordinates 
    #    of the new sketch (center region).
    #    This is not a reference point, so isReference=False.
    point_sketch.AddPoint(25, 25, False)

    # 7) Convert the 2D point location to 3D global coordinates
    #    The newly added point is figure[0], but safer to reference last figure index:
    sketch_pt_2d = point_sketch.Figures[-1]  # The newly added AlibreScript figure
    x2d, y2d = sketch_pt_2d.X, sketch_pt_2d.Y  # 2D coords in the sketch
    pt_3d = point_sketch.PointtoGlobal(x2d, y2d)
    # pt_3d is now a Python list [globalX, globalY, globalZ]

    # 8) Create a plane at the 3D point location 
    #    Let the plane be parallel to XY-plane → normal vector is [0, 0, 1].
    #    Or pick any normal of your choice: e.g., [1, 1, 1].
    normal_vector = [0, 0, 1]
    plane_name = "PlaneAtPoint"
    # Use AddPlane( name, normal_vector, point_in_3d )
    #   Normal vector can be non-normalized. 
    #   The point_in_3d is [X, Y, Z] in part coordinates.
    new_plane = part_obj.AddPlane(plane_name, normal_vector, pt_3d)

    print("Created a block and added a plane at the location of a sketch point.")
    print("Plane name:", plane_name)
    print("Plane location:", pt_3d)
    print("Plane normal vector:", normal_vector)

# Uncomment to run directly:
create_plane_at_sketch_point()
```