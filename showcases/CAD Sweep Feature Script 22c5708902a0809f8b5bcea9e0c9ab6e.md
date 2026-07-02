# CAD Sweep Feature Script

ID: A7246742B-36
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: July 10, 2025 2:44 AM
AI summary: A class in Alibre Script that builds sweep features. Its methods create planes, add profile circles, and build 3D paths. An example builds a helical sweep.

![image.png](image%2010.png)

```python
import math

class SweepBuilder:
    def __init__(self, part, name_prefix="SweepFeature"):
        self.part = part
        self.name_prefix = name_prefix
        self.profile_sketch = None
        self.path_sketch = None
        self.plane = None
        self.axis = None
        self.counter = 1

    def create_start_plane_from_path(self, path_points):
        p0 = path_points[0:3]
        p1 = path_points[3:6]
        direction = [p1[i] - p0[i] for i in range(3)]
        self.plane = self.part.AddPlane("%s_StartPlane" % self.name_prefix, direction, p0)
        return self.plane

    def add_profile_circle(self, radius, center_point):
        self.profile_sketch = self.part.AddSketch("%s_Profile" % self.name_prefix, self.plane)
        cx, cy = self.profile_sketch.GlobaltoPoint(center_point[0], center_point[1], center_point[2])
        self.profile_sketch.AddCircle(cx, cy, radius, False)
        return self.profile_sketch

    def add_3d_path(self, path_points):
        self.path_sketch = self.part.Add3DSketch("%s_Path" % self.name_prefix)
        self.path_sketch.AddBspline(path_points)
        return self.path_sketch

    def sweep_profile(self, draft_angle=0.0, outward=False):
        feature_name = "%s_%d" % (self.name_prefix, self.counter)
        self.counter += 1
        return self.part.AddSweepBoss(
            feature_name,
            self.profile_sketch,
            self.path_sketch,
            False,
            Part.EndCondition.EntirePath,
            None,
            0.0,
            draft_angle,
            outward
        )
        
 # SweepExample.py

from math import cos, sin, pi

# Create part
P = Part("HelixSweepTest")
builder = SweepBuilder(P, "HelixSweep")

# Parameters
turns = 3
pitch = 10.0
radius = 5.0
segments = 100
circle_radius = 1.0

# Compute helix points
points = []
for i in range(segments + 1):
    t = (2 * pi * turns) * i / float(segments)
    x = radius * cos(t)
    y = radius * sin(t)
    z = pitch * t / (2 * pi)
    points.extend([x, y, z])

# Construct geometry
plane = builder.create_start_plane_from_path(points)
builder.add_profile_circle(circle_radius, points[0:3])
builder.add_3d_path(points)
builder.sweep_profile(draft_angle=0.0)
```