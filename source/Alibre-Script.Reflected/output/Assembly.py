class Assembly:
    def __init__(
        self,
        Name,
        ParameterList,
        ConfigurationList,
        PartList,
        SubAssemblyList,
        Parameters,
        Configurations,
        Parts,
        SubAssemblies,
        FileName,
        XYPlane,
        YZPlane,
        ZXPlane,
        XAxis,
        YAxis,
        ZAxis,
        Origin,
        Selections,
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
        Density,
        Material,
        Description,
        Number,
    ):
        pass
        self.Name = Name
        self.ParameterList = ParameterList
        self.ConfigurationList = ConfigurationList
        self.PartList = PartList
        self.SubAssemblyList = SubAssemblyList
        self.Parameters = Parameters
        self.Configurations = Configurations
        self.Parts = Parts
        self.SubAssemblies = SubAssemblies
        self.FileName = FileName
        self.XYPlane = XYPlane
        self.YZPlane = YZPlane
        self.ZXPlane = ZXPlane
        self.XAxis = XAxis
        self.YAxis = YAxis
        self.ZAxis = ZAxis
        self.Origin = Origin
        self.Selections = Selections
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
        self.Density = Density
        self.Material = Material
        self.Description = Description
        self.Number = Number
    def AddSubAssembly(
        self, StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
        self,
        StringFileName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AddMateConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddMateConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddMateConstraint2(
        self,
        DoubleDistance1,
        DoubleDistance2,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
        ConstraintBoundsTypeBoundsType,
    ):
        pass
    def AddFastenerConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddFastenerConstraint2(
        self,
        DoubleDistance1,
        DoubleDistance2,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
        ConstraintBoundsTypeBoundsType,
    ):
        pass
    def AddAlignConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAlignConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddAlignConstraint2(
        self,
        DoubleDistance1,
        DoubleDistance2,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
        ConstraintBoundsTypeBoundsType,
    ):
        pass
    def AddOrientConstraint(
        self,
        DoubleValue,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddOrientConstraint(
        self,
        DoubleValue,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddAngleConstraint(
        self,
        DoubleAngle,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAngleConstraint(
        self,
        DoubleAngle,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddAngleConstraint2(
        self,
        DoubleAngle1,
        DoubleAngle2,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
        ConstraintBoundsTypeBoundsType,
    ):
        pass
    def AddGearConstraint(
        self,
        DoubleRatioA,
        DoubleRatioB,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddRackAndPinionConstraint(
        self,
        DoublePitchDiameter,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddScrewConstraint(
        self,
        DoubleThreadPitch,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def AddTangentConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanOutside,
    ):
        pass
    def AddTangentConstraint(
        self,
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanOutside,
        BooleanIsReversed,
        StringName,
    ):
        pass
    def CreateUniqueName(self, StringBaseName):
        pass
    def ExportSTL(self, StringFileName):
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
    def SetUserData(self, StringName, PythonDictionaryDict):
        pass
    def GetUserData(self, StringName):
        pass
    def PauseUpdating(
        self,
    ):
        pass
    def ResumeUpdating(
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
    def GetSelection(
        self,
    ):
        pass
    def AddPlane(self, StringName, ISketchSurfaceSourcePlane, DoubleOffset):
        pass
    def AddPlane(self, StringName, ListNormalVector, ListPointonPlane):
        pass
    def AddPlane(
        self, StringName, ISketchSurfaceSourcePlane, AxisRotationAxis, DoubleAngle
    ):
        pass
    def AddParameter(self, StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter(self, StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration(self, StringName):
        pass
    def AddConfiguration(self, StringName, StringBaseConfigurationName):
        pass
    def AddPlane(self, StringName, ListPoint1, ListPoint2, ListPoint3):
        pass
    def AddAxis(self, StringName, ISketchSurfacePlane1, ISketchSurfacePlane2):
        pass
    def AddAxis(self, StringName, ListPoint1, ListPoint2):
        pass
    def AddPoint(self, StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoints(self, StringPrefix, ListPoints):
        pass
    def Regenerate(
        self,
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
    def SaveAll(self, StringFolder):
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
    def Close(
        self,
    ):
        pass
    def SaveThumbnail(self, StringFileName, Int32Width, Int32Height):
        pass
    def AddPart(self, StringFolder, StringName):
        pass
    def AddPart(
        self, StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddPart(
        self,
        StringFolder,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AddPart(self, PartPart):
        pass
    def AddPart(self, PartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart(self, StringFileName):
        pass
    def AddPart(self, StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart(
        self,
        StringFileName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def GetPartOrientation(self, AssembledPartPart):
        pass
    def GetPartOrientation(self, StringPartName):
        pass
    def DisplayUnits(
        self,
    ):
        pass
    def AddPart(
        self,
        PartPart,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AddNewPart(self, StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def GetPart(self, StringName):
        pass
    def GetSubAssembly(self, StringName):
        pass
    def DuplicatePart(self, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def DuplicatePart(
        self, AssembledPartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicatePart(
        self,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def DuplicatePart(
        self,
        AssembledPartPart,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def DuplicatePart(
        self,
        IADOccurrencePartOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def DuplicateSubAssembly(
        self,
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
    ):
        pass
    def DuplicateSubAssembly(
        self, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicateSubAssembly(
        self,
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def DuplicateSubAssembly(
        self,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def DuplicateSubAssembly(
        self,
        IADOccurrenceAssemOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AnchorPart(self, StringName):
        pass
    def AnchorPart(self, AssembledPartPart):
        pass
    def AnchorSubAssembly(self, StringName):
        pass
    def UnanchorPart(self, StringName):
        pass
    def UnanchorPart(self, AssembledPartPart):
        pass
    def UnanchorSubAssembly(self, StringName):
        pass
    def HidePart(self, StringName):
        pass
    def HidePart(self, AssembledPartPart):
        pass
    def HideSubAssembly(self, StringName):
        pass
    def ShowPart(self, StringName):
        pass
    def ShowPart(self, AssembledPartPart):
        pass
    def ShowSubAssembly(self, StringName):
        pass
    def SuppressPart(self, StringName):
        pass
    def SuppressPart(self, AssembledPartPart):
        pass
    def SuppressSubAssembly(self, StringName):
        pass
    def UnsuppressPart(self, StringName):
        pass
    def UnsuppressPart(self, AssembledPartPart):
        pass
    def UnsuppressSubAssembly(self, StringName):
        pass
    def MovePart(
        self,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        self,
        AssembledPartPart,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        self,
        IADOccurrencePartOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        self,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        self,
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        self,
        IADOccurrenceAssemOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveParts(
        self,
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssemblies(
        self,
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        self,
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        self,
        AssembledPartPart,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        self,
        IADOccurrencePartOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        self,
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        self,
        AssembledSubAssemblySubAssembly,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        self,
        IADOccurrenceAssemOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateParts(
        self,
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssemblies(
        self,
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def AddNewSubAssembly(self, StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddSubAssembly(self, AssemblyAssembly):
        pass
    def AddSubAssembly(
        self, AssemblyAssembly, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
        self,
        AssemblyAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AddSubAssembly(self, StringFolder, StringName):
        pass
    def AddSubAssembly(
        self, StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
        self,
        StringFolder,
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanTranslationFirst,
    ):
        pass
    def AddSubAssembly(self, StringFileName):
        pass
