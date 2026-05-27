# Alibre Script Example

ID: A7246742B-19
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 17, 2025 9:29 PM
AI summary: Example Alibre Script demonstrates creating a part, adding sketches, and performing operations like extrusion and cutting using IronPython 2.7 syntax.

```python
# =========================
# Alibre Script Example
# =========================

# Notes:
#  1) This script is “flat”: no class definitions or advanced function definitions.
#  2) Replace any paths or input parameters as needed.
#  3) AlibreScript uses IronPython 2.7 syntax.

# ---------------------------------------------------------
#  Example usage of the AlibreScript API
# ---------------------------------------------------------

# (Optional) Set working units, e.g. millimeters:
Units.Current = UnitTypes.Millimeters

# PART CREATION
# Creates a new part named "Example Part":
MyPart = Part("Example Part")

# Access a default reference plane (e.g. XY-Plane)
XYPlane = MyPart.GetPlane("XY-Plane")

# Add a 2D sketch on the XY-Plane
Sketch1 = MyPart.AddSketch("Sketch1", XYPlane)

# EXAMPLE: Add a rectangle to the sketch
Sketch1.AddRectangle(0, 0, 50, 20, False)

# Extrude Boss
ExtrudeFeature = MyPart.AddExtrudeBoss("Base-Block", Sketch1, 10, False)

# EXAMPLE: Add a circle for a hole, then cut
HoleSketch = MyPart.AddSketch("HoleSketch", MyPart.GetFace("Face<3>"))   # "Face<3>" is just an example face name
# Convert the point (25,10) from the above extrude's face coordinate system
HoleSketch.AddCircle(25, 10, 5, False)
HoleCut = MyPart.AddExtrudeCut("HoleCut", HoleSketch, 10, False)

# End of file
```