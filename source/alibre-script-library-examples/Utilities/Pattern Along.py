# Pattern Along script
# Demonstrates copying a sketch along a bspline
# For use with Alibre Design
from __future__ import division
from math import sqrt
ScriptName = 'Pattern Along'
# adds a copy of a sketch to a specific point and normal
def AddPattern(CurrentPart, Point, Normal, SourceSketch):
  Pl = CurrentPart.AddPlane('Sk', Normal, Point)
  PlSk = CurrentPart.AddSketch('PlSk', Pl)
  SkPoint = PlSk.GlobaltoPoint(Point[0], Point[1], Point[2])
  PlSk.CopyFrom(SourceSketch, 0, 0, 0, SkPoint[0], SkPoint[1], 0, 0, 100.0)
  Pl.Hide()
Win = Windows()
# define options to show in dialog window
Options = []
Options.append([None, WindowsInputTypes.Image, 'PatternAlong.png', 170])
Options.append(['Path 3D Sketch', WindowsInputTypes.Sketch3D, None])
Options.append(['Pattern 2D Sketch', WindowsInputTypes.Sketch, None])
Options.append(['Number of Patterns', WindowsInputTypes.Integer, 10])
Options.append(['Add Pattern to Start', WindowsInputTypes.Boolean, False])
Options.append(['Add Pattern to End', WindowsInputTypes.Boolean, False])
# show dialog to user, get inputs
Values = Win.OptionsDialog(ScriptName, Options, 170)
if Values == None:
  sys.exit()
# get the inputs
PathSketch = Values[1]
PatternSketch = Values[2]
NumPatterns = Values[3]
AddtoStart = Values[4]
AddtoEnd = Values[5]
# validate
if PathSketch == None:
  Win.ErrorDialog('No path sketch selected', ScriptName)
  sys.exit()
if PatternSketch == None:
  Win.ErrorDialog('No pattern sketch selected', ScriptName)
  sys.exit()
if NumPatterns < 1:
  Win.ErrorDialog('Invalid number of patterns', ScriptName)
  sys.exit()
NumSegments = NumPatterns + 1
# get the part to use
Prt = PathSketch.GetPart()
# get the bspline from the sketch
Spl = None
for Figure in PathSketch.Figures:
  if isinstance(Figure, Bspline3D):
    Spl = Figure
# check  bspline was found
if Spl == None:
  Win.ErrorDialog('No Bspline found in the path sketch', ScriptName)
  sys.exit()
print 'Calculating...'
# divide the bspline up into segments and get the point between the
# segments and the normal at each point
SubPt = Spl.SubdivideGetNormals(NumSegments)
# extract points and normals and create sketch copies
it = iter(SubPt)
for Pt in it:
  Point = [Pt, next(it), next(it)]
  Normal = [next(it), next(it), next(it)]
  AddPattern(Prt, Point, Normal, PatternSketch)
# add copy of sketch to start of bspline
if AddtoStart == True:
  Point = Spl.GetPointAt(0.0)
  Normal = Spl.GetNormalAt(0.0)
  AddPattern(Prt, Point, Normal, PatternSketch)
# add copy of sketch to end of bspline
if AddtoEnd == True:
  Point = Spl.GetPointAt(1.0)
  Normal = Spl.GetNormalAt(1.0)
  AddPattern(Prt, Point, Normal, PatternSketch)
