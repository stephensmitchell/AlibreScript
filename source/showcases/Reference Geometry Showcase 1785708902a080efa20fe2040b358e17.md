# Reference Geometry Showcase

ID: A7246742B-13
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 11, 2025 9:00 AM
AI summary: Python code that builds a reference geometry showcase. It creates a block, adds an angled plane, defines a plane from three points, and creates an intersection axis, avoiding parallel-plane errors.

```python
def reference_geometry_showcase_fixed():
    """
    Similar to your original code, but the second plane is angled 
    so it properly intersects XY-plane (instead of being parallel).
    """
    part_obj = Part("ReferenceGeometryShowcaseFixed")

    # Step 1: Create a 40×20×10 block
    xy_plane = part_obj.GetPlane("XY-Plane")
    base_sketch = part_obj.AddSketch("BaseSketch", xy_plane)
    base_sketch.AddRectangle(0, 0, 40, 20, False)
    part_obj.AddExtrudeBoss("BaseExtrusion", base_sketch, 10, False)
    print("Step 1: Created a 40×20×10 block.")

    # Instead of an offset plane, create a plane at a 30-degree angle from XY-plane around the Y-axis
    # 1) Get the Y-axis as the rotation axis
    y_axis = part_obj.YAxis   # (language independent property)
    # 2) Add the angled plane
    plane_with_angle = part_obj.AddPlane("PlaneAngleXY", xy_plane, y_axis, 30.0)
    print("Step 2: Added plane 'PlaneAngleXY' at 30 degrees to XY-plane.")

    # Step 3: Plane from three 3D points
    #   (Same as before, corners of block)
    ptA = part_obj.AddPoint("CornerA", 0, 0, 0)
    ptB = part_obj.AddPoint("CornerB", 40, 0, 0)
    ptC = part_obj.AddPoint("CornerC", 0, 0, 10)
    plane3Points = part_obj.AddPlane("PlaneFrom3Points",
                                     [0, 0, 0],
                                     [40, 0, 0],
                                     [0, 0, 10])
    print("Step 3: Created 'PlaneFrom3Points' using three 3D coords.")

    # Step 4: Axis from the intersection of XY-plane and plane_with_angle
    #   This time they are not parallel, so we get a valid axis
    axis_intersect = part_obj.AddAxis("AxisXYandAngle",
                                      xy_plane,
                                      plane_with_angle)
    print("Step 4: Created axis 'AxisXYandAngle' from intersection of XY-plane and 'PlaneAngleXY'.")

    # You can then continue with your other steps (e.g., axis from two points, plane from offset, etc.)
    # Just remember: if you create an offset plane from XY-plane, that new plane remains parallel. 
    # So don't attempt intersection with XY-plane again unless you want an error.

    print("All done without the parallel-plane intersection error!")

```

![image.png](image.png)