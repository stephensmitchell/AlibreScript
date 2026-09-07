class GearSketch:
    def __init__(self, Name, Figures, Origin):
        pass
        self.Name = Name
        self.Figures = Figures
        self.Origin = Origin
    def GetPart(
        self,
    ):
        pass
    def GetSurface(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
        pass
    def StartEditing(
        self,
    ):
        pass
    def StopEditing(
        self,
    ):
        pass
    def AddConstraint(self, ISketchFigureFigure, ConstraintsConstraint):
        pass
    def AddConstraint(self, ListFigures, ConstraintsConstraint):
        pass
    def AddLine(self, ListStartPoint, ListEndPoint, BooleanIsReference):
        pass
    def AddLine(self, LineNewLine):
        pass
    def AddLine(self, DoubleX1, DoubleY1, DoubleX2, DoubleY2, BooleanIsReference):
        pass
    def AddPoint(self, DoubleX, DoubleY):
        pass
    def AddPoint(self, DoubleX, DoubleY, BooleanIsReference):
        pass
    def AddPoint(self, SketchPointNewPoint):
        pass
    def AddLines(self, ListPoints, BooleanIsReference):
        pass
    def AddPolyline(self, PolylineLine, BooleanIsReference):
        pass
    def AddArcCenterStartEnd(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleStartX,
        DoubleStartY,
        DoubleEndX,
        DoubleEndY,
        BooleanIsReference,
    ):
        pass
    def AddArcCenterStartAngle(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleStartX,
        DoubleStartY,
        DoubleAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleMajorX,
        DoubleMajorY,
        DoubleMinorX,
        DoubleMinorY,
        BooleanIsReference,
    ):
        pass
    def AddEllipse(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleMajorAxisDiameter,
        DoubleMinorMajorRatio,
        DoubleMajorAxisAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse(self, EllipseNewEllipse):
        pass
    def AddEllipticalArc(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleStartX,
        DoubleStartY,
        DoubleEndX,
        DoubleEndY,
        DoubleMajorAxisDiameter,
        DoubleMinorMajorRatio,
        DoubleMajorAxisAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipticalArc(self, EllipticalArcNewEllipticalArc):
        pass
    def AddArc(self, CircularArcNewArc):
        pass
    def AddRectangle(
        self,
        DoubleBottomLeftX,
        DoubleBottomLeftY,
        DoubleTopRightX,
        DoubleTopRightY,
        BooleanIsReference,
    ):
        pass
    def AddCircle(
        self, DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def AddCircle(self, CircleNewCircle):
        pass
    def AddBspline(
        self,
        Int32Order,
        ListControlPoints,
        ListKnotVectors,
        ListWeights,
        BooleanIsReference,
    ):
        pass
    def AddBspline(self, ListPoints, BooleanIsReference):
        pass
    def AddFigure(self, ISketchFigureNewFigure):
        pass
    def AddBspline(self, BsplineNewBspline):
        pass
    def AddBspline(
        self,
        Int32Order,
        List1ControlPoints,
        List1KnotVectors,
        List1Weights,
        BooleanIsReference,
    ):
        pass
    def AddBsplineInterpolated(self, List1Points, BooleanIsReference):
        pass
    def AddBsplineThroughPoints(self, List1Points, BooleanIsReference):
        pass
    def AddPolygon(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleDiameter,
        Int32Sides,
        BooleanIsReference,
    ):
        pass
    def AddPolyhole(
        self, DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def PathObject(
        self,
    ):
        pass
    def CrossSectionObject(
        self,
    ):
        pass
    def CopyFrom(self, SketchSource):
        pass
    def CopyFrom(
        self,
        SketchSource,
        DoubleAngle,
        DoubleRotationCenterX,
        DoubleRotationCenterY,
        DoubleTranslateX,
        DoubleTranslateY,
        DoubleScaleOriginX,
        DoubleScaleOriginY,
        DoubleScaleFactor,
    ):
        pass
    def PointtoGlobal(self, Doublex, Doubley):
        pass
    def GlobaltoPoint(self, Doublex, Doubley, Doublez):
        pass
    def VertextoPoint(self, VertexVert):
        pass
    def GetSelectionAssembly(
        self,
    ):
        pass
    def SetOccurrence(self, IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
        self,
    ):
        pass
    def SetParentAssembly(self, AssemblyParentAssembly):
        pass
    def GetParentAssembly(
        self,
    ):
        pass
    def AddDimension(self, SketchPointP1, SketchPointP2):
        pass
    def AddDimension(self, CircleCircle):
        pass
    def AddDimension(self, CircularArcArc):
        pass
    def SavetoXml(self, StringFileName):
        pass
    def ToXml(
        self,
    ):
        pass
    def LoadXml(self, StringFileName):
        pass
    def FromXml(self, StringXml):
        pass
    def StartFaceMapping(self, VertexEdgeVertex1, VertexEdgeVertex2):
        pass
    def StartFaceMapping(self, ListEdgeEndPoint1, ListEdgeEndPoint2):
        pass
    def StopFaceMapping(
        self,
    ):
        pass
    def StartMapping(self, ListPoint1, ListPoint2, ListPointAboveAxis):
        pass
    def StopMapping(
        self,
    ):
        pass
    def ImportSVG(self, StringFileName):
        pass
    def ImportSVG(
        self,
        StringFileName,
        DoubleTranslateX,
        DoubleTranslateY,
        DoubleRotationAngle,
        BooleanTranslateThenRotate,
        BooleanNativeFigures,
    ):
        pass
    def ExportSVG(self, StringFileName):
        pass
    def ExportSVG(self, StringFileName, BooleanIncludeReferences):
        pass
    def ExportSVG(
        self,
        StringFileName,
        BooleanIncludeReferences,
        DoubleStrokeWidth,
        StringStrokeColor,
        StringStrokeLineCap,
        BooleanStrokeDashed,
        DoubleStrokeDashLength,
        DoubleReferenceStrokeWidth,
        StringReferenceStrokeColor,
        StringReferenceStrokeLineCap,
        BooleanReferenceStrokeDashed,
        DoubleReferenceStrokeDashLength,
    ):
        pass
