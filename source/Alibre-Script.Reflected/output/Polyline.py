class Polyline:
    def __init__(
        self,
    ):
        pass
    def AddPoint(self, PolylinePointPoint):
        pass
    def AddPoint(self, DoubleX, DoubleY):
        pass
    def InsertPoint(self, Int32Index, PolylinePointPoint):
        pass
    def AddCircle(self, DoubleCenterX, DoubleCenterY, DoubleDiameter, Int32sides):
        pass
    def AddArc(
        self,
        PolylinePointCenter,
        PolylinePointStart,
        PolylinePointEnd,
        Int32MinimumSegments,
    ):
        pass
    def AddPolyline(self, PolylineAppendLine):
        pass
    def FindIntersection(self, PolylineL1, PolylineL2):
        pass
    def FindIntersectionWithCircle(
        self, PolylineL1, DoubleCircleX, DoubleCircleY, DoubleRadius
    ):
        pass
    def FindIntersection(
        self, PolylinePointA1, PolylinePointA2, PolylinePointB1, PolylinePointB2
    ):
        pass
    def IsPointOnLine(
        self, PolylinePointA1, PolylinePointA2, PolylinePointPoint, DoubleTolerance
    ):
        pass
    def SplitAtPoint(self, PolylinePointSplitPoint, DoubleTolerence):
        pass
    def Clone(
        self,
    ):
        pass
    def Clone(self, Int32StartIndex, Int32EndIndex):
        pass
    def Join(self, PolylineAppendLine):
        pass
    def RotateZ(self, DoubleCenterX, DoubleCenterY, DoubleAngle):
        pass
    def Offset(self, DoubleOffsetX, DoubleOffsetY):
        pass
    def RemoveDuplicates(
        self,
    ):
        pass
