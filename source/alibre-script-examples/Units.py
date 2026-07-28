#https://help.alibre.com/articles/#!alibre-help-v23/units
# demonstrates using multiple units in a script
# create a part and a sketch
MyPart = Part('My Part')
XYPlane = MyPart.GetPlane('XY-Plane')
Sketch = MyPart.AddSketch('Sketch', XYPlane)
# set units to mm - this is implied at the start of every script
Units.Current = UnitTypes.Millimeters
# create circle 50mm in diameter
Sketch.AddCircle(0, 0, 50, False)
# set units to inches
# all values from now on are in inches
Units.Current = UnitTypes.Inches
# create a circle 1.34 inches in diameter
Sketch.AddCircle(0, 0, 1.34, False)
# switch to cm
# now all values from this point until the next units change are in cm
Units.Current = UnitTypes.Centimeters
# create a circle 4.2cm in diameter
Sketch.AddCircle(0, 0, 4.2, False)