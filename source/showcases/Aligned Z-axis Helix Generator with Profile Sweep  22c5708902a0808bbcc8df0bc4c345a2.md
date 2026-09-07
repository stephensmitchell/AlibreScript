# Aligned Z-axis Helix Generator with Profile Sweep [Not Working As Intended]

ID: A7246742B-35
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: July 10, 2025 2:38 AM
AI summary: Python script that generates an aligned Z-axis helix with a profile sweep. It takes radius, pitch, turns, and step parameters and builds a helix path and profile plane in a 3D sketch.

> See page below for working inplementation
> 
> 
> [CAD Sweep Feature Script](CAD%20Sweep%20Feature%20Script%2022c5708902a0809f8b5bcea9e0c9ab6e.md)
> 

```python
# Aligned Z-axis helix with profile starting at same point and normal
import math
P = Part("Helix_ZAxisAligned")

# PARAMETERS
radius = 65
pitch = 300
turns = 3
step = 10
profile_radius = 2

# BUILD HELIX AROUND Z-AXIS (centered)
points = []
for a in range(0, 360 * turns + 1, step):
    rad = math.radians(a)
    x = radius * math.cos(rad)
    y = radius * math.sin(rad)
    z = pitch * a / 360.0
    points.extend([x, y, z])

print("Helix path starts at:", [points[0], points[1], points[2]])

# CREATE PATH
Path = P.Add3DSketch("HelixPath")
Path.AddBspline(points)

# CREATE PROFILE PLANE at path start: normal to Z, origin at [0, 0, 0]
Pln = P.AddPlane("ProfilePlane", [0, 0, 1], [0, 0, 0])
Sketch = P.AddSketch("Profile", Pln)

# PROFILE CENTERED AT PATH START (drawn at [radius, 0] on Z-normal plane at origin)
Sketch.AddCircle(radius, 0, profile_radius, False)
print("Profile circle drawn at (%.2f, %.2f) on sketch plane at origin" % (radius, 0))

# SWEEP
P.AddSweepBoss("ZHelixSweep", Sketch, Path, False, Part.EndCondition.EntirePath, None, 0, 0, False)
print("Sweep complete.")

```