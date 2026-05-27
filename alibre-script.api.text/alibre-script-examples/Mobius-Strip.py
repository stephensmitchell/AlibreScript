#https://help.alibre.com/articles/#!alibre-help-v23/mobius-strip
# creates a mobius strip with a configurable number of rotations
Mobius = Part('Mobius')
# dimensions of mobius strip
Diameter = 100.0
Width = 20.0
Height = 5.0
# number of 360 degree twists in mobius strip
Rotations = 2
# more steps = better accuracy
Steps = 30
# calculate how far we rotate through 360 degrees for each step
RotationPerStep = Rotations / float(Steps) * 360.0
DegreesPerStep = 360.0 / Steps
# create the base sketch we will use as a template for all other sketches
S0Plane = Mobius.GetPlane('XY-Plane')
S0 = Mobius.AddSketch('S0', S0Plane)
S0.AddRectangle(Diameter, -Height / 2, Diameter + Width, Height / 2, False)
Sketches = [S0]
# generate sketches
for Step in range (1, Steps):
  Plane = Mobius.AddPlane('S' + str(Step), S0Plane, Mobius.GetAxis('Y-Axis'), DegreesPerStep * Step)
  Sketch = Mobius.AddSketch('S' + str(Step), Plane)
  Sketch.CopyFrom(S0, RotationPerStep * Step, Diameter + (Width / 2), 0, 0, 0, 0, 0, 100.0)
  Sketches.append(Sketch)
# create loft, connecting ends
Mobius.AddLoftBoss('Strip', Sketches, True, True, False, True)
