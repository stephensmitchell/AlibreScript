# Runtime companion to __init__.pyi, IronPython 2.7.10 compatible.
# Authoring aid only: Alibre Script supplies the real API as built-in
# globals. Every member here raises if called outside Alibre Design.


def _unavailable(name):
    raise NotImplementedError(
        name + ' is only available inside Alibre Design.'
        ' These stubs exist for editor autocomplete.')


ScriptFileName = ''
ScriptFolder = ''

class IAssembled(object):
    def GetMappedOccurrence(self, *args, **kwargs): _unavailable('IAssembled.GetMappedOccurrence')

class IAxis(object):
    def AxisObject(self, *args, **kwargs): _unavailable('IAxis.AxisObject')
    def GetOccurrence(self, *args, **kwargs): _unavailable('IAxis.GetOccurrence')

class IChamferable(object):
    def ChamferableObject(self, *args, **kwargs): _unavailable('IChamferable.ChamferableObject')

class IConstrainable(object):
    def ConstraintObject(self, *args, **kwargs): _unavailable('IConstrainable.ConstraintObject')

class IFilletable(object):
    def FilletableObject(self, *args, **kwargs): _unavailable('IFilletable.FilletableObject')

class IPlane(object):
    def GetOccurrence(self, *args, **kwargs): _unavailable('IPlane.GetOccurrence')
    def PlaneObject(self, *args, **kwargs): _unavailable('IPlane.PlaneObject')

class IPoint(object):
    def GetOccurrence(self, *args, **kwargs): _unavailable('IPoint.GetOccurrence')
    def PointObject(self, *args, **kwargs): _unavailable('IPoint.PointObject')

class ISelectableGeometry(object):
    def SelectableObject(self, *args, **kwargs): _unavailable('ISelectableGeometry.SelectableObject')

class ISketchFigure(object):
    def FigureObject(self, *args, **kwargs): _unavailable('ISketchFigure.FigureObject')
    def SetInstance(self, *args, **kwargs): _unavailable('ISketchFigure.SetInstance')
    def ToXml(self, *args, **kwargs): _unavailable('ISketchFigure.ToXml')

class ISketchSurface(object):
    def SurfaceObject(self, *args, **kwargs): _unavailable('ISketchSurface.SurfaceObject')

class ISweepPath(object):
    def PathObject(self, *args, **kwargs): _unavailable('ISweepPath.PathObject')

class Part(object):
    class DirectionType(object):
        Axis = None
        Edge = None
        Normal = None
        value__ = None

    class EndCondition(object):
        EntirePath = None
        MidPlane = None
        ThroughAll = None
        ToDepth = None
        ToGeometry = None
        ToNext = None
        value__ = None

    class FileTypes(object):
        AlibreDesignPart = None
        GeomagicDesignPart = None
        IGES = None
        SAT = None
        STEP = None
        STL_cm = None
        STL_in = None
        STL_mm = None
        ThreeDM = None
        value__ = None

    Axes = None
    Features = None
    Planes = None
    Points = None
    Sketches = None
    Sketches3D = None
    _Part = None
    _SelectionSession = None
    Comment = None
    ConfigurationList = None
    Configurations = None
    CostCenter = None
    CreatedBy = None
    CreatedDate = None
    CreatingApplication = None
    Density = None
    Description = None
    DocumentNumber = None
    Edges = None
    EngineeringApprovalDate = None
    EngineeringApprovedBy = None
    EstimatedCost = None
    ExtendedMaterialInformation = None
    Faces = None
    FileName = None
    Keywords = None
    LastAuthor = None
    LastUpdateDate = None
    ManufacturingApprovedBy = None
    ManufacturingApprovedDate = None
    Mass = None
    Material = None
    ModifiedInformation = None
    Name = None
    Number = None
    Origin = None
    ParameterList = None
    Parameters = None
    Product = None
    ReceivedFrom = None
    Revision = None
    Selections = None
    StockSize = None
    Supplier = None
    Title = None
    Vendor = None
    Vertices = None
    WebLink = None
    XAxis = None
    XYPlane = None
    YAxis = None
    YZPlane = None
    ZAxis = None
    ZXPlane = None
    def Add3DSketch(self, *args, **kwargs): _unavailable('Part.Add3DSketch')
    def AddAxis(self, *args, **kwargs): _unavailable('Part.AddAxis')
    def AddChamfer(self, *args, **kwargs): _unavailable('Part.AddChamfer')
    def AddChamferAngle(self, *args, **kwargs): _unavailable('Part.AddChamferAngle')
    def AddConfiguration(self, *args, **kwargs): _unavailable('Part.AddConfiguration')
    def AddExtrudeBoss(self, *args, **kwargs): _unavailable('Part.AddExtrudeBoss')
    def AddExtrudeCut(self, *args, **kwargs): _unavailable('Part.AddExtrudeCut')
    def AddFillet(self, *args, **kwargs): _unavailable('Part.AddFillet')
    def AddGear(self, *args, **kwargs): _unavailable('Part.AddGear')
    def AddGearDN(self, *args, **kwargs): _unavailable('Part.AddGearDN')
    def AddGearDP(self, *args, **kwargs): _unavailable('Part.AddGearDP')
    def AddGearNP(self, *args, **kwargs): _unavailable('Part.AddGearNP')
    def AddLoftBoss(self, *args, **kwargs): _unavailable('Part.AddLoftBoss')
    def AddLoftCut(self, *args, **kwargs): _unavailable('Part.AddLoftCut')
    def AddParameter(self, *args, **kwargs): _unavailable('Part.AddParameter')
    def AddPlane(self, *args, **kwargs): _unavailable('Part.AddPlane')
    def AddPoint(self, *args, **kwargs): _unavailable('Part.AddPoint')
    def AddPointFromCircularEdge(self, *args, **kwargs): _unavailable('Part.AddPointFromCircularEdge')
    def AddPointFromToroidalFace(self, *args, **kwargs): _unavailable('Part.AddPointFromToroidalFace')
    def AddPoints(self, *args, **kwargs): _unavailable('Part.AddPoints')
    def AddRack(self, *args, **kwargs): _unavailable('Part.AddRack')
    def AddRevolveBoss(self, *args, **kwargs): _unavailable('Part.AddRevolveBoss')
    def AddRevolveCut(self, *args, **kwargs): _unavailable('Part.AddRevolveCut')
    def AddSketch(self, *args, **kwargs): _unavailable('Part.AddSketch')
    def AddSweepBoss(self, *args, **kwargs): _unavailable('Part.AddSweepBoss')
    def AddSweepCut(self, *args, **kwargs): _unavailable('Part.AddSweepCut')
    def AddVertexChamfer(self, *args, **kwargs): _unavailable('Part.AddVertexChamfer')
    def Close(self, *args, **kwargs): _unavailable('Part.Close')
    def Debug1(self, *args, **kwargs): _unavailable('Part.Debug1')
    def DisplayUnits(self, *args, **kwargs): _unavailable('Part.DisplayUnits')
    def ExportBIP(self, *args, **kwargs): _unavailable('Part.ExportBIP')
    def ExportIGES(self, *args, **kwargs): _unavailable('Part.ExportIGES')
    def ExportRotatedSTL(self, *args, **kwargs): _unavailable('Part.ExportRotatedSTL')
    def ExportSAT(self, *args, **kwargs): _unavailable('Part.ExportSAT')
    def ExportSTEP203(self, *args, **kwargs): _unavailable('Part.ExportSTEP203')
    def ExportSTEP214(self, *args, **kwargs): _unavailable('Part.ExportSTEP214')
    def ExportSTL(self, *args, **kwargs): _unavailable('Part.ExportSTL')
    def Get3DSketch(self, *args, **kwargs): _unavailable('Part.Get3DSketch')
    def GetActiveConfiguration(self, *args, **kwargs): _unavailable('Part.GetActiveConfiguration')
    def GetAxis(self, *args, **kwargs): _unavailable('Part.GetAxis')
    def GetBoundingBox(self, *args, **kwargs): _unavailable('Part.GetBoundingBox')
    def GetConfiguration(self, *args, **kwargs): _unavailable('Part.GetConfiguration')
    def GetCustomProperty(self, *args, **kwargs): _unavailable('Part.GetCustomProperty')
    def GetEdge(self, *args, **kwargs): _unavailable('Part.GetEdge')
    def GetEdges(self, *args, **kwargs): _unavailable('Part.GetEdges')
    def GetFace(self, *args, **kwargs): _unavailable('Part.GetFace')
    def GetFaces(self, *args, **kwargs): _unavailable('Part.GetFaces')
    def GetFeature(self, *args, **kwargs): _unavailable('Part.GetFeature')
    def GetParameter(self, *args, **kwargs): _unavailable('Part.GetParameter')
    def GetPlane(self, *args, **kwargs): _unavailable('Part.GetPlane')
    def GetPoint(self, *args, **kwargs): _unavailable('Part.GetPoint')
    def GetSelection(self, *args, **kwargs): _unavailable('Part.GetSelection')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Part.GetSelectionAssembly')
    def GetSketch(self, *args, **kwargs): _unavailable('Part.GetSketch')
    def GetUserData(self, *args, **kwargs): _unavailable('Part.GetUserData')
    def GetVertex(self, *args, **kwargs): _unavailable('Part.GetVertex')
    def GetVertices(self, *args, **kwargs): _unavailable('Part.GetVertices')
    def HideFeature(self, *args, **kwargs): _unavailable('Part.HideFeature')
    def IsOpen(self, *args, **kwargs): _unavailable('Part.IsOpen')
    def NonUniformScale(self, *args, **kwargs): _unavailable('Part.NonUniformScale')
    def PauseUpdating(self, *args, **kwargs): _unavailable('Part.PauseUpdating')
    def Regenerate(self, *args, **kwargs): _unavailable('Part.Regenerate')
    def RemoveFeature(self, *args, **kwargs): _unavailable('Part.RemoveFeature')
    def RemovePlane(self, *args, **kwargs): _unavailable('Part.RemovePlane')
    def RemovePoint(self, *args, **kwargs): _unavailable('Part.RemovePoint')
    def RemoveSketch(self, *args, **kwargs): _unavailable('Part.RemoveSketch')
    def ResumeUpdating(self, *args, **kwargs): _unavailable('Part.ResumeUpdating')
    def Save(self, *args, **kwargs): _unavailable('Part.Save')
    def SaveAs(self, *args, **kwargs): _unavailable('Part.SaveAs')
    def SaveSnapshot(self, *args, **kwargs): _unavailable('Part.SaveSnapshot')
    def SaveThumbnail(self, *args, **kwargs): _unavailable('Part.SaveThumbnail')
    def Scale(self, *args, **kwargs): _unavailable('Part.Scale')
    def Select(self, *args, **kwargs): _unavailable('Part.Select')
    def SetColor(self, *args, **kwargs): _unavailable('Part.SetColor')
    def SetCustomProperty(self, *args, **kwargs): _unavailable('Part.SetCustomProperty')
    def SetUserData(self, *args, **kwargs): _unavailable('Part.SetUserData')
    def ShowFeature(self, *args, **kwargs): _unavailable('Part.ShowFeature')
    def SuppressFeature(self, *args, **kwargs): _unavailable('Part.SuppressFeature')
    def ToString(self, *args, **kwargs): _unavailable('Part.ToString')
    def UnsuppressFeature(self, *args, **kwargs): _unavailable('Part.UnsuppressFeature')

class Assembly(object):
    class ConstraintBoundsType(object):
        Between = None
        Equals = None
        GreaterOrEquals = None
        LessOrEquals = None
        value__ = None

    Axes = None
    Planes = None
    Points = None
    _Assembly = None
    Comment = None
    ConfigurationList = None
    Configurations = None
    CostCenter = None
    CreatedBy = None
    CreatedDate = None
    CreatingApplication = None
    Density = None
    Description = None
    DocumentNumber = None
    EngineeringApprovalDate = None
    EngineeringApprovedBy = None
    EstimatedCost = None
    ExtendedMaterialInformation = None
    FileName = None
    Keywords = None
    LastAuthor = None
    LastUpdateDate = None
    ManufacturingApprovedBy = None
    ManufacturingApprovedDate = None
    Material = None
    ModifiedInformation = None
    Name = None
    Number = None
    Origin = None
    ParameterList = None
    Parameters = None
    PartList = None
    Parts = None
    Product = None
    ReceivedFrom = None
    Revision = None
    Selections = None
    StockSize = None
    SubAssemblies = None
    SubAssemblyList = None
    Supplier = None
    Title = None
    Vendor = None
    WebLink = None
    XAxis = None
    XYPlane = None
    YAxis = None
    YZPlane = None
    ZAxis = None
    ZXPlane = None
    def AddAlignConstraint(self, *args, **kwargs): _unavailable('Assembly.AddAlignConstraint')
    def AddAlignConstraint2(self, *args, **kwargs): _unavailable('Assembly.AddAlignConstraint2')
    def AddAngleConstraint(self, *args, **kwargs): _unavailable('Assembly.AddAngleConstraint')
    def AddAngleConstraint2(self, *args, **kwargs): _unavailable('Assembly.AddAngleConstraint2')
    def AddAxis(self, *args, **kwargs): _unavailable('Assembly.AddAxis')
    def AddConfiguration(self, *args, **kwargs): _unavailable('Assembly.AddConfiguration')
    def AddFastenerConstraint(self, *args, **kwargs): _unavailable('Assembly.AddFastenerConstraint')
    def AddFastenerConstraint2(self, *args, **kwargs): _unavailable('Assembly.AddFastenerConstraint2')
    def AddGearConstraint(self, *args, **kwargs): _unavailable('Assembly.AddGearConstraint')
    def AddMateConstraint(self, *args, **kwargs): _unavailable('Assembly.AddMateConstraint')
    def AddMateConstraint2(self, *args, **kwargs): _unavailable('Assembly.AddMateConstraint2')
    def AddNewPart(self, *args, **kwargs): _unavailable('Assembly.AddNewPart')
    def AddNewSubAssembly(self, *args, **kwargs): _unavailable('Assembly.AddNewSubAssembly')
    def AddOrientConstraint(self, *args, **kwargs): _unavailable('Assembly.AddOrientConstraint')
    def AddParameter(self, *args, **kwargs): _unavailable('Assembly.AddParameter')
    def AddPart(self, *args, **kwargs): _unavailable('Assembly.AddPart')
    def AddPlane(self, *args, **kwargs): _unavailable('Assembly.AddPlane')
    def AddPoint(self, *args, **kwargs): _unavailable('Assembly.AddPoint')
    def AddPointFromCircularEdge(self, *args, **kwargs): _unavailable('Assembly.AddPointFromCircularEdge')
    def AddPointFromToroidalFace(self, *args, **kwargs): _unavailable('Assembly.AddPointFromToroidalFace')
    def AddPoints(self, *args, **kwargs): _unavailable('Assembly.AddPoints')
    def AddRackAndPinionConstraint(self, *args, **kwargs): _unavailable('Assembly.AddRackAndPinionConstraint')
    def AddScrewConstraint(self, *args, **kwargs): _unavailable('Assembly.AddScrewConstraint')
    def AddSubAssembly(self, *args, **kwargs): _unavailable('Assembly.AddSubAssembly')
    def AddTangentConstraint(self, *args, **kwargs): _unavailable('Assembly.AddTangentConstraint')
    def AnchorPart(self, *args, **kwargs): _unavailable('Assembly.AnchorPart')
    def AnchorSubAssembly(self, *args, **kwargs): _unavailable('Assembly.AnchorSubAssembly')
    def Close(self, *args, **kwargs): _unavailable('Assembly.Close')
    def CreateUniqueName(self, *args, **kwargs): _unavailable('Assembly.CreateUniqueName')
    def DisplayUnits(self, *args, **kwargs): _unavailable('Assembly.DisplayUnits')
    def DuplicatePart(self, *args, **kwargs): _unavailable('Assembly.DuplicatePart')
    def DuplicateSubAssembly(self, *args, **kwargs): _unavailable('Assembly.DuplicateSubAssembly')
    def ExportBIP(self, *args, **kwargs): _unavailable('Assembly.ExportBIP')
    def ExportIGES(self, *args, **kwargs): _unavailable('Assembly.ExportIGES')
    def ExportSAT(self, *args, **kwargs): _unavailable('Assembly.ExportSAT')
    def ExportSTEP203(self, *args, **kwargs): _unavailable('Assembly.ExportSTEP203')
    def ExportSTEP214(self, *args, **kwargs): _unavailable('Assembly.ExportSTEP214')
    def ExportSTL(self, *args, **kwargs): _unavailable('Assembly.ExportSTL')
    def GetActiveConfiguration(self, *args, **kwargs): _unavailable('Assembly.GetActiveConfiguration')
    def GetAxis(self, *args, **kwargs): _unavailable('Assembly.GetAxis')
    def GetConfiguration(self, *args, **kwargs): _unavailable('Assembly.GetConfiguration')
    def GetCustomProperty(self, *args, **kwargs): _unavailable('Assembly.GetCustomProperty')
    def GetParameter(self, *args, **kwargs): _unavailable('Assembly.GetParameter')
    def GetPart(self, *args, **kwargs): _unavailable('Assembly.GetPart')
    def GetPartOrientation(self, *args, **kwargs): _unavailable('Assembly.GetPartOrientation')
    def GetPlane(self, *args, **kwargs): _unavailable('Assembly.GetPlane')
    def GetPoint(self, *args, **kwargs): _unavailable('Assembly.GetPoint')
    def GetSelection(self, *args, **kwargs): _unavailable('Assembly.GetSelection')
    def GetSubAssembly(self, *args, **kwargs): _unavailable('Assembly.GetSubAssembly')
    def GetUserData(self, *args, **kwargs): _unavailable('Assembly.GetUserData')
    def HidePart(self, *args, **kwargs): _unavailable('Assembly.HidePart')
    def HideSubAssembly(self, *args, **kwargs): _unavailable('Assembly.HideSubAssembly')
    def MovePart(self, *args, **kwargs): _unavailable('Assembly.MovePart')
    def MoveParts(self, *args, **kwargs): _unavailable('Assembly.MoveParts')
    def MoveSubAssemblies(self, *args, **kwargs): _unavailable('Assembly.MoveSubAssemblies')
    def MoveSubAssembly(self, *args, **kwargs): _unavailable('Assembly.MoveSubAssembly')
    def PauseUpdating(self, *args, **kwargs): _unavailable('Assembly.PauseUpdating')
    def Regenerate(self, *args, **kwargs): _unavailable('Assembly.Regenerate')
    def ResumeUpdating(self, *args, **kwargs): _unavailable('Assembly.ResumeUpdating')
    def RotatePart(self, *args, **kwargs): _unavailable('Assembly.RotatePart')
    def RotateParts(self, *args, **kwargs): _unavailable('Assembly.RotateParts')
    def RotateSubAssemblies(self, *args, **kwargs): _unavailable('Assembly.RotateSubAssemblies')
    def RotateSubAssembly(self, *args, **kwargs): _unavailable('Assembly.RotateSubAssembly')
    def Save(self, *args, **kwargs): _unavailable('Assembly.Save')
    def SaveAll(self, *args, **kwargs): _unavailable('Assembly.SaveAll')
    def SaveAs(self, *args, **kwargs): _unavailable('Assembly.SaveAs')
    def SaveSnapshot(self, *args, **kwargs): _unavailable('Assembly.SaveSnapshot')
    def SaveThumbnail(self, *args, **kwargs): _unavailable('Assembly.SaveThumbnail')
    def SetCustomProperty(self, *args, **kwargs): _unavailable('Assembly.SetCustomProperty')
    def SetUserData(self, *args, **kwargs): _unavailable('Assembly.SetUserData')
    def ShowPart(self, *args, **kwargs): _unavailable('Assembly.ShowPart')
    def ShowSubAssembly(self, *args, **kwargs): _unavailable('Assembly.ShowSubAssembly')
    def SuppressPart(self, *args, **kwargs): _unavailable('Assembly.SuppressPart')
    def SuppressSubAssembly(self, *args, **kwargs): _unavailable('Assembly.SuppressSubAssembly')
    def ToString(self, *args, **kwargs): _unavailable('Assembly.ToString')
    def UnanchorPart(self, *args, **kwargs): _unavailable('Assembly.UnanchorPart')
    def UnanchorSubAssembly(self, *args, **kwargs): _unavailable('Assembly.UnanchorSubAssembly')
    def UnsuppressPart(self, *args, **kwargs): _unavailable('Assembly.UnsuppressPart')
    def UnsuppressSubAssembly(self, *args, **kwargs): _unavailable('Assembly.UnsuppressSubAssembly')

class Sketch(object):
    class Constraints(object):
        Coincident = None
        Collinear = None
        Coradial = None
        Equal = None
        Fix = None
        Horizontal = None
        Intersection = None
        Midpoint = None
        Normal = None
        Parallel = None
        Perpendicular = None
        Symmetric = None
        Tangent = None
        Vertical = None
        value__ = None

    AutomaticStartEndEditing = None
    _SelectionSession = None
    _Sketch = None
    Figures = None
    Name = None
    Origin = None
    def AddArc(self, *args, **kwargs): _unavailable('Sketch.AddArc')
    def AddArcCenterStartAngle(self, *args, **kwargs): _unavailable('Sketch.AddArcCenterStartAngle')
    def AddArcCenterStartEnd(self, *args, **kwargs): _unavailable('Sketch.AddArcCenterStartEnd')
    def AddBspline(self, *args, **kwargs): _unavailable('Sketch.AddBspline')
    def AddBsplineInterpolated(self, *args, **kwargs): _unavailable('Sketch.AddBsplineInterpolated')
    def AddBsplineThroughPoints(self, *args, **kwargs): _unavailable('Sketch.AddBsplineThroughPoints')
    def AddCircle(self, *args, **kwargs): _unavailable('Sketch.AddCircle')
    def AddConstraint(self, *args, **kwargs): _unavailable('Sketch.AddConstraint')
    def AddDimension(self, *args, **kwargs): _unavailable('Sketch.AddDimension')
    def AddEllipse(self, *args, **kwargs): _unavailable('Sketch.AddEllipse')
    def AddEllipticalArc(self, *args, **kwargs): _unavailable('Sketch.AddEllipticalArc')
    def AddFigure(self, *args, **kwargs): _unavailable('Sketch.AddFigure')
    def AddLine(self, *args, **kwargs): _unavailable('Sketch.AddLine')
    def AddLines(self, *args, **kwargs): _unavailable('Sketch.AddLines')
    def AddPoint(self, *args, **kwargs): _unavailable('Sketch.AddPoint')
    def AddPolygon(self, *args, **kwargs): _unavailable('Sketch.AddPolygon')
    def AddPolyhole(self, *args, **kwargs): _unavailable('Sketch.AddPolyhole')
    def AddPolyline(self, *args, **kwargs): _unavailable('Sketch.AddPolyline')
    def AddRectangle(self, *args, **kwargs): _unavailable('Sketch.AddRectangle')
    def CopyFrom(self, *args, **kwargs): _unavailable('Sketch.CopyFrom')
    def CrossSectionObject(self, *args, **kwargs): _unavailable('Sketch.CrossSectionObject')
    def ExportSVG(self, *args, **kwargs): _unavailable('Sketch.ExportSVG')
    def FromXml(self, *args, **kwargs): _unavailable('Sketch.FromXml')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Sketch.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Sketch.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Sketch.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Sketch.GetSelectionAssembly')
    def GetSurface(self, *args, **kwargs): _unavailable('Sketch.GetSurface')
    def GlobaltoPoint(self, *args, **kwargs): _unavailable('Sketch.GlobaltoPoint')
    def ImportSVG(self, *args, **kwargs): _unavailable('Sketch.ImportSVG')
    def LoadXml(self, *args, **kwargs): _unavailable('Sketch.LoadXml')
    def PathObject(self, *args, **kwargs): _unavailable('Sketch.PathObject')
    def PointtoGlobal(self, *args, **kwargs): _unavailable('Sketch.PointtoGlobal')
    def SavetoXml(self, *args, **kwargs): _unavailable('Sketch.SavetoXml')
    def SelectableObject(self, *args, **kwargs): _unavailable('Sketch.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Sketch.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Sketch.SetParentAssembly')
    def StartEditing(self, *args, **kwargs): _unavailable('Sketch.StartEditing')
    def StartFaceMapping(self, *args, **kwargs): _unavailable('Sketch.StartFaceMapping')
    def StartMapping(self, *args, **kwargs): _unavailable('Sketch.StartMapping')
    def StopEditing(self, *args, **kwargs): _unavailable('Sketch.StopEditing')
    def StopFaceMapping(self, *args, **kwargs): _unavailable('Sketch.StopFaceMapping')
    def StopMapping(self, *args, **kwargs): _unavailable('Sketch.StopMapping')
    def ToString(self, *args, **kwargs): _unavailable('Sketch.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Sketch.ToXml')
    def VertextoPoint(self, *args, **kwargs): _unavailable('Sketch.VertextoPoint')

class Sketch3D(object):
    AutomaticStartEndEditing = None
    _SelectionSession = None
    _Sketch = None
    Figures = None
    Name = None
    def AddArc(self, *args, **kwargs): _unavailable('Sketch3D.AddArc')
    def AddArcCenterStartEnd(self, *args, **kwargs): _unavailable('Sketch3D.AddArcCenterStartEnd')
    def AddBspline(self, *args, **kwargs): _unavailable('Sketch3D.AddBspline')
    def AddLine(self, *args, **kwargs): _unavailable('Sketch3D.AddLine')
    def AddLines(self, *args, **kwargs): _unavailable('Sketch3D.AddLines')
    def AddPoint(self, *args, **kwargs): _unavailable('Sketch3D.AddPoint')
    def AddPolyline(self, *args, **kwargs): _unavailable('Sketch3D.AddPolyline')
    def FromXml(self, *args, **kwargs): _unavailable('Sketch3D.FromXml')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Sketch3D.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Sketch3D.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Sketch3D.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Sketch3D.GetSelectionAssembly')
    def LoadXml(self, *args, **kwargs): _unavailable('Sketch3D.LoadXml')
    def PathObject(self, *args, **kwargs): _unavailable('Sketch3D.PathObject')
    def SavetoXml(self, *args, **kwargs): _unavailable('Sketch3D.SavetoXml')
    def SelectableObject(self, *args, **kwargs): _unavailable('Sketch3D.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Sketch3D.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Sketch3D.SetParentAssembly')
    def StartEditing(self, *args, **kwargs): _unavailable('Sketch3D.StartEditing')
    def StopEditing(self, *args, **kwargs): _unavailable('Sketch3D.StopEditing')
    def ToString(self, *args, **kwargs): _unavailable('Sketch3D.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Sketch3D.ToXml')

class Plane(object):
    _Plane = None
    _SelectionSession = None
    Name = None
    def ConstraintObject(self, *args, **kwargs): _unavailable('Plane.ConstraintObject')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Plane.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Plane.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Plane.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Plane.GetSelectionAssembly')
    def Hide(self, *args, **kwargs): _unavailable('Plane.Hide')
    def IsParallel(self, *args, **kwargs): _unavailable('Plane.IsParallel')
    def PlaneObject(self, *args, **kwargs): _unavailable('Plane.PlaneObject')
    def SelectableObject(self, *args, **kwargs): _unavailable('Plane.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Plane.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Plane.SetParentAssembly')
    def Show(self, *args, **kwargs): _unavailable('Plane.Show')
    def SurfaceObject(self, *args, **kwargs): _unavailable('Plane.SurfaceObject')
    def ToString(self, *args, **kwargs): _unavailable('Plane.ToString')

class Axis(object):
    _Axis = None
    _SelectionSession = None
    Name = None
    def AxisObject(self, *args, **kwargs): _unavailable('Axis.AxisObject')
    def ConstraintObject(self, *args, **kwargs): _unavailable('Axis.ConstraintObject')
    def GetGeometry(self, *args, **kwargs): _unavailable('Axis.GetGeometry')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Axis.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Axis.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Axis.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Axis.GetSelectionAssembly')
    def Hide(self, *args, **kwargs): _unavailable('Axis.Hide')
    def SelectableObject(self, *args, **kwargs): _unavailable('Axis.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Axis.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Axis.SetParentAssembly')
    def Show(self, *args, **kwargs): _unavailable('Axis.Show')
    def ToString(self, *args, **kwargs): _unavailable('Axis.ToString')

class Point(object):
    _Point = None
    _SelectionSession = None
    Name = None
    X = None
    Y = None
    Z = None
    def ConstraintObject(self, *args, **kwargs): _unavailable('Point.ConstraintObject')
    def CrossSectionObject(self, *args, **kwargs): _unavailable('Point.CrossSectionObject')
    def GetCoordinates(self, *args, **kwargs): _unavailable('Point.GetCoordinates')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Point.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Point.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Point.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Point.GetSelectionAssembly')
    def Hide(self, *args, **kwargs): _unavailable('Point.Hide')
    def PointObject(self, *args, **kwargs): _unavailable('Point.PointObject')
    def SelectableObject(self, *args, **kwargs): _unavailable('Point.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Point.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Point.SetParentAssembly')
    def Show(self, *args, **kwargs): _unavailable('Point.Show')
    def ToString(self, *args, **kwargs): _unavailable('Point.ToString')

class Face(object):
    _SelectionSession = None
    _Session = None
    AdjoiningFaces = None
    Coedges = None
    Edges = None
    Name = None
    PartnerCoedges = None
    Vertices = None
    _Face = None
    def ChamferableObject(self, *args, **kwargs): _unavailable('Face.ChamferableObject')
    def ConstraintObject(self, *args, **kwargs): _unavailable('Face.ConstraintObject')
    def CrossSectionObject(self, *args, **kwargs): _unavailable('Face.CrossSectionObject')
    def DistanceTo(self, *args, **kwargs): _unavailable('Face.DistanceTo')
    def FilletableObject(self, *args, **kwargs): _unavailable('Face.FilletableObject')
    def GetAdjoiningFaces(self, *args, **kwargs): _unavailable('Face.GetAdjoiningFaces')
    def GetArea(self, *args, **kwargs): _unavailable('Face.GetArea')
    def GetEdges(self, *args, **kwargs): _unavailable('Face.GetEdges')
    def GetNormal(self, *args, **kwargs): _unavailable('Face.GetNormal')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Face.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Face.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Face.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Face.GetSelectionAssembly')
    def GetVertices(self, *args, **kwargs): _unavailable('Face.GetVertices')
    def IsParallel(self, *args, **kwargs): _unavailable('Face.IsParallel')
    def IsRectangle(self, *args, **kwargs): _unavailable('Face.IsRectangle')
    def PlaneObject(self, *args, **kwargs): _unavailable('Face.PlaneObject')
    def SelectableObject(self, *args, **kwargs): _unavailable('Face.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Face.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Face.SetParentAssembly')
    def SurfaceObject(self, *args, **kwargs): _unavailable('Face.SurfaceObject')
    def ToString(self, *args, **kwargs): _unavailable('Face.ToString')

class Edge(object):
    _SelectionSession = None
    _Session = None
    Diameter = None
    Length = None
    Name = None
    Vertices = None
    _Edge = None
    def AxisObject(self, *args, **kwargs): _unavailable('Edge.AxisObject')
    def ChamferableObject(self, *args, **kwargs): _unavailable('Edge.ChamferableObject')
    def ConstraintObject(self, *args, **kwargs): _unavailable('Edge.ConstraintObject')
    def FilletableObject(self, *args, **kwargs): _unavailable('Edge.FilletableObject')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Edge.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Edge.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Edge.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Edge.GetSelectionAssembly')
    def GetVertices(self, *args, **kwargs): _unavailable('Edge.GetVertices')
    def PathObject(self, *args, **kwargs): _unavailable('Edge.PathObject')
    def SelectableObject(self, *args, **kwargs): _unavailable('Edge.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Edge.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Edge.SetParentAssembly')
    def ToString(self, *args, **kwargs): _unavailable('Edge.ToString')

class Vertex(object):
    _SelectionSession = None
    _Session = None
    Name = None
    X = None
    Y = None
    Z = None
    _Vertex = None
    def ChamferableObject(self, *args, **kwargs): _unavailable('Vertex.ChamferableObject')
    def ConstraintObject(self, *args, **kwargs): _unavailable('Vertex.ConstraintObject')
    def GetOccurrence(self, *args, **kwargs): _unavailable('Vertex.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('Vertex.GetParentAssembly')
    def GetPart(self, *args, **kwargs): _unavailable('Vertex.GetPart')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('Vertex.GetSelectionAssembly')
    def PointObject(self, *args, **kwargs): _unavailable('Vertex.PointObject')
    def SelectableObject(self, *args, **kwargs): _unavailable('Vertex.SelectableObject')
    def SetOccurrence(self, *args, **kwargs): _unavailable('Vertex.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('Vertex.SetParentAssembly')
    def ToString(self, *args, **kwargs): _unavailable('Vertex.ToString')

class Feature(object):
    _Feature = None
    Name = None
    def GetColor(self, *args, **kwargs): _unavailable('Feature.GetColor')
    def SetColor(self, *args, **kwargs): _unavailable('Feature.SetColor')
    def ToString(self, *args, **kwargs): _unavailable('Feature.ToString')

class Configuration(object):
    _Configuration = None
    _Occurrence = None
    _Session = None
    IsActive = None
    Name = None
    def Activate(self, *args, **kwargs): _unavailable('Configuration.Activate')
    def LockAll(self, *args, **kwargs): _unavailable('Configuration.LockAll')
    def SetLocks(self, *args, **kwargs): _unavailable('Configuration.SetLocks')
    def ToString(self, *args, **kwargs): _unavailable('Configuration.ToString')
    def UnlockAll(self, *args, **kwargs): _unavailable('Configuration.UnlockAll')

class Parameter(object):
    _Parameter = None
    _Session = None
    Comment = None
    Equation = None
    ExcelCell = None
    ExcelSheet = None
    ExcelWorkbook = None
    Name = None
    RawValue = None
    Type = None
    Units = None
    Value = None
    def AttachToExcel(self, *args, **kwargs): _unavailable('Parameter.AttachToExcel')
    def ToString(self, *args, **kwargs): _unavailable('Parameter.ToString')

class Windows(object):
    ProductName = None
    def CloseForm(self, *args, **kwargs): _unavailable('Windows.CloseForm')
    def DisableInput(self, *args, **kwargs): _unavailable('Windows.DisableInput')
    def EnableInput(self, *args, **kwargs): _unavailable('Windows.EnableInput')
    def ErrorDialog(self, *args, **kwargs): _unavailable('Windows.ErrorDialog')
    def GetDisplayedForm(self, *args, **kwargs): _unavailable('Windows.GetDisplayedForm')
    def GetInputValue(self, *args, **kwargs): _unavailable('Windows.GetInputValue')
    def InfoDialog(self, *args, **kwargs): _unavailable('Windows.InfoDialog')
    def OpenFileDialog(self, *args, **kwargs): _unavailable('Windows.OpenFileDialog')
    def OptionsDialog(self, *args, **kwargs): _unavailable('Windows.OptionsDialog')
    def QuestionDialog(self, *args, **kwargs): _unavailable('Windows.QuestionDialog')
    def SaveFileDialog(self, *args, **kwargs): _unavailable('Windows.SaveFileDialog')
    def SelectFolderDialog(self, *args, **kwargs): _unavailable('Windows.SelectFolderDialog')
    def SetInputValue(self, *args, **kwargs): _unavailable('Windows.SetInputValue')
    def SetStringList(self, *args, **kwargs): _unavailable('Windows.SetStringList')
    def UtilityDialog(self, *args, **kwargs): _unavailable('Windows.UtilityDialog')

class AssembledPart(object):
    _SelectionSession = None
    ConfigurationList = None
    Configurations = None
    Edges = None
    Faces = None
    Name = None
    def AddPoint(self, *args, **kwargs): _unavailable('AssembledPart.AddPoint')
    def AddPointFromCircularEdge(self, *args, **kwargs): _unavailable('AssembledPart.AddPointFromCircularEdge')
    def AddPointFromToroidalFace(self, *args, **kwargs): _unavailable('AssembledPart.AddPointFromToroidalFace')
    def AssemblyPointtoPartPoint(self, *args, **kwargs): _unavailable('AssembledPart.AssemblyPointtoPartPoint')
    def GetAssembledPath(self, *args, **kwargs): _unavailable('AssembledPart.GetAssembledPath')
    def GetAssembly(self, *args, **kwargs): _unavailable('AssembledPart.GetAssembly')
    def GetAssemblyBoundingBox(self, *args, **kwargs): _unavailable('AssembledPart.GetAssemblyBoundingBox')
    def GetAssemblyVertices(self, *args, **kwargs): _unavailable('AssembledPart.GetAssemblyVertices')
    def GetConfiguration(self, *args, **kwargs): _unavailable('AssembledPart.GetConfiguration')
    def GetEdge(self, *args, **kwargs): _unavailable('AssembledPart.GetEdge')
    def GetEdges(self, *args, **kwargs): _unavailable('AssembledPart.GetEdges')
    def GetFace(self, *args, **kwargs): _unavailable('AssembledPart.GetFace')
    def GetFaces(self, *args, **kwargs): _unavailable('AssembledPart.GetFaces')
    def GetMappedOccurrence(self, *args, **kwargs): _unavailable('AssembledPart.GetMappedOccurrence')
    def GetOccurrence(self, *args, **kwargs): _unavailable('AssembledPart.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('AssembledPart.GetParentAssembly')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('AssembledPart.GetSelectionAssembly')
    def GetTransformation(self, *args, **kwargs): _unavailable('AssembledPart.GetTransformation')
    def PartPointtoAssemblyPoint(self, *args, **kwargs): _unavailable('AssembledPart.PartPointtoAssemblyPoint')
    def SetOccurrence(self, *args, **kwargs): _unavailable('AssembledPart.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('AssembledPart.SetParentAssembly')
    def ToString(self, *args, **kwargs): _unavailable('AssembledPart.ToString')

class AssembledSubAssembly(object):
    _SelectionSession = None
    ConfigurationList = None
    Configurations = None
    Name = None
    def GetAssembledPath(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetAssembledPath')
    def GetConfiguration(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetConfiguration')
    def GetMappedOccurrence(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetMappedOccurrence')
    def GetOccurrence(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetOccurrence')
    def GetParentAssembly(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetParentAssembly')
    def GetSelectionAssembly(self, *args, **kwargs): _unavailable('AssembledSubAssembly.GetSelectionAssembly')
    def SetOccurrence(self, *args, **kwargs): _unavailable('AssembledSubAssembly.SetOccurrence')
    def SetParentAssembly(self, *args, **kwargs): _unavailable('AssembledSubAssembly.SetParentAssembly')
    def ToString(self, *args, **kwargs): _unavailable('AssembledSubAssembly.ToString')

class Bspline(object):
    ControlPoints = None
    IsReference = None
    KnotVectors = None
    Length = None
    Order = None
    Weights = None
    def FigureObject(self, *args, **kwargs): _unavailable('Bspline.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('Bspline.FromXml')
    def GetNormalAt(self, *args, **kwargs): _unavailable('Bspline.GetNormalAt')
    def GetPointAt(self, *args, **kwargs): _unavailable('Bspline.GetPointAt')
    def GetX(self, *args, **kwargs): _unavailable('Bspline.GetX')
    def GetY(self, *args, **kwargs): _unavailable('Bspline.GetY')
    def SetInstance(self, *args, **kwargs): _unavailable('Bspline.SetInstance')
    def Subdivide(self, *args, **kwargs): _unavailable('Bspline.Subdivide')
    def ToString(self, *args, **kwargs): _unavailable('Bspline.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Bspline.ToXml')

class Bspline3D(object):
    ControlPoints = None
    IsReference = None
    KnotVectors = None
    Length = None
    Order = None
    Weights = None
    def FromXml(self, *args, **kwargs): _unavailable('Bspline3D.FromXml')
    def GetNormalAt(self, *args, **kwargs): _unavailable('Bspline3D.GetNormalAt')
    def GetPointAt(self, *args, **kwargs): _unavailable('Bspline3D.GetPointAt')
    def GetX(self, *args, **kwargs): _unavailable('Bspline3D.GetX')
    def GetY(self, *args, **kwargs): _unavailable('Bspline3D.GetY')
    def GetZ(self, *args, **kwargs): _unavailable('Bspline3D.GetZ')
    def Subdivide(self, *args, **kwargs): _unavailable('Bspline3D.Subdivide')
    def SubdivideGetNormals(self, *args, **kwargs): _unavailable('Bspline3D.SubdivideGetNormals')
    def ToString(self, *args, **kwargs): _unavailable('Bspline3D.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Bspline3D.ToXml')

class CSharp(object):
    class WriteHandler(object):
        def BeginInvoke(self, *args, **kwargs): _unavailable('WriteHandler.BeginInvoke')
        def EndInvoke(self, *args, **kwargs): _unavailable('WriteHandler.EndInvoke')
        def Invoke(self, *args, **kwargs): _unavailable('WriteHandler.Invoke')

    class WriteLineHandler(object):
        def BeginInvoke(self, *args, **kwargs): _unavailable('WriteLineHandler.BeginInvoke')
        def EndInvoke(self, *args, **kwargs): _unavailable('WriteLineHandler.EndInvoke')
        def Invoke(self, *args, **kwargs): _unavailable('WriteLineHandler.Invoke')

    def Compile(self, *args, **kwargs): _unavailable('CSharp.Compile')
    def CompileAndRun(self, *args, **kwargs): _unavailable('CSharp.CompileAndRun')
    def Run(self, *args, **kwargs): _unavailable('CSharp.Run')

class Circle(object):
    Center = None
    CenterPoint = None
    IsReference = None
    Length = None
    Radius = None
    def FigureObject(self, *args, **kwargs): _unavailable('Circle.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('Circle.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('Circle.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('Circle.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Circle.ToXml')

class CircularArc(object):
    class ArcType(object):
        CenterStartAngle = None
        CenterStartEnd = None
        value__ = None

    Angle = None
    Center = None
    CenterPoint = None
    End = None
    EndPoint = None
    IsReference = None
    Radius = None
    Start = None
    StartPoint = None
    Type = None
    def FigureObject(self, *args, **kwargs): _unavailable('CircularArc.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('CircularArc.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('CircularArc.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('CircularArc.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('CircularArc.ToXml')

class CircularArc3D(object):
    class ArcType(object):
        CenterStartAngle = None
        CenterStartEnd = None
        value__ = None

    Angle = None
    Center = None
    EndPoint = None
    IsReference = None
    Radius = None
    StartPoint = None
    Type = None
    def FromXml(self, *args, **kwargs): _unavailable('CircularArc3D.FromXml')
    def ToString(self, *args, **kwargs): _unavailable('CircularArc3D.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('CircularArc3D.ToXml')

class Ellipse(object):
    Center = None
    CenterPoint = None
    IsReference = None
    MajorAxisAngle = None
    MinorMajorRatio = None
    Radius = None
    def FigureObject(self, *args, **kwargs): _unavailable('Ellipse.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('Ellipse.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('Ellipse.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('Ellipse.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Ellipse.ToXml')

class EllipticalArc(object):
    Center = None
    CenterPoint = None
    End = None
    EndPoint = None
    IsReference = None
    MajorAxisAngle = None
    MinorMajorRatio = None
    Radius = None
    Start = None
    StartPoint = None
    def FigureObject(self, *args, **kwargs): _unavailable('EllipticalArc.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('EllipticalArc.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('EllipticalArc.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('EllipticalArc.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('EllipticalArc.ToXml')

class GearSketch(object):
    CenterX = None
    CenterY = None
    DiametralPitch = None
    NumberofTeeth = None
    PitchDiameter = None
    PressureAngle = None
    def ToString(self, *args, **kwargs): _unavailable('GearSketch.ToString')

class GlobalParameters(object):
    _GlobalParameters = None
    ConfigurationList = None
    Configurations = None
    Name = None
    ParameterList = None
    Parameters = None
    def AddConfiguration(self, *args, **kwargs): _unavailable('GlobalParameters.AddConfiguration')
    def AddParameter(self, *args, **kwargs): _unavailable('GlobalParameters.AddParameter')
    def Close(self, *args, **kwargs): _unavailable('GlobalParameters.Close')
    def GetActiveConfiguration(self, *args, **kwargs): _unavailable('GlobalParameters.GetActiveConfiguration')
    def GetConfiguration(self, *args, **kwargs): _unavailable('GlobalParameters.GetConfiguration')
    def GetParameter(self, *args, **kwargs): _unavailable('GlobalParameters.GetParameter')
    def Save(self, *args, **kwargs): _unavailable('GlobalParameters.Save')
    def SaveAs(self, *args, **kwargs): _unavailable('GlobalParameters.SaveAs')
    def ToString(self, *args, **kwargs): _unavailable('GlobalParameters.ToString')

class GuideCurveTypes(object):
    Global = None
    Local = None
    Tangent = None
    value__ = None

class Line(object):
    End = None
    EndPoint = None
    IsReference = None
    Length = None
    Start = None
    StartPoint = None
    def FigureObject(self, *args, **kwargs): _unavailable('Line.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('Line.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('Line.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('Line.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Line.ToXml')

class Line3D(object):
    End = None
    EndPoint = None
    IsReference = None
    Length = None
    Start = None
    StartPoint = None
    def FromXml(self, *args, **kwargs): _unavailable('Line3D.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('Line3D.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('Line3D.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('Line3D.ToXml')

class LockTypes(object):
    All = None
    HideNewAnnotations = None
    HideNewDesignGeometry = None
    HideNewInclusions = None
    HideNewSketches = None
    LockActiveSectionView = None
    LockColorProperties = None
    LockComponentConfig = None
    LockParameterValues = None
    LockPropertyValues = None
    None_ = None
    SuppressNewComponents = None
    SuppressNewConstraints = None
    SuppressNewFeatures = None
    value__ = None

class Material(object):
    ABS = None
    PLA = None

class ParameterTypes(object):
    Angle = None
    Count = None
    Distance = None
    Scale = None
    value__ = None

class ParameterUnits(object):
    Centimeters = None
    Degrees = None
    DegreesMinutes = None
    DegreesMinutesSeconds = None
    Feet = None
    FeetInches = None
    Grams = None
    Inches = None
    Kilograms = None
    Meters = None
    Millimeters = None
    Pounds = None
    Radians = None
    Unitless = None
    value__ = None

class Polyline(object):
    Points = None
    def AddArc(self, *args, **kwargs): _unavailable('Polyline.AddArc')
    def AddCircle(self, *args, **kwargs): _unavailable('Polyline.AddCircle')
    def AddPoint(self, *args, **kwargs): _unavailable('Polyline.AddPoint')
    def AddPolyline(self, *args, **kwargs): _unavailable('Polyline.AddPolyline')
    def Clone(self, *args, **kwargs): _unavailable('Polyline.Clone')
    def FindIntersection(self, *args, **kwargs): _unavailable('Polyline.FindIntersection')
    def FindIntersectionWithCircle(self, *args, **kwargs): _unavailable('Polyline.FindIntersectionWithCircle')
    def InsertPoint(self, *args, **kwargs): _unavailable('Polyline.InsertPoint')
    def IsPointOnLine(self, *args, **kwargs): _unavailable('Polyline.IsPointOnLine')
    def Join(self, *args, **kwargs): _unavailable('Polyline.Join')
    def Offset(self, *args, **kwargs): _unavailable('Polyline.Offset')
    def RemoveDuplicates(self, *args, **kwargs): _unavailable('Polyline.RemoveDuplicates')
    def RotateZ(self, *args, **kwargs): _unavailable('Polyline.RotateZ')
    def SplitAtPoint(self, *args, **kwargs): _unavailable('Polyline.SplitAtPoint')

class Polyline3D(object):
    Points = None
    def AddPoint(self, *args, **kwargs): _unavailable('Polyline3D.AddPoint')
    def AddPolyline(self, *args, **kwargs): _unavailable('Polyline3D.AddPolyline')
    def Clone(self, *args, **kwargs): _unavailable('Polyline3D.Clone')
    def InsertPoint(self, *args, **kwargs): _unavailable('Polyline3D.InsertPoint')
    def IsPointOnLine(self, *args, **kwargs): _unavailable('Polyline3D.IsPointOnLine')
    def Join(self, *args, **kwargs): _unavailable('Polyline3D.Join')
    def Offset(self, *args, **kwargs): _unavailable('Polyline3D.Offset')
    def RemoveDuplicates(self, *args, **kwargs): _unavailable('Polyline3D.RemoveDuplicates')
    def SplitAtPoint(self, *args, **kwargs): _unavailable('Polyline3D.SplitAtPoint')

class PolylinePoint(object):
    X = None
    Y = None
    def CrossProduct(self, *args, **kwargs): _unavailable('PolylinePoint.CrossProduct')
    def Equals(self, *args, **kwargs): _unavailable('PolylinePoint.Equals')
    def GetHashCode(self, *args, **kwargs): _unavailable('PolylinePoint.GetHashCode')
    def Offset(self, *args, **kwargs): _unavailable('PolylinePoint.Offset')
    def RotateZ(self, *args, **kwargs): _unavailable('PolylinePoint.RotateZ')
    def Scale(self, *args, **kwargs): _unavailable('PolylinePoint.Scale')
    def ToString(self, *args, **kwargs): _unavailable('PolylinePoint.ToString')

class PolylinePoint3D(object):
    X = None
    Y = None
    Z = None
    def Equals(self, *args, **kwargs): _unavailable('PolylinePoint3D.Equals')
    def GetHashCode(self, *args, **kwargs): _unavailable('PolylinePoint3D.GetHashCode')
    def Offset(self, *args, **kwargs): _unavailable('PolylinePoint3D.Offset')
    def Scale(self, *args, **kwargs): _unavailable('PolylinePoint3D.Scale')
    def ToString(self, *args, **kwargs): _unavailable('PolylinePoint3D.ToString')

class SketchPoint(object):
    IsReference = None
    Point = None
    X = None
    Y = None
    def FigureObject(self, *args, **kwargs): _unavailable('SketchPoint.FigureObject')
    def FromXml(self, *args, **kwargs): _unavailable('SketchPoint.FromXml')
    def SetInstance(self, *args, **kwargs): _unavailable('SketchPoint.SetInstance')
    def ToString(self, *args, **kwargs): _unavailable('SketchPoint.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('SketchPoint.ToXml')

class SketchPoint3D(object):
    IsReference = None
    X = None
    Y = None
    Z = None
    def FromXml(self, *args, **kwargs): _unavailable('SketchPoint3D.FromXml')
    def ToString(self, *args, **kwargs): _unavailable('SketchPoint3D.ToString')
    def ToXml(self, *args, **kwargs): _unavailable('SketchPoint3D.ToXml')

class ThreeD(object):
    class RotationDirections(object):
        X = None
        Y = None
        Z = None
        value__ = None

    def CreateRotation(self, *args, **kwargs): _unavailable('ThreeD.CreateRotation')
    def CreateTransformation(self, *args, **kwargs): _unavailable('ThreeD.CreateTransformation')
    def CreateTranslation(self, *args, **kwargs): _unavailable('ThreeD.CreateTranslation')
    def DecomposeTransformation(self, *args, **kwargs): _unavailable('ThreeD.DecomposeTransformation')
    def GetMatrixFromTransformation(self, *args, **kwargs): _unavailable('ThreeD.GetMatrixFromTransformation')
    def GetPerpendicularVector(self, *args, **kwargs): _unavailable('ThreeD.GetPerpendicularVector')
    def TransformPoint(self, *args, **kwargs): _unavailable('ThreeD.TransformPoint')
    def TransformPointUsingVectors(self, *args, **kwargs): _unavailable('ThreeD.TransformPointUsingVectors')
    def TransformVector(self, *args, **kwargs): _unavailable('ThreeD.TransformVector')
    def VectorTransform(self, *args, **kwargs): _unavailable('ThreeD.VectorTransform')

class ThumbnailOptions(object):
    BiggerSizeOk = None
    IconOnly = None
    InCacheOnly = None
    InMemoryOnly = None
    None_ = None
    ThumbnailOnly = None
    value__ = None

class Trace(object):
    class LineTypes(object):
        API = None
        Internal = None
        ScriptFunc = None
        value__ = None

    def Output(self, *args, **kwargs): _unavailable('Trace.Output')
    def OutputLine(self, *args, **kwargs): _unavailable('Trace.OutputLine')
    def Start(self, *args, **kwargs): _unavailable('Trace.Start')
    def Stop(self, *args, **kwargs): _unavailable('Trace.Stop')

class TwoD(object):
    def GetPerpendicularVector(self, *args, **kwargs): _unavailable('TwoD.GetPerpendicularVector')
    def IsPointInsidePolygon(self, *args, **kwargs): _unavailable('TwoD.IsPointInsidePolygon')
    def NormalizeVector(self, *args, **kwargs): _unavailable('TwoD.NormalizeVector')
    def RotatePoint(self, *args, **kwargs): _unavailable('TwoD.RotatePoint')
    def TranslatePoint(self, *args, **kwargs): _unavailable('TwoD.TranslatePoint')
    def _RotatePoint(self, *args, **kwargs): _unavailable('TwoD._RotatePoint')

class UnitTypes(object):
    Centimeters = None
    Inches = None
    Millimeters = None
    value__ = None

class Units(object):
    Current = None
    def FromADUnitType(self, *args, **kwargs): _unavailable('Units.FromADUnitType')
    def FromADUnits(self, *args, **kwargs): _unavailable('Units.FromADUnits')
    def FromInches(self, *args, **kwargs): _unavailable('Units.FromInches')
    def FromMillimeters(self, *args, **kwargs): _unavailable('Units.FromMillimeters')
    def FromTeethPerInch(self, *args, **kwargs): _unavailable('Units.FromTeethPerInch')
    def ToADUnits(self, *args, **kwargs): _unavailable('Units.ToADUnits')
    def ToInches(self, *args, **kwargs): _unavailable('Units.ToInches')
    def ToMillimeters(self, *args, **kwargs): _unavailable('Units.ToMillimeters')
    def ToTeethPerInch(self, *args, **kwargs): _unavailable('Units.ToTeethPerInch')

class WindowsInputTypes(object):
    Assembly = None
    Axes = None
    Axis = None
    Boolean = None
    Edge = None
    Edges = None
    Face = None
    Faces = None
    File = None
    Folder = None
    Image = None
    Integer = None
    Label = None
    Part = None
    Plane = None
    Planes = None
    Point = None
    Points = None
    Real = None
    SaveFile = None
    Sketch = None
    Sketch3D = None
    Sketches = None
    String = None
    StringList = None
    Url = None
    Vertex = None
    Vertices = None
    value__ = None

def CurrentPart(*args, **kwargs): _unavailable('CurrentPart')
def CurrentAssembly(*args, **kwargs): _unavailable('CurrentAssembly')
def CurrentParts(*args, **kwargs): _unavailable('CurrentParts')
def CurrentAssemblies(*args, **kwargs): _unavailable('CurrentAssemblies')
