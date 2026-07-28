# Equation sketcher script
# Demonstrates selecting sketches, inserting a sketch
# For use with Alibre Design
from __future__ import division
from math import sqrt
Win = Windows()
ScriptName = 'Equation Sketcher'
Options = []
Options.append([None, WindowsInputTypes.Image, 'EquationSketcher.png', 170])
Options.append(['Start point X', WindowsInputTypes.Integer, 0])
Options.append(['Start point Y', WindowsInputTypes.Integer, 0])
Options.append(['Equation y = ', WindowsInputTypes.String, '0.1*x**2'])
Options.append(['Plane', WindowsInputTypes.Plane, None])
Options.append(['X Range Start', WindowsInputTypes.Real, 0])
Options.append(['X Range End', WindowsInputTypes.Real, 10])
Options.append(['Number of points', WindowsInputTypes.Integer, 10])
Options.append(['Swap X and Y', WindowsInputTypes.Boolean, False])
Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
  sys.exit()
# get the inputs
NodeX = Values[1]
NodeY = Values[2]
Equation = Values[3]
Pl = Values[4]
StartX = Values[5]
EndX = Values[6]
NumPoints = Values[7]
SwapXY = Values[8]
# validate
if not Equation:
  Win.ErrorDialog('No equation entered', ScriptName)
  sys.exit()
if Pl == None:
  Win.ErrorDialog('No plane selected', ScriptName)
  sys.exit()
if StartX > EndX:
  Win.ErrorDialog('Start X value is greater than end X value', ScriptName)
  sys.exit()
if NumPoints < 2:
  Win.ErrorDialog('Invalid number of points', ScriptName)
  sys.exit()
# get the part that defines the sketch
Prt = Pl.GetPart()
# create a sketch on the plane
Sk = Prt.AddSketch("Equation Sketch", Pl)
print "Loading library..."
# we only import this now because it can cause a bit of a delay
from sympy import *
print "Calculating..."
# parse equation
x = Symbol('x')
Eq = sympify(Equation)
# work out how much we increase x between points
StepX = (EndX - StartX) / NumPoints
# calculate the points
Points = []
ValX = StartX
for p in xrange(NumPoints):
  ValY = Eq.subs(x, ValX)
  if SwapXY == True:
    PY = ValX
    PX = ValY
  else:
    PX = ValX
    PY = ValY
  Points.extend([float(PX + NodeX), float(PY + NodeY)])
  ValX = ValX + StepX
print "Generating sketch..."
# generate the bspline
Sk.AddBspline(Points, False)
