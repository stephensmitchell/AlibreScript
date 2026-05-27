# 3D Sketch Showcase

ID: A7246742B-16
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 11, 2025 9:40 AM
AI summary: Demonstrates creating a 3D sketch using Alibre Script, including adding lines, an arc, a B-spline, a polyline, and individual points in a single sketch.

```python
def sketch_3d_showcase():
    """
    Demonstrates creating a 3D sketch and adding various 3D figures:
    1) Lines
    2) Arc (center-start-end)
    3) A B-spline (through 3D points)
    4) A polyline (multiple connected segments)
    5) Individual points
    """
    # 1) Create a new Part
    my_part = Part("3DSketchShowcase")

    # 2) Add a 3D sketch to the part
    sketch_3d = my_part.Add3DSketch("My3DSketch")

    # ------------------------------------------------------------------------
    # A) Lines
    # ------------------------------------------------------------------------
    # Add a single line from (0,0,0) to (10,0,5)
    # The signature: .AddLine(X1, Y1, Z1, X2, Y2, Z2) or .AddLine([X1, Y1, Z1], [X2, Y2, Z2])
    sketch_3d.AddLine([0, 0, 0], [10, 0, 5])

    # ------------------------------------------------------------------------
    # B) Arc (Center-Start-End)
    # ------------------------------------------------------------------------
    # AddArcCenterStartEnd(CenterX, CenterY, CenterZ, StartX, StartY, StartZ, EndX, EndY, EndZ)
    # We'll place the arc center at (15,0,0); start at (10,0,5); end at (15,5,5)
    sketch_3d.AddArcCenterStartEnd(15, 0, 0,    # center
                                   10, 0, 5,    # start
                                   15, 5, 5)    # end

    # ------------------------------------------------------------------------
    # C) B-spline
    # ------------------------------------------------------------------------
    # AddBspline(IronPython.Runtime.List) with points [X1, Y1, Z1, X2, Y2, Z2, ...]
    # Let's define a small 3D wave from (0,10,0) -> (5,15,5) -> (10,15,0) -> (15,20,10)
    bspline_points = [
        0, 10, 0,
        5, 15, 5,
        10, 15, 0,
        15, 20, 10
    ]
    sketch_3d.AddBspline(bspline_points)

    # ------------------------------------------------------------------------
    # D) Polyline (multiple connected line segments in 3D)
    # ------------------------------------------------------------------------
    # There's no direct "AddLines" for 3D identical to 2D, but we can do:
    #   .AddLines([x1,y1,z1, x2,y2,z2, x3,y3,z3, ...])
    #   OR use "AddPolyline( AlibreScript.API.Polyline3D )".
    # We'll try .AddLines(...) with a simple zig-zag:
    polyline_points = [
        20,  0, 0,
        25,  5, 5,
        30,  0, 10,
        35,  5, 15
    ]
    sketch_3d.AddLines(polyline_points)

    # ------------------------------------------------------------------------
    # E) Individual points
    # ------------------------------------------------------------------------
    # .AddPoint(X, Y, Z)
    # We'll drop a single reference point at (25,10,5)
    sketch_3d.AddPoint(25, 10, 5)

    print("3D Sketch Showcase completed. Created lines, an arc, a B-spline, a 3D polyline, and a point on a single 3D sketch.")

# Example usage:

sketch_3d_showcase()

```