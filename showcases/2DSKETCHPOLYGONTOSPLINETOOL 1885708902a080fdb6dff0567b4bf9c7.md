# 2DSKETCHPOLYGONTOSPLINETOOL

ID: A7246742B-22
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 27, 2025 5:51 PM
AI summary: Tool converts a selected closed sketch into a single B-spline, removing the original sketch and creating a new one with updated subdivision parameters. Users specify steps for lines, arcs, circles, and B-splines before conversion.

- 1st release snapshot - not the latest version of the tool.
    
    [2DSKETCHPOLYGONTOSPLINETOOL.zip](2DSKETCHPOLYGONTOSPLINETOOL.zip)
    
- Rough screenshots
    
    ![image.png](image%201.png)
    
    ![SNAG-0765.png](SNAG-0765.png)
    
    ![image.png](image%202.png)
    
    ![image.png](image%203.png)
    
    ![image.png](image%204.png)
    
    ![image.png](image%205.png)
    
    ![image.png](image%206.png)
    
    ![image.png](image%207.png)
    

```python
# --------------------------------------------------------------
# Script Name: 2DSKETCHPOLYGONTOSPLINETOOL.py
# Purpose:
#   Converts a selected closed sketch into a single Bspline
#   and removes the original sketch. A new sketch is
#   created on the same plane/face, with a new name that
#   includes the subdivision parameters.
#
# Usage:
#   1) Run the script in AlibreScript.
#   2) In the dialog, select the original Sketch to convert.
#   3) Specify the subdivision steps (line/arc/circle/bspline).
#   4) Click "Convert". The old sketch will be removed; a 
#      new sketch with a single Bspline is created with an
#      updated name.
#
# --------------------------------------------------------------

import sys
import math

def SubdivideLine(lineFigure, steps=8):
    """Return a list of [x, y] approximating a line."""
    pts = []
    x1, y1 = lineFigure.StartPoint
    x2, y2 = lineFigure.EndPoint
    for i in range(steps + 1):
        t = float(i)/steps
        x = x1 + t*(x2 - x1)
        y = y1 + t*(y2 - y1)
        pts.append([x, y])
    return pts

def SubdivideArc(arcFigure, steps=16):
    """Return a list of [x, y] approximating a circular arc."""
    pts = []
    cx, cy = arcFigure.Center
    r      = arcFigure.Radius
    arcDeg = arcFigure.Angle    # arc angle in degrees
    # start angle
    sx, sy = arcFigure.StartPoint
    angleStart = math.atan2(sy - cy, sx - cx)
    angleSweep = math.radians(arcDeg)
    for i in range(steps + 1):
        t = float(i)/steps
        ang = angleStart + angleSweep*t
        x = cx + r*math.cos(ang)
        y = cy + r*math.sin(ang)
        pts.append([x, y])
    return pts

def SubdivideCircle(circleFigure, steps=24):
    """Return a list of [x, y] approximating a full circle."""
    pts = []
    cx, cy = circleFigure.Center
    r      = circleFigure.Radius
    for i in range(steps):
        theta = 2.0*math.pi*(float(i)/steps)
        x = cx + r*math.cos(theta)
        y = cy + r*math.sin(theta)
        pts.append([x, y])
    # close the circle explicitly
    pts.append(pts[0])
    return pts

def SubdivideBspline(bsplineFigure, steps=24):
    """Return a list of [x, y] approximating the existing 2D Bspline."""
    subdiv = bsplineFigure.Subdivide(steps)  # [x1,y1, x2,y2, ...]
    pts = []
    for i in range(0, len(subdiv), 2):
        pts.append([subdiv[i], subdiv[i+1]])
    return pts

def GetFigurePoints(fig, lineSteps=8, arcSteps=16, circleSteps=24, bsplineSteps=24):
    """Return [ [x, y], ... ] for a single figure (Line, Arc, Circle, Bspline)."""
    figType = type(fig).__name__
    if figType == 'Line':
        return SubdivideLine(fig, lineSteps)
    elif figType == 'CircularArc':
        return SubdivideArc(fig, arcSteps)
    elif figType == 'Circle':
        return SubdivideCircle(fig, circleSteps)
    elif figType == 'Bspline':
        return SubdivideBspline(fig, bsplineSteps)
    else:
        # ignoring ellipse / ellipticalArc / ellipticalArc3D
        return []

def RemoveDupConsecutive(pts, tol=1e-9):
    """Remove consecutive duplicate points from the list."""
    if not pts:
        return pts
    newList = [pts[0]]
    for i in range(1, len(pts)):
        dx = pts[i][0] - newList[-1][0]
        dy = pts[i][1] - newList[-1][1]
        if (dx*dx + dy*dy) > (tol*tol):
            newList.append(pts[i])
    return newList

def CollectAllSketchPoints(oldSketch, lineSteps=8, arcSteps=16, circleSteps=24, bsplineSteps=24):
    """
    Collect subdivided points from all figures in the oldSketch,
    presumably forming a single closed loop. Return a list of [x,y].
    """
    allPts = []
    figs = oldSketch.Figures
    for f in figs:
        segPts = GetFigurePoints(f, lineSteps, arcSteps, circleSteps, bsplineSteps)
        if not segPts:
            continue
        if not allPts:
            allPts.extend(segPts)
        else:
            # if segPts' first ~ same as last of allPts, skip that
            dx = segPts[0][0] - allPts[-1][0]
            dy = segPts[0][1] - allPts[-1][1]
            if (dx*dx + dy*dy) < 1e-14 and len(segPts) > 1:
                allPts.extend(segPts[1:])
            else:
                allPts.extend(segPts)
    # refine duplicates
    refined = RemoveDupConsecutive(allPts, 1e-9)
    # enforce closure
    if len(refined) > 2:
        dx = refined[0][0] - refined[-1][0]
        dy = refined[0][1] - refined[-1][1]
        if (dx*dx + dy*dy) > 1e-14:
            refined.append(refined[0])
    return refined

def OnConvert(values):
    """
    Callback when user clicks "Convert". 
    We do:
    1) Get selected oldSketch
    2) Grab points
    3) Part.RemoveSketch(oldSketch)
    4) Create newSketch (with appended name) on the same plane/face
    5) Add Bspline
    """
    oldSketch   = values[0]
    lineSub     = values[1]
    arcSub      = values[2]
    circleSub   = values[3]
    bsplineSub  = values[4]

    if not oldSketch:
        print "No sketch selected."
        return

    # gather all points
    coords = CollectAllSketchPoints(oldSketch, lineSub, arcSub, circleSub, bsplineSub)
    if len(coords) < 2:
        print "No valid geometry or not enough points. Aborting."
        return

    oldName = oldSketch.Name
    surf = oldSketch.GetSurface()  # plane or face
    part = oldSketch.GetPart()

    # Remove the old sketch
    part.RemoveSketch(oldSketch)

    # Construct the new name for the sketch by appending the inputs:
    # e.g.  OLDNAME-TO-SPLINE-LINE<lineSub>ARC<arcSub>CIRCLE<circleSub>BSPLINE<bsplineSub>
    newName = "{}-TO-SPLINE-LINE<{}>ARC<{}>CIRCLE<{}>BSPLINE<{}>".format(
        oldName, lineSub, arcSub, circleSub, bsplineSub
    )

    # Create a brand-new sketch with the updated name on the same plane/face
    newSketch = part.AddSketch(newName, surf)

    # Flatten coords into [x1,y1, x2,y2, ...]
    flatten = []
    for p in coords:
        flatten.extend(p)

    # Add the B-spline to the new sketch
    newSketch.AddBspline(flatten, False)

    print "Done. Old sketch removed. New sketch named '%s' was created with a single Bspline." % newName

# Build the dialog for user input
Win = Windows()
dlgInputs = []
dlgInputs.append(['Closed Sketch to Convert', WindowsInputTypes.Sketch, None])
dlgInputs.append(['Line Steps',    WindowsInputTypes.Integer, 8])
dlgInputs.append(['Arc Steps',     WindowsInputTypes.Integer, 16])
dlgInputs.append(['Circle Steps',  WindowsInputTypes.Integer, 24])
dlgInputs.append(['Bspline Steps', WindowsInputTypes.Integer, 24])

Win.UtilityDialog(
    "2DSKETCHPOLYGONTOSPLINETOOL.py",
    "Convert",
    OnConvert,
    None,
    dlgInputs,
    500
)
```