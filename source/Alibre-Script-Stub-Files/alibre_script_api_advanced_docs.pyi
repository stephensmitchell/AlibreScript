from typing import Any
from abc import ABC, abstractmethod
class AssembledPart(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetMappedOccurrence(self, AlibreX.IADAssemblySession: Any) -> None:
        """Gets the occurrence of the part mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific assembly using the part"""
        pass
    @abstractmethod
    def GetConfiguration(self, System.String: Any) -> None:
        """Gets a configuration with a specific name"""
        pass
    @abstractmethod
    def PartPointtoAssemblyPoint(self, IronPython.Runtime.List: Any) -> None:
        """Converts a point in the part coordinate system into a point in the assembly coordinate system"""
        pass
    @abstractmethod
    def AssemblyPointtoPartPoint(self, IronPython.Runtime.List: Any) -> None:
        """Converts a point in the assembly coordinate system into a point in the part coordinate system"""
        pass
    @abstractmethod
    def GetFace(self, System.String: Any) -> None:
        """Gets a face using it's name Face<n>"""""
        pass
    @abstractmethod
    def GetEdge(self, System.String: Any) -> None:
        """Gets an edge using it's name Edge<n>"""""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a point at an offset to a point or a vertex"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPoint: Any, System.Double: Any) -> None:
        """Adds a point between two points/vertices"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IAxis: Any) -> None:
        """Adds a point at the intersection or two axes or edges"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any) -> None:
        """Adds a point at the intersection of three planes or faces"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IPlane: Any) -> None:
        """Adds a point at the the intersection of a axis or edge and a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPlane: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a point by projecting a point or vertex onto a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.Edge: Any, System.Double: Any) -> None:
        """Adds a point on an edge"""
        pass
    @abstractmethod
    def AddPointFromCircularEdge(self, System.String: Any, AlibreScript.API.Edge: Any) -> None:
        """Adds a point at the center of a circular edge"""
        pass
    @abstractmethod
    def AddPointFromToroidalFace(self, System.String: Any, AlibreScript.API.Face: Any) -> None:
        """Adds a point at the center of a toroidal face"""
        pass
class Part(ABC):
    """Generated stub class"""
    @abstractmethod
    def RemovePoint(self, AlibreScript.API.Point: Any) -> None:
        """Removes a point from the part"""
        pass
    @abstractmethod
    def RemovePlane(self, AlibreScript.API.Plane: Any) -> None:
        """Removes a plane from the part"""
        pass
    @abstractmethod
    def RemoveSketch(self, System.String: Any) -> None:
        """Removes a sketch from the part"""
        pass
    @abstractmethod
    def RemoveSketch(self, AlibreScript.API.Sketch: Any) -> None:
        """Removes a sketch from the part"""
        pass
    @abstractmethod
    def Add3DSketch(self, System.String: Any) -> None:
        """Creates a new 3D sketch"""
        pass
    @abstractmethod
    def AddGear(self, System.String: Any, System.Double: Any, System.Int32: Any, System.Double: Any, System.Double: Any, System.Boolean: Any, System.Double: Any, System.Double: Any, System.Int32: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part"""
        pass
    @abstractmethod
    def AddGearNP(self, System.String: Any, System.Int32: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using number of teeth and pitch diameter"""
        pass
    @abstractmethod
    def AddGearNP(self, System.String: Any, System.Int32: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using number of teeth and pitch diameter"""
        pass
    @abstractmethod
    def AddGearDP(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter"""
        pass
    @abstractmethod
    def AddGearDP(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter"""
        pass
    @abstractmethod
    def AddGearDN(self, System.String: Any, System.Double: Any, System.Int32: Any, System.Double: Any, System.Double: Any, System.Double: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using diametral pitch and number of teeth"""
        pass
    @abstractmethod
    def AddGearDN(self, System.String: Any, System.Double: Any, System.Int32: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Adds a gear sketch to the part using diametral pitch and number of teeth"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Creates an axis based on the intersection of two planes/faces"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, AlibreScript.API.Point: Any, AlibreScript.API.Point: Any) -> None:
        """Creates an axis based on two points"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, AlibreScript.API.Face: Any) -> None:
        """Creates an axis for a cylindrical face"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Creates an axis based on two points"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a point to the part"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.Point: Any) -> None:
        """Adds a point to the part"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a point to the part"""
        pass
    @abstractmethod
    def AddPoints(self, System.String: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a set of points to the part"""
        pass
    @abstractmethod
    def AddExtrudeBoss(self, System.String: Any, AlibreScript.API.Sketch: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a simple extrude boss to a specific depth"""
        pass
    @abstractmethod
    def AddExtrudeBoss(self, System.String: Any, AlibreScript.API.Sketch: Any, System.Double: Any, System.Boolean: Any, AlibreScript.API.Part.EndCondition: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any, AlibreScript.API.Part.DirectionType: Any, AlibreScript.API.ISweepPath: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds an extrude feature"""
        pass
    @abstractmethod
    def AddExtrudeCut(self, System.String: Any, AlibreScript.API.Sketch: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a simple extrude cut to a specific depth"""
        pass
    @abstractmethod
    def AddExtrudeCut(self, System.String: Any, AlibreScript.API.Sketch: Any, System.Double: Any, System.Boolean: Any, AlibreScript.API.Part.EndCondition: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any, AlibreScript.API.Part.DirectionType: Any, AlibreScript.API.ISweepPath: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds an extrude cut feature"""
        pass
    @abstractmethod
    def AddRevolveBoss(self, System.String: Any, AlibreScript.API.Sketch: Any, AlibreScript.API.Axis: Any, System.Double: Any) -> None:
        """Creates a revolve boss feature"""
        pass
    @abstractmethod
    def AddRevolveCut(self, System.String: Any, AlibreScript.API.Sketch: Any, AlibreScript.API.Axis: Any, System.Double: Any) -> None:
        """Creates a revolve cut feature"""
        pass
    @abstractmethod
    def AddLoftBoss(self, System.String: Any, IronPython.Runtime.List: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Adds a loft extrusion"""
        pass
    @abstractmethod
    def AddLoftBoss(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, AlibreScript.API.GuideCurveTypes: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Adds a loft extrusion using guide curves"""
        pass
    @abstractmethod
    def AddLoftCut(self, System.String: Any, IronPython.Runtime.List: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Adds a loft cut"""
        pass
    @abstractmethod
    def AddLoftCut(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, AlibreScript.API.GuideCurveTypes: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Adds a loft cut using guide curves"""
        pass
    @abstractmethod
    def AddSweepBoss(self, System.String: Any, AlibreScript.API.Sketch: Any, AlibreScript.API.ISweepPath: Any, System.Boolean: Any, AlibreScript.API.Part.EndCondition: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a sweep extrude feature"""
        pass
    @abstractmethod
    def AddSweepCut(self, System.String: Any, AlibreScript.API.Sketch: Any, AlibreScript.API.ISweepPath: Any, System.Boolean: Any, AlibreScript.API.Part.EndCondition: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a sweep extrude cut feature"""
        pass
    @abstractmethod
    def AddFillet(self, System.String: Any, AlibreScript.API.IFilletable: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a constant radius fillet to a face or edge"""
        pass
    @abstractmethod
    def AddFillet(self, System.String: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a constant radius fillet to a set of faces and edges"""
        pass
    @abstractmethod
    def AddFillet(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Adds a variable radius fillet to a set of faces and edges"""
        pass
    @abstractmethod
    def Scale(self, System.String: Any, System.Boolean: Any, System.Double: Any) -> None:
        """Uniform scaling of the part"""
        pass
    @abstractmethod
    def NonUniformScale(self, System.String: Any, System.Boolean: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Non-uniform scaling of the part"""
        pass
    @abstractmethod
    def AddChamfer(self, System.String: Any, AlibreScript.API.IChamferable: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a face or edge"""
        pass
    @abstractmethod
    def AddChamfer(self, System.String: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a set of faces and edges"""
        pass
    @abstractmethod
    def AddChamfer(self, System.String: Any, AlibreScript.API.IChamferable: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a face or edge"""
        pass
    @abstractmethod
    def AddChamfer(self, System.String: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a set of faces and edges"""
        pass
    @abstractmethod
    def AddChamferAngle(self, System.String: Any, AlibreScript.API.IChamferable: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a face or edge"""
        pass
    @abstractmethod
    def AddChamferAngle(self, System.String: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a chamfer to a set of faces and edges"""
        pass
    @abstractmethod
    def AddVertexChamfer(self, System.String: Any, AlibreScript.API.Vertex: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a chamfer to a vertex"""
        pass
    @abstractmethod
    def AddVertexChamfer(self, System.String: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a chamfer to a set of vertices"""
        pass
    @abstractmethod
    def Save(self, System.String: Any) -> None:
        """Saves the part to a specific folder"""
        pass
    @abstractmethod
    def SaveAs(self, System.String: Any, System.String: Any) -> None:
        """Saves the part to a specific folder with a new name"""
        pass
    @abstractmethod
    def ExportSTL(self, System.String: Any) -> None:
        """Exports the part as an STL file"""
        pass
    @abstractmethod
    def ExportRotatedSTL(self, System.String: Any, AlibreScript.API.Face: Any, System.Boolean: Any, System.Boolean: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Exports the part as an STL rotated so that a specific face is on the bottom"""
        pass
    @abstractmethod
    def ExportSTEP203(self, System.String: Any) -> None:
        """Exports the part as a STEP 203 file"""
        pass
    @abstractmethod
    def ExportSTEP214(self, System.String: Any) -> None:
        """Exports the part as a STEP 214 file"""
        pass
    @abstractmethod
    def ExportIGES(self, System.String: Any) -> None:
        """Exports the part as a IGES file"""
        pass
    @abstractmethod
    def ExportSAT(self, System.String: Any, System.Int32: Any, System.Boolean: Any) -> None:
        """Exports the part as a SAT file"""
        pass
    @abstractmethod
    def ExportBIP(self, System.String: Any) -> None:
        """Exports a keyshot file"""
        pass
    @abstractmethod
    def SetColor(self, System.Byte: Any, System.Byte: Any, System.Byte: Any) -> None:
        """Sets the color of the part"""
        pass
    @abstractmethod
    def SaveSnapshot(self, System.String: Any, System.Int32: Any, System.Int32: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Saves the current view as a bitmap image"""
        pass
    @abstractmethod
    def SaveThumbnail(self, System.String: Any, System.Int32: Any, System.Int32: Any) -> None:
        """Saves a thumbnail image of the part"""
        pass
    @abstractmethod
    def Select(self, AlibreScript.API.ISelectableGeometry: Any) -> None:
        """Selects a face, edge, vertex, point, axis, plane, sketch"""
        pass
    @abstractmethod
    def Select(self, IronPython.Runtime.List: Any) -> None:
        """Selects a group of faces, edges, vertices, points, axes, planes and sketches"""
        pass
    @abstractmethod
    def SetUserData(self, System.String: Any, IronPython.Runtime.PythonDictionary: Any) -> None:
        """Sets user data"""
        pass
    @abstractmethod
    def GetUserData(self, System.String: Any) -> None:
        """Gets user data"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Add a point at an offset to a point or a vertex"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPoint: Any, System.Double: Any) -> None:
        """Add a point between two points/vertices"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IAxis: Any) -> None:
        """Add a point at the intersection or two axes or edges"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any) -> None:
        """Add a point at the intersection of three planes or faces"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IPlane: Any) -> None:
        """Add a point at the the intersection of a axis or edge and a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPlane: Any, System.Double: Any, System.Double: Any) -> None:
        """Add a point by projecting a point or vertex onto a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.Edge: Any, System.Double: Any) -> None:
        """Add a point on an edge"""
        pass
    @abstractmethod
    def AddPointFromCircularEdge(self, System.String: Any, AlibreScript.API.Edge: Any) -> None:
        """Adds a point at the center of a circular edge"""
        pass
    @abstractmethod
    def AddPointFromToroidalFace(self, System.String: Any, AlibreScript.API.Face: Any) -> None:
        """Adds a point at the center of a toroidal face"""
        pass
    @abstractmethod
    def GetFeature(self, System.String: Any) -> None:
        """Gets a feature on the part"""
        pass
    @abstractmethod
    def RemoveFeature(self, System.String: Any) -> None:
        """Removes a feature from the part"""
        pass
    @abstractmethod
    def RemoveFeature(self, AlibreScript.API.Feature: Any) -> None:
        """Removes a feature from the part"""
        pass
    @abstractmethod
    def SuppressFeature(self, System.String: Any) -> None:
        """Suppresses a feature on the part"""
        pass
    @abstractmethod
    def SuppressFeature(self, AlibreScript.API.Feature: Any) -> None:
        """Suppresses a feature on the part"""
        pass
    @abstractmethod
    def UnsuppressFeature(self, System.String: Any) -> None:
        """Unsuppresses a feature on the part"""
        pass
    @abstractmethod
    def UnsuppressFeature(self, AlibreScript.API.Feature: Any) -> None:
        """Unsuppresses a feature on the part"""
        pass
    @abstractmethod
    def HideFeature(self, System.String: Any) -> None:
        """Hides a feature on the part"""
        pass
    @abstractmethod
    def HideFeature(self, AlibreScript.API.Feature: Any) -> None:
        """Hides a feature on the part"""
        pass
    @abstractmethod
    def ShowFeature(self, System.String: Any) -> None:
        """Shows a feature on the part"""
        pass
    @abstractmethod
    def ShowFeature(self, AlibreScript.API.Feature: Any) -> None:
        """Shows a feature on the part"""
        pass
    @abstractmethod
    def GetPlane(self, System.String: Any) -> None:
        """Gets a plane using the name of the plane"""
        pass
    @abstractmethod
    def GetAxis(self, System.String: Any) -> None:
        """Gets an axis from an axis name"""
        pass
    @abstractmethod
    def GetPoint(self, System.String: Any) -> None:
        """Gets a point on the part using the point name. The point must have been created in a script"""
        pass
    @abstractmethod
    def GetSketch(self, System.String: Any) -> None:
        """Gets a sketch using the name of the sketch"""
        pass
    @abstractmethod
    def Get3DSketch(self, System.String: Any) -> None:
        """Gets a sketch using the name of the sketch"""
        pass
    @abstractmethod
    def GetFace(self, System.String: Any) -> None:
        """Gets a face using it's name Face<n>"""""
        pass
    @abstractmethod
    def GetEdge(self, System.String: Any) -> None:
        """Gets an edge using it's name Edge<n>"""""
        pass
    @abstractmethod
    def GetVertex(self, System.String: Any) -> None:
        """Gets a vertex using it's name Vertex<n>"""""
        pass
    @abstractmethod
    def GetParameter(self, System.String: Any) -> None:
        """Gets a parameter with a specific name"""
        pass
    @abstractmethod
    def GetCustomProperty(self, System.String: Any) -> None:
        """Gets the value of a custonm property"""
        pass
    @abstractmethod
    def SetCustomProperty(self, System.String: Any, System.String: Any) -> None:
        """Sets the value of a custom property The custom property must already be defined on the part or defined on the user's PC"""
        pass
    @abstractmethod
    def GetConfiguration(self, System.String: Any) -> None:
        """Gets a configuration with a specific name"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any) -> None:
        """Creates a plane based on the offset from an existing plane"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a plane using a normal vector and a point on the plane"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, AlibreScript.API.Axis: Any, AlibreScript.API.Point: Any) -> None:
        """Creates a new plane contaning an axis and a point"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, AlibreScript.API.Axis: Any, System.Double: Any) -> None:
        """Creates a new plane at an angle to an existing plane"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.Double: Any) -> None:
        """Adds a cm/mm/in/deg parameter to the part"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, AlibreScript.API.ParameterUnits: Any, System.Double: Any) -> None:
        """Adds a parameter to the part with specific units"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.String: Any) -> None:
        """Adds a parameter to the part"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any) -> None:
        """Adds a configuration to the part"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any, System.String: Any) -> None:
        """Adds a configuration to the part using another configuration as a base"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Creates a plane using three points. Each point is defined as list of [x, y, z]"""
        pass
    @abstractmethod
    def AddSketch(self, System.String: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Creates a new sketch using a plane/face"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.String: Any) -> None:
        """Opens an existing part"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.String: Any, System.Boolean: Any) -> None:
        """Opens an existing part, optionally hiding the editor"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any) -> None:
        """Creates a new part"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.Boolean: Any) -> None:
        """Creates a new part or accesses an already opened part"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Creates a new part or accesses an already opened part, optionally hiding the editor"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, AlibreScript.API.Part.FileTypes: Any) -> None:
        """Opens or imports an existing file for editing"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, AlibreScript.API.Part.FileTypes: Any, System.Boolean: Any) -> None:
        """Opens or imports an existing file for editing, optionally hiding the editor"""
        pass
class AssembledSubAssembly(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetMappedOccurrence(self, AlibreX.IADAssemblySession: Any) -> None:
        """Gets the occurrence of the sub-assembly mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific sub-assembly using the part"""
        pass
    @abstractmethod
    def GetConfiguration(self, System.String: Any) -> None:
        """Gets a configuration with a specific name"""
        pass
class Assembly(ABC):
    """Generated stub class"""
    @abstractmethod
    def AddSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddMateConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any) -> None:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddMateConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddMateConstraint2(self, System.Double: Any, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any, AlibreScript.API.Assembly.ConstraintBoundsType: Any) -> None:
        """Adds a mate constraint between two planes/faces/axes/edges/points Uses bounds type"""
        pass
    @abstractmethod
    def AddFastenerConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a fastner constraint"""
        pass
    @abstractmethod
    def AddFastenerConstraint2(self, System.Double: Any, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any, AlibreScript.API.Assembly.ConstraintBoundsType: Any) -> None:
        """Adds a fastner constraint"""
        pass
    @abstractmethod
    def AddAlignConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any) -> None:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddAlignConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddAlignConstraint2(self, System.Double: Any, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any, AlibreScript.API.Assembly.ConstraintBoundsType: Any) -> None:
        """Adds an alignment constraint between two planes/faces/axes/edges/points Uses bounds type"""
        pass
    @abstractmethod
    def AddOrientConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any) -> None:
        """Adds an orient constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddOrientConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds an orient constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddAngleConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any) -> None:
        """Adds an angle constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddAngleConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a simple angle constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddAngleConstraint2(self, System.Double: Any, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any, AlibreScript.API.Assembly.ConstraintBoundsType: Any) -> None:
        """Adds an angle constraint between two planes/faces/axes/edges/points Uses bounds type"""
        pass
    @abstractmethod
    def AddGearConstraint(self, System.Double: Any, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a gear constraint using ratio RatioA:RatioB"""
        pass
    @abstractmethod
    def AddRackAndPinionConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a rack and pinion constraint"""
        pass
    @abstractmethod
    def AddScrewConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a screw constraint"""
        pass
    @abstractmethod
    def AddTangentConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any) -> None:
        """Adds a tangent constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def AddTangentConstraint(self, System.Double: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, AlibreScript.API.IAssembled: Any, AlibreScript.API.IConstrainable: Any, System.Boolean: Any, System.Boolean: Any, System.String: Any) -> None:
        """Adds a tangent constraint between two planes/faces/axes/edges/points"""
        pass
    @abstractmethod
    def CreateUniqueName(self, System.String: Any) -> None:
        """Creates a unique name that can be used to safely add a part or subassembly to the assembly if the names used in the assembly are not known in advance"""
        pass
    @abstractmethod
    def ExportSTL(self, System.String: Any) -> None:
        """Exports the assembly as an STL file"""
        pass
    @abstractmethod
    def ExportSTEP203(self, System.String: Any) -> None:
        """Exports the assembly as a STEP 203 file"""
        pass
    @abstractmethod
    def ExportSTEP214(self, System.String: Any) -> None:
        """Exports the assembly as a STEP 214 file"""
        pass
    @abstractmethod
    def ExportIGES(self, System.String: Any) -> None:
        """Exports the assembly as a IGES file"""
        pass
    @abstractmethod
    def ExportSAT(self, System.String: Any, System.Int32: Any, System.Boolean: Any) -> None:
        """Exports the assembly as a SAT file"""
        pass
    @abstractmethod
    def ExportBIP(self, System.String: Any) -> None:
        """Exports a keyshot file"""
        pass
    @abstractmethod
    def SetUserData(self, System.String: Any, IronPython.Runtime.PythonDictionary: Any) -> None:
        """Sets user data"""
        pass
    @abstractmethod
    def GetUserData(self, System.String: Any) -> None:
        """Gets user data"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Add a point at an offset to a point or a vertex"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPoint: Any, System.Double: Any) -> None:
        """Add a point between two points/vertices"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IAxis: Any) -> None:
        """Add a point at the intersection or two axes or edges"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any, AlibreScript.API.IPlane: Any) -> None:
        """Add a point at the intersection of three planes or faces"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IAxis: Any, AlibreScript.API.IPlane: Any) -> None:
        """Add a point at the the intersection of a axis or edge and a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.IPoint: Any, AlibreScript.API.IPlane: Any, System.Double: Any, System.Double: Any) -> None:
        """Add a point by projecting a point or vertex onto a plane or face"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, AlibreScript.API.Edge: Any, System.Double: Any) -> None:
        """Add a point on an edge"""
        pass
    @abstractmethod
    def AddPointFromCircularEdge(self, System.String: Any, AlibreScript.API.Edge: Any) -> None:
        """Adds a point at the center of a circular edge"""
        pass
    @abstractmethod
    def AddPointFromToroidalFace(self, System.String: Any, AlibreScript.API.Face: Any) -> None:
        """Adds a point at the center of a toroidal face"""
        pass
    @abstractmethod
    def GetPlane(self, System.String: Any) -> None:
        """Gets a plane using the name of the plane"""
        pass
    @abstractmethod
    def GetAxis(self, System.String: Any) -> None:
        """Gets an axis from an axis name"""
        pass
    @abstractmethod
    def GetPoint(self, System.String: Any) -> None:
        """Gets a point on the assembly using the point name. The point must have been created in a script"""
        pass
    @abstractmethod
    def GetParameter(self, System.String: Any) -> None:
        """Gets a parameter with a specific name"""
        pass
    @abstractmethod
    def GetCustomProperty(self, System.String: Any) -> None:
        """Gets the value of a custonm property"""
        pass
    @abstractmethod
    def SetCustomProperty(self, System.String: Any, System.String: Any) -> None:
        """Sets the value of a custom property The custom property must already be defined on the assembly or defined on the user's PC"""
        pass
    @abstractmethod
    def GetConfiguration(self, System.String: Any) -> None:
        """Gets a configuration with a specific name"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, System.Double: Any) -> None:
        """Creates a plane based on the offset from an existing plane"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a plane using a normal vector and a point on the plane"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, AlibreScript.API.Axis: Any, System.Double: Any) -> None:
        """Creates a new plane at an angle to an existing plane"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.Double: Any) -> None:
        """Adds a parameter to the assembly"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.String: Any) -> None:
        """Adds a parameter to the assembly NOTE: DOESN'T SEEM TO WORK IN GD V16 - THROWS EXCEPTION ABOUT TRANSACTION ALREADY BEING OPEN"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any) -> None:
        """Adds a configuration to the assembly"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any, System.String: Any) -> None:
        """Adds a configuration to the assembly using another configuration as a base"""
        pass
    @abstractmethod
    def AddPlane(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Creates a plane using three points"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, AlibreScript.API.ISketchSurface: Any, AlibreScript.API.ISketchSurface: Any) -> None:
        """Creates an axis based on the intersection of two planes/faces"""
        pass
    @abstractmethod
    def AddAxis(self, System.String: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Creates an axis based on two points"""
        pass
    @abstractmethod
    def AddPoint(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a point to the assembly"""
        pass
    @abstractmethod
    def AddPoints(self, System.String: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a set of points to the part"""
        pass
    @abstractmethod
    def Save(self, System.String: Any) -> None:
        """Saves the assembly to a specific folder"""
        pass
    @abstractmethod
    def SaveAs(self, System.String: Any, System.String: Any) -> None:
        """Saves the assembly to a specific folder with a new name"""
        pass
    @abstractmethod
    def SaveAll(self, System.String: Any) -> None:
        """Save the assembly and all parts/sub-assemblies to a folder"""
        pass
    @abstractmethod
    def SaveSnapshot(self, System.String: Any, System.Int32: Any, System.Int32: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Saves the current view as a bitmap image"""
        pass
    @abstractmethod
    def SaveThumbnail(self, System.String: Any, System.Int32: Any, System.Int32: Any) -> None:
        """Saves a thumbnail image of the assembly"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any, System.String: Any) -> None:
        """Adds a part to the assembly at the origin"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def AddPart(self, AlibreScript.API.Part: Any) -> None:
        """Adds a part to the assembly at the origin"""
        pass
    @abstractmethod
    def AddPart(self, AlibreScript.API.Part: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any) -> None:
        """Adds a part to the assembly at the origin"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def AddPart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def GetPartOrientation(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Gets the orientation of a part in an assembly"""
        pass
    @abstractmethod
    def GetPartOrientation(self, System.String: Any) -> None:
        """Gets the orientation of a part in an assembly"""
        pass
    @abstractmethod
    def AddPart(self, AlibreScript.API.Part: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a part to the assembly"""
        pass
    @abstractmethod
    def AddNewPart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a new part to the assembly"""
        pass
    @abstractmethod
    def GetPart(self, System.String: Any) -> None:
        """Gets a part in the assembly"""
        pass
    @abstractmethod
    def GetSubAssembly(self, System.String: Any) -> None:
        """Gets a sub-assembly in the assembly"""
        pass
    @abstractmethod
    def DuplicatePart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Duplicates a part in the assembly"""
        pass
    @abstractmethod
    def DuplicatePart(self, AlibreScript.API.AssembledPart: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Duplicates a part in the assembly"""
        pass
    @abstractmethod
    def DuplicatePart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Duplicates a part in the assembly"""
        pass
    @abstractmethod
    def DuplicatePart(self, AlibreScript.API.AssembledPart: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Duplicates a part in the assembly"""
        pass
    @abstractmethod
    def DuplicateSubAssembly(self, AlibreScript.API.AssembledSubAssembly: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Duplicates a sub-assembly in the assembly"""
        pass
    @abstractmethod
    def DuplicateSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Duplicates a sub-assembly in the assembly"""
        pass
    @abstractmethod
    def DuplicateSubAssembly(self, AlibreScript.API.AssembledSubAssembly: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Duplicates a sub-assembly in the assembly"""
        pass
    @abstractmethod
    def DuplicateSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Duplicates a sub-assembly in the assembly"""
        pass
    @abstractmethod
    def AnchorPart(self, System.String: Any) -> None:
        """Anchors a part"""
        pass
    @abstractmethod
    def AnchorPart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Anchors a part"""
        pass
    @abstractmethod
    def AnchorSubAssembly(self, System.String: Any) -> None:
        """Anchors a sub-assembly"""
        pass
    @abstractmethod
    def UnanchorPart(self, System.String: Any) -> None:
        """Un-anchors a part"""
        pass
    @abstractmethod
    def UnanchorPart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Un-anchors a part"""
        pass
    @abstractmethod
    def UnanchorSubAssembly(self, System.String: Any) -> None:
        """Un-anchors a sub-assembly"""
        pass
    @abstractmethod
    def HidePart(self, System.String: Any) -> None:
        """Hides a part"""
        pass
    @abstractmethod
    def HidePart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Hides a part"""
        pass
    @abstractmethod
    def HideSubAssembly(self, System.String: Any) -> None:
        """Hides a sub-assembly"""
        pass
    @abstractmethod
    def ShowPart(self, System.String: Any) -> None:
        """Shows a part"""
        pass
    @abstractmethod
    def ShowPart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Shows a part"""
        pass
    @abstractmethod
    def ShowSubAssembly(self, System.String: Any) -> None:
        """Shows a sub-assembly"""
        pass
    @abstractmethod
    def SuppressPart(self, System.String: Any) -> None:
        """Suppresses a part"""
        pass
    @abstractmethod
    def SuppressPart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Suppresses a part"""
        pass
    @abstractmethod
    def SuppressSubAssembly(self, System.String: Any) -> None:
        """Suppresses a sub-assembly"""
        pass
    @abstractmethod
    def UnsuppressPart(self, System.String: Any) -> None:
        """Un-suppresses a part"""
        pass
    @abstractmethod
    def UnsuppressPart(self, AlibreScript.API.AssembledPart: Any) -> None:
        """Un-suppresses a part"""
        pass
    @abstractmethod
    def UnsuppressSubAssembly(self, System.String: Any) -> None:
        """Un-suppresses a sub-assembly"""
        pass
    @abstractmethod
    def MovePart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a part"""
        pass
    @abstractmethod
    def MovePart(self, AlibreScript.API.AssembledPart: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a part"""
        pass
    @abstractmethod
    def MoveSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a sub-assembly"""
        pass
    @abstractmethod
    def MoveSubAssembly(self, AlibreScript.API.AssembledSubAssembly: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a sub-assembly"""
        pass
    @abstractmethod
    def MoveParts(self, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a set of parts"""
        pass
    @abstractmethod
    def MoveSubAssemblies(self, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Moves a set of sub-assemblies"""
        pass
    @abstractmethod
    def RotatePart(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a part"""
        pass
    @abstractmethod
    def RotatePart(self, AlibreScript.API.AssembledPart: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a part"""
        pass
    @abstractmethod
    def RotateSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a sub-assembly"""
        pass
    @abstractmethod
    def RotateSubAssembly(self, AlibreScript.API.AssembledSubAssembly: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a sub-assembly"""
        pass
    @abstractmethod
    def RotateSubAssembly(self, AlibreX.IADOccurrence: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a sub-assembly"""
        pass
    @abstractmethod
    def RotateParts(self, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a set of parts"""
        pass
    @abstractmethod
    def RotateSubAssemblies(self, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Rotates a set of sub-assemblies"""
        pass
    @abstractmethod
    def AddNewSubAssembly(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a new sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, AlibreScript.API.Assembly: Any) -> None:
        """Adds a sub-assembly to the assembly at the origin"""
        pass
    @abstractmethod
    def AddSubAssembly(self, AlibreScript.API.Assembly: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, AlibreScript.API.Assembly: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, System.String: Any, System.String: Any) -> None:
        """Adds a sub-assembly to the assembly at the origin"""
        pass
    @abstractmethod
    def AddSubAssembly(self, System.String: Any, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, System.String: Any, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a sub-assembly to the assembly"""
        pass
    @abstractmethod
    def AddSubAssembly(self, System.String: Any) -> None:
        """Adds a sub-assembly to the assembly at the origin"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.String: Any) -> None:
        """Opens an existing assembly"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.String: Any, System.Boolean: Any) -> None:
        """Opens an existing assembly, optionally hiding the editor"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any) -> None:
        """Creates a new assembly"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.Boolean: Any) -> None:
        """Creates a new assembly or accesses an already opened assembly"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Creates a new assembly or accesses an already opened assembly, optionally hiding the editor"""
        pass
class Bspline3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetX(self, System.Double: Any) -> None:
        """Gets the X value of the spline at a location along the spline"""
        pass
    @abstractmethod
    def GetY(self, System.Double: Any) -> None:
        """Gets the Y value of the spline at a location along the spline"""
        pass
    @abstractmethod
    def GetZ(self, System.Double: Any) -> None:
        """Gets the Z value of the spline at a location along the spline"""
        pass
    @abstractmethod
    def GetPointAt(self, System.Double: Any) -> None:
        """Gets a point on the spline"""
        pass
    @abstractmethod
    def GetNormalAt(self, System.Double: Any) -> None:
        """Gets the normal vector at a point on the spline"""
        pass
    @abstractmethod
    def Subdivide(self, System.Int32: Any) -> None:
        """Divides the Bspline up into segments"""
        pass
    @abstractmethod
    def SubdivideGetNormals(self, System.Int32: Any) -> None:
        """Divides the Bspline up into segments and gets the normal for each point"""
        pass
    @abstractmethod
    def #ctor(self, System.Int32: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates a bspline"""
        pass
class Bspline(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetX(self, System.Double: Any) -> None:
        """Gets the X value of the spline at a location along the spline"""
        pass
    @abstractmethod
    def GetY(self, System.Double: Any) -> None:
        """Gets the Y value of the spline at a location along the spline"""
        pass
    @abstractmethod
    def GetPointAt(self, System.Double: Any) -> None:
        """Gets a point on the spline"""
        pass
    @abstractmethod
    def GetNormalAt(self, System.Double: Any) -> None:
        """Gets the normal vector at a point on the spline"""
        pass
    @abstractmethod
    def Subdivide(self, System.Int32: Any) -> None:
        """Divides the Bspline up into segments"""
        pass
    @abstractmethod
    def #ctor(self, System.Int32: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates a bspline"""
        pass
class Circle(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates a 2D circle which can be added to sketches"""
        pass
class CircularArc3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates an arc using the center, start point and end point"""
        pass
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates an arc using the center, start point and an angle"""
        pass
class CircularArc(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates an arc using the center, start point and end point"""
        pass
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates an arc using the center, start point and an angle"""
        pass
class CSharp(ABC):
    """Generated stub class"""
    @abstractmethod
    def CompileAndRun(self, System.String: Any) -> None:
        """Compiles and runs C# code"""
        pass
    @abstractmethod
    def CompileAndRun(self, System.String: Any, IronPython.Runtime.PythonDictionary: Any) -> None:
        """Compiles and runs C# code"""
        pass
    @abstractmethod
    def Compile(self, System.String: Any) -> None:
        """Compiles C# code"""
        pass
    @abstractmethod
    def Run(self, Microsoft.CodeAnalysis.Scripting.Script{System.Object[]}: Any) -> None:
        """Runs compiled C# code"""
        pass
    @abstractmethod
    def Run(self, Microsoft.CodeAnalysis.Scripting.Script{System.Object[]}: Any, IronPython.Runtime.PythonDictionary: Any) -> None:
        """Runs compiled C# code"""
        pass
class Ellipse(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates an ellipse"""
        pass
class EllipticalArc(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates an elliptical arc"""
        pass
class GlobalParameters(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetParameter(self, System.String: Any) -> None:
        """Gets a parameter with a specific name"""
        pass
    @abstractmethod
    def GetConfiguration(self, System.String: Any) -> None:
        """Gets a configuration with a specific name"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.Double: Any) -> None:
        """Adds a parameter to the global parameters set"""
        pass
    @abstractmethod
    def AddParameter(self, System.String: Any, AlibreScript.API.ParameterTypes: Any, System.String: Any) -> None:
        """Adds a parameter to the global parameters set"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any) -> None:
        """Adds a configuration to the global parameters set"""
        pass
    @abstractmethod
    def AddConfiguration(self, System.String: Any, System.String: Any) -> None:
        """Adds a configuration to the global parameters set using another configuration as a base"""
        pass
    @abstractmethod
    def Save(self, System.String: Any) -> None:
        """Saves the global parameters set to a specific folder"""
        pass
    @abstractmethod
    def SaveAs(self, System.String: Any, System.String: Any) -> None:
        """Saves the global parameters set to a specific folder with a new name"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.String: Any) -> None:
        """Opens an existing global parameters set"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any) -> None:
        """Creates a new global parameters set"""
        pass
    @abstractmethod
    def #ctor(self, System.String: Any, System.Boolean: Any) -> None:
        """Creates a new global parameters set or accesses an already opened global parameters set"""
        pass
class Line3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates a new 3D line"""
        pass
class Polyline3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def AddPoint(self, AlibreScript.API.PolylinePoint3D: Any) -> None:
        """Adds a new point to the polyline"""
        pass
    @abstractmethod
    def InsertPoint(self, System.Int32: Any, AlibreScript.API.PolylinePoint3D: Any) -> None:
        """Inserts a point at a specific location"""
        pass
    @abstractmethod
    def AddPolyline(self, AlibreScript.API.Polyline3D: Any) -> None:
        """Appends a line to the current line"""
        pass
    @abstractmethod
    def IsPointOnLine(self, AlibreScript.API.PolylinePoint3D: Any, AlibreScript.API.PolylinePoint3D: Any, AlibreScript.API.PolylinePoint3D: Any, System.Double: Any) -> None:
        """Determines if a point is on a line segment"""
        pass
    @abstractmethod
    def SplitAtPoint(self, AlibreScript.API.PolylinePoint3D: Any, System.Double: Any) -> None:
        """Splits a polyline at a point, creating two polylines"""
        pass
    @abstractmethod
    def Clone(self, System.Int32: Any, System.Int32: Any) -> None:
        """Creates an exact copy of a section of the line"""
        pass
    @abstractmethod
    def Join(self, AlibreScript.API.Polyline3D: Any) -> None:
        """Joins a line onto the end of the current line and returns the new line"""
        pass
    @abstractmethod
    def Offset(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Applies an offset to all points on the line"""
        pass
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any) -> None:
        """Creates a new 3D polyline that can be later added to a 3D sketch"""
        pass
class PolylinePoint3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def Offset(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Applies an offset to the point and creates a new point"""
        pass
    @abstractmethod
    def Scale(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Scales the point location based on an origin for the scaling"""
        pass
    @abstractmethod
    def #ctor(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Creates a new 3D polyline point"""
        pass
class TwoD(ABC):
    """Generated stub class"""
    @abstractmethod
    def RotatePoint(self, IronPython.Runtime.List: Any, System.Double: Any) -> None:
        """Rotates a point"""
        pass
    @abstractmethod
    def GetPerpendicularVector(self, IronPython.Runtime.List: Any) -> None:
        """Gets a vector that is perpendicular to a vector"""
        pass
    @abstractmethod
    def NormalizeVector(self, IronPython.Runtime.List: Any) -> None:
        """Normalizes a vector"""
        pass
class Windows(ABC):
    """Generated stub class"""
    @abstractmethod
    def CloseForm(self, System.String: Any) -> None:
        """Close all currently open forms for a specific session"""
        pass
    @abstractmethod
    def GetDisplayedForm(self, System.String: Any) -> None:
        """Gets the currently displayed form for a specific session"""
        pass
    @abstractmethod
    def UtilityDialog(self, System.String: Any, System.String: Any, System.Object: Any, System.Object: Any, IronPython.Runtime.List: Any, System.Int32: Any) -> None:
        """Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script"""
        pass
    @abstractmethod
    def UtilityDialog(self, System.String: Any, System.String: Any, System.Object: Any, System.Object: Any, IronPython.Runtime.List: Any, System.Int32: Any, System.Object: Any) -> None:
        """Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script"""
        pass
    @abstractmethod
    def OptionsDialog(self, System.String: Any, IronPython.Runtime.List: Any, System.Int32: Any) -> None:
        """Shows a dialog prompting the user to enter values"""
        pass
    @abstractmethod
    def OptionsDialog(self, System.String: Any, IronPython.Runtime.List: Any, System.Int32: Any, System.Object: Any, System.Object: Any) -> None:
        """Shows a dialog prompting the user to enter values"""
        pass
    @abstractmethod
    def DisableInput(self, System.Int32: Any) -> None:
        """Disables an input"""
        pass
    @abstractmethod
    def EnableInput(self, System.Int32: Any) -> None:
        """Enables an input"""
        pass
    @abstractmethod
    def GetInputValue(self, System.Int32: Any) -> None:
        """Gets the current value of an input"""
        pass
    @abstractmethod
    def SetStringList(self, System.Int32: Any, System.Object: Any) -> None:
        """Updates the list of strings for a stringlist input"""
        pass
    @abstractmethod
    def SetInputValue(self, System.Int32: Any, System.Object: Any) -> None:
        """Sets the current value for an input"""
        pass
    @abstractmethod
    def OpenFileDialog(self, System.String: Any, System.String: Any, System.String: Any) -> None:
        """Prompts user to select a file"""
        pass
    @abstractmethod
    def SaveFileDialog(self, System.String: Any, System.String: Any, System.String: Any) -> None:
        """Prompts user to save a file"""
        pass
    @abstractmethod
    def SelectFolderDialog(self, System.String: Any, System.String: Any) -> None:
        """Prompts the user to select a folder"""
        pass
    @abstractmethod
    def InfoDialog(self, System.String: Any, System.String: Any) -> None:
        """Shows an information window"""
        pass
    @abstractmethod
    def ErrorDialog(self, System.String: Any, System.String: Any) -> None:
        """Shows an error window"""
        pass
    @abstractmethod
    def QuestionDialog(self, System.String: Any, System.String: Any) -> None:
        """Shows a question window"""
        pass
class Configuration(ABC):
    """Generated stub class"""
    @abstractmethod
    def SetLocks(self, AlibreScript.API.LockTypes: Any) -> None:
        """Sets the locks on the configuration"""
        pass
class Face(ABC):
    """Generated stub class"""
    @abstractmethod
    def IsParallel(self, AlibreScript.API.Face: Any) -> None:
        """Checks if another face is parallel to this one"""
        pass
    @abstractmethod
    def DistanceTo(self, AlibreScript.API.Face: Any) -> None:
        """Gets the distance from this face to another face"""
        pass
class Feature(ABC):
    """Generated stub class"""
    @abstractmethod
    def SetColor(self, System.Byte: Any, System.Byte: Any, System.Byte: Any) -> None:
        """Sets the color of the part"""
        pass
class Sketch(ABC):
    """Generated stub class"""
    @abstractmethod
    def AddConstraint(self, AlibreScript.API.ISketchFigure: Any, AlibreScript.API.Sketch.Constraints: Any) -> None:
        """Adds a constraint to the sketch"""
        pass
    @abstractmethod
    def AddConstraint(self, IronPython.Runtime.List: Any, AlibreScript.API.Sketch.Constraints: Any) -> None:
        """Adds a constraint to the sketch"""
        pass
    @abstractmethod
    def AddLine(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddLine(self, AlibreScript.API.Line: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddLine(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddPoint(self, System.Double: Any, System.Double: Any) -> None:
        """Adds a point to the sketch"""
        pass
    @abstractmethod
    def AddPoint(self, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a point to the sketch [DEPRECATED - DO NOT USE]"""
        pass
    @abstractmethod
    def AddPoint(self, AlibreScript.API.SketchPoint: Any) -> None:
        """Adds a point to the sketch"""
        pass
    @abstractmethod
    def AddLines(self, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Adds a polyline to the sketch"""
        pass
    @abstractmethod
    def AddPolyline(self, AlibreScript.API.Polyline: Any, System.Boolean: Any) -> None:
        """Adds a polyline to the sketch"""
        pass
    @abstractmethod
    def AddArcCenterStartEnd(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end"""
        pass
    @abstractmethod
    def AddArcCenterStartAngle(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a circular arc using center, start and angle Arc goes anti-clockwise from start"""
        pass
    @abstractmethod
    def AddEllipse(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds an ellipse to the sketch using three points"""
        pass
    @abstractmethod
    def AddEllipse(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds an ellipse to the sketch"""
        pass
    @abstractmethod
    def AddEllipse(self, AlibreScript.API.Ellipse: Any) -> None:
        """Adds an ellipse to the sketch"""
        pass
    @abstractmethod
    def AddEllipticalArc(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds an elliptical arc to the sketch"""
        pass
    @abstractmethod
    def AddEllipticalArc(self, AlibreScript.API.EllipticalArc: Any) -> None:
        """Adds an elliptical arc to the sketch"""
        pass
    @abstractmethod
    def AddArc(self, AlibreScript.API.CircularArc: Any) -> None:
        """Adds a circular arc to the sketch"""
        pass
    @abstractmethod
    def AddRectangle(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a rectangle to the sketch"""
        pass
    @abstractmethod
    def AddCircle(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a circle to the sketch"""
        pass
    @abstractmethod
    def AddCircle(self, AlibreScript.API.Circle: Any) -> None:
        """Adds a circle to the sketch"""
        pass
    @abstractmethod
    def AddBspline(self, System.Int32: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Adds a Bspline to the sketch"""
        pass
    @abstractmethod
    def AddBspline(self, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Adds a Bspline to the sketch through a set of points"""
        pass
    @abstractmethod
    def AddFigure(self, AlibreScript.API.ISketchFigure: Any) -> None:
        """Adds a figure to the sketch"""
        pass
    @abstractmethod
    def AddBspline(self, AlibreScript.API.Bspline: Any) -> None:
        """Adds a new bspline to the sketch"""
        pass
    @abstractmethod
    def AddPolygon(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Int32: Any, System.Boolean: Any) -> None:
        """Adds a regular polygon to the sketch"""
        pass
    @abstractmethod
    def AddPolyhole(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Adds a polyhole to the sketch Create a circle" whose size should be accurate regardless of the 3D printing method See: http://hydraraptor.blogspot.co.uk/2011/02/polyholes.html""""
        pass
    @abstractmethod
    def CopyFrom(self, AlibreScript.API.Sketch: Any) -> None:
        """Copies a sketch into this sketch"""
        pass
    @abstractmethod
    def CopyFrom(self, AlibreScript.API.Sketch: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Copies a sketch into this sketch"""
        pass
    @abstractmethod
    def PointtoGlobal(self, System.Double: Any, System.Double: Any) -> None:
        """Converts a point on the sketch into a 3D point in the part coordinate system"""
        pass
    @abstractmethod
    def GlobaltoPoint(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Projects a 3D point in the part coordinate system into a point on the sketch"""
        pass
    @abstractmethod
    def AddDimension(self, AlibreScript.API.SketchPoint: Any, AlibreScript.API.SketchPoint: Any) -> None:
        """Adds a dimension to the sketch between two points"""
        pass
    @abstractmethod
    def AddDimension(self, AlibreScript.API.Circle: Any) -> None:
        """Adds a dimension to the radius of a circle"""
        pass
    @abstractmethod
    def AddDimension(self, AlibreScript.API.CircularArc: Any) -> None:
        """Adds a dimension to the radius of an arc"""
        pass
    @abstractmethod
    def SavetoXml(self, System.String: Any) -> None:
        """Saves the sketch to an XML file Does not support ellipses and elliptical arcs"""
        pass
    @abstractmethod
    def LoadXml(self, System.String: Any) -> None:
        """Loads the sketch from an XML file"""
        pass
    @abstractmethod
    def FromXml(self, System.String: Any) -> None:
        """Adds elements to the sketch from XML"""
        pass
    @abstractmethod
    def StartFaceMapping(self, AlibreScript.API.Vertex: Any, AlibreScript.API.Vertex: Any) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0]"""
        pass
    @abstractmethod
    def StartFaceMapping(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values"""
        pass
    @abstractmethod
    def StartMapping(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Starts mapping the sketch so that the specified line is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values"""
        pass
    @abstractmethod
    def ImportSVG(self, System.String: Any) -> None:
        """Imports an SVG into the sketch"""
        pass
    @abstractmethod
    def ImportSVG(self, System.String: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any, System.Boolean: Any) -> None:
        """Imports an SVG into the sketch"""
        pass
    @abstractmethod
    def ExportSVG(self, System.String: Any) -> None:
        """Exports the sketch to an SVG"""
        pass
    @abstractmethod
    def ExportSVG(self, System.String: Any, System.Boolean: Any) -> None:
        """Exports the sketch to an SVG"""
        pass
    @abstractmethod
    def ExportSVG(self, System.String: Any, System.Boolean: Any, System.Double: Any, System.String: Any, System.String: Any, System.Boolean: Any, System.Double: Any, System.Double: Any, System.String: Any, System.String: Any, System.Boolean: Any, System.Double: Any) -> None:
        """Exports the sketch to an SVG with specific styling"""
        pass
class Line(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, System.Boolean: Any) -> None:
        """Creates a new 2D line"""
        pass
class Parameter(ABC):
    """Generated stub class"""
    @abstractmethod
    def AttachToExcel(self, System.String: Any, System.String: Any, System.String: Any, AlibreScript.API.UnitTypes: Any) -> None:
        """Attaches the parameter to a cell in an Ezcel spreadsheet"""
        pass
class Plane(ABC):
    """Generated stub class"""
    @abstractmethod
    def IsParallel(self, AlibreScript.API.Plane: Any) -> None:
        """Checks if another plane is parallel to this one"""
        pass
class Polyline(ABC):
    """Generated stub class"""
    @abstractmethod
    def AddPoint(self, AlibreScript.API.PolylinePoint: Any) -> None:
        """Adds a new point to the polyline"""
        pass
    @abstractmethod
    def InsertPoint(self, System.Int32: Any, AlibreScript.API.PolylinePoint: Any) -> None:
        """Inserts a point at a specific location"""
        pass
    @abstractmethod
    def AddCircle(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Int32: Any) -> None:
        """Adds a circle to the line"""
        pass
    @abstractmethod
    def AddArc(self, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, System.Int32: Any) -> None:
        """Adds an arc to the polyline. The arc is approcimated with straight line segments"""
        pass
    @abstractmethod
    def AddPolyline(self, AlibreScript.API.Polyline: Any) -> None:
        """Appends a line to the current line"""
        pass
    @abstractmethod
    def FindIntersection(self, AlibreScript.API.Polyline: Any, AlibreScript.API.Polyline: Any) -> None:
        """Finds the first intersection point between two lines"""
        pass
    @abstractmethod
    def FindIntersectionWithCircle(self, AlibreScript.API.Polyline: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Finds first intersection of line with a circle"""
        pass
    @abstractmethod
    def FindIntersection(self, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any) -> None:
        """Gets the intersection between the line segments A1A2 and B1B2"""
        pass
    @abstractmethod
    def IsPointOnLine(self, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, AlibreScript.API.PolylinePoint: Any, System.Double: Any) -> None:
        """Determines if a point is on a line segment"""
        pass
    @abstractmethod
    def SplitAtPoint(self, AlibreScript.API.PolylinePoint: Any, System.Double: Any) -> None:
        """Splits a polyline at a point, creating two polylines"""
        pass
    @abstractmethod
    def Clone(self, System.Int32: Any, System.Int32: Any) -> None:
        """Creates an exact copy of a section of the line"""
        pass
    @abstractmethod
    def Join(self, AlibreScript.API.Polyline: Any) -> None:
        """Joins a line onto the end of the current line and returns the new line"""
        pass
    @abstractmethod
    def RotateZ(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Rotates the polyline around the Z axis"""
        pass
    @abstractmethod
    def Offset(self, System.Double: Any, System.Double: Any) -> None:
        """Applies an offset to all points on the line"""
        pass
    @abstractmethod
    def #ctor(self, IronPython.Runtime.List: Any) -> None:
        """Creates a new 2D polyline that can be later added to a 2D sketch"""
        pass
class PolylinePoint(ABC):
    """Generated stub class"""
    @abstractmethod
    def Offset(self, System.Double: Any, System.Double: Any) -> None:
        """Applies an offset to the point and creates a new point"""
        pass
    @abstractmethod
    def Scale(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Scales the point location based on an origin for the scaling"""
        pass
    @abstractmethod
    def RotateZ(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Rotates the point around the Z axis"""
        pass
    @abstractmethod
    def #ctor(self, System.Double: Any, System.Double: Any) -> None:
        """Creates a new polyline point"""
        pass
class Sketch3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def AddLine(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddLine(self, AlibreScript.API.Line3D: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddPoint(self, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a point to the sketch"""
        pass
    @abstractmethod
    def AddPoint(self, AlibreScript.API.SketchPoint3D: Any) -> None:
        """Adds a point to the sketch"""
        pass
    @abstractmethod
    def AddLine(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a line to the sketch"""
        pass
    @abstractmethod
    def AddLines(self, IronPython.Runtime.List: Any) -> None:
        """Adds a polyline to the sketch"""
        pass
    @abstractmethod
    def AddPolyline(self, AlibreScript.API.Polyline3D: Any) -> None:
        """Adds a polyline to the sketch"""
        pass
    @abstractmethod
    def AddArcCenterStartEnd(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any, System.Double: Any) -> None:
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end"""
        pass
    @abstractmethod
    def AddArc(self, AlibreScript.API.CircularArc3D: Any) -> None:
        """Adds a circular arc to the sketch"""
        pass
    @abstractmethod
    def AddBspline(self, IronPython.Runtime.List: Any) -> None:
        """Adds a Bspline to the sketch"""
        pass
    @abstractmethod
    def AddBspline(self, AlibreScript.API.Bspline3D: Any) -> None:
        """Adds a Bspline to the sketch"""
        pass
    @abstractmethod
    def SavetoXml(self, System.String: Any) -> None:
        """Saves the sketch to an XML file"""
        pass
    @abstractmethod
    def LoadXml(self, System.String: Any) -> None:
        """Loads the sketch from an XML file"""
        pass
    @abstractmethod
    def FromXml(self, System.String: Any) -> None:
        """Adds elements to the sketch from XML"""
        pass
class SketchPoint(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates a new sketch point which can be added to sketches"""
        pass
class SketchPoint3D(ABC):
    """Generated stub class"""
    @abstractmethod
    def #ctor(self, System.Double: Any, System.Double: Any, System.Double: Any, System.Boolean: Any) -> None:
        """Creates a new 3D sketch point which can be added to sketches"""
        pass
class ThreeD(ABC):
    """Generated stub class"""
    @abstractmethod
    def GetPerpendicularVector(self, IronPython.Runtime.List: Any) -> None:
        """Gets a vector that is perpendicular to a vector"""
        pass
    @abstractmethod
    def TransformPointUsingVectors(self, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any, IronPython.Runtime.List: Any) -> None:
        """Transforms a point based on two vectors"""
        pass
