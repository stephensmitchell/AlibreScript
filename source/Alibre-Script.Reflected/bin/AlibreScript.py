class AssembledSubAssembly:
    def __init__(
        self,
        Name,
        ConfigurationList,
        Configurations,
        ParameterList,
        PartList,
        SubAssemblyList,
        Parameters,
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
        self.ConfigurationList = ConfigurationList
        self.Configurations = Configurations
        self.ParameterList = ParameterList
        self.PartList = PartList
        self.SubAssemblyList = SubAssemblyList
        self.Parameters = Parameters
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
    def GetSelectionAssembly(
        self,
    ):
        pass
    def SetOccurrence(self, IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
        self
    ):
        pass
    def GetMappedOccurrence(self, IADAssemblySessionAssembly):
        pass
    def SetParentAssembly(self, AssemblyParentAssembly):
        pass
    def GetParentAssembly(
        self
    ):
        pass
    def GetConfiguration(self, StringName):
        pass
    def GetAssembledPath(
        self
    ):
        pass
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
        self
    ):
        pass
    def ResumeUpdating(
        self
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
class Axis:
    def __init__(self, Name):
        pass
        self.Name = Name
    def GetPart(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
    def AxisObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
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
    def Hide(
        self,
    ):
        pass
    def Show(
        self,
    ):
        pass
    def GetGeometry(self, IADPointPoint, IADPointVector):
        pass
class Bspline:
    def __init__(self, ControlPoints, Weights, KnotVectors, IsReference, Order, Length):
        pass
        self.ControlPoints = ControlPoints
        self.Weights = Weights
        self.KnotVectors = KnotVectors
        self.IsReference = IsReference
        self.Order = Order
        self.Length = Length
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def GetX(self, Doubleu):
        pass
    def GetY(self, Doubleu):
        pass
    def GetPointAt(self, Doubleu):
        pass
    def GetNormalAt(self, Doubleu):
        pass
    def Subdivide(self, Int32Segments):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Bspline3D:
    def __init__(self, ControlPoints, Weights, KnotVectors, IsReference, Order, Length):
        pass
        self.ControlPoints = ControlPoints
        self.Weights = Weights
        self.KnotVectors = KnotVectors
        self.IsReference = IsReference
        self.Order = Order
        self.Length = Length
    def GetX(self, Doubleu):
        pass
    def GetY(self, Doubleu):
        pass
    def GetZ(self, Doubleu):
        pass
    def GetPointAt(self, Doubleu):
        pass
    def GetNormalAt(self, Doubleu):
        pass
    def Subdivide(self, Int32Segments):
        pass
    def SubdivideGetNormals(self, Int32Segments):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Circle:
    def __init__(self, CenterPoint, Center, Radius, IsReference, Length):
        pass
        self.CenterPoint = CenterPoint
        self.Center = Center
        self.Radius = Radius
        self.IsReference = IsReference
        self.Length = Length
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class CircularArc:
    def __init__(
        self,
        Center,
        StartPoint,
        EndPoint,
        Start,
        End,
        CenterPoint,
        Radius,
        Angle,
        Type,
        IsReference,
    ):
        pass
        self.Center = Center
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.Start = Start
        self.End = End
        self.CenterPoint = CenterPoint
        self.Radius = Radius
        self.Angle = Angle
        self.Type = Type
        self.IsReference = IsReference
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class CircularArc3D:
    def __init__(self, Center, StartPoint, EndPoint, Radius, Angle, Type, IsReference):
        pass
        self.Center = Center
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.Radius = Radius
        self.Angle = Angle
        self.Type = Type
        self.IsReference = IsReference
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Configuration:
    def __init__(self, Name, IsActive):
        pass
        self.Name = Name
        self.IsActive = IsActive
    def SetLocks(self, LockTypesLocks):
        pass
    def LockAll(
        self,
    ):
        pass
    def UnlockAll(
        self,
    ):
        pass
    def Activate(
        self,
    ):
        pass
class CSharp:
    def __init__(
        self,
    ):
        pass
    def add_OnWriteLine(self, WriteLineHandlervalue):
        pass
    def remove_OnWriteLine(self, WriteLineHandlervalue):
        pass
    def add_OnWrite(self, WriteHandlervalue):
        pass
    def remove_OnWrite(self, WriteHandlervalue):
        pass
    def CompileAndRun(self, StringCode):
        pass
    def CompileAndRun(self, StringCode, PythonDictionaryVariables):
        pass
    def Compile(self, StringCode):
        pass
    def Run(self, Script1Script):
        pass
    def Run(self, Script1Script, PythonDictionaryVariables):
        pass
class Edge:
    def __init__(self, _Edge, Name, Diameter, Length, Vertices):
        pass
        self._Edge = _Edge
        self.Name = Name
        self.Diameter = Diameter
        self.Length = Length
        self.Vertices = Vertices
    def GetPart(
        self,
    ):
        pass
    def GetVertices(
        self,
    ):
        pass
    def FilletableObject(
        self,
    ):
        pass
    def ChamferableObject(
        self,
    ):
        pass
    def AxisObject(
        self,
    ):
        pass
    def PathObject(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
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
class Ellipse:
    def __init__(
        self, Center, CenterPoint, Radius, MajorAxisAngle, MinorMajorRatio, IsReference
    ):
        pass
        self.Center = Center
        self.CenterPoint = CenterPoint
        self.Radius = Radius
        self.MajorAxisAngle = MajorAxisAngle
        self.MinorMajorRatio = MinorMajorRatio
        self.IsReference = IsReference
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class EllipticalArc:
    def __init__(
        self,
        Center,
        StartPoint,
        EndPoint,
        CenterPoint,
        Start,
        End,
        Radius,
        MajorAxisAngle,
        MinorMajorRatio,
        IsReference,
    ):
        pass
        self.Center = Center
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.CenterPoint = CenterPoint
        self.Start = Start
        self.End = End
        self.Radius = Radius
        self.MajorAxisAngle = MajorAxisAngle
        self.MinorMajorRatio = MinorMajorRatio
        self.IsReference = IsReference
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Face:
    def __init__(
        self, _Face, Name, Edges, PartnerCoedges, Coedges, AdjoiningFaces, Vertices
    ):
        pass
        self._Face = _Face
        self.Name = Name
        self.Edges = Edges
        self.PartnerCoedges = PartnerCoedges
        self.Coedges = Coedges
        self.AdjoiningFaces = AdjoiningFaces
        self.Vertices = Vertices
    def GetPart(
        self,
    ):
        pass
    def IsRectangle(
        self,
    ):
        pass
    def GetEdges(
        self,
    ):
        pass
    def GetAdjoiningFaces(
        self,
    ):
        pass
    def GetVertices(
        self,
    ):
        pass
    def SurfaceObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
        pass
    def PlaneObject(
        self,
    ):
        pass
    def FilletableObject(
        self,
    ):
        pass
    def ChamferableObject(
        self,
    ):
        pass
    def CrossSectionObject(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
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
    def IsParallel(self, FaceOtherFace):
        pass
    def DistanceTo(self, FaceOtherFace):
        pass
    def GetNormal(
        self,
    ):
        pass
    def GetArea(
        self,
    ):
        pass
class Feature:
    def __init__(self, Name):
        pass
        self.Name = Name
    def GetColor(
        self,
    ):
        pass
    def SetColor(self, ColorNewColor):
        pass
    def SetColor(self, ByteRed, ByteGreen, ByteBlue):
        pass
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
class GlobalParameters:
    def __init__(
        self, Name, ParameterList, ConfigurationList, Parameters, Configurations
    ):
        pass
        self.Name = Name
        self.ParameterList = ParameterList
        self.ConfigurationList = ConfigurationList
        self.Parameters = Parameters
        self.Configurations = Configurations
    def GetParameter(self, StringName):
        pass
    def GetConfiguration(self, StringName):
        pass
    def GetActiveConfiguration(
        self,
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
class IAssembled:
    def __init__(
        self,
    ):
        pass
    def GetMappedOccurrence(self, IADAssemblySessionAssembly):
        pass
class IAxis:
    def __init__(
        self,
    ):
        pass
    def AxisObject(
        self,
    ):
        pass
    def GetOccurrence(
        self,
    ):
        pass
class IChamferable:
    def __init__(
        self,
    ):
        pass
    def ChamferableObject(
        self,
    ):
        pass
class IConstrainable:
    def __init__(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
class ICrossSection:
    def __init__(
        self,
    ):
        pass
    def CrossSectionObject(
        self,
    ):
        pass
class IFilletable:
    def __init__(
        self,
    ):
        pass
    def FilletableObject(
        self,
    ):
        pass
class IInstance:
    def __init__(
        self,
    ):
        pass
    def GetSelectionAssembly(
        self,
    ):
        pass
    def GetParentAssembly(
        self,
    ):
        pass
    def SetParentAssembly(self, AssemblyParentAssembly):
        pass
    def SetOccurrence(self, IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
        self,
    ):
        pass
class IPlane:
    def __init__(
        self,
    ):
        pass
    def PlaneObject(
        self,
    ):
        pass
    def GetOccurrence(
        self,
    ):
        pass
class IPoint:
    def __init__(
        self,
    ):
        pass
    def PointObject(
        self,
    ):
        pass
    def GetOccurrence(
        self,
    ):
        pass
class ISelectableGeometry:
    def __init__(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
        pass
class ISketchFigure:
    def __init__(
        self,
    ):
        pass
    def ToXml(
        self,
    ):
        pass
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
class ISketchFigure3D:
    def __init__(
        self,
    ):
        pass
    def ToXml(
        self,
    ):
        pass
class ISketchSurface:
    def __init__(
        self,
    ):
        pass
    def SurfaceObject(
        self,
    ):
        pass
class ISweepPath:
    def __init__(
        self,
    ):
        pass
    def PathObject(
        self,
    ):
        pass
class Line:
    def __init__(self, StartPoint, EndPoint, IsReference, Length, Start, End):
        pass
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.IsReference = IsReference
        self.Length = Length
        self.Start = Start
        self.End = End
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Line3D:
    def __init__(self, StartPoint, EndPoint, IsReference, Length, Start, End):
        pass
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.IsReference = IsReference
        self.Length = Length
        self.Start = Start
        self.End = End
    def SetInstance(self, IAD3DSketchLineLine):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class Material:
    def __init__(
        self,
    ):
        pass
class Parameter:
    def __init__(
        self,
        Name,
        Comment,
        Equation,
        ExcelWorkbook,
        ExcelSheet,
        ExcelCell,
        Type,
        Units,
        Value,
        RawValue,
    ):
        pass
        self.Name = Name
        self.Comment = Comment
        self.Equation = Equation
        self.ExcelWorkbook = ExcelWorkbook
        self.ExcelSheet = ExcelSheet
        self.ExcelCell = ExcelCell
        self.Type = Type
        self.Units = Units
        self.Value = Value
        self.RawValue = RawValue
    def AttachToExcel(self, StringDocument, StringSheet, StringCell, UnitTypesUnits):
        pass
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
class Plane:
    def __init__(self, Name):
        pass
        self.Name = Name
    def GetPart(
        self,
    ):
        pass
    def SurfaceObject(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
    def PlaneObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
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
    def IsParallel(self, PlaneOtherPlane):
        pass
    def Hide(
        self,
    ):
        pass
    def Show(
        self,
    ):
        pass
class Point:
    def __init__(self, Name, X, Y, Z):
        pass
        self.Name = Name
        self.X = X
        self.Y = Y
        self.Z = Z
    def PointObject(
        self,
    ):
        pass
    def GetPart(
        self,
    ):
        pass
    def CrossSectionObject(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
        pass
    def GetCoordinates(
        self,
    ):
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
    def Hide(
        self,
    ):
        pass
    def Show(
        self,
    ):
        pass
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
class Polyline3D:
    def __init__(
        self,
    ):
        pass
    def AddPoint(self, PolylinePoint3DPoint):
        pass
    def AddPoint(self, DoubleX, DoubleY, DoubleZ):
        pass
    def InsertPoint(self, Int32Index, PolylinePoint3DPoint):
        pass
    def AddPolyline(self, Polyline3DAppendLine):
        pass
    def IsPointOnLine(
        self, PolylinePoint3DA, PolylinePoint3DB, PolylinePoint3DP, DoubleTolerance
    ):
        pass
    def SplitAtPoint(self, PolylinePoint3DSplitPoint, DoubleTolerence):
        pass
    def Clone(
        self,
    ):
        pass
    def Clone(self, Int32StartIndex, Int32EndIndex):
        pass
    def Join(self, Polyline3DAppendLine):
        pass
    def Offset(self, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def RemoveDuplicates(
        self,
    ):
        pass
class PolylinePoint:
    def __init__(
        self,
    ):
        pass
    def op_Multiply(self, Matrix3DMatrix, PolylinePointPoint):
        pass
    def op_Multiply(self, PolylinePointPoint, Matrix3DMatrix):
        pass
    def op_Subtraction(self, PolylinePointP2, PolylinePointP1):
        pass
    def CrossProduct(self, PolylinePointP1, PolylinePointP2):
        pass
    def Offset(self, DoubleX, DoubleY):
        pass
    def Scale(self, DoubleScaleOriginX, DoubleScaleOriginY, DoubleScaleFactor):
        pass
    def RotateZ(self, DoubleCenterX, DoubleCenterY, DoubleAngle):
        pass
class PolylinePoint3D:
    def __init__(
        self,
    ):
        pass
    def op_Multiply(self, Matrix3DMatrix, PolylinePoint3DPoint):
        pass
    def op_Multiply(self, PolylinePoint3DPoint, Matrix3DMatrix):
        pass
    def op_Subtraction(self, PolylinePoint3DP2, PolylinePoint3DP1):
        pass
    def Offset(self, DoubleX, DoubleY, DoubleZ):
        pass
    def Scale(
        self,
        DoubleScaleOriginX,
        DoubleScaleOriginY,
        DoubleScaleOriginZ,
        DoubleScaleFactor,
    ):
        pass
class Sketch:
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
class Sketch3D:
    def __init__(self, Name, Figures):
        pass
        self.Name = Name
        self.Figures = Figures
    def GetPart(
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
    def AddLine(self, ListStartPoint, ListEndPoint):
        pass
    def AddLine(self, Line3DNewLine):
        pass
    def AddPoint(self, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoint(self, SketchPoint3DNewPoint):
        pass
    def AddLine(self, DoubleX1, DoubleY1, DoubleZ1, DoubleX2, DoubleY2, DoubleZ2):
        pass
    def AddLines(self, ListPoints):
        pass
    def AddPolyline(self, Polyline3DLine):
        pass
    def AddArcCenterStartEnd(
        self,
        DoubleCenterX,
        DoubleCenterY,
        DoubleCenterZ,
        DoubleStartX,
        DoubleStartY,
        DoubleStartZ,
        DoubleEndX,
        DoubleEndY,
        DoubleEndZ,
    ):
        pass
    def AddArc(self, CircularArc3DNewArc):
        pass
    def AddBspline(self, ListPoints):
        pass
    def AddBspline(self, Bspline3DBspline):
        pass
    def AddBspline(self, List1Points):
        pass
    def PathObject(
        self,
    ):
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
    def SelectableObject(
        self,
    ):
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
class SketchPoint:
    def __init__(self, Point, X, Y, IsReference):
        pass
        self.Point = Point
        self.X = X
        self.Y = Y
        self.IsReference = IsReference
    def FigureObject(
        self,
    ):
        pass
    def SetInstance(self, IADSketchFigureFigure):
        pass
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
class SketchPoint3D:
    def __init__(self, X, Y, Z, IsReference):
        pass
        self.X = X
        self.Y = Y
        self.Z = Z
        self.IsReference = IsReference
    def ToXml(
        self,
    ):
        pass
    def FromXml(self, XElementXml):
        pass
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
class TwoD:
    def __init__(
        self,
    ):
        pass
    def TranslatePoint(self, Tuple2Point, DoubleXTranslation, DoubleYTranslation):
        pass
    def _RotatePoint(self, Tuple2Point, DoubleAngle):
        pass
    def RotatePoint(self, ListPoint, DoubleAngle):
        pass
    def IsPointInsidePolygon(self, List1Vertices, Tuple2Point):
        pass
    def GetPerpendicularVector(self, ListVector):
        pass
    def NormalizeVector(self, ListVector):
        pass
class Units:
    def __init__(
        self,
    ):
        pass
    def FromADUnitType(self, ADUnitsADUnit):
        pass
    def ToADUnits(self, DoubleValue):
        pass
    def FromADUnits(self, DoubleValue):
        pass
    def ToTeethPerInch(self, DoubleTeethPerCurrentUnits):
        pass
    def FromTeethPerInch(self, DoubleTeethPerInch):
        pass
    def ToInches(self, DoubleValue):
        pass
    def FromInches(self, DoubleValue):
        pass
    def ToMillimeters(self, DoubleValue):
        pass
    def FromMillimeters(self, DoubleValue):
        pass
    def ToADUnits(self, List1Values):
        pass
    def ToADUnits(self, DoubleValue, ADUnitsCurrentUnits):
        pass
    def FromADUnits(self, DoubleValue, ADUnitsCurrentUnits):
        pass
    def FromADUnits(self, List1ADValues):
        pass
class Vertex:
    def __init__(self, _Vertex, Name, X, Y, Z):
        pass
        self._Vertex = _Vertex
        self.Name = Name
        self.X = X
        self.Y = Y
        self.Z = Z
    def GetPart(
        self,
    ):
        pass
    def ChamferableObject(
        self,
    ):
        pass
    def ConstraintObject(
        self,
    ):
        pass
    def SelectableObject(
        self,
    ):
        pass
    def PointObject(
        self,
    ):
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
class Windows:
    def __init__(
        self
    ):
        pass
    def CloseForm(self, StringSessionIdentifier):
        pass
    def GetDisplayedForm(self, StringSessionIdentifier):
        pass
    def UtilityDialog(
        self,
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
    ):
        pass
    def UtilityDialog(
        self,
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def OptionsDialog(self, StringTitle, ListInputs, Int32InputAreaWidth):
        pass
    def OptionsDialog(
        self,
        StringTitle,
        ListInputs,
        Int32InputAreaWidth,
        ObjectInputChangedCallback,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def DisableInput(self, Int32Index):
        pass
    def EnableInput(self, Int32Index):
        pass
    def GetInputValue(self, Int32Index):
        pass
    def SetStringList(self, Int32Index, ObjectStrings):
        pass
    def SetInputValue(self, Int32Index, ObjectValue):
        pass
    def OpenFileDialog(self, StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SaveFileDialog(self, StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SelectFolderDialog(self, StringCurrentFolder, StringDescription):
        pass
    def InfoDialog(self, StringMessage, StringTitle):
        pass
    def ErrorDialog(self, StringMessage, StringTitle):
        pass
    def QuestionDialog(self, StringQuestion, StringTitle):
        pass
