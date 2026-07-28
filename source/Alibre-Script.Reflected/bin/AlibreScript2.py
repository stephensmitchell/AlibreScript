class AssembledSubAssembly:
    def __init__(
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
        Name = Name
        ConfigurationList = ConfigurationList
        Configurations = Configurations
        ParameterList = ParameterList
        PartList = PartList
        SubAssemblyList = SubAssemblyList
        Parameters = Parameters
        Parts = Parts
        SubAssemblies = SubAssemblies
        FileName = FileName
        XYPlane = XYPlane
        YZPlane = YZPlane
        ZXPlane = ZXPlane
        XAxis = XAxis
        YAxis = YAxis
        ZAxis = ZAxis
        Origin = Origin
        Selections = Selections
        Comment = Comment
        CostCenter = CostCenter
        CreatedBy = CreatedBy
        CreatedDate = CreatedDate
        CreatingApplication = CreatingApplication
        DocumentNumber = DocumentNumber
        EngineeringApprovalDate = EngineeringApprovalDate
        EngineeringApprovedBy = EngineeringApprovedBy
        EstimatedCost = EstimatedCost
        Keywords = Keywords
        LastAuthor = LastAuthor
        LastUpdateDate = LastUpdateDate
        ExtendedMaterialInformation = ExtendedMaterialInformation
        ManufacturingApprovedBy = ManufacturingApprovedBy
        ManufacturingApprovedDate = ManufacturingApprovedDate
        ModifiedInformation = ModifiedInformation
        Product = Product
        ReceivedFrom = ReceivedFrom
        Revision = Revision
        StockSize = StockSize
        Supplier = Supplier
        Title = Title
        Vendor = Vendor
        WebLink = WebLink
        Density = Density
        Material = Material
        Description = Description
        Number = Number
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
        self
    ):
        pass
    def GetMappedOccurrence( IADAssemblySessionAssembly):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
        self
    ):
        pass
    def GetConfiguration( StringName):
        pass
    def GetAssembledPath(
        self
    ):
        pass
    def AddSubAssembly(
         StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddMateConstraint(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAlignConstraint(
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
        DoubleValue,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddOrientConstraint(
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
        DoubleAngle,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAngleConstraint(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanOutside,
    ):
        pass
    def AddTangentConstraint(
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
    def CreateUniqueName( StringBaseName):
        pass
    def ExportSTL( StringFileName):
        pass
    def ExportSTEP203( StringFileName):
        pass
    def ExportSTEP214( StringFileName):
        pass
    def ExportIGES( StringFileName):
        pass
    def ExportSAT( StringFileName, Int32Version, BooleanSaveColors):
        pass
    def ExportBIP( StringFileName):
        pass
    def SetUserData( StringName, PythonDictionaryDict):
        pass
    def GetUserData( StringName):
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
        StringName,
        IPointPointOrVertex,
        DoubleXOffset,
        DoubleYOffset,
        DoubleZOffset,
    ):
        pass
    def AddPoint(
         StringName, IPointPointOrVertex1, IPointPointOrVertex2, DoubleRatio
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge1, IAxisAxisOrEdge2):
        pass
    def AddPoint(
         StringName, IPlanePlaneOrFace1, IPlanePlaneOrFace2, IPlanePlaneOrFace3
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge, IPlanePlaneOrFace):
        pass
    def AddPoint(
        StringName,
        IPointSourcePointOrVertex,
        IPlaneTargetPlaneOrFace,
        DoubleXOffset,
        DoubleYOffset,
    ):
        pass
    def AddPoint( StringName, EdgeTargetEdge, DoubleRatio):
        pass
    def AddPointFromCircularEdge( StringName, EdgeTargetEdge):
        pass
    def AddPointFromToroidalFace( StringName, FaceTargetFace):
        pass
    def GetPlane( StringName):
        pass
    def GetPlane( IADDesignPlaneDesignPlane):
        pass
    def GetAxis( StringName):
        pass
    def GetAxis( IADDesignAxisDesignAxis):
        pass
    def GetPoint( StringName):
        pass
    def GetPoint( IADDesignPointDesignPoint):
        pass
    def GetParameter( StringName):
        pass
    def GetCustomProperty( StringName):
        pass
    def SetCustomProperty( StringName, StringValue):
        pass
    def GetConfiguration( StringName):
        pass
    def GetActiveConfiguration(
    ):
        pass
    def GetSelection(
    ):
        pass
    def AddPlane( StringName, ISketchSurfaceSourcePlane, DoubleOffset):
        pass
    def AddPlane( StringName, ListNormalVector, ListPointonPlane):
        pass
    def AddPlane(
         StringName, ISketchSurfaceSourcePlane, AxisRotationAxis, DoubleAngle
    ):
        pass
    def AddParameter( StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter( StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration( StringName):
        pass
    def AddConfiguration( StringName, StringBaseConfigurationName):
        pass
    def AddPlane( StringName, ListPoint1, ListPoint2, ListPoint3):
        pass
    def AddAxis( StringName, ISketchSurfacePlane1, ISketchSurfacePlane2):
        pass
    def AddAxis( StringName, ListPoint1, ListPoint2):
        pass
    def AddPoint( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoints( StringPrefix, ListPoints):
        pass
    def Regenerate(
    ):
        pass
    def Save(
    ):
        pass
    def Save( StringFolder):
        pass
    def SaveAs( StringFolder, StringNewName):
        pass
    def SaveAll( StringFolder):
        pass
    def SaveSnapshot(
        StringFileName,
        Int32Width,
        Int32Height,
        BooleanUseAspectRatio,
        BooleanUseWidthandHeight,
    ):
        pass
    def Close(
    ):
        pass
    def SaveThumbnail( StringFileName, Int32Width, Int32Height):
        pass
    def AddPart( StringFolder, StringName):
        pass
    def AddPart(
         StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddPart(
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
    def AddPart( PartPart):
        pass
    def AddPart( PartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart( StringFileName):
        pass
    def AddPart( StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart(
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
    def GetPartOrientation( AssembledPartPart):
        pass
    def GetPartOrientation( StringPartName):
        pass
    def DisplayUnits(
    ):
        pass
    def AddPart(
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
    def AddNewPart( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def GetPart( StringName):
        pass
    def GetSubAssembly( StringName):
        pass
    def DuplicatePart( StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def DuplicatePart(
         AssembledPartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicatePart(
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
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
    ):
        pass
    def DuplicateSubAssembly(
         StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicateSubAssembly(
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
    def AnchorPart( StringName):
        pass
    def AnchorPart( AssembledPartPart):
        pass
    def AnchorSubAssembly( StringName):
        pass
    def UnanchorPart( StringName):
        pass
    def UnanchorPart( AssembledPartPart):
        pass
    def UnanchorSubAssembly( StringName):
        pass
    def HidePart( StringName):
        pass
    def HidePart( AssembledPartPart):
        pass
    def HideSubAssembly( StringName):
        pass
    def ShowPart( StringName):
        pass
    def ShowPart( AssembledPartPart):
        pass
    def ShowSubAssembly( StringName):
        pass
    def SuppressPart( StringName):
        pass
    def SuppressPart( AssembledPartPart):
        pass
    def SuppressSubAssembly( StringName):
        pass
    def UnsuppressPart( StringName):
        pass
    def UnsuppressPart( AssembledPartPart):
        pass
    def UnsuppressSubAssembly( StringName):
        pass
    def MovePart(
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        AssembledPartPart,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        IADOccurrencePartOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        IADOccurrenceAssemOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveParts(
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssemblies(
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        AssembledPartPart,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        IADOccurrencePartOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        AssembledSubAssemblySubAssembly,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        IADOccurrenceAssemOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateParts(
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssemblies(
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def AddNewSubAssembly( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddSubAssembly( AssemblyAssembly):
        pass
    def AddSubAssembly(
         AssemblyAssembly, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
    def AddSubAssembly( StringFolder, StringName):
        pass
    def AddSubAssembly(
         StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
    def AddSubAssembly( StringFileName):
        pass
class Assembly:
    def __init__(      
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
        Name = Name
        ParameterList = ParameterList
        ConfigurationList = ConfigurationList
        PartList = PartList
        SubAssemblyList = SubAssemblyList
        Parameters = Parameters
        Configurations = Configurations
        Parts = Parts
        SubAssemblies = SubAssemblies
        FileName = FileName
        XYPlane = XYPlane
        YZPlane = YZPlane
        ZXPlane = ZXPlane
        XAxis = XAxis
        YAxis = YAxis
        ZAxis = ZAxis
        Origin = Origin
        Selections = Selections
        Comment = Comment
        CostCenter = CostCenter
        CreatedBy = CreatedBy
        CreatedDate = CreatedDate
        CreatingApplication = CreatingApplication
        DocumentNumber = DocumentNumber
        EngineeringApprovalDate = EngineeringApprovalDate
        EngineeringApprovedBy = EngineeringApprovedBy
        EstimatedCost = EstimatedCost
        Keywords = Keywords
        LastAuthor = LastAuthor
        LastUpdateDate = LastUpdateDate
        ExtendedMaterialInformation = ExtendedMaterialInformation
        ManufacturingApprovedBy = ManufacturingApprovedBy
        ManufacturingApprovedDate = ManufacturingApprovedDate
        ModifiedInformation = ModifiedInformation
        Product = Product
        ReceivedFrom = ReceivedFrom
        Revision = Revision
        StockSize = StockSize
        Supplier = Supplier
        Title = Title
        Vendor = Vendor
        WebLink = WebLink
        Density = Density
        Material = Material
        Description = Description
        Number = Number
    def AddSubAssembly(
         StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddMateConstraint(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAlignConstraint(
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
        DoubleValue,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddOrientConstraint(
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
        DoubleAngle,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
    ):
        pass
    def AddAngleConstraint(
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
        DoubleDistance,
        IAssembledPartorAssemblyA,
        IConstrainableItemA,
        IAssembledPartorAssemblyB,
        IConstrainableItemB,
        BooleanOutside,
    ):
        pass
    def AddTangentConstraint(
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
    def CreateUniqueName( StringBaseName):
        pass
    def ExportSTL( StringFileName):
        pass
    def ExportSTEP203( StringFileName):
        pass
    def ExportSTEP214( StringFileName):
        pass
    def ExportIGES( StringFileName):
        pass
    def ExportSAT( StringFileName, Int32Version, BooleanSaveColors):
        pass
    def ExportBIP( StringFileName):
        pass
    def SetUserData( StringName, PythonDictionaryDict):
        pass
    def GetUserData( StringName):
        pass
    def PauseUpdating(
    ):
        pass
    def ResumeUpdating(
    ):
        pass
    def AddPoint(
        StringName,
        IPointPointOrVertex,
        DoubleXOffset,
        DoubleYOffset,
        DoubleZOffset,
    ):
        pass
    def AddPoint(
         StringName, IPointPointOrVertex1, IPointPointOrVertex2, DoubleRatio
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge1, IAxisAxisOrEdge2):
        pass
    def AddPoint(
         StringName, IPlanePlaneOrFace1, IPlanePlaneOrFace2, IPlanePlaneOrFace3
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge, IPlanePlaneOrFace):
        pass
    def AddPoint(
        StringName,
        IPointSourcePointOrVertex,
        IPlaneTargetPlaneOrFace,
        DoubleXOffset,
        DoubleYOffset,
    ):
        pass
    def AddPoint( StringName, EdgeTargetEdge, DoubleRatio):
        pass
    def AddPointFromCircularEdge( StringName, EdgeTargetEdge):
        pass
    def AddPointFromToroidalFace( StringName, FaceTargetFace):
        pass
    def GetPlane( StringName):
        pass
    def GetPlane( IADDesignPlaneDesignPlane):
        pass
    def GetAxis( StringName):
        pass
    def GetAxis( IADDesignAxisDesignAxis):
        pass
    def GetPoint( StringName):
        pass
    def GetPoint( IADDesignPointDesignPoint):
        pass
    def GetParameter( StringName):
        pass
    def GetCustomProperty( StringName):
        pass
    def SetCustomProperty( StringName, StringValue):
        pass
    def GetConfiguration( StringName):
        pass
    def GetActiveConfiguration(
    ):
        pass
    def GetSelection(
    ):
        pass
    def AddPlane( StringName, ISketchSurfaceSourcePlane, DoubleOffset):
        pass
    def AddPlane( StringName, ListNormalVector, ListPointonPlane):
        pass
    def AddPlane(
         StringName, ISketchSurfaceSourcePlane, AxisRotationAxis, DoubleAngle
    ):
        pass
    def AddParameter( StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter( StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration( StringName):
        pass
    def AddConfiguration( StringName, StringBaseConfigurationName):
        pass
    def AddPlane( StringName, ListPoint1, ListPoint2, ListPoint3):
        pass
    def AddAxis( StringName, ISketchSurfacePlane1, ISketchSurfacePlane2):
        pass
    def AddAxis( StringName, ListPoint1, ListPoint2):
        pass
    def AddPoint( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoints( StringPrefix, ListPoints):
        pass
    def Regenerate(
    ):
        pass
    def Save(
    ):
        pass
    def Save( StringFolder):
        pass
    def SaveAs( StringFolder, StringNewName):
        pass
    def SaveAll( StringFolder):
        pass
    def SaveSnapshot(
        StringFileName,
        Int32Width,
        Int32Height,
        BooleanUseAspectRatio,
        BooleanUseWidthandHeight,
    ):
        pass
    def Close(
    ):
        pass
    def SaveThumbnail( StringFileName, Int32Width, Int32Height):
        pass
    def AddPart( StringFolder, StringName):
        pass
    def AddPart(
         StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddPart(
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
    def AddPart( PartPart):
        pass
    def AddPart( PartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart( StringFileName):
        pass
    def AddPart( StringFileName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def AddPart(
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
    def GetPartOrientation( AssembledPartPart):
        pass
    def GetPartOrientation( StringPartName):
        pass
    def DisplayUnits(
    ):
        pass
    def AddPart(
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
    def AddNewPart( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def GetPart( StringName):
        pass
    def GetSubAssembly( StringName):
        pass
    def DuplicatePart( StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def DuplicatePart(
         AssembledPartPart, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicatePart(
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
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
    ):
        pass
    def DuplicateSubAssembly(
         StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def DuplicateSubAssembly(
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
    def AnchorPart( StringName):
        pass
    def AnchorPart( AssembledPartPart):
        pass
    def AnchorSubAssembly( StringName):
        pass
    def UnanchorPart( StringName):
        pass
    def UnanchorPart( AssembledPartPart):
        pass
    def UnanchorSubAssembly( StringName):
        pass
    def HidePart( StringName):
        pass
    def HidePart( AssembledPartPart):
        pass
    def HideSubAssembly( StringName):
        pass
    def ShowPart( StringName):
        pass
    def ShowPart( AssembledPartPart):
        pass
    def ShowSubAssembly( StringName):
        pass
    def SuppressPart( StringName):
        pass
    def SuppressPart( AssembledPartPart):
        pass
    def SuppressSubAssembly( StringName):
        pass
    def UnsuppressPart( StringName):
        pass
    def UnsuppressPart( AssembledPartPart):
        pass
    def UnsuppressSubAssembly( StringName):
        pass
    def MovePart(
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        AssembledPartPart,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MovePart(
        IADOccurrencePartOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        StringName,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        AssembledSubAssemblySubAssembly,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssembly(
        IADOccurrenceAssemOcc,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveParts(
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def MoveSubAssemblies(
        ListNames,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        AssembledPartPart,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotatePart(
        IADOccurrencePartOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        StringName,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        AssembledSubAssemblySubAssembly,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssembly(
        IADOccurrenceAssemOcc,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateParts(
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def RotateSubAssemblies(
        ListNames,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
        BooleanApplyConstraints,
    ):
        pass
    def AddNewSubAssembly( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddSubAssembly( AssemblyAssembly):
        pass
    def AddSubAssembly(
         AssemblyAssembly, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
    def AddSubAssembly( StringFolder, StringName):
        pass
    def AddSubAssembly(
         StringFolder, StringName, DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ
    ):
        pass
    def AddSubAssembly(
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
    def AddSubAssembly( StringFileName):
        pass
class Axis:
    def __init__( Name):
        pass
        Name = Name
    def GetPart(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def AxisObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def Hide(
    ):
        pass
    def Show(
    ):
        pass
    def GetGeometry( IADPointPoint, IADPointVector):
        pass
class Bspline:
    def __init__( ControlPoints, Weights, KnotVectors, IsReference, Order, Length):
        pass
        ControlPoints = ControlPoints
        Weights = Weights
        KnotVectors = KnotVectors
        IsReference = IsReference
        Order = Order
        Length = Length
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def GetX( Doubleu):
        pass
    def GetY( Doubleu):
        pass
    def GetPointAt( Doubleu):
        pass
    def GetNormalAt( Doubleu):
        pass
    def Subdivide( Int32Segments):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Bspline3D:
    def __init__( ControlPoints, Weights, KnotVectors, IsReference, Order, Length):
        pass
        ControlPoints = ControlPoints
        Weights = Weights
        KnotVectors = KnotVectors
        IsReference = IsReference
        Order = Order
        Length = Length
    def GetX( Doubleu):
        pass
    def GetY( Doubleu):
        pass
    def GetZ( Doubleu):
        pass
    def GetPointAt( Doubleu):
        pass
    def GetNormalAt( Doubleu):
        pass
    def Subdivide( Int32Segments):
        pass
    def SubdivideGetNormals( Int32Segments):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Circle:
    def __init__( CenterPoint, Center, Radius, IsReference, Length):
        pass
        CenterPoint = CenterPoint
        Center = Center
        Radius = Radius
        IsReference = IsReference
        Length = Length
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class CircularArc:
    def __init__(
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
        Center = Center
        StartPoint = StartPoint
        EndPoint = EndPoint
        Start = Start
        End = End
        CenterPoint = CenterPoint
        Radius = Radius
        Angle = Angle
        Type = Type
        IsReference = IsReference
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class CircularArc3D:
    def __init__( Center, StartPoint, EndPoint, Radius, Angle, Type, IsReference):
        pass
        Center = Center
        StartPoint = StartPoint
        EndPoint = EndPoint
        Radius = Radius
        Angle = Angle
        Type = Type
        IsReference = IsReference
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Configuration:
    def __init__( Name, IsActive):
        pass
        Name = Name
        IsActive = IsActive
    def SetLocks( LockTypesLocks):
        pass
    def LockAll(
    ):
        pass
    def UnlockAll(
    ):
        pass
    def Activate(
    ):
        pass
class CSharp:
    def __init__(
    ):
        pass
    def add_OnWriteLine( WriteLineHandlervalue):
        pass
    def remove_OnWriteLine( WriteLineHandlervalue):
        pass
    def add_OnWrite( WriteHandlervalue):
        pass
    def remove_OnWrite( WriteHandlervalue):
        pass
    def CompileAndRun( StringCode):
        pass
    def CompileAndRun( StringCode, PythonDictionaryVariables):
        pass
    def Compile( StringCode):
        pass
    def Run( Script1Script):
        pass
    def Run( Script1Script, PythonDictionaryVariables):
        pass
class Edge:
    def __init__( _Edge, Name, Diameter, Length, Vertices):
        pass
        _Edge = _Edge
        Name = Name
        Diameter = Diameter
        Length = Length
        Vertices = Vertices
    def GetPart(
    ):
        pass
    def GetVertices(
    ):
        pass
    def FilletableObject(
    ):
        pass
    def ChamferableObject(
    ):
        pass
    def AxisObject(
    ):
        pass
    def PathObject(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
class Ellipse:
    def __init__(
         Center, CenterPoint, Radius, MajorAxisAngle, MinorMajorRatio, IsReference
    ):
        pass
        Center = Center
        CenterPoint = CenterPoint
        Radius = Radius
        MajorAxisAngle = MajorAxisAngle
        MinorMajorRatio = MinorMajorRatio
        IsReference = IsReference
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class EllipticalArc:
    def __init__(
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
        Center = Center
        StartPoint = StartPoint
        EndPoint = EndPoint
        CenterPoint = CenterPoint
        Start = Start
        End = End
        Radius = Radius
        MajorAxisAngle = MajorAxisAngle
        MinorMajorRatio = MinorMajorRatio
        IsReference = IsReference
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Face:
    def __init__(
         _Face, Name, Edges, PartnerCoedges, Coedges, AdjoiningFaces, Vertices
    ):
        pass
        _Face = _Face
        Name = Name
        Edges = Edges
        PartnerCoedges = PartnerCoedges
        Coedges = Coedges
        AdjoiningFaces = AdjoiningFaces
        Vertices = Vertices
    def GetPart(
    ):
        pass
    def IsRectangle(
    ):
        pass
    def GetEdges(
    ):
        pass
    def GetAdjoiningFaces(
    ):
        pass
    def GetVertices(
    ):
        pass
    def SurfaceObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def PlaneObject(
    ):
        pass
    def FilletableObject(
    ):
        pass
    def ChamferableObject(
    ):
        pass
    def CrossSectionObject(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def IsParallel( FaceOtherFace):
        pass
    def DistanceTo( FaceOtherFace):
        pass
    def GetNormal(
    ):
        pass
    def GetArea(
    ):
        pass
class Feature:
    def __init__( Name):
        pass
        Name = Name
    def GetColor(
    ):
        pass
    def SetColor( ColorNewColor):
        pass
    def SetColor( ByteRed, ByteGreen, ByteBlue):
        pass
class GearSketch:
    def __init__( Name, Figures, Origin):
        pass
        Name = Name
        Figures = Figures
        Origin = Origin
    def GetPart(
    ):
        pass
    def GetSurface(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def StartEditing(
    ):
        pass
    def StopEditing(
    ):
        pass
    def AddConstraint( ISketchFigureFigure, ConstraintsConstraint):
        pass
    def AddConstraint( ListFigures, ConstraintsConstraint):
        pass
    def AddLine( ListStartPoint, ListEndPoint, BooleanIsReference):
        pass
    def AddLine( LineNewLine):
        pass
    def AddLine( DoubleX1, DoubleY1, DoubleX2, DoubleY2, BooleanIsReference):
        pass
    def AddPoint( DoubleX, DoubleY):
        pass
    def AddPoint( DoubleX, DoubleY, BooleanIsReference):
        pass
    def AddPoint( SketchPointNewPoint):
        pass
    def AddLines( ListPoints, BooleanIsReference):
        pass
    def AddPolyline( PolylineLine, BooleanIsReference):
        pass
    def AddArcCenterStartEnd(
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
        DoubleCenterX,
        DoubleCenterY,
        DoubleStartX,
        DoubleStartY,
        DoubleAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse(
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
        DoubleCenterX,
        DoubleCenterY,
        DoubleMajorAxisDiameter,
        DoubleMinorMajorRatio,
        DoubleMajorAxisAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse( EllipseNewEllipse):
        pass
    def AddEllipticalArc(
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
    def AddEllipticalArc( EllipticalArcNewEllipticalArc):
        pass
    def AddArc( CircularArcNewArc):
        pass
    def AddRectangle(
        DoubleBottomLeftX,
        DoubleBottomLeftY,
        DoubleTopRightX,
        DoubleTopRightY,
        BooleanIsReference,
    ):
        pass
    def AddCircle(
         DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def AddCircle( CircleNewCircle):
        pass
    def AddBspline(
        Int32Order,
        ListControlPoints,
        ListKnotVectors,
        ListWeights,
        BooleanIsReference,
    ):
        pass
    def AddBspline( ListPoints, BooleanIsReference):
        pass
    def AddFigure( ISketchFigureNewFigure):
        pass
    def AddBspline( BsplineNewBspline):
        pass
    def AddBspline(
        Int32Order,
        List1ControlPoints,
        List1KnotVectors,
        List1Weights,
        BooleanIsReference,
    ):
        pass
    def AddBsplineInterpolated( List1Points, BooleanIsReference):
        pass
    def AddBsplineThroughPoints( List1Points, BooleanIsReference):
        pass
    def AddPolygon(
        DoubleCenterX,
        DoubleCenterY,
        DoubleDiameter,
        Int32Sides,
        BooleanIsReference,
    ):
        pass
    def AddPolyhole(
         DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def PathObject(
    ):
        pass
    def CrossSectionObject(
    ):
        pass
    def CopyFrom( SketchSource):
        pass
    def CopyFrom(
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
    def PointtoGlobal( Doublex, Doubley):
        pass
    def GlobaltoPoint( Doublex, Doubley, Doublez):
        pass
    def VertextoPoint( VertexVert):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def AddDimension( SketchPointP1, SketchPointP2):
        pass
    def AddDimension( CircleCircle):
        pass
    def AddDimension( CircularArcArc):
        pass
    def SavetoXml( StringFileName):
        pass
    def ToXml(
    ):
        pass
    def LoadXml( StringFileName):
        pass
    def FromXml( StringXml):
        pass
    def StartFaceMapping( VertexEdgeVertex1, VertexEdgeVertex2):
        pass
    def StartFaceMapping( ListEdgeEndPoint1, ListEdgeEndPoint2):
        pass
    def StopFaceMapping(
    ):
        pass
    def StartMapping( ListPoint1, ListPoint2, ListPointAboveAxis):
        pass
    def StopMapping(
    ):
        pass
    def ImportSVG( StringFileName):
        pass
    def ImportSVG(
        StringFileName,
        DoubleTranslateX,
        DoubleTranslateY,
        DoubleRotationAngle,
        BooleanTranslateThenRotate,
        BooleanNativeFigures,
    ):
        pass
    def ExportSVG( StringFileName):
        pass
    def ExportSVG( StringFileName, BooleanIncludeReferences):
        pass
    def ExportSVG(
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
         Name, ParameterList, ConfigurationList, Parameters, Configurations
    ):
        pass
        Name = Name
        ParameterList = ParameterList
        ConfigurationList = ConfigurationList
        Parameters = Parameters
        Configurations = Configurations
    def GetParameter( StringName):
        pass
    def GetConfiguration( StringName):
        pass
    def GetActiveConfiguration(
    ):
        pass
    def AddParameter( StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter( StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration( StringName):
        pass
    def AddConfiguration( StringName, StringBaseConfigurationName):
        pass
    def Save(
    ):
        pass
    def Save( StringFolder):
        pass
    def SaveAs( StringFolder, StringNewName):
        pass
    def Close(
    ):
        pass
class IAssembled:
    def __init__(
    ):
        pass
    def GetMappedOccurrence( IADAssemblySessionAssembly):
        pass
class IAxis:
    def __init__(
    ):
        pass
    def AxisObject(
    ):
        pass
    def GetOccurrence(
    ):
        pass
class IChamferable:
    def __init__(
    ):
        pass
    def ChamferableObject(
    ):
        pass
class IConstrainable:
    def __init__(
    ):
        pass
    def ConstraintObject(
    ):
        pass
class ICrossSection:
    def __init__(
    ):
        pass
    def CrossSectionObject(
    ):
        pass
class IFilletable:
    def __init__(
    ):
        pass
    def FilletableObject(
    ):
        pass
class IInstance:
    def __init__(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def GetParentAssembly(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
class IPlane:
    def __init__(
    ):
        pass
    def PlaneObject(
    ):
        pass
    def GetOccurrence(
    ):
        pass
class IPoint:
    def __init__(
    ):
        pass
    def PointObject(
    ):
        pass
    def GetOccurrence(
    ):
        pass
class ISelectableGeometry:
    def __init__(
    ):
        pass
    def SelectableObject(
    ):
        pass
class ISketchFigure:
    def __init__(
    ):
        pass
    def ToXml(
    ):
        pass
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
class ISketchFigure3D:
    def __init__(
    ):
        pass
    def ToXml(
    ):
        pass
class ISketchSurface:
    def __init__(
    ):
        pass
    def SurfaceObject(
    ):
        pass
class ISweepPath:
    def __init__(
    ):
        pass
    def PathObject(
    ):
        pass
class Line:
    def __init__( StartPoint, EndPoint, IsReference, Length, Start, End):
        pass
        StartPoint = StartPoint
        EndPoint = EndPoint
        IsReference = IsReference
        Length = Length
        Start = Start
        End = End
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Line3D:
    def __init__( StartPoint, EndPoint, IsReference, Length, Start, End):
        pass
        StartPoint = StartPoint
        EndPoint = EndPoint
        IsReference = IsReference
        Length = Length
        Start = Start
        End = End
    def SetInstance( IAD3DSketchLineLine):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class Material:
    def __init__(
    ):
        pass
class Parameter:
    def __init__(
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
        Name = Name
        Comment = Comment
        Equation = Equation
        ExcelWorkbook = ExcelWorkbook
        ExcelSheet = ExcelSheet
        ExcelCell = ExcelCell
        Type = Type
        Units = Units
        Value = Value
        RawValue = RawValue
    def AttachToExcel( StringDocument, StringSheet, StringCell, UnitTypesUnits):
        pass
class Part:
    def __init__(
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
        Name = Name
        Faces = Faces
        Edges = Edges
        Vertices = Vertices
        ParameterList = ParameterList
        ConfigurationList = ConfigurationList
        Parameters = Parameters
        Configurations = Configurations
        Density = Density
        Material = Material
        Description = Description
        Number = Number
        Mass = Mass
        Comment = Comment
        CostCenter = CostCenter
        CreatedBy = CreatedBy
        CreatedDate = CreatedDate
        CreatingApplication = CreatingApplication
        DocumentNumber = DocumentNumber
        EngineeringApprovalDate = EngineeringApprovalDate
        EngineeringApprovedBy = EngineeringApprovedBy
        EstimatedCost = EstimatedCost
        Keywords = Keywords
        LastAuthor = LastAuthor
        LastUpdateDate = LastUpdateDate
        ExtendedMaterialInformation = ExtendedMaterialInformation
        ManufacturingApprovedBy = ManufacturingApprovedBy
        ManufacturingApprovedDate = ManufacturingApprovedDate
        ModifiedInformation = ModifiedInformation
        Product = Product
        ReceivedFrom = ReceivedFrom
        Revision = Revision
        StockSize = StockSize
        Supplier = Supplier
        Title = Title
        Vendor = Vendor
        WebLink = WebLink
        FileName = FileName
        XYPlane = XYPlane
        YZPlane = YZPlane
        ZXPlane = ZXPlane
        XAxis = XAxis
        YAxis = YAxis
        ZAxis = ZAxis
        Origin = Origin
        Selections = Selections
    def RemovePoint( PointPoint):
        pass
    def RemovePlane( PlanePlane):
        pass
    def RemoveSketch( StringName):
        pass
    def RemoveSketch( SketchSketch):
        pass
    def Add3DSketch( StringName):
        pass
    def AddGear(
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
    def AddAxis( StringName, ISketchSurfacePlane1, ISketchSurfacePlane2):
        pass
    def AddAxis( StringName, PointPointA, PointPointB):
        pass
    def AddAxis( StringName, FaceCylindricalFace):
        pass
    def AddAxis( StringName, ListPoint1, ListPoint2):
        pass
    def AddPoint( StringName, ListPoint):
        pass
    def AddPoint( StringName, PointPoint):
        pass
    def AddPoint( StringName, DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoints( StringPrefix, ListPoints):
        pass
    def Regenerate(
    ):
        pass
    def AddExtrudeBoss( StringName, SketchSketch, DoubleDepth, BooleanIsReversed):
        pass
    def AddExtrudeBoss(
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
    def AddExtrudeCut( StringName, SketchSketch, DoubleDepth, BooleanIsReversed):
        pass
    def AddExtrudeCut(
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
    def AddRevolveBoss( StringName, SketchSketch, AxisAxis, DoubleAngle):
        pass
    def AddRevolveCut( StringName, SketchSketch, AxisAxis, DoubleAngle):
        pass
    def AddLoftBoss(
        StringName,
        ListCrossSections,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddLoftBoss(
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
        StringName,
        ListCrossSections,
        BooleanMinimizeTwist,
        BooleanMinimizeCurvature,
        BooleanSimplifySurface,
        BooleanConnectEnds,
    ):
        pass
    def AddLoftCut(
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
         StringName, IFilletableItem, DoubleRadius, BooleanTangentPropagate
    ):
        pass
    def AddFillet( StringName, ListItems, DoubleRadius, BooleanTangentPropagate):
        pass
    def AddFillet(
        StringName,
        ListItems,
        ListStartRadii,
        ListEndRadii,
        BooleanTangentPropagate,
    ):
        pass
    def Scale( StringName, BooleanScaleAboutCenter, DoubleScaleFactor):
        pass
    def NonUniformScale(
        StringName,
        BooleanScaleAboutCenter,
        DoubleScaleFactorX,
        DoubleScaleFactorY,
        DoubleScaleFactorZ,
    ):
        pass
    def AddChamfer(
        StringName,
        IChamferableItem,
        DoubleDistance1,
        DoubleDistance2,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamfer(
        StringName,
        ListItems,
        DoubleDistance1,
        DoubleDistance2,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamfer(
         StringName, IChamferableItem, DoubleDistance, BooleanTangentPropagate
    ):
        pass
    def GetEdges(
    ):
        pass
    def GetFaces(
    ):
        pass
    def GetVertices(
    ):
        pass
    def GetBoundingBox(
    ):
        pass
    def AddChamfer(
         StringName, ListItems, DoubleDistance, BooleanTangentPropagate
    ):
        pass
    def AddChamferAngle(
        StringName,
        IChamferableItem,
        DoubleDistance,
        DoubleAngle,
        BooleanTangentPropagate,
    ):
        pass
    def AddChamferAngle(
        StringName,
        ListItems,
        DoubleDistance,
        DoubleAngle,
        BooleanTangentPropagate,
    ):
        pass
    def AddVertexChamfer(
         StringName, VertexItem, DoubleDistance1, DoubleDistance2, DoubleDistance3
    ):
        pass
    def AddVertexChamfer(
         StringName, ListItems, DoubleDistance1, DoubleDistance2, DoubleDistance3
    ):
        pass
    def Save(
    ):
        pass
    def Save( StringFolder):
        pass
    def SaveAs( StringFolder, StringNewName):
        pass
    def Close(
    ):
        pass
    def ExportSTL( StringFileName):
        pass
    def ExportRotatedSTL(
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
    ):
        pass
    def ExportSTEP203( StringFileName):
        pass
    def ExportSTEP214( StringFileName):
        pass
    def ExportIGES( StringFileName):
        pass
    def ExportSAT( StringFileName, Int32Version, BooleanSaveColors):
        pass
    def ExportBIP( StringFileName):
        pass
    def SetColor( ByteRed, ByteGreen, ByteBlue):
        pass
    def SaveSnapshot(
        StringFileName,
        Int32Width,
        Int32Height,
        BooleanUseAspectRatio,
        BooleanUseWidthandHeight,
    ):
        pass
    def SaveThumbnail( StringFileName, Int32Width, Int32Height):
        pass
    def GetSelection(
    ):
        pass
    def Select( ISelectableGeometryFaceorEdge):
        pass
    def Select( ListFacesEdgesList):
        pass
    def SetUserData( StringName, PythonDictionaryDict):
        pass
    def GetUserData( StringName):
        pass
    def Debug1( PlanePlane):
        pass
    def PauseUpdating(
    ):
        pass
    def ResumeUpdating(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def AddPoint(
        StringName,
        IPointPointOrVertex,
        DoubleXOffset,
        DoubleYOffset,
        DoubleZOffset,
    ):
        pass
    def AddPoint(
         StringName, IPointPointOrVertex1, IPointPointOrVertex2, DoubleRatio
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge1, IAxisAxisOrEdge2):
        pass
    def AddPoint(
         StringName, IPlanePlaneOrFace1, IPlanePlaneOrFace2, IPlanePlaneOrFace3
    ):
        pass
    def AddPoint( StringName, IAxisAxisOrEdge, IPlanePlaneOrFace):
        pass
    def AddPoint(
        StringName,
        IPointSourcePointOrVertex,
        IPlaneTargetPlaneOrFace,
        DoubleXOffset,
        DoubleYOffset,
    ):
        pass
    def AddPoint( StringName, EdgeTargetEdge, DoubleRatio):
        pass
    def AddPointFromCircularEdge( StringName, EdgeTargetEdge):
        pass
    def AddPointFromToroidalFace( StringName, FaceTargetFace):
        pass
    def IsOpen(
    ):
        pass
    def GetFeature( StringName):
        pass
    def RemoveFeature( StringName):
        pass
    def RemoveFeature( FeatureFeature):
        pass
    def SuppressFeature( StringName):
        pass
    def SuppressFeature( FeatureFeature):
        pass
    def UnsuppressFeature( StringName):
        pass
    def UnsuppressFeature( FeatureFeature):
        pass
    def HideFeature( StringName):
        pass
    def HideFeature( FeatureFeature):
        pass
    def ShowFeature( StringName):
        pass
    def ShowFeature( FeatureFeature):
        pass
    def GetPlane( StringName):
        pass
    def GetPlane( IADDesignPlaneDesignPlane):
        pass
    def GetAxis( StringName):
        pass
    def GetAxis( IADDesignAxisDesignAxis):
        pass
    def GetPoint( StringName):
        pass
    def GetPoint( IADDesignPointDesignPoint):
        pass
    def GetSketch( StringName):
        pass
    def Get3DSketch( StringName):
        pass
    def GetFace( StringName):
        pass
    def GetEdge( StringName):
        pass
    def GetVertex( StringName):
        pass
    def GetParameter( StringName):
        pass
    def GetCustomProperty( StringName):
        pass
    def SetCustomProperty( StringName, StringValue):
        pass
    def GetConfiguration( StringName):
        pass
    def GetActiveConfiguration(
    ):
        pass
    def AddPlane( StringName, ISketchSurfaceSourcePlane, DoubleOffset):
        pass
    def AddPlane( StringName, ListNormalVector, ListPointonPlane):
        pass
    def AddPlane( StringName, AxisAxis, PointPoint):
        pass
    def AddPlane(
         StringName, ISketchSurfaceSourcePlane, AxisRotationAxis, DoubleAngle
    ):
        pass
    def AddParameter( StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter(
         StringName, ParameterTypesType, ParameterUnitsUnitstoUse, DoubleValue
    ):
        pass
    def AddParameter( StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration( StringName):
        pass
    def AddConfiguration( StringName, StringBaseConfigurationName):
        pass
    def AddPlane( StringName, ListPoint1, ListPoint2, ListPoint3):
        pass
    def AddSketch( StringName, ISketchSurfacePlane):
        pass
class Plane:
    def __init__( Name):
        pass
        Name = Name
    def GetPart(
    ):
        pass
    def SurfaceObject(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def PlaneObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def IsParallel( PlaneOtherPlane):
        pass
    def Hide(
    ):
        pass
    def Show(
    ):
        pass
class Point:
    def __init__( Name, X, Y, Z):
        pass
        Name = Name
        X = X
        Y = Y
        Z = Z
    def PointObject(
    ):
        pass
    def GetPart(
    ):
        pass
    def CrossSectionObject(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def GetCoordinates(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def Hide(
    ):
        pass
    def Show(
    ):
        pass
class Polyline:
    def __init__(
    ):
        pass
    def AddPoint( PolylinePointPoint):
        pass
    def AddPoint( DoubleX, DoubleY):
        pass
    def InsertPoint( Int32Index, PolylinePointPoint):
        pass
    def AddCircle( DoubleCenterX, DoubleCenterY, DoubleDiameter, Int32sides):
        pass
    def AddArc(
        PolylinePointCenter,
        PolylinePointStart,
        PolylinePointEnd,
        Int32MinimumSegments,
    ):
        pass
    def AddPolyline( PolylineAppendLine):
        pass
    def FindIntersection( PolylineL1, PolylineL2):
        pass
    def FindIntersectionWithCircle(
         PolylineL1, DoubleCircleX, DoubleCircleY, DoubleRadius
    ):
        pass
    def FindIntersection(
         PolylinePointA1, PolylinePointA2, PolylinePointB1, PolylinePointB2
    ):
        pass
    def IsPointOnLine(
         PolylinePointA1, PolylinePointA2, PolylinePointPoint, DoubleTolerance
    ):
        pass
    def SplitAtPoint( PolylinePointSplitPoint, DoubleTolerence):
        pass
    def Clone(
    ):
        pass
    def Clone( Int32StartIndex, Int32EndIndex):
        pass
    def Join( PolylineAppendLine):
        pass
    def RotateZ( DoubleCenterX, DoubleCenterY, DoubleAngle):
        pass
    def Offset( DoubleOffsetX, DoubleOffsetY):
        pass
    def RemoveDuplicates(
    ):
        pass
class Polyline3D:
    def __init__(
    ):
        pass
    def AddPoint( PolylinePoint3DPoint):
        pass
    def AddPoint( DoubleX, DoubleY, DoubleZ):
        pass
    def InsertPoint( Int32Index, PolylinePoint3DPoint):
        pass
    def AddPolyline( Polyline3DAppendLine):
        pass
    def IsPointOnLine(
         PolylinePoint3DA, PolylinePoint3DB, PolylinePoint3DP, DoubleTolerance
    ):
        pass
    def SplitAtPoint( PolylinePoint3DSplitPoint, DoubleTolerence):
        pass
    def Clone(
    ):
        pass
    def Clone( Int32StartIndex, Int32EndIndex):
        pass
    def Join( Polyline3DAppendLine):
        pass
    def Offset( DoubleOffsetX, DoubleOffsetY, DoubleOffsetZ):
        pass
    def RemoveDuplicates(
    ):
        pass
class PolylinePoint:
    def __init__(
    ):
        pass
    def op_Multiply( Matrix3DMatrix, PolylinePointPoint):
        pass
    def op_Multiply( PolylinePointPoint, Matrix3DMatrix):
        pass
    def op_Subtraction( PolylinePointP2, PolylinePointP1):
        pass
    def CrossProduct( PolylinePointP1, PolylinePointP2):
        pass
    def Offset( DoubleX, DoubleY):
        pass
    def Scale( DoubleScaleOriginX, DoubleScaleOriginY, DoubleScaleFactor):
        pass
    def RotateZ( DoubleCenterX, DoubleCenterY, DoubleAngle):
        pass
class PolylinePoint3D:
    def __init__(
    ):
        pass
    def op_Multiply( Matrix3DMatrix, PolylinePoint3DPoint):
        pass
    def op_Multiply( PolylinePoint3DPoint, Matrix3DMatrix):
        pass
    def op_Subtraction( PolylinePoint3DP2, PolylinePoint3DP1):
        pass
    def Offset( DoubleX, DoubleY, DoubleZ):
        pass
    def Scale(
        DoubleScaleOriginX,
        DoubleScaleOriginY,
        DoubleScaleOriginZ,
        DoubleScaleFactor,
    ):
        pass
class Sketch:
    def __init__( Name, Figures, Origin):
        pass
        Name = Name
        Figures = Figures
        Origin = Origin
    def GetPart(
    ):
        pass
    def GetSurface(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def StartEditing(
    ):
        pass
    def StopEditing(
    ):
        pass
    def AddConstraint( ISketchFigureFigure, ConstraintsConstraint):
        pass
    def AddConstraint( ListFigures, ConstraintsConstraint):
        pass
    def AddLine( ListStartPoint, ListEndPoint, BooleanIsReference):
        pass
    def AddLine( LineNewLine):
        pass
    def AddLine( DoubleX1, DoubleY1, DoubleX2, DoubleY2, BooleanIsReference):
        pass
    def AddPoint( DoubleX, DoubleY):
        pass
    def AddPoint( DoubleX, DoubleY, BooleanIsReference):
        pass
    def AddPoint( SketchPointNewPoint):
        pass
    def AddLines( ListPoints, BooleanIsReference):
        pass
    def AddPolyline( PolylineLine, BooleanIsReference):
        pass
    def AddArcCenterStartEnd(
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
        DoubleCenterX,
        DoubleCenterY,
        DoubleStartX,
        DoubleStartY,
        DoubleAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse(
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
        DoubleCenterX,
        DoubleCenterY,
        DoubleMajorAxisDiameter,
        DoubleMinorMajorRatio,
        DoubleMajorAxisAngle,
        BooleanIsReference,
    ):
        pass
    def AddEllipse( EllipseNewEllipse):
        pass
    def AddEllipticalArc(
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
    def AddEllipticalArc( EllipticalArcNewEllipticalArc):
        pass
    def AddArc( CircularArcNewArc):
        pass
    def AddRectangle(
        DoubleBottomLeftX,
        DoubleBottomLeftY,
        DoubleTopRightX,
        DoubleTopRightY,
        BooleanIsReference,
    ):
        pass
    def AddCircle(
         DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def AddCircle( CircleNewCircle):
        pass
    def AddBspline(
        Int32Order,
        ListControlPoints,
        ListKnotVectors,
        ListWeights,
        BooleanIsReference,
    ):
        pass
    def AddBspline( ListPoints, BooleanIsReference):
        pass
    def AddFigure( ISketchFigureNewFigure):
        pass
    def AddBspline( BsplineNewBspline):
        pass
    def AddBspline(
        Int32Order,
        List1ControlPoints,
        List1KnotVectors,
        List1Weights,
        BooleanIsReference,
    ):
        pass
    def AddBsplineInterpolated( List1Points, BooleanIsReference):
        pass
    def AddBsplineThroughPoints( List1Points, BooleanIsReference):
        pass
    def AddPolygon(
        DoubleCenterX,
        DoubleCenterY,
        DoubleDiameter,
        Int32Sides,
        BooleanIsReference,
    ):
        pass
    def AddPolyhole(
         DoubleCenterX, DoubleCenterY, DoubleDiameter, BooleanIsReference
    ):
        pass
    def PathObject(
    ):
        pass
    def CrossSectionObject(
    ):
        pass
    def CopyFrom( SketchSource):
        pass
    def CopyFrom(
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
    def PointtoGlobal( Doublex, Doubley):
        pass
    def GlobaltoPoint( Doublex, Doubley, Doublez):
        pass
    def VertextoPoint( VertexVert):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def AddDimension( SketchPointP1, SketchPointP2):
        pass
    def AddDimension( CircleCircle):
        pass
    def AddDimension( CircularArcArc):
        pass
    def SavetoXml( StringFileName):
        pass
    def ToXml(
    ):
        pass
    def LoadXml( StringFileName):
        pass
    def FromXml( StringXml):
        pass
    def StartFaceMapping( VertexEdgeVertex1, VertexEdgeVertex2):
        pass
    def StartFaceMapping( ListEdgeEndPoint1, ListEdgeEndPoint2):
        pass
    def StopFaceMapping(
    ):
        pass
    def StartMapping( ListPoint1, ListPoint2, ListPointAboveAxis):
        pass
    def StopMapping(
    ):
        pass
    def ImportSVG( StringFileName):
        pass
    def ImportSVG(
        StringFileName,
        DoubleTranslateX,
        DoubleTranslateY,
        DoubleRotationAngle,
        BooleanTranslateThenRotate,
        BooleanNativeFigures,
    ):
        pass
    def ExportSVG( StringFileName):
        pass
    def ExportSVG( StringFileName, BooleanIncludeReferences):
        pass
    def ExportSVG(
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
    def __init__( Name, Figures):
        pass
        Name = Name
        Figures = Figures
    def GetPart(
    ):
        pass
    def StartEditing(
    ):
        pass
    def StopEditing(
    ):
        pass
    def AddLine( ListStartPoint, ListEndPoint):
        pass
    def AddLine( Line3DNewLine):
        pass
    def AddPoint( DoubleX, DoubleY, DoubleZ):
        pass
    def AddPoint( SketchPoint3DNewPoint):
        pass
    def AddLine( DoubleX1, DoubleY1, DoubleZ1, DoubleX2, DoubleY2, DoubleZ2):
        pass
    def AddLines( ListPoints):
        pass
    def AddPolyline( Polyline3DLine):
        pass
    def AddArcCenterStartEnd(
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
    def AddArc( CircularArc3DNewArc):
        pass
    def AddBspline( ListPoints):
        pass
    def AddBspline( Bspline3DBspline):
        pass
    def AddBspline( List1Points):
        pass
    def PathObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def SavetoXml( StringFileName):
        pass
    def ToXml(
    ):
        pass
    def LoadXml( StringFileName):
        pass
    def FromXml( StringXml):
        pass
class SketchPoint:
    def __init__( Point, X, Y, IsReference):
        pass
        Point = Point
        X = X
        Y = Y
        IsReference = IsReference
    def FigureObject(
    ):
        pass
    def SetInstance( IADSketchFigureFigure):
        pass
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class SketchPoint3D:
    def __init__( X, Y, Z, IsReference):
        pass
        X = X
        Y = Y
        Z = Z
        IsReference = IsReference
    def ToXml(
    ):
        pass
    def FromXml( XElementXml):
        pass
class ThreeD:
    def __init__(
    ):
        pass
    def VectorTransform( Vector3DVector1, Vector3DVector2):
        pass
    def GetMatrixFromTransformation( IADTransformationTransformation):
        pass
    def TransformPoint( DoublePoint, IADTransformationTransformation):
        pass
    def TransformVector( DoubleVector, IADTransformationTransformation):
        pass
    def CreateTransformation(
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
         Doublex, Doubley, Doublez, IADGeometryFactoryGeomFactory
    ):
        pass
    def CreateRotation(
         DoubleAngle, RotationDirectionsDirection, IADGeometryFactoryGeomFactory
    ):
        pass
    def DecomposeTransformation(
        IADTransformationTransformation,
        DoubleOffsetX,
        DoubleOffsetY,
        DoubleOffsetZ,
        DoubleAngleX,
        DoubleAngleY,
        DoubleAngleZ,
    ):
        pass
    def GetPerpendicularVector( ListVector):
        pass
    def TransformPointUsingVectors(
         ListSourceVector, ListDestinationVector, ListPoint
    ):
        pass
class TwoD:
    def __init__(
    ):
        pass
    def TranslatePoint( Tuple2Point, DoubleXTranslation, DoubleYTranslation):
        pass
    def _RotatePoint( Tuple2Point, DoubleAngle):
        pass
    def RotatePoint( ListPoint, DoubleAngle):
        pass
    def IsPointInsidePolygon( List1Vertices, Tuple2Point):
        pass
    def GetPerpendicularVector( ListVector):
        pass
    def NormalizeVector( ListVector):
        pass
class Units:
    def __init__(
    ):
        pass
    def FromADUnitType( ADUnitsADUnit):
        pass
    def ToADUnits( DoubleValue):
        pass
    def FromADUnits( DoubleValue):
        pass
    def ToTeethPerInch( DoubleTeethPerCurrentUnits):
        pass
    def FromTeethPerInch( DoubleTeethPerInch):
        pass
    def ToInches( DoubleValue):
        pass
    def FromInches( DoubleValue):
        pass
    def ToMillimeters( DoubleValue):
        pass
    def FromMillimeters( DoubleValue):
        pass
    def ToADUnits( List1Values):
        pass
    def ToADUnits( DoubleValue, ADUnitsCurrentUnits):
        pass
    def FromADUnits( DoubleValue, ADUnitsCurrentUnits):
        pass
    def FromADUnits( List1ADValues):
        pass
class Vertex:
    def __init__( _Vertex, Name, X, Y, Z):
        pass
        _Vertex = _Vertex
        Name = Name
        X = X
        Y = Y
        Z = Z
    def GetPart(
    ):
        pass
    def ChamferableObject(
    ):
        pass
    def ConstraintObject(
    ):
        pass
    def SelectableObject(
    ):
        pass
    def PointObject(
    ):
        pass
    def GetSelectionAssembly(
    ):
        pass
    def SetOccurrence( IADOccurrenceOccurrence):
        pass
    def GetOccurrence(
    ):
        pass
    def SetParentAssembly( AssemblyParentAssembly):
        pass
    def GetParentAssembly(
    ):
        pass
class Windows:
    def __init__(
        self
    ):
        pass
    def CloseForm( StringSessionIdentifier):
        pass
    def GetDisplayedForm( StringSessionIdentifier):
        pass
    def UtilityDialog(
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
    ):
        pass
    def UtilityDialog(
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def OptionsDialog( StringTitle, ListInputs, Int32InputAreaWidth):
        pass
    def OptionsDialog(
        StringTitle,
        ListInputs,
        Int32InputAreaWidth,
        ObjectInputChangedCallback,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def DisableInput( Int32Index):
        pass
    def EnableInput( Int32Index):
        pass
    def GetInputValue( Int32Index):
        pass
    def SetStringList( Int32Index, ObjectStrings):
        pass
    def SetInputValue( Int32Index, ObjectValue):
        pass
    def OpenFileDialog( StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SaveFileDialog( StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SelectFolderDialog( StringCurrentFolder, StringDescription):
        pass
    def InfoDialog( StringMessage, StringTitle):
        pass
    def ErrorDialog( StringMessage, StringTitle):
        pass
    def QuestionDialog( StringQuestion, StringTitle):
        pass
