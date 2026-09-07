class Part:
    def __init__(
        self,
        Name,
        Faces,
        Edges,
        Vertices,
        ParameterList,
        ConfigurationList,
        Parameters,
        Configurations,
        Density,
        Material,
        Description,
        Number,
        Mass,
        Comment,
        CostCenter,
        CreatedBy,
        CreatedDate,
        CreatingApplication,
        DocumentNumber,
        EngineeringApprovalDate,
        EngineeringApprovedBy,
        EstimatedCost,
        Keywords,
        LastAuthor,
        LastUpdateDate,
        ExtendedMaterialInformation,
        ManufacturingApprovedBy,
        ManufacturingApprovedDate,
        ModifiedInformation,
        Product,
        ReceivedFrom,
        Revision,
        StockSize,
        Supplier,
        Title,
        Vendor,
        WebLink,
        FileName,
        XYPlane,
        YZPlane,
        ZXPlane,
        XAxis,
        YAxis,
        ZAxis,
        Origin,
        Selections,
    ):
        pass
        self.Name = Name
        self.Faces = Faces
        self.Edges = Edges
        self.Vertices = Vertices
        self.ParameterList = ParameterList
        self.ConfigurationList = ConfigurationList
        self.Parameters = Parameters
        self.Configurations = Configurations
        self.Density = Density
        self.Material = Material
        self.Description = Description
        self.Number = Number
        self.Mass = Mass
        self.Comment = Comment
        self.CostCenter = CostCenter
        self.CreatedBy = CreatedBy
        self.CreatedDate = CreatedDate
        self.CreatingApplication = CreatingApplication
        self.DocumentNumber = DocumentNumber
        self.EngineeringApprovalDate = EngineeringApprovalDate
        self.EngineeringApprovedBy = EngineeringApprovedBy
        self.EstimatedCost = EstimatedCost
        self.Keywords = Keywords
        self.LastAuthor = LastAuthor
        self.LastUpdateDate = LastUpdateDate
        self.ExtendedMaterialInformation = ExtendedMaterialInformation
        self.ManufacturingApprovedBy = ManufacturingApprovedBy
        self.ManufacturingApprovedDate = ManufacturingApprovedDate
        self.ModifiedInformation = ModifiedInformation
        self.Product = Product
        self.ReceivedFrom = ReceivedFrom
        self.Revision = Revision
        self.StockSize = StockSize
        self.Supplier = Supplier
        self.Title = Title
        self.Vendor = Vendor
        self.WebLink = WebLink
        self.FileName = FileName
        self.XYPlane = XYPlane
        self.YZPlane = YZPlane
        self.ZXPlane = ZXPlane
        self.XAxis = XAxis
        self.YAxis = YAxis
        self.ZAxis = ZAxis
        self.Origin = Origin
        self.Selections = Selections
    def RemovePoint(self, PointPoint):
        pass
    def RemovePlane(self, PlanePlane):
        pass
    def RemoveSketch(self, StringName):
        pass
    def RemoveSketch(self, SketchSketch):
        pass
    def Add3DSketch(self, StringName):
        pass
    def AddGear(
        self,
        StringName,
        DoubleDiametralPitch,
        Int32NumberofTeeth,
        DoublePitchDiameter,
        DoublePressureAngle,
        BooleanSingleTooth,
        DoubleCenterX,
        DoubleCenterY,
        Int32InvolutePoints,
        ISketchSurfacePlane,
    ):
        pass
    def AddGear(
        self,
        StringName,
        DoubleDiametralPitch,
        Int32NumberofTeeth,
        DoublePitchDiameter,
        DoublePressureAngle,
        BooleanSingleTooth,
        DoubleCenterX,
        DoubleCenterY,
        Int32InvolutePoints,
        DoubleProfileShiftFactor,
        DoubleAddendumCoefficient,
        DoubleDedendumCoefficient,
        DoubleClearanceCoefficient,
        ISketchSurfacePlane,
    ):
        pass
    def AddRack(
        self,
        StringName,
        DoubleDiametralPitch,
        Int32NumberofTeeth,
        DoublePitchDiameter,
        DoublePressureAngle,
        DoubleProfileShiftFactor,
        DoubleAddendumCoefficient,
        DoubleDedendumCoefficient,
        DoubleClearanceCoefficient,
        DoublePitchPointtoBase,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearNP(
        self,
        StringName,
        Int32NumberofTeeth,
        DoublePitchDiameter,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearNP(
        self,
        StringName,
        Int32NumberofTeeth,
        DoublePitchDiameter,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        BooleanSingleTooth,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearDP(
        self,
        StringName,
        DoubleDiametralPitch,
        DoublePitchDiameter,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearDP(
        self,
        StringName,
        DoubleDiametralPitch,
        DoublePitchDiameter,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        BooleanSingleTooth,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearDN(
        self,
        StringName,
        DoubleDiametralPitch,
        Int32NumberofTeeth,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        ISketchSurfacePlane,
    ):
        pass
    def AddGearDN(
        self,
        StringName,
        DoubleDiametralPitch,
        Int32NumberofTeeth,
        DoublePressureAngle,
        DoubleCenterX,
        DoubleCenterY,
        BooleanSingleTooth,
        ISketchSurfacePlane,
    ):
        pass
    def AddAxis(self, StringName, ISketchSurfacePlane1, ISketchSurfacePlane2):
        pass
    def AddAxis(self, StringName, PointPointA, PointPointB):
        pass
    def AddAxis(self, StringName, FaceCylindricalFace):
        pass
    def AddAxis(self, StringName, ListPoint1, ListPoint2):
        pass
    def AddPoint(self, StringName, ListPoint):
        pass
    def AddPoint(self, StringName, PointPoint):
        pass
    def AddPoint(self, StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoints(self, StringPrefix, ListPoints):
        pass
    def Regenerate(
        self,
    ):
        pass
    def AddExtrudeBoss(self, StringName, SketchSketch, DoubleDepth, BooleanIsReversed):
        pass
    def AddExtrudeBoss(
        self,
        StringName,
        SketchSketch,
        DoubleDepth,
        BooleanIsReversed,
        EndConditionEndCondition,
        ISketchSurfaceEndPlane,
        DoubleEndOffset,
        DirectionTypeDirection,
        ISweepPathSweepPath,
        DoubleDraftAngle,
        BooleanOutwardDraft,
    ):
        pass
    def AddExtrudeCut(self, StringName, SketchSketch, DoubleDepth, BooleanIsReversed):
        pass
    def AddExtrudeCut(
        self,
        StringName,
        SketchSketch,
        DoubleDepth,
        BooleanIsReversed,
        EndConditionEndCondition,
        ISketchSurfaceEndPlane,
        DoubleEndOffset,
        DirectionTypeDirection,
        ISweepPathSweepPath,
        DoubleDraftAngle,
        BooleanOutwardDraft,
    ):
        pass
    def AddRevolveBoss(self, StringName, SketchSketch, AxisAxis, DoubleAngle):
        pass
    def AddRevolveCut(self, StringName, SketchSketch, AxisAxis, DoubleAngle):
        pass
    def AddLoftBoss(
        self,
        StringName,
        ListCrossSections,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddLoftBoss(
        self,
        StringName,
        ListCrossSections,
        ListGuideCurves,
        GuideCurveTypesGuideType,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddLoftCut(
        self,
        StringName,
        ListCrossSections,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddLoftCut(
        self,
        StringName,
        ListCrossSections,
        ListGuideCurves,
        GuideCurveTypesGuideType,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddSweepBoss(
        self,
        StringName,
        SketchProfileSketch,
        ISweepPathPathSketch,
        BooleanIsRigid,
        EndConditionEndCondition,
        ISketchSurfaceEndPlane,
        DoubleEndOffset,
        DoubleDraftAngle,
        BooleanOutwardDraft,
    ):
        pass
    def AddSweepCut(
        self,
        StringName,
        SketchProfileSketch,
        ISweepPathPathSketch,
        BooleanIsRigid,
        EndConditionEndCondition,
        ISketchSurfaceEndPlane,
        DoubleEndOffset,
        DoubleDraftAngle,
        BooleanOutwardDraft,
    ):
        pass
    def AddFillet(
        self, StringName, IFilletableItem, DoubleRadius, BooleanTangentPropagate
    ):
        pass
    def AddFillet(self, StringName, ListItems, DoubleRadius, BooleanTangentPropagate):
        pass
    def AddFillet(
        self,
        StringName,
        ListItems,
        ListStartRadii,
        ListEndRadii,
        BooleanTangentPropagate,
    ):
        pass
    def Scale(self, StringName, BooleanScaleAboutCenter, DoubleScaleFactor):
        pass
    def NonUniformScale(
        self,
        StringName,
        BooleanScaleAboutCenter,
        DoubleScaleFactorX,
        DoubleScaleFactorY,
        DoubleScaleFactorZ,
    ):
        pass
    def AddChamfer(
        self,
        StringName,
        IChamferableItem,
        DoubleDistance1,
        DoubleDistance2,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamfer(
        self,
        StringName,
        ListItems,
        DoubleDistance1,
        DoubleDistance2,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamfer(
        self, StringName, IChamferableItem, DoubleDistance, BooleanTangentPropagate
    ):
        pass
    def GetEdges(
        self,
    ):
        pass
    def GetFaces(
        self,
    ):
        pass
    def GetVertices(
        self,
    ):
        pass
    def GetBoundingBox(
        self,
    ):
        pass
    def AddChamfer(
        self, StringName, ListItems, DoubleDistance, BooleanTangentPropagate
    ):
        pass
    def AddChamferAngle(
        self,
        StringName,
        IChamferableItem,
        DoubleDistance,
        DoubleAngle,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamferAngle(
        self,
        StringName,
        ListItems,
        DoubleDistance,
        DoubleAngle,
        BooleanTangentPropagate,
    ):
        pass
    def AddVertexChamfer(
        self, StringName, VertexItem, DoubleDistance1, DoubleDistance2, DoubleDistance3
    ):
        pass
    def AddVertexChamfer(
        self, StringName, ListItems, DoubleDistance1, DoubleDistance2, DoubleDistance3
    ):
        pass
    def Save(
        self,
    ):
        pass
    def Save(self, StringFolder):
        pass
    def SaveAs(self, StringFolder, StringNewName):
        pass
    def Close(
        self,
    ):
        pass
    def ExportSTL(self, StringFileName):
        pass
    def ExportRotatedSTL(
        self,
        StringFileName,
        FaceBottomFace,
        BooleanForcetoMillimeters,
        BooleanUseCustomSettings,
        DoubleMaxCellSize,
        DoubleNormalDeviation,
        DoubleSurfaceDeviation,
    ):
        pass
    def DisplayUnits(
        self,
    ):
        pass
    def ExportSTEP203(self, StringFileName):
        pass
    def ExportSTEP214(self, StringFileName):
        pass
    def ExportIGES(self, StringFileName):
        pass
    def ExportSAT(self, StringFileName, Int32Version, BooleanSaveColors):
        pass
    def ExportBIP(self, StringFileName):
        pass
    def SetColor(self, ByteRed, ByteGreen, ByteBlue):
        pass
    def SaveSnapshot(
        self,
        StringFileName,
        Int32Width,
        Int32Height,
        BooleanUseAspectRatio,
        BooleanUseWidthandHeight,
    ):
        pass
    def SaveThumbnail(self, StringFileName, Int32Width, Int32Height):
        pass
    def GetSelection(
        self,
    ):
        pass
    def Select(self, ISelectableGeometryFaceorEdge):
        pass
    def Select(self, ListFacesEdgesList):
        pass
    def SetUserData(self, StringName, PythonDictionaryDict):
        pass
    def GetUserData(self, StringName):
        pass
    def Debug1(self, PlanePlane):
        pass
    def PauseUpdating(
        self,
    ):
        pass
    def ResumeUpdating(
        self,
    ):
        pass
    def GetSelectionAssembly(
        self,
    ):
        pass
    def AddPoint(
        self,
        StringName,
        IPointPointOrVertex,
        DoubleXOffset,
        DoubleYOffset,
        DoubleZOffset,
    ):
        pass
    def AddPoint(
        self, StringName, IPointPointOrVertex1, IPointPointOrVertex2, DoubleRatio
    ):
        pass
    def AddPoint(self, StringName, IAxisAxisOrEdge1, IAxisAxisOrEdge2):
        pass
    def AddPoint(
        self, StringName, IPlanePlaneOrFace1, IPlanePlaneOrFace2, IPlanePlaneOrFace3
    ):
        pass
    def AddPoint(self, StringName, IAxisAxisOrEdge, IPlanePlaneOrFace):
        pass
    def AddPoint(
        self,
        StringName,
        IPointSourcePointOrVertex,
        IPlaneTargetPlaneOrFace,
        DoubleXOffset,
        DoubleYOffset,
    ):
        pass
    def AddPoint(self, StringName, EdgeTargetEdge, DoubleRatio):
        pass
    def AddPointFromCircularEdge(self, StringName, EdgeTargetEdge):
        pass
    def AddPointFromToroidalFace(self, StringName, FaceTargetFace):
        pass
    def IsOpen(
        self,
    ):
        pass
    def GetFeature(self, StringName):
        pass
    def RemoveFeature(self, StringName):
        pass
    def RemoveFeature(self, FeatureFeature):
        pass
    def SuppressFeature(self, StringName):
        pass
    def SuppressFeature(self, FeatureFeature):
        pass
    def UnsuppressFeature(self, StringName):
        pass
    def UnsuppressFeature(self, FeatureFeature):
        pass
    def HideFeature(self, StringName):
        pass
    def HideFeature(self, FeatureFeature):
        pass
    def ShowFeature(self, StringName):
        pass
    def ShowFeature(self, FeatureFeature):
        pass
    def GetPlane(self, StringName):
        pass
    def GetPlane(self, IADDesignPlaneDesignPlane):
        pass
    def GetAxis(self, StringName):
        pass
    def GetAxis(self, IADDesignAxisDesignAxis):
        pass
    def GetPoint(self, StringName):
        pass
    def GetPoint(self, IADDesignPointDesignPoint):
        pass
    def GetSketch(self, StringName):
        pass
    def Get3DSketch(self, StringName):
        pass
    def GetFace(self, StringName):
        pass
    def GetEdge(self, StringName):
        pass
    def GetVertex(self, StringName):
        pass
    def GetParameter(self, StringName):
        pass
    def GetCustomProperty(self, StringName):
        pass
    def SetCustomProperty(self, StringName, StringValue):
        pass
    def GetConfiguration(self, StringName):
        pass
    def GetActiveConfiguration(
        self,
    ):
        pass
    def AddPlane(self, StringName, ISketchSurfaceSourcePlane, DoubleOffset):
        pass
    def AddPlane(self, StringName, ListNormalVector, ListPointonPlane):
        pass
    def AddPlane(self, StringName, AxisAxis, PointPoint):
        pass
    def AddPlane(
        self, StringName, ISketchSurfaceSourcePlane, AxisRotationAxis, DoubleAngle
    ):
        pass
    def AddParameter(self, StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter(
        self, StringName, ParameterTypesType, ParameterUnitsUnitstoUse, DoubleValue
    ):
        pass
    def AddParameter(self, StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration(self, StringName):
        pass
    def AddConfiguration(self, StringName, StringBaseConfigurationName):
        pass
    def AddPlane(self, StringName, ListPoint1, ListPoint2, ListPoint3):
        pass
    def AddSketch(self, StringName, ISketchSurfacePlane):
        pass
