# Cycloidal Disk Generator with Performance Metrics

ID: A7246742B-28
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: March 22, 2025 8:41 PM
AI summary: Generates a cycloidal disk in Alibre Script and IronPython using a class that calculates the points of the cycloidal disk curve. The script times point calculation, polyline building, and adding the result to a sketch.

[CycloidalDiskPoints to import into Sketches](CycloidalDiskPoints%20to%20import%20into%20Sketches%201bf5708902a080d5ae50caaa7987465b.md)

```python
from __future__ import division
import math
import sys
print math.pi
from System.Diagnostics import Stopwatch
from System import TimeSpan

class CycloidalDiskCalculator(object):
    def __init__(self, rotor_radius, roller_radius, eccentricity, number_of_rollers):
        # Store parameters
        self.R  = rotor_radius
        self.Rr = roller_radius
        self.E  = eccentricity
        self.N  = number_of_rollers

        # For speed, create local references to math functions
        self._sin   = math.sin
        self._cos   = math.cos
        self._atan2 = math.atan2
        self._pi    = math.pi

    def calc_points(self, num_points):
        """
        Calculates all (x, y) points for the cycloidal disk curve.
        Returns a list of (x, y) tuples. 
        """
        points = []
        # Precompute for speed
        R_div_EN = self.R / (self.E * self.N)
        two_pi = 2 * self._pi

        # Generate parameter t values
        t_values = [i * two_pi / num_points for i in range(num_points)]

        for t in t_values:
            try:
                # Calculate psi
                psi = self._atan2(
                    self._sin((1 - self.N) * t),
                    R_div_EN - self._cos((1 - self.N) * t)
                )
                # Calculate x, y
                x = (self.R * self._cos(t)) - (self.Rr * self._cos(t + psi)) - (self.E * self._cos(self.N * t))
                y = (-self.R * self._sin(t)) + (self.Rr * self._sin(t + psi)) + (self.E * self._sin(self.N * t))
                points.append((x, y))
            except:
                # Ignore any math errors silently (as in the original script)
                pass

        # Close the loop by duplicating the first point
        if points:
            points.append(points[0])

        return points

    def build_polyline(self, points):
        """
        Creates and returns a Polyline object from the provided list of (x, y) points.
        """
        Poly = Polyline()
        for pt in points:
            Poly.AddPoint(PolylinePoint(pt[0], pt[1]))
        return Poly

Win = Windows()
ScriptName = 'Cycloidal Disk Gen'

# Create input window (same as original, minus the image field to match your snippet)
Options = []
Options.append(['Rotor Radius (mm)', WindowsInputTypes.Real, 45])
Options.append(['Roller Radius (mm)', WindowsInputTypes.Real, 6.5])
Options.append(['Eccentricity (mm)', WindowsInputTypes.Real, 1.5])
Options.append(['Number of Rollers', WindowsInputTypes.Integer, 16])
Options.append(['Plane', WindowsInputTypes.Plane, None])

Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
    sys.exit()

print 'Generating cycloidal disk profile'

# Get user inputs
R  = Values[0]  # Rotor Radius
Rr = Values[1]  # Roller Radius
E  = Values[2]  # Eccentricity
N  = Values[3]  # Number of Rollers
Pl = Values[4]  # Plane Selected

print "Rotor Radius:", R, "Roller Radius:", Rr, "Eccentricity:", E, "Number of Rollers:", N

# Get the current part
Prt = CurrentPart()

# Create the sketch (on XY-plane, or use Pl if you want)
Sk = Prt.AddSketch("Cycloid Disk", Prt.GetPlane('XY-Plane'))

# Number of points for the calculation
num_points = 2000  # Increase resolution
print('Number of Points: ' + str(num_points))

# Create an instance of the new calculation class
calc = CycloidalDiskCalculator(R, Rr, E, N)

watch = Stopwatch.StartNew()

points = calc.calc_points(num_points)

watch.Stop()
ts_calcpoints = watch.Elapsed
print 'Time To Calc Points: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_calcpoints.Hours,
    ts_calcpoints.Minutes,
    ts_calcpoints.Seconds,
    ts_calcpoints.Milliseconds
)

watch.Restart()

Poly = calc.build_polyline(points)

watch.Stop()
ts_buildpoly = watch.Elapsed
print 'Time To Build Poly: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_buildpoly.Hours,
    ts_buildpoly.Minutes,
    ts_buildpoly.Seconds,
    ts_buildpoly.Milliseconds
)

watch.Restart()

Sk.AddPolyline(Poly, False)

watch.Stop()
ts_addpolyline = watch.Elapsed
print 'Time To AddPolyline: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_addpolyline.Hours,
    ts_addpolyline.Minutes,
    ts_addpolyline.Seconds,
    ts_addpolyline.Milliseconds
)

```

```python
from __future__ import division
import math
import sys
print math.pi
from System.Diagnostics import Stopwatch
from System import TimeSpan

sin_   = math.sin
cos_   = math.cos
atan2_ = math.atan2
pi_    = math.pi

Win = Windows()
ScriptName = 'Cycloidal Disk Gen'

# Create input window
Options = []
Options.append(['Rotor Radius (mm)', WindowsInputTypes.Real, 45])
Options.append(['Roller Radius (mm)', WindowsInputTypes.Real, 6.5])
Options.append(['Eccentricity (mm)', WindowsInputTypes.Real, 1.5])
Options.append(['Number of Rollers', WindowsInputTypes.Integer, 16])
Options.append(['Plane', WindowsInputTypes.Plane, None])

Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
    sys.exit()

print 'Generating cycloidal disk profile'

# Get user inputs
R  = Values[0]  # Rotor Radius
Rr = Values[1]  # Roller Radius
E  = Values[2]  # Eccentricity
N  = Values[3]  # Number of Rollers
Pl = Values[4]  # Plane Selected

print "Rotor Radius:", R, "Roller Radius:", Rr, "Eccentricity:", E, "Number of Rollers:", N

# Get current part and XY plane
Prt = CurrentPart()
Sk = Prt.AddSketch("Cycloid Disk", Prt.GetPlane('XY-Plane'))

num_points = 1000
print('Number of Points: ' + str(num_points))

two_pi   = 2.0 * pi_
R_div_EN = R / (E * N)

Poly = Polyline()
points = []

watch = Stopwatch.StartNew()

for i in xrange(num_points):
    t = i * two_pi / num_points

    # Calculate psi
    psi = atan2_(sin_((1 - N)*t), (R_div_EN - cos_((1 - N)*t)))

    # Calculate x and y coordinates
    x = (R * cos_(t)) - (Rr * cos_(t + psi)) - (E * cos_(N * t))
    y = (-R * sin_(t)) + (Rr * sin_(t + psi)) + (E * sin_(N * t))

    points.append((x, y))

# Add the first point again to close the polyline
if points:
    points.append(points[0])

watch.Stop()
ts_calcpoints = watch.Elapsed
print 'Time To Calc Points: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_calcpoints.Hours, ts_calcpoints.Minutes, ts_calcpoints.Seconds, ts_calcpoints.Milliseconds
)

watch.Restart()

# Add points to the polyline
for p in points:
    Poly.AddPoint(PolylinePoint(p[0], p[1]))

watch.Stop()
ts_buildpoly = watch.Elapsed
print 'Time To Build Poly: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_buildpoly.Hours, ts_buildpoly.Minutes, ts_buildpoly.Seconds, ts_buildpoly.Milliseconds
)

watch.Restart()

# Add the polyline to the sketch
Sk.AddPolyline(Poly, False)

watch.Stop()
ts_addpolyline = watch.Elapsed
print 'Time To AddPolyline: {} Hours, {} Minutes, {} Seconds, and {} Milliseconds.'.format(
    ts_addpolyline.Hours, ts_addpolyline.Minutes, ts_addpolyline.Seconds, ts_addpolyline.Milliseconds
)

```