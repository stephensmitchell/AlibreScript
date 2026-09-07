class ThreeD:
    def __init__(
        self,
    ):
        pass
    def VectorTransform(self, Vector3DVector1, Vector3DVector2):
        pass
    def GetMatrixFromTransformation(self, IADTransformationTransformation):
        pass
    def TransformPoint(self, DoublePoint, IADTransformationTransformation):
        pass
    def TransformVector(self, DoubleVector, IADTransformationTransformation):
        pass
    def CreateTransformation(
        self,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
        IADGeometryFactoryGeomFactory,
    ):
        pass
    def CreateTranslation(
        self, Doublex, Doubley, Doublez, IADGeometryFactoryGeomFactory
    ):
        pass
    def CreateRotation(
        self, DoubleAngle, RotationDirectionsDirection, IADGeometryFactoryGeomFactory
    ):
        pass
    def DecomposeTransformation(
        self,
        IADTransformationTransformation,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
    ):
        pass
    def GetPerpendicularVector(self, ListVector):
        pass
    def TransformPointUsingVectors(
        self, ListSourceVector, ListDestinationVector, ListPoint
    ):
        pass
