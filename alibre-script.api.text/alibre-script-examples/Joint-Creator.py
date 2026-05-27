#https://help.alibre.com/articles/#!alibre-help-v23/joint-creator
# Joint Creator
# (c) Alibre, LLC 2019, All Rights Reserved
# Version 1.00
from __future__ import division
from math import *
# gets locaton of edge in a part coordinate system
# returns a list of two points defining the edge
def GetPartEdge(Prt, SharedEdge):
  Point1 = Prt.AssemblyPointtoPartPoint(SharedEdge[0])
  Point2 = Prt.AssemblyPointtoPartPoint(SharedEdge[1])
  return [Point1, Point2]
# compares two points [X1, Y1, Z1] and [X2, Y2, Z2]
# returns true if they are the same
def PointsAreEqual(P1, P2):
  if (round(P1[0], 6) == round(P2[0], 6) and
      round(P1[1], 6) == round(P2[1], 6) and
      round(P1[2], 6) == round(P2[2], 6)):
    return True
  else:
    return False
# gets part faces that use an edge
# returns a list of faces
def GetFacesFromEdge(Prt, SharedEdge):
  Faces = []
  PartEdge = GetPartEdge(Prt, SharedEdge)
  for Fce in Prt.Faces:
    for Edg in Fce.GetEdges():
      EdgeVertices = Edg.GetVertices()
      V1 = [EdgeVertices[0].X, EdgeVertices[0].Y, EdgeVertices[0].Z]
      V2 = [EdgeVertices[1].X, EdgeVertices[1].Y, EdgeVertices[1].Z]
      if ((PointsAreEqual(V1, PartEdge[0]) and PointsAreEqual(V2, PartEdge[1])) or
          (PointsAreEqual(V2, PartEdge[0]) and PointsAreEqual(V1, PartEdge[1]))):
         Faces.append(Fce)
  return Faces
# gets an edge that is shared between two parts
# returns list of edge vertices
def GetSharedEdge(Prt1, Prt2):  
  CornerVertices = []
  for TabVert in Prt1.GetAssemblyVertices():
    for BaseVert in Prt2.GetAssemblyVertices():
      if PointsAreEqual(TabVert, BaseVert):
        CornerVertices.append(TabVert)
  return CornerVertices
# gets the length of an edge
# returns edge length
def GetEdgeLength(Vert1, Vert2):
  a = abs(Vert2[0] - Vert1[0])
  b = abs(Vert2[1] - Vert1[1])
  c = abs(Vert2[2] - Vert1[2])
  return sqrt(a * a + b * b + c * c)
# gets the largest face from a set of faces
def GetLargestFace(Faces):
  if Faces[0].GetArea() > Faces[1].GetArea():
    return Faces[0]
  elif Faces[1].GetArea() > Faces[0].GetArea():
    return Faces[1]
  else:
    print "Unable to determine face of part."
    sys.exit()
# gets the smallest face from a set of faces
def GetSmallestFace(Faces):
  if Faces[0].GetArea() < Faces[1].GetArea():
    return Faces[0]
  elif Faces[1].GetArea() < Faces[0].GetArea():
    return Faces[1]
  else:
    print "Unable to determine face of part."
    sys.exit()
# generates a range of real values from start to stop
# incremented by step
def frange(start, stop, step):
  i = start
  if start < stop:
    while i < stop:
      yield i
      i += step
  else:
    while i > stop:
      yield i
      i += step
# gets the shortest edge of a face
# returns shortest edge
def GetShortestEdge(Fce):
  Shortest = Fce.GetEdges()[0]
  for E in Fce.GetEdges():
    if E.Length < Shortest.Length:
      Shortest = E
  return Shortest
# generates pin offsets
# NumPins = number of pins
# EdgeLength = length of edge for pins
# PinSense = True = slot at edge, False = pin at edge
# EdgeOffset = distance from ends of edges before pins
# Gap = distance between slot and pin
# returns: [ [Pin_1_Start, Pin_1_End], ..., [Pin_n_Start, Pin_n_End] ]
def GeneratePinOffsets(NumPins, EdgeLength, PinSense, EdgeOffset, Gap):
  Offsets = []
  # reduce length of edge by the edge offset at each end
  # giving a length that we generate pins and slots over
  PinEdgeLength = EdgeLength - (EdgeOffset * 2)
  # get length of each pin
  if PinSense == False:
    PinLength = PinEdgeLength / (NumPins + (NumPins - 1))
    PinState = True
  else:
    PinLength = PinEdgeLength / (NumPins + (NumPins + 1))
    PinState = False
  # generate start and end point of each pin
  CurrentPin = 0
  for Y in frange(EdgeOffset, EdgeLength - EdgeOffset, PinLength):
    if PinState:
      # if pins are never at the edges then always use gap on each
      # side of pin
      if PinSense == True:
        Offsets.append([Y - Gap, Y + PinLength + Gap])
      # pins could be at edges where we don't want the gap to be applied
      else:
        if CurrentPin == 0:
          # first pin, no gap at start
          Offsets.append([Y, Y + PinLength + Gap])
        elif CurrentPin == NumPins - 1:
          # last pin, no gap at end
          Offsets.append([Y - Gap, Y + PinLength])
        else:
          # middle pin, gap at start and end
          Offsets.append([Y - Gap, Y + PinLength + Gap])
      CurrentPin += 1
    PinState = not PinState
  return Offsets
# generates slot offsets
# NumPins = number of pins
# EdgeLength = length of edge for slots
# PinSense = True = slot at edge, False = pin at edge
# EdgeOffset = distance from ends of edges before pins
# Gap = distance between slot and pin
# returns: [ [Slot_1_Start, Slot_1_End], ..., [Slot_n_Start, Slot_n_End] ]
def GenerateSlotOffsets(NumPins, EdgeLength, PinSense, EdgeOffset, Gap):
  Offsets = []
  # reduce length of edge by the edge offset at each end
  # giving a length that we generate pins and slots over
  PinEdgeLength = EdgeLength - (EdgeOffset * 2)
  # get length of each pin
  if PinSense == False:
    PinLength = PinEdgeLength / (NumPins + (NumPins - 1))
    PinState = False
  else:
    PinLength = PinEdgeLength / (NumPins + (NumPins + 1))
    PinState = True
  if PinSense == True:
    NumSlots = NumPins + 1
  else:
    NumSlots = NumPins - 1
  # add initial slot for edge offset if pins are on outside of slots
  if EdgeOffset > 0 and PinSense == False:
    Offsets.append([0, EdgeOffset + (Gap * 2.0)])
  # generate start and end point of each slot
  CurrentSlot = 0
  for Y in frange(EdgeOffset, EdgeLength - EdgeOffset, PinLength):
    if PinState:
      # if slots are never at the edges then always use gap on each
      # side of slot
      if PinSense == False or (EdgeOffset > 0):
        Offsets.append([Y - Gap, Y + PinLength + Gap])
      # slots could be at edges where we don't want the gap to be applied
      else:
        if CurrentSlot == 0:
          # first slot, no gap at start
          Offsets.append([Y, Y + PinLength + Gap])
        elif CurrentSlot == NumSlots - 1:
          # last slot, no gap at end
          Offsets.append([Y - Gap, Y + PinLength])
        else:
          # middle pin, gap at start and end
          Offsets.append([Y - Gap, Y + PinLength + Gap])
      CurrentSlot += 1
    PinState = not PinState
  # add final slot for edge offset if pins are on outside of slots
  if EdgeOffset > 0 and PinSense == False:
    Offsets.append([EdgeLength - EdgeOffset - (Gap * 2.0), EdgeLength])
  if EdgeOffset > 0 and PinSense == True:
    # extend first slot to cover edge offset
    Offsets[0][0] = 0
    # extend last slot to cover edge offset
    Offsets[len(Offsets) - 1][1] = EdgeLength
  return Offsets
# generates the pins
# Prt = part to create pins on
# Fce = face on part to create pins
# PinOffsets = start and end values for pins
# Thickness = depth of pins
# SharedEdge = edge to generate pins along
def GeneratePins(Prt, Fce, PinOffsets, Thickness, SharedEdge):
  TabProfile = Prt.AddSketch('Pin Profile', Fce)
  TabEdge = GetPartEdge(Prt, SharedEdge)
  TabProfile.StartFaceMapping(TabEdge[0], TabEdge[1])
  for PinOffset in PinOffsets:
    TabProfile.AddRectangle(PinOffset[0], 0, PinOffset[1], Thickness, False)
  TabProfile.StopFaceMapping()
  # cut out rectangles (pins)
  Prt.AddExtrudeCut('Pins', TabProfile, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, False)
# generates the slots
# Prt = part to create slots on
# Fce = face on part to create slots
# SlotOffsets = start and end values for slots
# Thickness = depth of slots
# SharedEdge = edge to generate slots along
def GenerateSlots(Prt, Fce, SlotOffsets, Thickness, SharedEdge):
  BaseProfile = Prt.AddSketch('Slot Profile', Fce)
  BaseEdge = GetPartEdge(Prt, SharedEdge)
  BaseProfile.StartFaceMapping(BaseEdge[0], BaseEdge[1])
  for SlotOffset in SlotOffsets:
    BaseProfile.AddRectangle(SlotOffset[0], 0, SlotOffset[1], Thickness, False)
  BaseProfile.StopFaceMapping()
  # cut out rectangles (slots)
  Prt.AddExtrudeCut('Slots', BaseProfile, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, False)
# creates a joint based on user inputs
def CreateJoint(Values):
  TabPart      = Values[1]
  BasePart     = Values[2]
  NumberofPins = Values[3]
  PinSense     = Values[4]
  EdgeOffset   = Values[5]
  Gap          = Values[6]
  print "Gathering information..."
  # get edge shared by both parts
  SharedEdge = GetSharedEdge(TabPart, BasePart)
  # get the part faces for the shared edge
  TabFaces = GetFacesFromEdge(TabPart, SharedEdge)
  BaseFaces = GetFacesFromEdge(BasePart, SharedEdge)
  # get the largest faces on each part that use the shared edge
  TabFace = GetLargestFace(TabFaces)
  BaseFace = GetLargestFace(BaseFaces)
  # the smallest faces on each part that use the shared edge
  TabEndFace = GetSmallestFace(TabFaces)
  BaseEndFace = GetSmallestFace(BaseFaces)
  # get length of shared edge
  SharedEdgeLength = GetEdgeLength(SharedEdge[0], SharedEdge[1])
  # get thickness of each part
  TabThickness = GetShortestEdge(TabEndFace).Length
  BaseThickness = GetShortestEdge(BaseEndFace).Length
  print "Calculating..."
  # generate pin and slot offsets
  PinOffsets = GeneratePinOffsets(NumberofPins, SharedEdgeLength, PinSense, EdgeOffset, Gap / 2.0)
  SlotOffsets = GenerateSlotOffsets(NumberofPins, SharedEdgeLength, PinSense, EdgeOffset, Gap / 2.0)
  print "Generating..."
  # generate pins and slots
  GeneratePins(TabPart, TabFace, PinOffsets, BaseThickness, SharedEdge)
  GenerateSlots(BasePart, BaseFace, SlotOffsets, TabThickness, SharedEdge)
  print "Finished"
#################################################################################################
# check minimum requirements
if AlibreScriptVersion < 1110:
  sys.exit('Please upgrade your copy of Alibre Design to use this script')
ScriptName = 'Joint Creator'
Win = Windows()
# define options to show in dialog window
Options = []
Options.append([None, WindowsInputTypes.Image, 'JointCreatorIcon.png', 200])
Options.append(['Tab Part', WindowsInputTypes.Part, None])
Options.append(['Base Part', WindowsInputTypes.Part, None])
Options.append(['Number of Pins', WindowsInputTypes.Integer, 5])
Options.append(['Pins on Inside', WindowsInputTypes.Boolean, False])
Options.append(['Offset From Ends', WindowsInputTypes.Real, 0.0])
Options.append(['Gap Between Pins and Slots', WindowsInputTypes.Real, 0.0])
# show utility window
Win.UtilityDialog(ScriptName, 'Create Joint', CreateJoint, None, Options, 200)