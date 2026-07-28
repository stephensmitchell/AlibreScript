# API Quick Reference

Use this as a short retrieval guide. Confirm edge cases in `alibre.script.api3.csv`
or `alibre.script.api2.csv`.

## Part And Assembly Entry Points

```python
print ScriptFileName
print ScriptFolder

P = CurrentPart()
A = CurrentAssembly()

Parts = CurrentParts()
Assys = CurrentAssemblies()

P = Part('My Part')
P = Part(r'C:\path\folder', 'ExistingPartName')
```

Default reference geometry:

```python
XY = P.GetPlane('XY-Plane')
YZ = P.GetPlane('YZ-Plane')
ZX = P.GetPlane('ZX-Plane')
X = P.GetAxis('X-Axis')
Y = P.GetAxis('Y-Axis')
Z = P.GetAxis('Z-Axis')
```

Language-independent properties are also available in newer references:

```python
XY = P.XYPlane
YZ = P.YZPlane
ZX = P.ZXPlane
X = P.XAxis
Y = P.YAxis
Z = P.ZAxis
Origin = P.Origin
```

## Planes

Offset from an existing plane or face:

```python
Plane1 = P.AddPlane('Offset Plane', XY, 25.0)
```

Plane from a normal vector and point:

```python
Plane1 = P.AddPlane('Normal Plane', [0.0, 0.0, 1.0], [0.0, 0.0, 0.0])
```

Plane containing an axis and point:

```python
Plane1 = P.AddPlane('Axis Point Plane', Axis1, Point1)
```

Plane at angle to an existing plane around an axis:

```python
Plane1 = P.AddPlane('Angled Plane', XY, X, 16.0)
```

Plane through three points:

```python
Plane1 = P.AddPlane('Three Point Plane', [0, 0, 0], [10, 0, 0], [0, 10, 0])
```

## Axes

Axis at the intersection of two planes or faces:

```python
Axis1 = P.AddAxis('Intersection Axis', PlaneA, PlaneB)
```

Axis through two points or coordinate lists:

```python
Axis1 = P.AddAxis('Point Axis', [0.0, 0.0, 0.0], [0.0, 0.0, 100.0])
```

Axis from a cylindrical face:

```python
Axis1 = P.AddAxis('Cylinder Axis', CylindricalFace)
```

The UI can create some reference geometry combinations that are not directly
listed as script overloads. For example, an axis from `Origin` plus a plane can
be reproduced by creating an axis through origin and a second point along that
plane's normal.

## Points

```python
P0 = P.AddPoint('P0', 0.0, 0.0, 0.0)
P1 = P.AddPoint('P1', [10.0, 0.0, 0.0])
P2 = P.AddPoint('Plane Axis Point', Axis1, Plane1)
P3 = P.AddPoint('Three Plane Point', PlaneA, PlaneB, PlaneC)
```

## Sketches

```python
S = P.AddSketch('Profile', XY)
S.AddRectangle(-10.0, -5.0, 10.0, 5.0, False)
S.AddCircle(0.0, 0.0, 5.0, False)
S.AddLine(0.0, 0.0, 10.0, 0.0, False)
```

Reference figures use `True` as the final argument in most sketch add methods.

## Features

Simple extrude:

```python
P.AddExtrudeBoss('Boss', S, 10.0, False)
P.AddExtrudeCut('Cut', S, 10.0, False)
```

Through-all cut:

```python
P.AddExtrudeCut('Cut', S, 0, False, Part.EndCondition.ThroughAll,
                None, 0, Part.DirectionType.Normal, None, 0, False)
```

Revolve:

```python
P.AddRevolveBoss('Revolve', S, P.GetAxis('X-Axis'), 360.0)
P.AddRevolveCut('Revolve Cut', S, Axis1, 180.0)
```

Loft:

```python
P.AddLoftBoss('Loft', [SketchA, SketchB], True, False, False, False)
```

Sweep:

```python
P.AddSweepBoss('Sweep', ProfileSketch, PathSketch, False,
               Part.EndCondition.EntirePath, None, 0, 0, False)
```

## Dialogs

```python
Options = []
Options.append(['Distance', WindowsInputTypes.Real, 10.0])
Options.append(['Count', WindowsInputTypes.Integer, 4])
Options.append(['Plane', WindowsInputTypes.Plane, None])
Values = Windows().OptionsDialog('Script Inputs', Options, 200)
```

Library examples show richer dialog patterns with images, file pickers, and
remembered settings.

## Fixture Plane Pattern

This pattern creates a 16 degree plane, an axis normal to that plane through
origin, and a -30 degree plane from `YZ-Plane` around that axis.

```python
from math import sin, cos, radians

P = CurrentPart()

Angle16 = 16.0
Angle30 = -30.0
AxisLength = 100.0

XYPlane = P.GetPlane('XY-Plane')
YZPlane = P.GetPlane('YZ-Plane')
XAxis = P.GetAxis('X-Axis')

Plane16 = P.AddPlane('16 degree', XYPlane, XAxis, Angle16)

A = radians(Angle16)
Axis2 = P.AddAxis('Axis<2>',
                  [0.0, 0.0, 0.0],
                  [0.0, -sin(A) * AxisLength, cos(A) * AxisLength])

Plane30 = P.AddPlane('30 degree', YZPlane, Axis2, Angle30)
```
