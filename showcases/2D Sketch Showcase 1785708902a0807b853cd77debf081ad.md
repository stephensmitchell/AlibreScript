# 2D Sketch Showcase

ID: A7246742B-15
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 11, 2025 9:22 AM
AI summary: A Python function demonstrates creating a 2D sketch with various shapes including lines, rectangles, circles, arcs, ellipses, polygons, polylines, and B-splines using Alibre Script and IronPython.

```python
def sketch_2d_showcase():
    """
    Demonstrates creating a single 2D sketch with multiple shapes:
    - Lines, rectangle
    - Circle
    - Arc (Center-Start-End)
    - Ellipse
    - Elliptical arc
    - Polygon
    - Polyline
    - Bspline (through points)
    """
    # 1) Create a new Part
    my_part = Part("Sketch2DShowcase")

    # 2) Get the XY-plane to place a sketch
    xy_plane = my_part.GetPlane("XY-Plane")

    # 3) Create one big sketch for demonstration
    sketch = my_part.AddSketch("MultiShapeSketch", xy_plane)

    # -------------------------
    # A. Lines & Rectangle
    # -------------------------
    sketch.AddLine([0,  0], [30,  0], False)
    sketch.AddLine([30, 0], [30, 10], False)
    sketch.AddLine([30,10], [ 0, 10], False)
    sketch.AddLine([ 0,10], [ 0,  0], False)

    sketch.AddRectangle(35, 0, 45, 5, False)

    # -------------------------
    # B. Circle
    # -------------------------
    # centerX=70, centerY=5, diameter=10
    sketch.AddCircle(70, 5, 10, False)

    # -------------------------
    # C. Arc (Center-Start-End)
    # -------------------------
    # center=(95, 5), start=(90, 5), end=(95, 10)
    sketch.AddArcCenterStartEnd(95, 5, 90, 5, 95, 10, False)

    # -------------------------
    # D. Ellipse
    # -------------------------
    # AddEllipse(CenterX, CenterY, MajorDiameter, MinorMajorRatio, MajorAxisAngle, isRef)
    # center=(120,5), major=20, ratio=0.5 => minor=major*0.5, angle=0
    sketch.AddEllipse(120, 5, 20, 0.5, 0.0, False)

    # -------------------------
    # E. Elliptical Arc
    # -------------------------
    # Must pass all 10 arguments:
    #   1) CenterX=150
    #   2) CenterY=5
    #   3) StartX=140
    #   4) StartY=5
    #   5) EndX=150
    #   6) EndY=10
    #   7) MajorAxisDiameter=20
    #   8) MinorMajorRatio=0.5
    #   9) MajorAxisAngle=0.0
    #   10) IsReference=False
    sketch.AddEllipticalArc(150, 5, 140, 5, 150, 10, 20, 0.5, 0.0, False)

    # -------------------------
    # F. Polygon
    # -------------------------
    # AddPolygon(centerX, centerY, diameter, sides, isRef)
    # center=(180,5), diameter=15, 6 sides
    sketch.AddPolygon(180, 5, 15, 6, False)

    # -------------------------
    # G. Polylines
    # -------------------------
    # We'll add a "zigzag" polyline near (0,30)
    poly_points = [  0,30,
                    10,40,
                    20,30,
                    30,40,
                    40,30 ]
    sketch.AddLines(poly_points, False)

    # -------------------------
    # H. Bspline
    # -------------------------
    # Add a spline from (0,50) → (10,60) → (20,55) → (30,65)
    spline_points = [0,50, 10,60, 20,55, 30,65]
    sketch.AddBspline(spline_points, False)

    print("2D Sketch Showcase: Created lines, arcs, circles, ellipse, elliptical arcs, rectangle, polygon, polyline, and a Bspline on one sketch.")

# Uncomment to run:

sketch_2d_showcase()

```