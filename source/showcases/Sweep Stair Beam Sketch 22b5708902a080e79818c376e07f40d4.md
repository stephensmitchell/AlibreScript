# Sweep Stair Beam Sketch

ID: A7246742B-34
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: July 9, 2025 4:58 AM
AI summary: Python script using Alibre Script and IronPython that builds a sweep stair beam with valid geometry: defines the path, computes the unit direction vector, creates the profile plane, and adds the sweep feature.

```python
# Corrected Sweep Stair Beam with Valid Geometry
P = Part("StairBeamFixed")

# Define 3D sweep path (gentle incline)
Path = P.Add3DSketch("SweepPath")
Path.AddLines([0, 0, 0, 3000, 3000, 0])

# Compute unit direction vector of the path
import math
dx = 3000 - 0
dy = 3000 - 0
dz = 0 - 0
length = math.sqrt(dx**2 + dy**2 + dz**2)
nx = dx / length
ny = dy / length
nz = dz / length

# Create profile plane perpendicular to path
Pln = P.AddPlane("StartProfilePlane", [nx, ny, nz], [0, 0, 0])

# Profile Sketch
S = P.AddSketch("Profile", Pln)
S.AddRectangle(-75, -10, 75, 10, False)

# Sweep Feature
P.AddSweepBoss("BeamSweep", S, Path, False, Part.EndCondition.EntirePath, None, 0, 0, False)

```