class AssembledPart:
    """Generated stub class"""
    def GetMappedOccurrence(self, AlibreX.IADAssemblySession):
        """Generated stub method"""
        pass
    def GetConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def PartPointtoAssemblyPoint(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AssemblyPointtoPartPoint(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def GetFace(self, System.String):
        """Generated stub method"""
        pass
    def GetEdge(self, System.String):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPoint,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IAxis):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPlane,AlibreScript.API.IPlane,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPlane,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.Edge,System.Double):
        """Generated stub method"""
        pass
    def AddPointFromCircularEdge(self, System.String,AlibreScript.API.Edge):
        """Generated stub method"""
        pass
    def AddPointFromToroidalFace(self, System.String,AlibreScript.API.Face):
        """Generated stub method"""
        pass
class Part:
    """Generated stub class"""
    def RemovePoint(self, AlibreScript.API.Point):
        """Generated stub method"""
        pass
    def RemovePlane(self, AlibreScript.API.Plane):
        """Generated stub method"""
        pass
    def RemoveSketch(self, System.String):
        """Generated stub method"""
        pass
    def RemoveSketch(self, AlibreScript.API.Sketch):
        """Generated stub method"""
        pass
    def Add3DSketch(self, System.String):
        """Generated stub method"""
        pass
    def AddGear(self, System.String,System.Double,System.Int32,System.Double,System.Double,System.Boolean,System.Double,System.Double,System.Int32,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearNP(self, System.String,System.Int32,System.Double,System.Double,System.Double,System.Double,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearNP(self, System.String,System.Int32,System.Double,System.Double,System.Double,System.Double,System.Boolean,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearDP(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearDP(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearDN(self, System.String,System.Double,System.Int32,System.Double,System.Double,System.Double,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddGearDN(self, System.String,System.Double,System.Int32,System.Double,System.Double,System.Double,System.Boolean,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,AlibreScript.API.ISketchSurface,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,AlibreScript.API.Point,AlibreScript.API.Point):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,AlibreScript.API.Face):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.Point):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoints(self, System.String,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddExtrudeBoss(self, System.String,AlibreScript.API.Sketch,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddExtrudeBoss(self, System.String,AlibreScript.API.Sketch,System.Double,System.Boolean,AlibreScript.API.Part.EndCondition,AlibreScript.API.ISketchSurface,System.Double,AlibreScript.API.Part.DirectionType,AlibreScript.API.ISweepPath,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddExtrudeCut(self, System.String,AlibreScript.API.Sketch,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddExtrudeCut(self, System.String,AlibreScript.API.Sketch,System.Double,System.Boolean,AlibreScript.API.Part.EndCondition,AlibreScript.API.ISketchSurface,System.Double,AlibreScript.API.Part.DirectionType,AlibreScript.API.ISweepPath,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddRevolveBoss(self, System.String,AlibreScript.API.Sketch,AlibreScript.API.Axis,System.Double):
        """Generated stub method"""
        pass
    def AddRevolveCut(self, System.String,AlibreScript.API.Sketch,AlibreScript.API.Axis,System.Double):
        """Generated stub method"""
        pass
    def AddLoftBoss(self, System.String,IronPython.Runtime.List,System.Boolean,System.Boolean,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def AddLoftBoss(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List,AlibreScript.API.GuideCurveTypes,System.Boolean,System.Boolean,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def AddLoftCut(self, System.String,IronPython.Runtime.List,System.Boolean,System.Boolean,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def AddLoftCut(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List,AlibreScript.API.GuideCurveTypes,System.Boolean,System.Boolean,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def AddSweepBoss(self, System.String,AlibreScript.API.Sketch,AlibreScript.API.ISweepPath,System.Boolean,AlibreScript.API.Part.EndCondition,AlibreScript.API.ISketchSurface,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddSweepCut(self, System.String,AlibreScript.API.Sketch,AlibreScript.API.ISweepPath,System.Boolean,AlibreScript.API.Part.EndCondition,AlibreScript.API.ISketchSurface,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddFillet(self, System.String,AlibreScript.API.IFilletable,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddFillet(self, System.String,IronPython.Runtime.List,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddFillet(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def Scale(self, System.String,System.Boolean,System.Double):
        """Generated stub method"""
        pass
    def NonUniformScale(self, System.String,System.Boolean,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddChamfer(self, System.String,AlibreScript.API.IChamferable,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddChamfer(self, System.String,IronPython.Runtime.List,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddChamfer(self, System.String,AlibreScript.API.IChamferable,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddChamfer(self, System.String,IronPython.Runtime.List,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddChamferAngle(self, System.String,AlibreScript.API.IChamferable,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddChamferAngle(self, System.String,IronPython.Runtime.List,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddVertexChamfer(self, System.String,AlibreScript.API.Vertex,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddVertexChamfer(self, System.String,IronPython.Runtime.List,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def Save(self, System.String):
        """Generated stub method"""
        pass
    def SaveAs(self, System.String,System.String):
        """Generated stub method"""
        pass
    def ExportSTL(self, System.String):
        """Generated stub method"""
        pass
    def ExportRotatedSTL(self, System.String,AlibreScript.API.Face,System.Boolean,System.Boolean,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def ExportSTEP203(self, System.String):
        """Generated stub method"""
        pass
    def ExportSTEP214(self, System.String):
        """Generated stub method"""
        pass
    def ExportIGES(self, System.String):
        """Generated stub method"""
        pass
    def ExportSAT(self, System.String,System.Int32,System.Boolean):
        """Generated stub method"""
        pass
    def ExportBIP(self, System.String):
        """Generated stub method"""
        pass
    def SetColor(self, System.Byte,System.Byte,System.Byte):
        """Generated stub method"""
        pass
    def SaveSnapshot(self, System.String,System.Int32,System.Int32,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def SaveThumbnail(self, System.String,System.Int32,System.Int32):
        """Generated stub method"""
        pass
    def Select(self, AlibreScript.API.ISelectableGeometry):
        """Generated stub method"""
        pass
    def Select(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def SetUserData(self, System.String,IronPython.Runtime.PythonDictionary):
        """Generated stub method"""
        pass
    def GetUserData(self, System.String):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPoint,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IAxis):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPlane,AlibreScript.API.IPlane,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPlane,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.Edge,System.Double):
        """Generated stub method"""
        pass
    def AddPointFromCircularEdge(self, System.String,AlibreScript.API.Edge):
        """Generated stub method"""
        pass
    def AddPointFromToroidalFace(self, System.String,AlibreScript.API.Face):
        """Generated stub method"""
        pass
    def GetFeature(self, System.String):
        """Generated stub method"""
        pass
    def RemoveFeature(self, System.String):
        """Generated stub method"""
        pass
    def RemoveFeature(self, AlibreScript.API.Feature):
        """Generated stub method"""
        pass
    def SuppressFeature(self, System.String):
        """Generated stub method"""
        pass
    def SuppressFeature(self, AlibreScript.API.Feature):
        """Generated stub method"""
        pass
    def UnsuppressFeature(self, System.String):
        """Generated stub method"""
        pass
    def UnsuppressFeature(self, AlibreScript.API.Feature):
        """Generated stub method"""
        pass
    def HideFeature(self, System.String):
        """Generated stub method"""
        pass
    def HideFeature(self, AlibreScript.API.Feature):
        """Generated stub method"""
        pass
    def ShowFeature(self, System.String):
        """Generated stub method"""
        pass
    def ShowFeature(self, AlibreScript.API.Feature):
        """Generated stub method"""
        pass
    def GetPlane(self, System.String):
        """Generated stub method"""
        pass
    def GetAxis(self, System.String):
        """Generated stub method"""
        pass
    def GetPoint(self, System.String):
        """Generated stub method"""
        pass
    def GetSketch(self, System.String):
        """Generated stub method"""
        pass
    def Get3DSketch(self, System.String):
        """Generated stub method"""
        pass
    def GetFace(self, System.String):
        """Generated stub method"""
        pass
    def GetEdge(self, System.String):
        """Generated stub method"""
        pass
    def GetVertex(self, System.String):
        """Generated stub method"""
        pass
    def GetParameter(self, System.String):
        """Generated stub method"""
        pass
    def GetCustomProperty(self, System.String):
        """Generated stub method"""
        pass
    def SetCustomProperty(self, System.String,System.String):
        """Generated stub method"""
        pass
    def GetConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,AlibreScript.API.ISketchSurface,System.Double):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,AlibreScript.API.Axis,AlibreScript.API.Point):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,AlibreScript.API.ISketchSurface,AlibreScript.API.Axis,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,AlibreScript.API.ParameterUnits,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String,System.String):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddSketch(self, System.String,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.String,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,AlibreScript.API.Part.FileTypes):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,AlibreScript.API.Part.FileTypes,System.Boolean):
        """Generated stub method"""
        pass
class AssembledSubAssembly:
    """Generated stub class"""
    def GetMappedOccurrence(self, AlibreX.IADAssemblySession):
        """Generated stub method"""
        pass
    def GetConfiguration(self, System.String):
        """Generated stub method"""
        pass
class Assembly:
    """Generated stub class"""
    def AddSubAssembly(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddMateConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable):
        """Generated stub method"""
        pass
    def AddMateConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddMateConstraint2(self, System.Double,System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String,AlibreScript.API.Assembly.ConstraintBoundsType):
        """Generated stub method"""
        pass
    def AddFastenerConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddFastenerConstraint2(self, System.Double,System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String,AlibreScript.API.Assembly.ConstraintBoundsType):
        """Generated stub method"""
        pass
    def AddAlignConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable):
        """Generated stub method"""
        pass
    def AddAlignConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddAlignConstraint2(self, System.Double,System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String,AlibreScript.API.Assembly.ConstraintBoundsType):
        """Generated stub method"""
        pass
    def AddOrientConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable):
        """Generated stub method"""
        pass
    def AddOrientConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddAngleConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable):
        """Generated stub method"""
        pass
    def AddAngleConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddAngleConstraint2(self, System.Double,System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String,AlibreScript.API.Assembly.ConstraintBoundsType):
        """Generated stub method"""
        pass
    def AddGearConstraint(self, System.Double,System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddRackAndPinionConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddScrewConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def AddTangentConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean):
        """Generated stub method"""
        pass
    def AddTangentConstraint(self, System.Double,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,AlibreScript.API.IAssembled,AlibreScript.API.IConstrainable,System.Boolean,System.Boolean,System.String):
        """Generated stub method"""
        pass
    def CreateUniqueName(self, System.String):
        """Generated stub method"""
        pass
    def ExportSTL(self, System.String):
        """Generated stub method"""
        pass
    def ExportSTEP203(self, System.String):
        """Generated stub method"""
        pass
    def ExportSTEP214(self, System.String):
        """Generated stub method"""
        pass
    def ExportIGES(self, System.String):
        """Generated stub method"""
        pass
    def ExportSAT(self, System.String,System.Int32,System.Boolean):
        """Generated stub method"""
        pass
    def ExportBIP(self, System.String):
        """Generated stub method"""
        pass
    def SetUserData(self, System.String,IronPython.Runtime.PythonDictionary):
        """Generated stub method"""
        pass
    def GetUserData(self, System.String):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPoint,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IAxis):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPlane,AlibreScript.API.IPlane,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IAxis,AlibreScript.API.IPlane):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.IPoint,AlibreScript.API.IPlane,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,AlibreScript.API.Edge,System.Double):
        """Generated stub method"""
        pass
    def AddPointFromCircularEdge(self, System.String,AlibreScript.API.Edge):
        """Generated stub method"""
        pass
    def AddPointFromToroidalFace(self, System.String,AlibreScript.API.Face):
        """Generated stub method"""
        pass
    def GetPlane(self, System.String):
        """Generated stub method"""
        pass
    def GetAxis(self, System.String):
        """Generated stub method"""
        pass
    def GetPoint(self, System.String):
        """Generated stub method"""
        pass
    def GetParameter(self, System.String):
        """Generated stub method"""
        pass
    def GetCustomProperty(self, System.String):
        """Generated stub method"""
        pass
    def SetCustomProperty(self, System.String,System.String):
        """Generated stub method"""
        pass
    def GetConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,AlibreScript.API.ISketchSurface,System.Double):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,AlibreScript.API.ISketchSurface,AlibreScript.API.Axis,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String,System.String):
        """Generated stub method"""
        pass
    def AddPlane(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,AlibreScript.API.ISketchSurface,AlibreScript.API.ISketchSurface):
        """Generated stub method"""
        pass
    def AddAxis(self, System.String,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPoint(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoints(self, System.String,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def Save(self, System.String):
        """Generated stub method"""
        pass
    def SaveAs(self, System.String,System.String):
        """Generated stub method"""
        pass
    def SaveAll(self, System.String):
        """Generated stub method"""
        pass
    def SaveSnapshot(self, System.String,System.Int32,System.Int32,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def SaveThumbnail(self, System.String,System.Int32,System.Int32):
        """Generated stub method"""
        pass
    def AddPart(self, System.String,System.String):
        """Generated stub method"""
        pass
    def AddPart(self, System.String,System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPart(self, System.String,System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddPart(self, AlibreScript.API.Part):
        """Generated stub method"""
        pass
    def AddPart(self, AlibreScript.API.Part,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPart(self, System.String):
        """Generated stub method"""
        pass
    def AddPart(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPart(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def GetPartOrientation(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def GetPartOrientation(self, System.String):
        """Generated stub method"""
        pass
    def AddPart(self, AlibreScript.API.Part,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddNewPart(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def GetPart(self, System.String):
        """Generated stub method"""
        pass
    def GetSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def DuplicatePart(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def DuplicatePart(self, AlibreScript.API.AssembledPart,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def DuplicatePart(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def DuplicatePart(self, AlibreScript.API.AssembledPart,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def DuplicateSubAssembly(self, AlibreScript.API.AssembledSubAssembly,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def DuplicateSubAssembly(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def DuplicateSubAssembly(self, AlibreScript.API.AssembledSubAssembly,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def DuplicateSubAssembly(self, System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AnchorPart(self, System.String):
        """Generated stub method"""
        pass
    def AnchorPart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def AnchorSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def UnanchorPart(self, System.String):
        """Generated stub method"""
        pass
    def UnanchorPart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def UnanchorSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def HidePart(self, System.String):
        """Generated stub method"""
        pass
    def HidePart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def HideSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def ShowPart(self, System.String):
        """Generated stub method"""
        pass
    def ShowPart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def ShowSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def SuppressPart(self, System.String):
        """Generated stub method"""
        pass
    def SuppressPart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def SuppressSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def UnsuppressPart(self, System.String):
        """Generated stub method"""
        pass
    def UnsuppressPart(self, AlibreScript.API.AssembledPart):
        """Generated stub method"""
        pass
    def UnsuppressSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def MovePart(self, System.String,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def MovePart(self, AlibreScript.API.AssembledPart,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def MoveSubAssembly(self, System.String,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def MoveSubAssembly(self, AlibreScript.API.AssembledSubAssembly,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def MoveParts(self, IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def MoveSubAssemblies(self, IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotatePart(self, System.String,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotatePart(self, AlibreScript.API.AssembledPart,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotateSubAssembly(self, System.String,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotateSubAssembly(self, AlibreScript.API.AssembledSubAssembly,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotateSubAssembly(self, AlibreX.IADOccurrence,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotateParts(self, IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def RotateSubAssemblies(self, IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddNewSubAssembly(self, System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, AlibreScript.API.Assembly):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, AlibreScript.API.Assembly,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, AlibreScript.API.Assembly,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, System.String,System.String):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, System.String,System.String,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, System.String,System.String,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddSubAssembly(self, System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.String,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
class Bspline3D:
    """Generated stub class"""
    def GetX(self, System.Double):
        """Generated stub method"""
        pass
    def GetY(self, System.Double):
        """Generated stub method"""
        pass
    def GetZ(self, System.Double):
        """Generated stub method"""
        pass
    def GetPointAt(self, System.Double):
        """Generated stub method"""
        pass
    def GetNormalAt(self, System.Double):
        """Generated stub method"""
        pass
    def Subdivide(self, System.Int32):
        """Generated stub method"""
        pass
    def SubdivideGetNormals(self, System.Int32):
        """Generated stub method"""
        pass
    def #ctor(self, System.Int32,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
class Bspline:
    """Generated stub class"""
    def GetX(self, System.Double):
        """Generated stub method"""
        pass
    def GetY(self, System.Double):
        """Generated stub method"""
        pass
    def GetPointAt(self, System.Double):
        """Generated stub method"""
        pass
    def GetNormalAt(self, System.Double):
        """Generated stub method"""
        pass
    def Subdivide(self, System.Int32):
        """Generated stub method"""
        pass
    def #ctor(self, System.Int32,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
class Circle:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class CircularArc3D:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class CircularArc:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class CSharp:
    """Generated stub class"""
    def CompileAndRun(self, System.String):
        """Generated stub method"""
        pass
    def CompileAndRun(self, System.String,IronPython.Runtime.PythonDictionary):
        """Generated stub method"""
        pass
    def Compile(self, System.String):
        """Generated stub method"""
        pass
    def Run(self, Microsoft.CodeAnalysis.Scripting.Script{System.Object[]}):
        """Generated stub method"""
        pass
    def Run(self, Microsoft.CodeAnalysis.Scripting.Script{System.Object[]},IronPython.Runtime.PythonDictionary):
        """Generated stub method"""
        pass
class Ellipse:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class EllipticalArc:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class GlobalParameters:
    """Generated stub class"""
    def GetParameter(self, System.String):
        """Generated stub method"""
        pass
    def GetConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.Double):
        """Generated stub method"""
        pass
    def AddParameter(self, System.String,AlibreScript.API.ParameterTypes,System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String):
        """Generated stub method"""
        pass
    def AddConfiguration(self, System.String,System.String):
        """Generated stub method"""
        pass
    def Save(self, System.String):
        """Generated stub method"""
        pass
    def SaveAs(self, System.String,System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String):
        """Generated stub method"""
        pass
    def #ctor(self, System.String,System.Boolean):
        """Generated stub method"""
        pass
class Line3D:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
class Polyline3D:
    """Generated stub class"""
    def AddPoint(self, AlibreScript.API.PolylinePoint3D):
        """Generated stub method"""
        pass
    def InsertPoint(self, System.Int32,AlibreScript.API.PolylinePoint3D):
        """Generated stub method"""
        pass
    def AddPolyline(self, AlibreScript.API.Polyline3D):
        """Generated stub method"""
        pass
    def IsPointOnLine(self, AlibreScript.API.PolylinePoint3D,AlibreScript.API.PolylinePoint3D,AlibreScript.API.PolylinePoint3D,System.Double):
        """Generated stub method"""
        pass
    def SplitAtPoint(self, AlibreScript.API.PolylinePoint3D,System.Double):
        """Generated stub method"""
        pass
    def Clone(self, System.Int32,System.Int32):
        """Generated stub method"""
        pass
    def Join(self, AlibreScript.API.Polyline3D):
        """Generated stub method"""
        pass
    def Offset(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def #ctor(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
class PolylinePoint3D:
    """Generated stub class"""
    def Offset(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def Scale(self, System.Double,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def #ctor(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
class TwoD:
    """Generated stub class"""
    def RotatePoint(self, IronPython.Runtime.List,System.Double):
        """Generated stub method"""
        pass
    def GetPerpendicularVector(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def NormalizeVector(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
class Windows:
    """Generated stub class"""
    def CloseForm(self, System.String):
        """Generated stub method"""
        pass
    def GetDisplayedForm(self, System.String):
        """Generated stub method"""
        pass
    def UtilityDialog(self, System.String,System.String,System.Object,System.Object,IronPython.Runtime.List,System.Int32):
        """Generated stub method"""
        pass
    def UtilityDialog(self, System.String,System.String,System.Object,System.Object,IronPython.Runtime.List,System.Int32,System.Object):
        """Generated stub method"""
        pass
    def OptionsDialog(self, System.String,IronPython.Runtime.List,System.Int32):
        """Generated stub method"""
        pass
    def OptionsDialog(self, System.String,IronPython.Runtime.List,System.Int32,System.Object,System.Object):
        """Generated stub method"""
        pass
    def DisableInput(self, System.Int32):
        """Generated stub method"""
        pass
    def EnableInput(self, System.Int32):
        """Generated stub method"""
        pass
    def GetInputValue(self, System.Int32):
        """Generated stub method"""
        pass
    def SetStringList(self, System.Int32,System.Object):
        """Generated stub method"""
        pass
    def SetInputValue(self, System.Int32,System.Object):
        """Generated stub method"""
        pass
    def OpenFileDialog(self, System.String,System.String,System.String):
        """Generated stub method"""
        pass
    def SaveFileDialog(self, System.String,System.String,System.String):
        """Generated stub method"""
        pass
    def SelectFolderDialog(self, System.String,System.String):
        """Generated stub method"""
        pass
    def InfoDialog(self, System.String,System.String):
        """Generated stub method"""
        pass
    def ErrorDialog(self, System.String,System.String):
        """Generated stub method"""
        pass
    def QuestionDialog(self, System.String,System.String):
        """Generated stub method"""
        pass
class Configuration:
    """Generated stub class"""
    def SetLocks(self, AlibreScript.API.LockTypes):
        """Generated stub method"""
        pass
class Face:
    """Generated stub class"""
    def IsParallel(self, AlibreScript.API.Face):
        """Generated stub method"""
        pass
    def DistanceTo(self, AlibreScript.API.Face):
        """Generated stub method"""
        pass
class Feature:
    """Generated stub class"""
    def SetColor(self, System.Byte,System.Byte,System.Byte):
        """Generated stub method"""
        pass
class Sketch:
    """Generated stub class"""
    def AddConstraint(self, AlibreScript.API.ISketchFigure,AlibreScript.API.Sketch.Constraints):
        """Generated stub method"""
        pass
    def AddConstraint(self, IronPython.Runtime.List,AlibreScript.API.Sketch.Constraints):
        """Generated stub method"""
        pass
    def AddLine(self, IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def AddLine(self, AlibreScript.API.Line):
        """Generated stub method"""
        pass
    def AddLine(self, System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddPoint(self, System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddPoint(self, AlibreScript.API.SketchPoint):
        """Generated stub method"""
        pass
    def AddLines(self, IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def AddPolyline(self, AlibreScript.API.Polyline,System.Boolean):
        """Generated stub method"""
        pass
    def AddArcCenterStartEnd(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddArcCenterStartAngle(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddEllipse(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddEllipse(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddEllipse(self, AlibreScript.API.Ellipse):
        """Generated stub method"""
        pass
    def AddEllipticalArc(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddEllipticalArc(self, AlibreScript.API.EllipticalArc):
        """Generated stub method"""
        pass
    def AddArc(self, AlibreScript.API.CircularArc):
        """Generated stub method"""
        pass
    def AddRectangle(self, System.Double,System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddCircle(self, System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def AddCircle(self, AlibreScript.API.Circle):
        """Generated stub method"""
        pass
    def AddBspline(self, System.Int32,IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def AddBspline(self, IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
    def AddFigure(self, AlibreScript.API.ISketchFigure):
        """Generated stub method"""
        pass
    def AddBspline(self, AlibreScript.API.Bspline):
        """Generated stub method"""
        pass
    def AddPolygon(self, System.Double,System.Double,System.Double,System.Int32,System.Boolean):
        """Generated stub method"""
        pass
    def AddPolyhole(self, System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
    def CopyFrom(self, AlibreScript.API.Sketch):
        """Generated stub method"""
        pass
    def CopyFrom(self, AlibreScript.API.Sketch,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def PointtoGlobal(self, System.Double,System.Double):
        """Generated stub method"""
        pass
    def GlobaltoPoint(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddDimension(self, AlibreScript.API.SketchPoint,AlibreScript.API.SketchPoint):
        """Generated stub method"""
        pass
    def AddDimension(self, AlibreScript.API.Circle):
        """Generated stub method"""
        pass
    def AddDimension(self, AlibreScript.API.CircularArc):
        """Generated stub method"""
        pass
    def SavetoXml(self, System.String):
        """Generated stub method"""
        pass
    def LoadXml(self, System.String):
        """Generated stub method"""
        pass
    def FromXml(self, System.String):
        """Generated stub method"""
        pass
    def StartFaceMapping(self, AlibreScript.API.Vertex,AlibreScript.API.Vertex):
        """Generated stub method"""
        pass
    def StartFaceMapping(self, IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def StartMapping(self, IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def ImportSVG(self, System.String):
        """Generated stub method"""
        pass
    def ImportSVG(self, System.String,System.Double,System.Double,System.Double,System.Boolean,System.Boolean):
        """Generated stub method"""
        pass
    def ExportSVG(self, System.String):
        """Generated stub method"""
        pass
    def ExportSVG(self, System.String,System.Boolean):
        """Generated stub method"""
        pass
    def ExportSVG(self, System.String,System.Boolean,System.Double,System.String,System.String,System.Boolean,System.Double,System.Double,System.String,System.String,System.Boolean,System.Double):
        """Generated stub method"""
        pass
class Line:
    """Generated stub class"""
    def #ctor(self, IronPython.Runtime.List,IronPython.Runtime.List,System.Boolean):
        """Generated stub method"""
        pass
class Parameter:
    """Generated stub class"""
    def AttachToExcel(self, System.String,System.String,System.String,AlibreScript.API.UnitTypes):
        """Generated stub method"""
        pass
class Plane:
    """Generated stub class"""
    def IsParallel(self, AlibreScript.API.Plane):
        """Generated stub method"""
        pass
class Polyline:
    """Generated stub class"""
    def AddPoint(self, AlibreScript.API.PolylinePoint):
        """Generated stub method"""
        pass
    def InsertPoint(self, System.Int32,AlibreScript.API.PolylinePoint):
        """Generated stub method"""
        pass
    def AddCircle(self, System.Double,System.Double,System.Double,System.Int32):
        """Generated stub method"""
        pass
    def AddArc(self, AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,System.Int32):
        """Generated stub method"""
        pass
    def AddPolyline(self, AlibreScript.API.Polyline):
        """Generated stub method"""
        pass
    def FindIntersection(self, AlibreScript.API.Polyline,AlibreScript.API.Polyline):
        """Generated stub method"""
        pass
    def FindIntersectionWithCircle(self, AlibreScript.API.Polyline,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def FindIntersection(self, AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint):
        """Generated stub method"""
        pass
    def IsPointOnLine(self, AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,AlibreScript.API.PolylinePoint,System.Double):
        """Generated stub method"""
        pass
    def SplitAtPoint(self, AlibreScript.API.PolylinePoint,System.Double):
        """Generated stub method"""
        pass
    def Clone(self, System.Int32,System.Int32):
        """Generated stub method"""
        pass
    def Join(self, AlibreScript.API.Polyline):
        """Generated stub method"""
        pass
    def RotateZ(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def Offset(self, System.Double,System.Double):
        """Generated stub method"""
        pass
    def #ctor(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
class PolylinePoint:
    """Generated stub class"""
    def Offset(self, System.Double,System.Double):
        """Generated stub method"""
        pass
    def Scale(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def RotateZ(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def #ctor(self, System.Double,System.Double):
        """Generated stub method"""
        pass
class Sketch3D:
    """Generated stub class"""
    def AddLine(self, IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddLine(self, AlibreScript.API.Line3D):
        """Generated stub method"""
        pass
    def AddPoint(self, System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddPoint(self, AlibreScript.API.SketchPoint3D):
        """Generated stub method"""
        pass
    def AddLine(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddLines(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddPolyline(self, AlibreScript.API.Polyline3D):
        """Generated stub method"""
        pass
    def AddArcCenterStartEnd(self, System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double):
        """Generated stub method"""
        pass
    def AddArc(self, AlibreScript.API.CircularArc3D):
        """Generated stub method"""
        pass
    def AddBspline(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def AddBspline(self, AlibreScript.API.Bspline3D):
        """Generated stub method"""
        pass
    def SavetoXml(self, System.String):
        """Generated stub method"""
        pass
    def LoadXml(self, System.String):
        """Generated stub method"""
        pass
    def FromXml(self, System.String):
        """Generated stub method"""
        pass
class SketchPoint:
    """Generated stub class"""
    def #ctor(self, System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class SketchPoint3D:
    """Generated stub class"""
    def #ctor(self, System.Double,System.Double,System.Double,System.Boolean):
        """Generated stub method"""
        pass
class ThreeD:
    """Generated stub class"""
    def GetPerpendicularVector(self, IronPython.Runtime.List):
        """Generated stub method"""
        pass
    def TransformPointUsingVectors(self, IronPython.Runtime.List,IronPython.Runtime.List,IronPython.Runtime.List):
        """Generated stub method"""
        pass
