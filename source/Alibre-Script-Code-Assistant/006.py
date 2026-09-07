import math
from AlibreScript import *
# Initialize the part session
part = CurrentPart()
# Fetch the standard planes
xy_plane = part.GetPlane("XY-Plane")
zx_plane = part.GetPlane("ZX-Plane")
# Create a profile sketch on the XY plane
profile_sketch = part.AddSketch("ProfileSketch", xy_plane)
# Add a circle to the profile sketch as the sweep profile
profile_sketch.AddCircle(0, 0, 2, False)  # Center at (0,0), Radius = 2
# Create a path sketch on the ZX plane
path_sketch = part.AddSketch("PathSketch", zx_plane)
# Add a line to the path sketch as the sweep path
path_sketch.AddLine([0, 0], [10, 10], False)  # Line from (0,0) to (10,10)
# Define parameters for the sweep boss
is_rigid = False
end_condition = part.EndCondition.EntirePath  # Using EntirePath as the end condition
end_plane = None
end_offset = 0
draft_angle = 0  # No draft angle
outward_draft = False  # No outward draft
# Add the sweep boss feature
part.AddSweepBoss("SweepBossFeature", profile_sketch, path_sketch, is_rigid, end_condition, end_plane, end_offset, draft_angle, outward_draft)
# Regenerate the part to update the view
part.Regenerate()