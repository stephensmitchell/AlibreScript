# Generated type stubs for the Alibre Script API.
# Source: AlibreScriptAddOn 6.1.0.0 + AlibreScriptAPI.xml
# Do not hand-edit: regenerate with tools/generate_stubs_from_model.py.
from typing import Any, Dict, List, Optional, overload

ScriptFileName: str
"""Full path of the running script."""
ScriptFolder: str
"""Folder containing the running script."""

class IAssembled:
    def GetMappedOccurrence(self, Assembly: Any) -> Any: ...

class IAxis:
    def AxisObject(self) -> Any: ...
    def GetOccurrence(self) -> Any:
        """Gets the part occurrence for this instance

        Returns:
            Occurrence of part
        """
        ...

class IChamferable:
    def ChamferableObject(self) -> Any: ...

class IConstrainable:
    def ConstraintObject(self) -> Any: ...

class IFilletable:
    def FilletableObject(self) -> Any: ...

class IPlane:
    def GetOccurrence(self) -> Any:
        """Gets the part occurrence for this instance

        Returns:
            Occurrence of part
        """
        ...
    def PlaneObject(self) -> Any: ...

class IPoint:
    def GetOccurrence(self) -> Any:
        """Gets the part occurrence for this instance

        Returns:
            Occurrence of part
        """
        ...
    def PointObject(self) -> Any:
        """Low level object that represents the point"""
        ...

class ISelectableGeometry:
    def SelectableObject(self) -> Any: ...

class ISketchFigure:
    def FigureObject(self) -> Any: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToXml(self) -> Any: ...

class ISketchSurface:
    def SurfaceObject(self) -> Any: ...

class ISweepPath:
    def PathObject(self) -> Any: ...

class Part:
    class DirectionType:
        Axis: Part.DirectionType
        Edge: Part.DirectionType
        Normal: Part.DirectionType

    class EndCondition:
        EntirePath: Part.EndCondition
        MidPlane: Part.EndCondition
        ThroughAll: Part.EndCondition
        ToDepth: Part.EndCondition
        ToGeometry: Part.EndCondition
        ToNext: Part.EndCondition

    class FileTypes:
        AlibreDesignPart: Part.FileTypes
        GeomagicDesignPart: Part.FileTypes
        IGES: Part.FileTypes
        SAT: Part.FileTypes
        STEP: Part.FileTypes
        STL_cm: Part.FileTypes
        STL_in: Part.FileTypes
        STL_mm: Part.FileTypes
        ThreeDM: Part.FileTypes

    Axes: Any
    Features: Any
    Planes: Any
    Points: Any
    Sketches: Any
    Sketches3D: Any
    _Part: Any
    _SelectionSession: Any
    Comment: str
    """Comment property"""
    ConfigurationList: Any
    Configurations: List[Any]
    """List of configurations defined on the part (read-only)"""
    CostCenter: str
    """Cost center property"""
    CreatedBy: str
    """Created By property"""
    CreatedDate: str
    """Created Date property"""
    CreatingApplication: str
    """Creating Application property"""
    Density: float
    """Density of the part"""
    Description: str
    """Description of the part"""
    DocumentNumber: str
    """Document Number property"""
    Edges: Any
    EngineeringApprovalDate: str
    """Engineering Approval Date property"""
    EngineeringApprovedBy: str
    """Engineering Approved By property"""
    EstimatedCost: str
    """Estimated Cost property"""
    ExtendedMaterialInformation: str
    """Material (extended information) property"""
    Faces: Any
    FileName: str
    """Path and filename of the part (read-only)"""
    Keywords: str
    """Keywords property"""
    LastAuthor: str
    """Last Author property"""
    LastUpdateDate: str
    """Last Update Date property"""
    ManufacturingApprovedBy: str
    """Manufacturing Approved By property"""
    ManufacturingApprovedDate: str
    """Product property"""
    Mass: float
    """Mass of the part (read-only)"""
    Material: str
    """Material of the part"""
    ModifiedInformation: str
    """Modified Information property"""
    Name: str
    """Name of the part (read-only)"""
    Number: str
    """User-defined number for the part"""
    Origin: Point
    """Gets the origin (language independent) (read-only)"""
    ParameterList: Any
    Parameters: List[Any]
    """List of parameters defined on the part (read-only)"""
    Product: str
    """Product property"""
    ReceivedFrom: str
    """Received From property"""
    Revision: str
    """Revision property"""
    Selections: List[Any]
    """Gets the currently selected items as [ItemA, ItemB, ...] Supports faces, edges, vertices, planes, axes and points (read-only)"""
    StockSize: str
    """Stock Size property"""
    Supplier: str
    """Supplier property"""
    Title: str
    """Title property"""
    Vendor: str
    """Vendor property"""
    Vertices: Any
    WebLink: str
    """Web Link property"""
    XAxis: Axis
    """Gets the X-axis (language independent) (read-only)"""
    XYPlane: Plane
    """Gets the XY-plane (language independent) (read-only)"""
    YAxis: Axis
    """Gets the Y-axis (language independent) (read-only)"""
    YZPlane: Plane
    """Gets the YZ-plane (language independent) (read-only)"""
    ZAxis: Axis
    """Gets the Z-axis (language independent) (read-only)"""
    ZXPlane: Plane
    """Gets the ZX-plane (language independent) (read-only)"""
    @overload
    def __init__(self, Folder: str, Name: str) -> None:
        """Opens an existing part

        Args:
            Folder: Folder containing part
            Name: Name of part to open
        """
        ...
    @overload
    def __init__(self, Folder: str, Name: str, HideEditor: bool) -> None:
        """Opens an existing part, optionally hiding the editor

        Args:
            Folder: Folder containing part
            Name: Name of part to open
            HideEditor: True to hide the editor (only valid if part is not already open)
        """
        ...
    @overload
    def __init__(self, Name: str) -> None:
        """Creates a new part

        Args:
            Name: Name of new part
        """
        ...
    @overload
    def __init__(self, Name: str, CreateNew: bool) -> None:
        """Creates a new part or accesses an already opened part

        Args:
            Name: Name of part to create or access
            CreateNew: True to create a new part, false to access an opened part
        """
        ...
    @overload
    def __init__(self, Name: str, CreateNew: bool, HideEditor: bool) -> None:
        """Creates a new part or accesses an already opened part, optionally hiding the editor

        Args:
            Name: Name of part to create or access
            CreateNew: True to create a new part, false to access an opened part
            HideEditor: True to hide the editor (only valid if CreateNew is true)
        """
        ...
    @overload
    def __init__(self, PartSession: Any) -> None: ...
    @overload
    def __init__(self, FileName: str, Type: Optional[Part.FileTypes]) -> None:
        """Opens or imports an existing file for editing

        Args:
            FileName: Name of file to open
            Type: Type of file (GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
        """
        ...
    @overload
    def __init__(self, FileName: str, Type: Optional[Part.FileTypes], HideEditor: bool) -> None:
        """Opens or imports an existing file for editing, optionally hiding the editor

        Args:
            FileName: Name of file to open
            Type: Type of file (GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
            HideEditor: True to hide the editor
        """
        ...
    def Add3DSketch(self, Name: str) -> Sketch3D:
        """Creates a new 3D sketch

        Args:
            Name: Name of sketch

        Returns:
            Created sketch
        """
        ...
    @overload
    def AddAxis(self, Name: str, Plane1: Optional[ISketchSurface], Plane2: Optional[ISketchSurface]) -> Axis:
        """Creates an axis based on the intersection of two planes/faces

        Args:
            Name: Name of axis
            Plane1: First plane/face
            Plane2: Second plane/face

        Returns:
            New Axis
        """
        ...
    @overload
    def AddAxis(self, Name: str, PointA: Optional[Point], PointB: Optional[Point]) -> Axis:
        """Creates an axis based on two points

        Args:
            Name: Name of axis
            PointA: First point object
            PointB: Second point object

        Returns:
            New axis
        """
        ...
    @overload
    def AddAxis(self, Name: str, CylindricalFace: Optional[Face]) -> Axis:
        """Creates an axis for a cylindrical face

        Args:
            Name: Name of axis
            CylindricalFace: Cylindrical face

        Returns:
            New axis
        """
        ...
    @overload
    def AddAxis(self, Name: str, Point1: List[Any], Point2: List[Any]) -> Axis:
        """Creates an axis based on two points

        Args:
            Name: Name of axis
            Point1: First point [X, Y, Z]
            Point2: Second point [X, Y, Z]

        Returns:
            New axis
        """
        ...
    @overload
    def AddChamfer(self, Name: str, Item: Optional[IChamferable], Distance1: float, Distance2: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge

        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddChamfer(self, Name: str, Items: List[Any], Distance1: float, Distance2: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges

        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddChamfer(self, Name: str, Item: Optional[IChamferable], Distance: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge

        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance: Chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddChamfer(self, Name: str, Items: List[Any], Distance: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges

        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance: Chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddChamferAngle(self, Name: str, Item: Optional[IChamferable], Distance: float, Angle: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge

        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance: Chamfer distance
            Angle: Chamfer angle
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddChamferAngle(self, Name: str, Items: List[Any], Distance: float, Angle: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges

        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance: Chamfer distance
            Angle: Chamfer angle
            TangentPropagate: True to propagate the chamfer along connected edges

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the part

        Args:
            Name: Name of configuration

        Returns:
            New configuration
        """
        ...
    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the part using another configuration as a base

        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use

        Returns:
            New configuration
        """
        ...
    @overload
    def AddExtrudeBoss(self, Name: str, Sketch: Optional[Sketch], Depth: float, IsReversed: bool) -> Feature:
        """Adds a simple extrude boss to a specific depth

        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Extrusion distance
            IsReversed: True if extrusion direction is reversed

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddExtrudeBoss(self, Name: str, Sketch: Optional[Sketch], Depth: float, IsReversed: bool, EndCondition: Optional[Part.EndCondition], EndPlane: Optional[ISketchSurface], EndOffset: float, Direction: Optional[Part.DirectionType], SweepPath: Optional[ISweepPath], DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds an extrude feature

        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Depth of extrusion
            IsReversed: true if direction is reversed
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            Direction: Direction of extrusion
            SweepPath: Sketch or edge to follow when extruding
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddExtrudeCut(self, Name: str, Sketch: Optional[Sketch], Depth: float, IsReversed: bool) -> Feature:
        """Adds a simple extrude cut to a specific depth

        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Extrusion distance
            IsReversed: True if extrusion direction is reversed

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddExtrudeCut(self, Name: str, Sketch: Optional[Sketch], Depth: float, IsReversed: bool, EndCondition: Optional[Part.EndCondition], EndPlane: Optional[ISketchSurface], EndOffset: float, Direction: Optional[Part.DirectionType], SweepPath: Optional[ISweepPath], DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds an extrude cut feature

        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Depth of extrusion
            IsReversed: true if direction is reversed
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            Direction: Direction of extrusion
            SweepPath: Sketch or edge to follow when extruding
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddFillet(self, Name: str, Item: Optional[IFilletable], Radius: float, TangentPropagate: bool) -> Feature:
        """Adds a constant radius fillet to a face or edge

        Args:
            Name: Name of fillet
            Item: Face or edge to fillet
            Radius: Radius of fillet
            TangentPropagate: True to propagate the fillet along connected edges

        Returns:
            Fillet feature
        """
        ...
    @overload
    def AddFillet(self, Name: str, Items: List[Any], Radius: float, TangentPropagate: bool) -> Feature:
        """Adds a constant radius fillet to a set of faces and edges

        Args:
            Name: Name of fillet
            Items: Faces and edges to fillet
            Radius: Radius of fillet
            TangentPropagate: True to propagate the fillet along connected edges

        Returns:
            Fillet feature
        """
        ...
    @overload
    def AddFillet(self, Name: str, Items: List[Any], StartRadii: List[Any], EndRadii: List[Any], TangentPropagate: bool) -> Feature:
        """Adds a variable radius fillet to a set of faces and edges

        Args:
            Name: Name of fillet
            Items: Faces and edges to fillet
            StartRadii: Start radii of fillets
            EndRadii: End radii of fillets
            TangentPropagate: True to propagate the fillet along connected edges

        Returns:
            Fillet feature
        """
        ...
    @overload
    def AddGear(self, Name: str, DiametralPitch: float, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, SingleTooth: bool, CenterX: float, CenterY: float, InvolutePoints: int, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (25.4/module) in teeth per inch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle in current units
            PressureAngle: Pressure angle (14.5 is typical)
            SingleTooth: true to create only a single tooth profile
            CenterX: X-coordinate of gear center
            CenterY: Y-coordinate of gear center
            InvolutePoints: Number of points for involute curve. Decreasing this makes Cubify/Geomagic faster. Increasing makes tooth profiles more accurate and allows gears with more teeth to be generated.
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGear(self, Name: str, DiametralPitch: float, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, SingleTooth: bool, CenterX: float, CenterY: float, InvolutePoints: int, ProfileShiftFactor: float, AddendumCoefficient: float, DedendumCoefficient: float, ClearanceCoefficient: float, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (25.4/module) in teeth per inch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle in current units
            PressureAngle: Pressure angle (14.5 is typical)
            SingleTooth: true to create only a single tooth profile
            CenterX: X-coordinate of gear center
            CenterY: Y-coordinate of gear center
            InvolutePoints: Number of points for involute curve. Decreasing this makes Cubify/Geomagic faster. Increasing makes tooth profiles more accurate and allows gears with more teeth to be generated.
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearDN(self, Name: str, DiametralPitch: float, NumberofTeeth: int, PressureAngle: float, CenterX: float, CenterY: float, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using diametral pitch and number of teeth

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (1/module)
            NumberofTeeth: Number of teeth
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearDN(self, Name: str, DiametralPitch: float, NumberofTeeth: int, PressureAngle: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using diametral pitch and number of teeth

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (1/module)
            NumberofTeeth: Number of teeth
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearDP(self, Name: str, DiametralPitch: float, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (1/module)
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearDP(self, Name: str, DiametralPitch: float, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter

        Args:
            Name: Name of gear sketch
            DiametralPitch: Diametral angle (tooth size) (1/module)
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearNP(self, Name: str, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using number of teeth and pitch diameter

        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddGearNP(self, Name: str, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: Optional[ISketchSurface]) -> GearSketch:
        """Adds a gear sketch to the part using number of teeth and pitch diameter

        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on

        Returns:
            Gear sketch
        """
        ...
    @overload
    def AddLoftBoss(self, Name: str, CrossSections: List[Any], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft extrusion

        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddLoftBoss(self, Name: str, CrossSections: List[Any], GuideCurves: List[Any], GuideType: Optional[GuideCurveTypes], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft extrusion using guide curves

        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            GuideCurves: Python list of guide curves (3D sketches)
            GuideType: Type of guide curve
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddLoftCut(self, Name: str, CrossSections: List[Any], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft cut

        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end

        Returns:
            Cut feature
        """
        ...
    @overload
    def AddLoftCut(self, Name: str, CrossSections: List[Any], GuideCurves: List[Any], GuideType: Optional[GuideCurveTypes], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft cut using guide curves

        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            GuideCurves: Python list of guide curves (3D sketches)
            GuideType: Type of guide curve
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Value: float) -> Parameter:
        """Adds a cm/mm/in/deg parameter to the part

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], UnitstoUse: Optional[ParameterUnits], Value: float) -> Parameter:
        """Adds a parameter to the part with specific units

        Args:
            Name: Name of parameter
            Type: Type of parameter
            UnitstoUse: Units to use
            Value: Value for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Equation: str) -> Parameter:
        """Adds a parameter to the part

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddPlane(self, Name: str, SourcePlane: Optional[ISketchSurface], Offset: float) -> Plane:
        """Creates a plane based on the offset from an existing plane

        Args:
            Name: Name of plane
            SourcePlane: Plane/face to use as basis
            Offset: Offset from basis plane in currently chosen units

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, NormalVector: List[Any], PointonPlane: List[Any]) -> Plane:
        """Adds a plane using a normal vector and a point on the plane

        Args:
            Name: Name of plane to add
            NormalVector: Normal vector as a list [nx, ny, nz]. Does not need to be a unit vector
            PointonPlane: A point on the plane as a list [px, py, pz]

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, Axis: Optional[Axis], Point: Optional[Point]) -> Plane:
        """Creates a new plane contaning an axis and a point

        Args:
            Name: Name of new plane
            Axis: Axis that lies on plane
            Point: Point that lies on plane

        Returns:
            New plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, SourcePlane: Optional[ISketchSurface], RotationAxis: Optional[Axis], Angle: float) -> Plane:
        """Creates a new plane at an angle to an existing plane

        Args:
            Name: Name of new plane
            SourcePlane: Plane/face to use as basis for new plane
            RotationAxis: Axis of rotation for new plane
            Angle: Angle of new plane in degrees

        Returns:
            New plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, Point1: List[Any], Point2: List[Any], Point3: List[Any]) -> Plane:
        """Creates a plane using three points. Each point is defined as list of [x, y, z]

        Args:
            Name: Name of plane
            Point1: Point on plane
            Point2: Point on plane
            Point3: Point on plane

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPoint(self, Name: str, Point: List[Any]) -> Point:
        """Adds a point to the part

        Args:
            Name: Name of the new point
            Point: Point location [x, y, z]

        Returns:
            The new point
        """
        ...
    @overload
    def AddPoint(self, Name: str, Point: Optional[Point]) -> None:
        """Adds a point to the part

        Args:
            Name: Name of the point
            Point: Point to add
        """
        ...
    @overload
    def AddPoint(self, Name: str, X: float, Y: float, Z: float) -> Point:
        """Adds a point to the part

        Args:
            Name: Name of new point
            X: X coordinate
            Y: Y coordinate
            Z: Z coordinate

        Returns:
            The new point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex: Optional[IPoint], XOffset: float, YOffset: float, ZOffset: float) -> Point:
        """Add a point at an offset to a point or a vertex

        Args:
            Name: Name of point
            PointOrVertex: Point or vertex
            XOffset: X offse
            YOffset: Y offset
            ZOffset: Z offset

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex1: Optional[IPoint], PointOrVertex2: Optional[IPoint], Ratio: float) -> Point:
        """Add a point between two points/vertices

        Args:
            Name: Name of point
            PointOrVertex1: First point or vertex
            PointOrVertex2: Second point or vertex
            Ratio: Ratio of distance between points/vertices

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge1: Optional[IAxis], AxisOrEdge2: Optional[IAxis]) -> Point:
        """Add a point at the intersection or two axes or edges

        Args:
            Name: Name of point
            AxisOrEdge1: First axis or edge
            AxisOrEdge2: Second axis or edge

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PlaneOrFace1: Optional[IPlane], PlaneOrFace2: Optional[IPlane], PlaneOrFace3: Optional[IPlane]) -> Point:
        """Add a point at the intersection of three planes or faces

        Args:
            Name: Name of point
            PlaneOrFace1: First plane or face
            PlaneOrFace2: Second plane or face
            PlaneOrFace3: Third plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge: Optional[IAxis], PlaneOrFace: Optional[IPlane]) -> Point:
        """Add a point at the the intersection of a axis or edge and a plane or face

        Args:
            Name: Name of point
            AxisOrEdge: Axis or edge
            PlaneOrFace: Plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, SourcePointOrVertex: Optional[IPoint], TargetPlaneOrFace: Optional[IPlane], XOffset: float, YOffset: float) -> Point:
        """Add a point by projecting a point or vertex onto a plane or face

        Args:
            Name: Name of point
            SourcePointOrVertex: Point or vertex to project
            TargetPlaneOrFace: Plane or face to project onto
            XOffset: X offset to apply to point once projected
            YOffset: Y offset to apply to point once projected

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, TargetEdge: Optional[Edge], Ratio: float) -> Point:
        """Add a point on an edge

        Args:
            Name: Name of point
            TargetEdge: The edge to create the point on
            Ratio: Ratio along the edge from 0.0 -> 1.0

        Returns:
            The created point
        """
        ...
    def AddPointFromCircularEdge(self, Name: str, TargetEdge: Optional[Edge]) -> Point:
        """Adds a point at the center of a circular edge

        Args:
            Name: Name of point
            TargetEdge: The edge to use for creating the point

        Returns:
            The created point
        """
        ...
    def AddPointFromToroidalFace(self, Name: str, TargetFace: Optional[Face]) -> Point:
        """Adds a point at the center of a toroidal face

        Args:
            Name: Name of point
            TargetFace: Toroidal face to use in creating the point

        Returns:
            The created point
        """
        ...
    def AddPoints(self, Prefix: str, Points: List[Any]) -> None:
        """Adds a set of points to the part

        Args:
            Prefix: Prefix for the point names
            Points: List of points [x1,y1,z1, ..., xn,yn,zn]
        """
        ...
    def AddRack(self, Name: str, DiametralPitch: float, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, ProfileShiftFactor: float, AddendumCoefficient: float, DedendumCoefficient: float, ClearanceCoefficient: float, PitchPointtoBase: float, Plane: Optional[ISketchSurface]) -> GearSketch: ...
    def AddRevolveBoss(self, Name: str, Sketch: Optional[Sketch], Axis: Optional[Axis], Angle: float) -> Feature:
        """Creates a revolve boss feature

        Args:
            Name: Name of feature
            Sketch: Sketch to revolve
            Axis: Axis to rotate around
            Angle: Rotation angle in degrees

        Returns:
            Created feature
        """
        ...
    def AddRevolveCut(self, Name: str, Sketch: Optional[Sketch], Axis: Optional[Axis], Angle: float) -> Feature:
        """Creates a revolve cut feature

        Args:
            Name: Name of feature
            Sketch: Sketch to revolve
            Axis: Axis to rotate around
            Angle: Rotation angle in degrees

        Returns:
            Created feature
        """
        ...
    def AddSketch(self, Name: str, Plane: Optional[ISketchSurface]) -> Sketch:
        """Creates a new sketch using a plane/face

        Args:
            Name: Name of sketch
            Plane: Plane/face to use for sketch

        Returns:
            Created sketch
        """
        ...
    def AddSweepBoss(self, Name: str, ProfileSketch: Optional[Sketch], PathSketch: Optional[ISweepPath], IsRigid: bool, EndCondition: Optional[Part.EndCondition], EndPlane: Optional[ISketchSurface], EndOffset: float, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds a sweep extrude feature

        Args:
            Name: Name of extrusion
            ProfileSketch: Sketch to extrude
            PathSketch: Sketch or edge to sweep along
            IsRigid: true if path is parallel to profile
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft

        Returns:
            Extruded feature
        """
        ...
    def AddSweepCut(self, Name: str, ProfileSketch: Optional[Sketch], PathSketch: Optional[ISweepPath], IsRigid: bool, EndCondition: Optional[Part.EndCondition], EndPlane: Optional[ISketchSurface], EndOffset: float, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds a sweep extrude cut feature

        Args:
            Name: Name of extrusion
            ProfileSketch: Sketch to extrude
            PathSketch: Sketch or edge to sweep along
            IsRigid: true if path is parallel to profile
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft

        Returns:
            Extruded feature
        """
        ...
    @overload
    def AddVertexChamfer(self, Name: str, Item: Optional[Vertex], Distance1: float, Distance2: float, Distance3: float) -> Feature:
        """Adds a chamfer to a vertex

        Args:
            Name: Name of chamfer
            Item: Vertex to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            Distance3: Third chamfer distance

        Returns:
            Chamfer feature
        """
        ...
    @overload
    def AddVertexChamfer(self, Name: str, Items: List[Any], Distance1: float, Distance2: float, Distance3: float) -> Feature:
        """Adds a chamfer to a set of vertices

        Args:
            Name: Name of chamfer
            Items: Vertices to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            Distance3: Third chamfer distance

        Returns:
            Chamfer feature
        """
        ...
    def Close(self) -> None:
        """Closes the part If it is unsaved then changes will be lost"""
        ...
    def Debug1(self, Plane: Optional[Plane]) -> None: ...
    def DisplayUnits(self) -> UnitTypes:
        """Gets the display units for the part

        Returns:
            The display units
        """
        ...
    def ExportBIP(self, FileName: str) -> None:
        """Exports a keyshot file

        Args:
            FileName: Path and name of keyshot file
        """
        ...
    def ExportIGES(self, FileName: str) -> None:
        """Exports the part as a IGES file

        Args:
            FileName: Path and name of IGES file
        """
        ...
    def ExportRotatedSTL(self, FileName: str, BottomFace: Optional[Face], ForcetoMillimeters: bool, UseCustomSettings: bool, MaxCellSize: float, NormalDeviation: float, SurfaceDeviation: float) -> None:
        """Exports the part as an STL rotated so that a specific face is on the bottom

        Args:
            FileName: Path and name of STL file
            BottomFace: Face to use as bottom of part
            ForcetoMillimeters: true to output STL in millimeters regardless of part units
            UseCustomSettings: true to use custom STL settings, false to use settings in system properties
            MaxCellSize: Custom max cell size
            NormalDeviation: Custom normal deviation
            SurfaceDeviation: Custom surface deviation
        """
        ...
    def ExportSAT(self, FileName: str, Version: int, SaveColors: bool) -> None:
        """Exports the part as a SAT file

        Args:
            FileName: Path and name of SAT file
            Version: Exported SAT file version
            SaveColors: true to preseve colors
        """
        ...
    def ExportSTEP203(self, FileName: str) -> None:
        """Exports the part as a STEP 203 file

        Args:
            FileName: Path and name of STEP 203 file
        """
        ...
    def ExportSTEP214(self, FileName: str) -> None:
        """Exports the part as a STEP 214 file

        Args:
            FileName: Path and name of STEP 214 file
        """
        ...
    def ExportSTL(self, FileName: str) -> None:
        """Exports the part as an STL file

        Args:
            FileName: Path and name of STL file
        """
        ...
    def Get3DSketch(self, Name: str) -> Sketch3D:
        """Gets a sketch using the name of the sketch

        Args:
            Name: Name of sketch

        Returns:
            Sketch object
        """
        ...
    def GetActiveConfiguration(self) -> Configuration:
        """Gets the currently active configuration

        Returns:
            Configuration object
        """
        ...
    @overload
    def GetAxis(self, Name: str) -> Axis:
        """Gets an axis from an axis name

        Args:
            Name: Name of axis to find

        Returns:
            Found axis
        """
        ...
    @overload
    def GetAxis(self, DesignAxis: Any) -> Axis:
        """Gets an axis from an axis name

        Returns:
            Found axis
        """
        ...
    def GetBoundingBox(self) -> List[Any]:
        """Gets the bounding box for the part as eight points

        Returns:
            Python list of eight points as [P1, P2, ... P8]. Each point is [X, Y, Z]
        """
        ...
    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name

        Args:
            Name: Name of confguration

        Returns:
            Configuration object
        """
        ...
    def GetCustomProperty(self, Name: str) -> str:
        """Gets the value of a custonm property

        Args:
            Name: Name of the custom property

        Returns:
            The value of the property as a string
        """
        ...
    def GetEdge(self, Name: str) -> Edge:
        """Gets an edge using it's name "Edge<n>"

        Args:
            Name: Name of edge

        Returns:
            Edge if found
        """
        ...
    def GetEdges(self) -> List[Any]:
        """Gets a python list of the current edges in the part

        Returns:
            Python list of edges
        """
        ...
    def GetFace(self, Name: str) -> Face:
        """Gets a face using it's name "Face<n>"

        Args:
            Name: Name of face

        Returns:
            Face if found
        """
        ...
    def GetFaces(self) -> List[Any]:
        """Gets a python list of the current faces in the part

        Returns:
            Python list of faces
        """
        ...
    def GetFeature(self, Name: str) -> Feature:
        """Gets a feature on the part

        Args:
            Name: Name of the feature to get

        Returns:
            The feature or null if not found
        """
        ...
    def GetParameter(self, Name: str) -> Parameter:
        """Gets a parameter with a specific name

        Args:
            Name: Name of parameter

        Returns:
            Parameter object
        """
        ...
    @overload
    def GetPlane(self, Name: str) -> Plane:
        """Gets a plane using the name of the plane

        Args:
            Name: Name of plane to find

        Returns:
            The plane
        """
        ...
    @overload
    def GetPlane(self, DesignPlane: Any) -> Plane:
        """Gets a plane using the name of the plane

        Returns:
            The plane
        """
        ...
    @overload
    def GetPoint(self, Name: str) -> Point:
        """Gets a point on the part using the point name. The point must have been created in a script

        Args:
            Name: Name of point to get

        Returns:
            Point on the part
        """
        ...
    @overload
    def GetPoint(self, DesignPoint: Any) -> Point:
        """Gets a point on the part using the point name. The point must have been created in a script

        Returns:
            Point on the part
        """
        ...
    def GetSelection(self) -> Any: ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the part was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def GetSketch(self, Name: str) -> Sketch:
        """Gets a sketch using the name of the sketch

        Args:
            Name: Name of sketch

        Returns:
            Sketch object
        """
        ...
    def GetUserData(self, Name: str) -> Dict[Any, Any]:
        """Gets user data

        Args:
            Name: Name of data to get

        Returns:
            Data as a python dictionary or None if not found
        """
        ...
    def GetVertex(self, Name: str) -> Vertex:
        """Gets a vertex using it's name "Vertex<n>"

        Args:
            Name: Name of vertex

        Returns:
            Vertex if found
        """
        ...
    def GetVertices(self) -> List[Any]:
        """Gets a python list of the current vertices in the part

        Returns:
            Python list of vertices
        """
        ...
    @overload
    def HideFeature(self, Name: str) -> None:
        """Hides a feature on the part

        Args:
            Name: Name of the feature to hide
        """
        ...
    @overload
    def HideFeature(self, Feature: Optional[Feature]) -> None:
        """Hides a feature on the part

        Args:
            Feature: Feature to hide
        """
        ...
    def IsOpen(self) -> bool:
        """Checks if the part is opened"""
        ...
    def NonUniformScale(self, Name: str, ScaleAboutCenter: bool, ScaleFactorX: float, ScaleFactorY: float, ScaleFactorZ: float) -> Feature:
        """Non-uniform scaling of the part

        Args:
            Name: Name of the scaling
            ScaleAboutCenter: true to scale around the center of the part
            ScaleFactorX: X scale factor
            ScaleFactorY: Y scale factor
            ScaleFactorZ: Z scale factor

        Returns:
            Scale feature
        """
        ...
    def PauseUpdating(self) -> None:
        """Pauses updating the part user interface"""
        ...
    def Regenerate(self) -> None:
        """Regenerates the part"""
        ...
    @overload
    def RemoveFeature(self, Name: str) -> None:
        """Removes a feature from the part

        Args:
            Name: Name of the feature to remove
        """
        ...
    @overload
    def RemoveFeature(self, Feature: Optional[Feature]) -> None:
        """Removes a feature from the part

        Args:
            Feature: Feature to remove
        """
        ...
    def RemovePlane(self, Plane: Optional[Plane]) -> None:
        """Removes a plane from the part

        Args:
            Plane: Plane to remove
        """
        ...
    def RemovePoint(self, Point: Optional[Point]) -> None:
        """Removes a point from the part

        Args:
            Point: Point to remove
        """
        ...
    @overload
    def RemoveSketch(self, Name: str) -> None:
        """Removes a sketch from the part

        Args:
            Name: Name of sketch to remove
        """
        ...
    @overload
    def RemoveSketch(self, Sketch: Optional[Sketch]) -> None:
        """Removes a sketch from the part

        Args:
            Sketch: Sketch to remove
        """
        ...
    def ResumeUpdating(self) -> None:
        """Resumes updating the part user interface"""
        ...
    @overload
    def Save(self) -> None:
        """Saves the part using the current path and file name"""
        ...
    @overload
    def Save(self, Folder: str) -> None:
        """Saves the part to a specific folder

        Args:
            Folder: Folder to save to
        """
        ...
    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the part to a specific folder with a new name

        Args:
            Folder: Folder to save to
            NewName: New name for part
        """
        ...
    def SaveSnapshot(self, FileName: str, Width: int, Height: int, UseAspectRatio: bool, UseWidthandHeight: bool) -> None:
        """Saves the current view as a bitmap image

        Args:
            FileName: Path and name of file to save to
            Width: Width in pixels
            Height: Height in pixels
            UseAspectRatio: if true uses greater of width/height along with current aspect ratio
            UseWidthandHeight: if true uses current width/height of view
        """
        ...
    def SaveThumbnail(self, FileName: str, Width: int, Height: int) -> None:
        """Saves a thumbnail image of the part

        Args:
            FileName: Path and name of file to save to
            Width: Width of thumbnail in pixels
            Height: Height of thumbnail in pixels
        """
        ...
    def Scale(self, Name: str, ScaleAboutCenter: bool, ScaleFactor: float) -> Feature:
        """Uniform scaling of the part

        Args:
            Name: Name of the scaling
            ScaleAboutCenter: true to scale around the center of the part
            ScaleFactor: Scale factor

        Returns:
            Scale feature
        """
        ...
    @overload
    def Select(self, FaceorEdge: Optional[ISelectableGeometry]) -> None:
        """Selects a face, edge, vertex, point, axis, plane, sketch

        Args:
            FaceorEdge: Face, edge, vertex, point, axis plane or sketch to select
        """
        ...
    @overload
    def Select(self, FacesEdgesList: List[Any]) -> None:
        """Selects a group of faces, edges, vertices, points, axes, planes and sketches

        Args:
            FacesEdgesList: List of Faces, edges, vertices, points, axes, planes and sketches to select [FaceA, FaceB, EdgeA, EdgeB, ...]
        """
        ...
    def SetColor(self, Red: int, Green: int, Blue: int) -> None:
        """Sets the color of the part

        Args:
            Red: Red component 0 - 255
            Green: Green component 0 - 255
            Blue: Blue component 0 - 255
        """
        ...
    def SetCustomProperty(self, Name: str, Value: str) -> None:
        """Sets the value of a custom property The custom property must already be defined on the part or defined on the user's PC

        Args:
            Name: Name of the custom property
            Value: New value for the custom property
        """
        ...
    def SetUserData(self, Name: str, Dict: Dict[Any, Any]) -> None:
        """Sets user data

        Args:
            Name: Data name of the format companyname.projectname.dataname
            Dict: Python dictionary of data to store
        """
        ...
    @overload
    def ShowFeature(self, Name: str) -> None:
        """Shows a feature on the part

        Args:
            Name: Name of the feature to show
        """
        ...
    @overload
    def ShowFeature(self, Feature: Optional[Feature]) -> None:
        """Shows a feature on the part

        Args:
            Feature: Feature to show
        """
        ...
    @overload
    def SuppressFeature(self, Name: str) -> None:
        """Suppresses a feature on the part

        Args:
            Name: Name of the feature to suppress
        """
        ...
    @overload
    def SuppressFeature(self, Feature: Optional[Feature]) -> None:
        """Suppresses a feature on the part

        Args:
            Feature: Feature to suppress
        """
        ...
    def ToString(self) -> str: ...
    @overload
    def UnsuppressFeature(self, Name: str) -> None:
        """Unsuppresses a feature on the part

        Args:
            Name: Name of the feature to unsuppress
        """
        ...
    @overload
    def UnsuppressFeature(self, Feature: Optional[Feature]) -> None:
        """Unsuppresses a feature on the part

        Args:
            Feature: Feature to unsuppress
        """
        ...

class Assembly:
    class ConstraintBoundsType:
        Between: Assembly.ConstraintBoundsType
        Equals: Assembly.ConstraintBoundsType
        GreaterOrEquals: Assembly.ConstraintBoundsType
        LessOrEquals: Assembly.ConstraintBoundsType

    Axes: Any
    Planes: Any
    Points: Any
    _Assembly: Any
    Comment: str
    """Comment property"""
    ConfigurationList: Any
    Configurations: List[Any]
    """A list of configurations defined on the assembly (read-only)"""
    CostCenter: str
    """Cost center property"""
    CreatedBy: str
    """Created By property"""
    CreatedDate: str
    """Created Date property"""
    CreatingApplication: str
    """Creating Application property"""
    Density: float
    """Density of the part"""
    Description: str
    """Description of the part"""
    DocumentNumber: str
    """Document Number property"""
    EngineeringApprovalDate: str
    """Engineering Approval Date property"""
    EngineeringApprovedBy: str
    """Engineering Approved By property"""
    EstimatedCost: str
    """Estimated Cost property"""
    ExtendedMaterialInformation: str
    """Material (extended information) property"""
    FileName: str
    """Path and filename of the assembly (read-only)"""
    Keywords: str
    """Keywords property"""
    LastAuthor: str
    """Last Author property"""
    LastUpdateDate: str
    """Last Update Date property"""
    ManufacturingApprovedBy: str
    """Manufacturing Approved By property"""
    ManufacturingApprovedDate: str
    """Product property"""
    Material: str
    """Material of the part"""
    ModifiedInformation: str
    """Modified Information property"""
    Name: str
    """Name of the assembly (read-only)"""
    Number: str
    """User-defined number for the part"""
    Origin: Point
    """Gets the origin (language independent) (read-only)"""
    ParameterList: Any
    Parameters: List[Any]
    """A list of parameters defined on the assembly (read-only)"""
    PartList: Any
    Parts: List[Any]
    """A list of parts defined on the assembly (read-only)"""
    Product: str
    """Product property"""
    ReceivedFrom: str
    """Received From property"""
    Revision: str
    """Revision property"""
    Selections: List[Any]
    """Gets the currently selected items as [ItemA, ItemB, ...] Supports subassemblies, parts, faces, edges, vertices, planes, axes and points (read-only)"""
    StockSize: str
    """Stock Size property"""
    SubAssemblies: List[Any]
    """A list of subassemblies defined on the assembly (read-only)"""
    SubAssemblyList: Any
    Supplier: str
    """Supplier property"""
    Title: str
    """Title property"""
    Vendor: str
    """Vendor property"""
    WebLink: str
    """Web Link property"""
    XAxis: Axis
    """Gets the X-axis (language independent) (read-only)"""
    XYPlane: Plane
    """Gets the XY-plane (language independent) (read-only)"""
    YAxis: Axis
    """Gets the Y-axis (language independent) (read-only)"""
    YZPlane: Plane
    """Gets the YZ-plane (language independent) (read-only)"""
    ZAxis: Axis
    """Gets the Z-axis (language independent) (read-only)"""
    ZXPlane: Plane
    """Gets the ZX-plane (language independent) (read-only)"""
    @overload
    def __init__(self, Folder: str, Name: str) -> None:
        """Opens an existing assembly

        Args:
            Folder: Folder containing assembly
            Name: Name of assembly to open
        """
        ...
    @overload
    def __init__(self, Folder: str, Name: str, HideEditor: bool) -> None:
        """Opens an existing assembly, optionally hiding the editor

        Args:
            Folder: Folder containing assembly
            Name: Name of assembly to open
            HideEditor: True to hide the editor
        """
        ...
    @overload
    def __init__(self, Name: str) -> None:
        """Creates a new assembly

        Args:
            Name: Name of new assembly
        """
        ...
    @overload
    def __init__(self, Name: str, CreateNew: bool) -> None:
        """Creates a new assembly or accesses an already opened assembly

        Args:
            Name: Name of assembly to create or access
            CreateNew: True to create a new assembly, false to access an opened assembly
        """
        ...
    @overload
    def __init__(self, Name: str, CreateNew: bool, HideEditor: bool) -> None:
        """Creates a new assembly or accesses an already opened assembly, optionally hiding the editor

        Args:
            Name: Name of assembly to create or access
            CreateNew: True to create a new assembly, false to access an opened assembly
            HideEditor: True to hide the editor (only valid if assembly is not already open)
        """
        ...
    @overload
    def __init__(self, AssemblySession: Any) -> None: ...
    @overload
    def AddAlignConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable]) -> None:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...
    @overload
    def AddAlignConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    def AddAlignConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str, BoundsType: Optional[Assembly.ConstraintBoundsType]) -> None:
        """Adds an alignment constraint between two planes/faces/axes/edges/points Uses bounds type

        Args:
            Distance1: Align distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...
    @overload
    def AddAngleConstraint(self, Angle: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable]) -> None:
        """Adds an angle constraint between two planes/faces/axes/edges/points

        Args:
            Angle: Angle in degrees
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...
    @overload
    def AddAngleConstraint(self, Angle: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a simple angle constraint between two planes/faces/axes/edges/points

        Args:
            Angle: Angle in degrees
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    def AddAngleConstraint2(self, Angle1: float, Angle2: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str, BoundsType: Optional[Assembly.ConstraintBoundsType]) -> None:
        """Adds an angle constraint between two planes/faces/axes/edges/points Uses bounds type

        Args:
            Angle1: Angle for constraint
            Angle2: Second angle for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...
    @overload
    def AddAxis(self, Name: str, Plane1: Optional[ISketchSurface], Plane2: Optional[ISketchSurface]) -> Axis:
        """Creates an axis based on the intersection of two planes/faces

        Args:
            Name: Name of axis
            Plane1: First plane/face
            Plane2: Second plane/face

        Returns:
            New Axis
        """
        ...
    @overload
    def AddAxis(self, Name: str, Point1: List[Any], Point2: List[Any]) -> Axis:
        """Creates an axis based on two points

        Args:
            Name: Name of axis
            Point1: First point
            Point2: Second point

        Returns:
            New axis
        """
        ...
    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the assembly

        Args:
            Name: Name of configuration

        Returns:
            New configuration
        """
        ...
    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the assembly using another configuration as a base

        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use

        Returns:
            New configuration
        """
        ...
    def AddFastenerConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a fastner constraint

        Args:
            Distance: Fastener to surface mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    def AddFastenerConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str, BoundsType: Optional[Assembly.ConstraintBoundsType]) -> None:
        """Adds a fastner constraint

        Args:
            Distance1: Fastener to surface mate distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...
    def AddGearConstraint(self, RatioA: float, RatioB: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a gear constraint using ratio RatioA:RatioB

        Args:
            RatioA: First value in gear ratio
            RatioB: Second value in gear ratio
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    @overload
    def AddMateConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable]) -> None:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...
    @overload
    def AddMateConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    def AddMateConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str, BoundsType: Optional[Assembly.ConstraintBoundsType]) -> None:
        """Adds a mate constraint between two planes/faces/axes/edges/points Uses bounds type

        Args:
            Distance1: Mate distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...
    def AddNewPart(self, Name: str, X: float, Y: float, Z: float) -> AssembledPart:
        """Adds a new part to the assembly

        Args:
            Name: Name of the new part
            X: X location of part
            Y: Y location of part
            Z: Z location of part

        Returns:
            New part
        """
        ...
    def AddNewSubAssembly(self, Name: str, X: float, Y: float, Z: float) -> AssembledSubAssembly:
        """Adds a new sub-assembly to the assembly

        Args:
            Name: Name of the new assembly
            X: X location of assembly
            Y: Y location of assembly
            Z: Z location of assembly

        Returns:
            New part
        """
        ...
    @overload
    def AddOrientConstraint(self, Value: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable]) -> None:
        """Adds an orient constraint between two planes/faces/axes/edges/points

        Args:
            Value: Value
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...
    @overload
    def AddOrientConstraint(self, Value: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds an orient constraint between two planes/faces/axes/edges/points

        Args:
            Value: Value
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Value: float) -> Parameter:
        """Adds a parameter to the assembly

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Equation: str) -> Parameter:
        """Adds a parameter to the assembly NOTE: DOESN'T SEEM TO WORK IN GD V16 - THROWS EXCEPTION ABOUT TRANSACTION ALREADY BEING OPEN

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddPart(self, Folder: str, Name: str) -> AssembledPart:
        """Adds a part to the assembly at the origin

        Args:
            Folder: Folder containing part
            Name: Name of part to open

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            Folder: Folder containing part
            Name: Name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            Folder: Folder containing part
            Name: Name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, Part: Optional[Part]) -> AssembledPart:
        """Adds a part to the assembly at the origin

        Args:
            Part: Part to add

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, Part: Optional[Part], OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            Part: Part to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, FileName: str) -> AssembledPart:
        """Adds a part to the assembly at the origin

        Args:
            FileName: Path and name of part to open

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            FileName: Path and name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            FileName: Path and name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added part
        """
        ...
    @overload
    def AddPart(self, Part: Optional[Part], OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Adds a part to the assembly

        Args:
            Part: Part to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added part
        """
        ...
    @overload
    def AddPlane(self, Name: str, SourcePlane: Optional[ISketchSurface], Offset: float) -> Plane:
        """Creates a plane based on the offset from an existing plane

        Args:
            Name: Name of plane
            SourcePlane: Plane/face to use as basis
            Offset: Offset from basis plane in currently chosen units

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, NormalVector: List[Any], PointonPlane: List[Any]) -> Plane:
        """Adds a plane using a normal vector and a point on the plane

        Args:
            Name: Name of plane to add
            NormalVector: Normal vector as a list [nx, ny, nz]. Does not need to be a unit vector
            PointonPlane: A point on the plane as a list [px, py, pz]

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, SourcePlane: Optional[ISketchSurface], RotationAxis: Optional[Axis], Angle: float) -> Plane:
        """Creates a new plane at an angle to an existing plane

        Args:
            Name: Name of new plane
            SourcePlane: Plane/face to use as basis for new plane
            RotationAxis: Axis of rotation for new plane
            Angle: Angle of new plane in degrees

        Returns:
            New plane
        """
        ...
    @overload
    def AddPlane(self, Name: str, Point1: List[Any], Point2: List[Any], Point3: List[Any]) -> Plane:
        """Creates a plane using three points

        Args:
            Name: Name of plane
            Point1: Point on plane
            Point2: Point on plane
            Point3: Point on plane

        Returns:
            Created plane
        """
        ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex: Optional[IPoint], XOffset: float, YOffset: float, ZOffset: float) -> Point:
        """Add a point at an offset to a point or a vertex

        Args:
            Name: Name of point
            PointOrVertex: Point or vertex
            XOffset: X offse
            YOffset: Y offset
            ZOffset: Z offset

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex1: Optional[IPoint], PointOrVertex2: Optional[IPoint], Ratio: float) -> Point:
        """Add a point between two points/vertices

        Args:
            Name: Name of point
            PointOrVertex1: First point or vertex
            PointOrVertex2: Second point or vertex
            Ratio: Ratio of distance between points/vertices

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge1: Optional[IAxis], AxisOrEdge2: Optional[IAxis]) -> Point:
        """Add a point at the intersection or two axes or edges

        Args:
            Name: Name of point
            AxisOrEdge1: First axis or edge
            AxisOrEdge2: Second axis or edge

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PlaneOrFace1: Optional[IPlane], PlaneOrFace2: Optional[IPlane], PlaneOrFace3: Optional[IPlane]) -> Point:
        """Add a point at the intersection of three planes or faces

        Args:
            Name: Name of point
            PlaneOrFace1: First plane or face
            PlaneOrFace2: Second plane or face
            PlaneOrFace3: Third plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge: Optional[IAxis], PlaneOrFace: Optional[IPlane]) -> Point:
        """Add a point at the the intersection of a axis or edge and a plane or face

        Args:
            Name: Name of point
            AxisOrEdge: Axis or edge
            PlaneOrFace: Plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, SourcePointOrVertex: Optional[IPoint], TargetPlaneOrFace: Optional[IPlane], XOffset: float, YOffset: float) -> Point:
        """Add a point by projecting a point or vertex onto a plane or face

        Args:
            Name: Name of point
            SourcePointOrVertex: Point or vertex to project
            TargetPlaneOrFace: Plane or face to project onto
            XOffset: X offset to apply to point once projected
            YOffset: Y offset to apply to point once projected

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, TargetEdge: Optional[Edge], Ratio: float) -> Point:
        """Add a point on an edge

        Args:
            Name: Name of point
            TargetEdge: The edge to create the point on
            Ratio: Ratio along the edge from 0.0 -> 1.0

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, X: float, Y: float, Z: float) -> Point:
        """Adds a point to the assembly

        Args:
            Name: Name of new point
            X: X coordinate
            Y: Y coordinate
            Z: Z coordinate

        Returns:
            The new point
        """
        ...
    def AddPointFromCircularEdge(self, Name: str, TargetEdge: Optional[Edge]) -> Point:
        """Adds a point at the center of a circular edge

        Args:
            Name: Name of point
            TargetEdge: The edge to use for creating the point

        Returns:
            The created point
        """
        ...
    def AddPointFromToroidalFace(self, Name: str, TargetFace: Optional[Face]) -> Point:
        """Adds a point at the center of a toroidal face

        Args:
            Name: Name of point
            TargetFace: Toroidal face to use in creating the point

        Returns:
            The created point
        """
        ...
    def AddPoints(self, Prefix: str, Points: List[Any]) -> None:
        """Adds a set of points to the part

        Args:
            Prefix: Prefix for the point names
            Points: List of points [x1,y1,z1, ..., xn,yn,zn]
        """
        ...
    def AddRackAndPinionConstraint(self, PitchDiameter: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a rack and pinion constraint

        Args:
            PitchDiameter: Pitch diameter
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    def AddScrewConstraint(self, ThreadPitch: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], IsReversed: bool, Name: str) -> None:
        """Adds a screw constraint

        Args:
            ThreadPitch: Pitch of thread
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    @overload
    def AddSubAssembly(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            FileName: Path and name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddSubAssembly(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            FileName: Path and name of sub-asembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Assembly: Optional[Assembly]) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly at the origin

        Args:
            Assembly: Assembly to add

        Returns:
            The added assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Assembly: Optional[Assembly], OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            Assembly: Assembly to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Assembly: Optional[Assembly], OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            Assembly: Sub-assembly to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Folder: str, Name: str) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly at the origin

        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddSubAssembly(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly

        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddSubAssembly(self, FileName: str) -> AssembledSubAssembly:
        """Adds a sub-assembly to the assembly at the origin

        Args:
            FileName: Path and name of sub-assembly to open

        Returns:
            The added sub-assembly
        """
        ...
    @overload
    def AddTangentConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], Outside: bool) -> None:
        """Adds a tangent constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            Outside: true for an outside tangent constraint, false for an inside tangent constraint
        """
        ...
    @overload
    def AddTangentConstraint(self, Distance: float, PartorAssemblyA: Optional[IAssembled], ItemA: Optional[IConstrainable], PartorAssemblyB: Optional[IAssembled], ItemB: Optional[IConstrainable], Outside: bool, IsReversed: bool, Name: str) -> None:
        """Adds a tangent constraint between two planes/faces/axes/edges/points

        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            Outside: true for an outside tangent constraint, false for an inside tangent constraint
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...
    @overload
    def AnchorPart(self, Name: str) -> None:
        """Anchors a part

        Args:
            Name: Name of part to anchor
        """
        ...
    @overload
    def AnchorPart(self, Part: Optional[AssembledPart]) -> None:
        """Anchors a part

        Args:
            Part: Part to anchor
        """
        ...
    def AnchorSubAssembly(self, Name: str) -> None:
        """Anchors a sub-assembly

        Args:
            Name: Name of sub-assembly to anchor
        """
        ...
    def Close(self) -> None:
        """Closes the assembly If it is unsaved then changes will be lost"""
        ...
    def CreateUniqueName(self, BaseName: str) -> str:
        """Creates a unique name that can be used to safely add a part or subassembly to the assembly if the names used in the assembly are not known in advance

        Args:
            BaseName: Base name to use

        Returns:
            Unique name
        """
        ...
    def DisplayUnits(self) -> UnitTypes:
        """Gets the display units for the assembly

        Returns:
            The display units
        """
        ...
    @overload
    def DuplicatePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledPart:
        """Duplicates a part in the assembly

        Args:
            Name: Name of part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate part
        """
        ...
    @overload
    def DuplicatePart(self, Part: Optional[AssembledPart], OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledPart:
        """Duplicates a part in the assembly

        Args:
            Part: Part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate part
        """
        ...
    @overload
    def DuplicatePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Duplicates a part in the assembly

        Args:
            Name: Name of part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The duplicate part
        """
        ...
    @overload
    def DuplicatePart(self, Part: Optional[AssembledPart], OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Duplicates a part in the assembly

        Args:
            Part: Part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The duplicate part
        """
        ...
    @overload
    def DuplicatePart(self, PartOcc: Any, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledPart:
        """Duplicates a part in the assembly

        Args:
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate part
        """
        ...
    @overload
    def DuplicateSubAssembly(self, SubAssembly: Optional[AssembledSubAssembly], OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledSubAssembly:
        """Duplicates a sub-assembly in the assembly

        Args:
            SubAssembly: Sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate sub-assembly
        """
        ...
    @overload
    def DuplicateSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> AssembledSubAssembly:
        """Duplicates a sub-assembly in the assembly

        Args:
            Name: Name of sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate sub-assembly
        """
        ...
    @overload
    def DuplicateSubAssembly(self, SubAssembly: Optional[AssembledSubAssembly], OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Duplicates a sub-assembly in the assembly

        Args:
            SubAssembly: Sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The duplicate sub-assembly
        """
        ...
    @overload
    def DuplicateSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Duplicates a sub-assembly in the assembly

        Args:
            Name: Name of sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation

        Returns:
            The duplicate sub-assembly
        """
        ...
    @overload
    def DuplicateSubAssembly(self, AssemOcc: Any, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> AssembledSubAssembly:
        """Duplicates a sub-assembly in the assembly

        Args:
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset

        Returns:
            The duplicate sub-assembly
        """
        ...
    def ExportBIP(self, FileName: str) -> None:
        """Exports a keyshot file

        Args:
            FileName: Path and name of keyshot file
        """
        ...
    def ExportIGES(self, FileName: str) -> None:
        """Exports the assembly as a IGES file

        Args:
            FileName: Path and name of IGES file
        """
        ...
    def ExportSAT(self, FileName: str, Version: int, SaveColors: bool) -> None:
        """Exports the assembly as a SAT file

        Args:
            FileName: Path and name of SAT file
            Version: Exported SAT file version
            SaveColors: true to preseve colors
        """
        ...
    def ExportSTEP203(self, FileName: str) -> None:
        """Exports the assembly as a STEP 203 file

        Args:
            FileName: Path and name of STEP 203 file
        """
        ...
    def ExportSTEP214(self, FileName: str) -> None:
        """Exports the assembly as a STEP 214 file

        Args:
            FileName: Path and name of STEP 214 file
        """
        ...
    def ExportSTL(self, FileName: str) -> None:
        """Exports the assembly as an STL file

        Args:
            FileName: Path and name of STL file
        """
        ...
    def GetActiveConfiguration(self) -> Configuration:
        """Gets the currently active configuration

        Returns:
            Configuration object
        """
        ...
    @overload
    def GetAxis(self, Name: str) -> Axis:
        """Gets an axis from an axis name

        Args:
            Name: Name of axis to find

        Returns:
            Found axis
        """
        ...
    @overload
    def GetAxis(self, DesignAxis: Any) -> Axis:
        """Gets an axis from an axis name

        Returns:
            Found axis
        """
        ...
    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name

        Args:
            Name: Name of confguration

        Returns:
            Configuration object
        """
        ...
    def GetCustomProperty(self, Name: str) -> str:
        """Gets the value of a custonm property

        Args:
            Name: Name of the custom property

        Returns:
            The value of the property as a string
        """
        ...
    def GetParameter(self, Name: str) -> Parameter:
        """Gets a parameter with a specific name

        Args:
            Name: Name of parameter

        Returns:
            Parameter object
        """
        ...
    def GetPart(self, Name: str) -> AssembledPart:
        """Gets a part in the assembly

        Args:
            Name: Name of part instance to get

        Returns:
            The part
        """
        ...
    @overload
    def GetPartOrientation(self, Part: Optional[AssembledPart]) -> List[Any]:
        """Gets the orientation of a part in an assembly

        Args:
            Part: Part in an assembly

        Returns:
            Part orientation as [OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ], translation before rotation
        """
        ...
    @overload
    def GetPartOrientation(self, PartName: str) -> List[Any]:
        """Gets the orientation of a part in an assembly

        Args:
            PartName: Name of part to get orientation

        Returns:
            Part orientation as [OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ], translation before rotation
        """
        ...
    @overload
    def GetPlane(self, Name: str) -> Plane:
        """Gets a plane using the name of the plane

        Args:
            Name: Name of plane to find

        Returns:
            The plane
        """
        ...
    @overload
    def GetPlane(self, DesignPlane: Any) -> Plane:
        """Gets a plane using the name of the plane

        Returns:
            The plane
        """
        ...
    @overload
    def GetPoint(self, Name: str) -> Point:
        """Gets a point on the assembly using the point name. The point must have been created in a script

        Args:
            Name: Name of point to get

        Returns:
            The point
        """
        ...
    @overload
    def GetPoint(self, DesignPoint: Any) -> Point:
        """Gets a point on the assembly using the point name. The point must have been created in a script

        Returns:
            The point
        """
        ...
    def GetSelection(self) -> Any: ...
    def GetSubAssembly(self, Name: str) -> AssembledSubAssembly:
        """Gets a sub-assembly in the assembly

        Args:
            Name: Name of sub-assembly instance to get

        Returns:
            The sub-assembly
        """
        ...
    def GetUserData(self, Name: str) -> Dict[Any, Any]:
        """Gets user data

        Args:
            Name: Name of data to get

        Returns:
            Data as a python dictionary or None if not found
        """
        ...
    @overload
    def HidePart(self, Name: str) -> None:
        """Hides a part

        Args:
            Name: Name of part to hide
        """
        ...
    @overload
    def HidePart(self, Part: Optional[AssembledPart]) -> None:
        """Hides a part

        Args:
            Part: Part to hide
        """
        ...
    def HideSubAssembly(self, Name: str) -> None:
        """Hides a sub-assembly

        Args:
            Name: Name of sub-assembly to hide
        """
        ...
    @overload
    def MovePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a part

        Args:
            Name: Name of part to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def MovePart(self, Part: Optional[AssembledPart], OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a part

        Args:
            Part: Part to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def MovePart(self, PartOcc: Any, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a part

        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    def MoveParts(self, Names: List[Any], OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a set of parts

        Args:
            Names: Names of parts to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    def MoveSubAssemblies(self, Names: List[Any], OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a set of sub-assemblies

        Args:
            Names: Names of sub-assemblies to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def MoveSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a sub-assembly

        Args:
            Name: Name of sub-assembly to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def MoveSubAssembly(self, SubAssembly: Optional[AssembledSubAssembly], OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a sub-assembly

        Args:
            SubAssembly: Sub-assembly to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def MoveSubAssembly(self, AssemOcc: Any, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> None:
        """Moves a sub-assembly

        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...
    def PauseUpdating(self) -> None:
        """Pauses updating the assembly user interface"""
        ...
    def Regenerate(self) -> None:
        """Regenerates the assembly"""
        ...
    def ResumeUpdating(self) -> None:
        """Resumes updating the assembly user interface"""
        ...
    @overload
    def RotatePart(self, Name: str, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a part

        Args:
            Name: Name of part to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def RotatePart(self, Part: Optional[AssembledPart], AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a part

        Args:
            Part: Part to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def RotatePart(self, PartOcc: Any, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a part

        Args:
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    def RotateParts(self, Names: List[Any], AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a set of parts

        Args:
            Names: Names of parts to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    def RotateSubAssemblies(self, Names: List[Any], AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a set of sub-assemblies

        Args:
            Names: Names of sub-assemblies to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def RotateSubAssembly(self, Name: str, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a sub-assembly

        Args:
            Name: Name of sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def RotateSubAssembly(self, SubAssembly: Optional[AssembledSubAssembly], AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a sub-assembly

        Args:
            SubAssembly: Sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def RotateSubAssembly(self, AssemOcc: Any, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> None:
        """Rotates a sub-assembly

        Args:
            AssemOcc: Occurence of sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...
    @overload
    def Save(self) -> None:
        """Saves the assembly using the current path and file name"""
        ...
    @overload
    def Save(self, Folder: str) -> None:
        """Saves the assembly to a specific folder

        Args:
            Folder: Folder to save to
        """
        ...
    def SaveAll(self, Folder: str) -> None:
        """Save the assembly and all parts/sub-assemblies to a folder

        Args:
            Folder: Folder to save to
        """
        ...
    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the assembly to a specific folder with a new name

        Args:
            Folder: Folder to save to
            NewName: New name for assembly
        """
        ...
    def SaveSnapshot(self, FileName: str, Width: int, Height: int, UseAspectRatio: bool, UseWidthandHeight: bool) -> None:
        """Saves the current view as a bitmap image

        Args:
            FileName: Path and mame of file to save to
            Width: Width in pixels
            Height: Height in pixels
            UseAspectRatio: if true uses greater of width/height along with current aspect ratio
            UseWidthandHeight: if true uses current width/height of view
        """
        ...
    def SaveThumbnail(self, FileName: str, Width: int, Height: int) -> None:
        """Saves a thumbnail image of the assembly

        Args:
            FileName: Path and name of file to save to
            Width: Width of thumbnail in pixels
            Height: Height of thumbnail in pixels
        """
        ...
    def SetCustomProperty(self, Name: str, Value: str) -> None:
        """Sets the value of a custom property The custom property must already be defined on the assembly or defined on the user's PC

        Args:
            Name: Name of the custom property
            Value: New value for the custom property
        """
        ...
    def SetUserData(self, Name: str, Dict: Dict[Any, Any]) -> None:
        """Sets user data

        Args:
            Name: Data name of the format companyname.projectname.dataname
            Dict: Python dictionary of data to store
        """
        ...
    @overload
    def ShowPart(self, Name: str) -> None:
        """Shows a part

        Args:
            Name: Name of part to show
        """
        ...
    @overload
    def ShowPart(self, Part: Optional[AssembledPart]) -> None:
        """Shows a part

        Args:
            Part: Part to show
        """
        ...
    def ShowSubAssembly(self, Name: str) -> None:
        """Shows a sub-assembly

        Args:
            Name: Name of sub-assembly to show
        """
        ...
    @overload
    def SuppressPart(self, Name: str) -> None:
        """Suppresses a part

        Args:
            Name: Name of part to suppress
        """
        ...
    @overload
    def SuppressPart(self, Part: Optional[AssembledPart]) -> None:
        """Suppresses a part

        Args:
            Part: Part to suppress
        """
        ...
    def SuppressSubAssembly(self, Name: str) -> None:
        """Suppresses a sub-assembly

        Args:
            Name: Name of sub-assembly to suppress
        """
        ...
    def ToString(self) -> str: ...
    @overload
    def UnanchorPart(self, Name: str) -> None:
        """Un-anchors a part

        Args:
            Name: Name of part to un-anchor
        """
        ...
    @overload
    def UnanchorPart(self, Part: Optional[AssembledPart]) -> None:
        """Un-anchors a part

        Args:
            Part: Part to un-anchor
        """
        ...
    def UnanchorSubAssembly(self, Name: str) -> None:
        """Un-anchors a sub-assembly

        Args:
            Name: Name of sub-assembly to un-anchor
        """
        ...
    @overload
    def UnsuppressPart(self, Name: str) -> None:
        """Un-suppresses a part

        Args:
            Name: Name of part to un-suppress
        """
        ...
    @overload
    def UnsuppressPart(self, Part: Optional[AssembledPart]) -> None:
        """Un-suppresses a part

        Args:
            Part: Part to un-suppress
        """
        ...
    def UnsuppressSubAssembly(self, Name: str) -> None:
        """Un-suppresses a sub-assembly

        Args:
            Name: Name of sub-assembly to un-suppress
        """
        ...

class Sketch(ISelectableGeometry, ISweepPath):
    class Constraints:
        Coincident: Sketch.Constraints
        Collinear: Sketch.Constraints
        Coradial: Sketch.Constraints
        Equal: Sketch.Constraints
        Fix: Sketch.Constraints
        Horizontal: Sketch.Constraints
        Intersection: Sketch.Constraints
        Midpoint: Sketch.Constraints
        Normal: Sketch.Constraints
        Parallel: Sketch.Constraints
        Perpendicular: Sketch.Constraints
        Symmetric: Sketch.Constraints
        Tangent: Sketch.Constraints
        Vertical: Sketch.Constraints

    AutomaticStartEndEditing: bool
    _SelectionSession: Any
    _Sketch: Any
    Figures: List[Any]
    """A list of figures (line, circle, circulararc, bspline, ellipse, elliptical arc) defined on the sketch (read-only)"""
    Name: str
    """Name of the sketch (read-only)"""
    Origin: SketchPoint
    """The point that defines the origin (read-only)"""
    def __init__(self, Sketch: Any) -> None: ...
    def AddArc(self, NewArc: Optional[CircularArc]) -> CircularArc:
        """Adds a circular arc to the sketch

        Args:
            NewArc: Arc to add

        Returns:
            The added circular arc
        """
        ...
    def AddArcCenterStartAngle(self, CenterX: float, CenterY: float, StartX: float, StartY: float, Angle: float, IsReference: bool) -> CircularArc:
        """Adds a circular arc using center, start and angle Arc goes anti-clockwise from start

        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            Angle: Arc angle in degrees
            IsReference: True if arc is a reference figure

        Returns:
            The added circular arc
        """
        ...
    def AddArcCenterStartEnd(self, CenterX: float, CenterY: float, StartX: float, StartY: float, EndX: float, EndY: float, IsReference: bool) -> CircularArc:
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end

        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            EndX: X coordinate for end
            EndY: Y cordinate for end
            IsReference: True if arc is a reference figure

        Returns:
            The added circular arc
        """
        ...
    @overload
    def AddBspline(self, Order: int, ControlPoints: List[Any], KnotVectors: List[Any], Weights: List[Any], IsReference: bool) -> Bspline:
        """Adds a Bspline to the sketch

        Args:
            Order: Order of the Bspline (Degree - 1)
            ControlPoints: List of control points
            KnotVectors: List of knot vectors
            Weights: List of control point weights
            IsReference: True to create a reference bspline

        Returns:
            The created Bspline
        """
        ...
    @overload
    def AddBspline(self, Points: List[Any], IsReference: bool) -> Bspline:
        """Adds a Bspline to the sketch through a set of points

        Args:
            Points: List of points
            IsReference: True to create a reference bspline

        Returns:
            The created Bspline
        """
        ...
    @overload
    def AddBspline(self, NewBspline: Optional[Bspline]) -> Bspline:
        """Adds a new bspline to the sketch

        Args:
            NewBspline: Bspline to add to the sketch

        Returns:
            The added Bspline
        """
        ...
    @overload
    def AddBspline(self, Order: int, ControlPoints: Any, KnotVectors: Any, Weights: Any, IsReference: bool) -> Bspline:
        """Adds a Bspline to the sketch

        Args:
            Order: Order of the Bspline (Degree - 1)
            ControlPoints: List of control points
            KnotVectors: List of knot vectors
            Weights: List of control point weights
            IsReference: True to create a reference bspline

        Returns:
            The created Bspline
        """
        ...
    def AddBsplineInterpolated(self, Points: Any, IsReference: bool) -> Bspline: ...
    def AddBsplineThroughPoints(self, Points: Any, IsReference: bool) -> Bspline: ...
    @overload
    def AddCircle(self, CenterX: float, CenterY: float, Diameter: float, IsReference: bool) -> Circle:
        """Adds a circle to the sketch

        Args:
            CenterX: X coordinate of circle center
            CenterY: Y coordinate of circle center
            Diameter: Circle diameter
            IsReference: True to create a reference circle

        Returns:
            A circle object
        """
        ...
    @overload
    def AddCircle(self, NewCircle: Optional[Circle]) -> Circle:
        """Adds a circle to the sketch

        Args:
            NewCircle: Circle to add to sketch

        Returns:
            The added circle
        """
        ...
    @overload
    def AddConstraint(self, Figure: Optional[ISketchFigure], Constraint: Optional[Sketch.Constraints]) -> bool:
        """Adds a constraint to the sketch

        Args:
            Figure: Figure to constrain (e.g. Line)
            Constraint: Constraint to apply

        Returns:
            True if constraint was added
        """
        ...
    @overload
    def AddConstraint(self, Figures: List[Any], Constraint: Optional[Sketch.Constraints]) -> bool:
        """Adds a constraint to the sketch

        Args:
            Figures: List of Sketch figures to constrain [Figure1, Figure2, ...] (Circle, Line, CircularArc, etc.)
            Constraint: Constraint to apply

        Returns:
            Returns True if constraint was added
        """
        ...
    @overload
    def AddDimension(self, P1: Optional[SketchPoint], P2: Optional[SketchPoint]) -> None:
        """Adds a dimension to the sketch between two points

        Args:
            P1: First point
            P2: Second point
        """
        ...
    @overload
    def AddDimension(self, Circle: Optional[Circle]) -> None:
        """Adds a dimension to the radius of a circle

        Args:
            Circle: Circle to dimension
        """
        ...
    @overload
    def AddDimension(self, Arc: Optional[CircularArc]) -> None:
        """Adds a dimension to the radius of an arc

        Args:
            Arc: Arc to dimension
        """
        ...
    @overload
    def AddEllipse(self, CenterX: float, CenterY: float, MajorX: float, MajorY: float, MinorX: float, MinorY: float, IsReference: bool) -> Ellipse:
        """Adds an ellipse to the sketch using three points

        Args:
            CenterX: X coordinate of ellipse center
            CenterY: Y coordinate of ellipse center
            MajorX: X coordinate of ellipse on major axis
            MajorY: Y coordinate of ellipse on major axis
            MinorX: X coordinate of ellipse on minor axis
            MinorY: Y coordinate of ellipse on minor axis
            IsReference: True to create a reference ellipse

        Returns:
            An ellipse object
        """
        ...
    @overload
    def AddEllipse(self, CenterX: float, CenterY: float, MajorAxisDiameter: float, MinorMajorRatio: float, MajorAxisAngle: float, IsReference: bool) -> Ellipse:
        """Adds an ellipse to the sketch

        Args:
            CenterX: X coordinate of ellipse center
            CenterY: Y coordinate of ellipse center
            MajorAxisDiameter: Diameter of ellipse on major axis
            MinorMajorRatio: Ratio of minor diameter to major diameter
            MajorAxisAngle: Angle of major axis
            IsReference: True to create a reference ellipse

        Returns:
            An ellipse object
        """
        ...
    @overload
    def AddEllipse(self, NewEllipse: Optional[Ellipse]) -> Ellipse:
        """Adds an ellipse to the sketch

        Args:
            NewEllipse: Ellipse to add

        Returns:
            Added ellipse
        """
        ...
    @overload
    def AddEllipticalArc(self, CenterX: float, CenterY: float, StartX: float, StartY: float, EndX: float, EndY: float, MajorAxisDiameter: float, MinorMajorRatio: float, MajorAxisAngle: float, IsReference: bool) -> EllipticalArc:
        """Adds an elliptical arc to the sketch

        Args:
            CenterX: X coordinate of arc center
            CenterY: Y coordinate of arc center
            StartX: X coorindate of arc start
            StartY: Y coordinate of arc start
            EndX: X coordinate of arc end
            EndY: Y coordinate of arc end
            MajorAxisDiameter: Diameter of ellipse on major axis
            MinorMajorRatio: Ratio of minor diameter to major diameter
            MajorAxisAngle: Angle of major axis
            IsReference: True to create a reference elliptical arc

        Returns:
            An elliptical arc object
        """
        ...
    @overload
    def AddEllipticalArc(self, NewEllipticalArc: Optional[EllipticalArc]) -> EllipticalArc:
        """Adds an elliptical arc to the sketch

        Args:
            NewEllipticalArc: Elliptical arc to add

        Returns:
            Added elliptical arc
        """
        ...
    def AddFigure(self, NewFigure: Optional[ISketchFigure]) -> Any:
        """Adds a figure to the sketch

        Args:
            NewFigure: Figure to add

        Returns:
            The added figure
        """
        ...
    @overload
    def AddLine(self, StartPoint: List[Any], EndPoint: List[Any], IsReference: bool) -> Line:
        """Adds a line to the sketch

        Args:
            StartPoint: Start of line [X, Y]
            EndPoint: End of line [X, Y]
            IsReference: true if line is a reference line

        Returns:
            The added line
        """
        ...
    @overload
    def AddLine(self, NewLine: Optional[Line]) -> Line:
        """Adds a line to the sketch

        Args:
            NewLine: 2D line to add

        Returns:
            The added line
        """
        ...
    @overload
    def AddLine(self, X1: float, Y1: float, X2: float, Y2: float, IsReference: bool) -> Line:
        """Adds a line to the sketch

        Args:
            X1: Start point X
            Y1: Start point Y
            X2: End point X
            Y2: End point Y
            IsReference: true to create a reference line

        Returns:
            The added line
        """
        ...
    def AddLines(self, Points: List[Any], IsReference: bool) -> None:
        """Adds a polyline to the sketch

        Args:
            Points: Set of points [Point1X, Point1Y, Point2X, Point2Y, ...]
            IsReference: true if line is a reference line
        """
        ...
    @overload
    def AddPoint(self, X: float, Y: float) -> SketchPoint:
        """Adds a point to the sketch

        Args:
            X: Point X coordinate
            Y: Point Y coordinate

        Returns:
            The created sketch point
        """
        ...
    @overload
    def AddPoint(self, X: float, Y: float, IsReference: bool) -> SketchPoint:
        """Adds a point to the sketch [DEPRECATED - DO NOT USE]

        Args:
            X: Point X coordinate
            Y: Point Y coordinate
            IsReference: Set to false

        Returns:
            The added point
        """
        ...
    @overload
    def AddPoint(self, NewPoint: Optional[SketchPoint]) -> SketchPoint:
        """Adds a point to the sketch

        Args:
            NewPoint: Point to add

        Returns:
            The added point
        """
        ...
    def AddPolygon(self, CenterX: float, CenterY: float, Diameter: float, Sides: int, IsReference: bool) -> None:
        """Adds a regular polygon to the sketch

        Args:
            CenterX: X coordinate for polygon center
            CenterY: Y coordinate for polygon center
            Diameter: Diameter of polygon
            Sides: Number of sides
            IsReference: True to create a reference polygon
        """
        ...
    def AddPolyhole(self, CenterX: float, CenterY: float, Diameter: float, IsReference: bool) -> None:
        """Adds a polyhole to the sketch Create a "circle" whose size should be accurate regardless of the 3D printing method See: http://hydraraptor.blogspot.co.uk/2011/02/polyholes.html

        Args:
            CenterX: X coordinate for hole center
            CenterY: Y coordinate for hole center
            Diameter: Diameter of hole
            IsReference: true if line is a reference line
        """
        ...
    def AddPolyline(self, Line: Optional[Polyline], IsReference: bool) -> None:
        """Adds a polyline to the sketch

        Args:
            Line: Polyine to add
            IsReference: true if line is a reference line
        """
        ...
    def AddRectangle(self, BottomLeftX: float, BottomLeftY: float, TopRightX: float, TopRightY: float, IsReference: bool) -> None:
        """Adds a rectangle to the sketch

        Args:
            BottomLeftX: X coordinate of bottom left corner
            BottomLeftY: Y coordinate of bottom left corner
            TopRightX: X coordinate of top right
            TopRightY: Y coordinate of top right
            IsReference: True to create a reference rectangle
        """
        ...
    @overload
    def CopyFrom(self, Source: Optional[Sketch]) -> None:
        """Copies a sketch into this sketch

        Args:
            Source: Sketch to copy from
        """
        ...
    @overload
    def CopyFrom(self, Source: Optional[Sketch], Angle: float, RotationCenterX: float, RotationCenterY: float, TranslateX: float, TranslateY: float, ScaleOriginX: float, ScaleOriginY: float, ScaleFactor: float) -> None:
        """Copies a sketch into this sketch

        Args:
            Source: Sketch to copy from
            Angle: Rotation angle
            RotationCenterX: X-coodinate for center of rotation
            RotationCenterY: Y-coordinate for center of rotation
            TranslateX: Amount to move sketch in X direction
            TranslateY: Amount to move sketch in Y direction
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleFactor: Factor for scaling as a percentage
        """
        ...
    def CrossSectionObject(self) -> Any: ...
    @overload
    def ExportSVG(self, FileName: str) -> None:
        """Exports the sketch to an SVG

        Args:
            FileName: Path and name of SVG file to export to
        """
        ...
    @overload
    def ExportSVG(self, FileName: str, IncludeReferences: bool) -> None:
        """Exports the sketch to an SVG

        Args:
            FileName: Path and name of SVG file to export to
            IncludeReferences: true to include reference figures in export
        """
        ...
    @overload
    def ExportSVG(self, FileName: str, IncludeReferences: bool, StrokeWidth: float, StrokeColor: str, StrokeLineCap: str, StrokeDashed: bool, StrokeDashLength: float, ReferenceStrokeWidth: float, ReferenceStrokeColor: str, ReferenceStrokeLineCap: str, ReferenceStrokeDashed: bool, ReferenceStrokeDashLength: float) -> None:
        """Exports the sketch to an SVG with specific styling

        Args:
            FileName: Path and name of SVG file to export to
            IncludeReferences: true to include reference figures in export
            StrokeWidth: Stroke width
            StrokeColor: String containing name of stroke color
            StrokeLineCap: String containing name of stroke line cap type
            StrokeDashed: true if stroke dashed, false if solid
            StrokeDashLength: Length of stroke dashes if dashed
            ReferenceStrokeWidth: Reference stroke width
            ReferenceStrokeColor: String containing name of reference stroke color
            ReferenceStrokeLineCap: String containing name of reference stroke line cap type, can be: butt, round, square
            ReferenceStrokeDashed: true if reference stroke dashed, false if solid
            ReferenceStrokeDashLength: Length of reference stroke dashes if dashed
        """
        ...
    def FromXml(self, Xml: str) -> None:
        """Adds elements to the sketch from XML

        Args:
            Xml: XML to parse
        """
        ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Part that the sketch is defined on

        Returns:
            Part that defines the sketch
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the sketch was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def GetSurface(self) -> ISketchSurface:
        """Gets the surface that the sketch was created on, e.g. a design plane or a face

        Returns:
            Plane or Face object
        """
        ...
    def GlobaltoPoint(self, x: float, y: float, z: float) -> List[Any]:
        """Projects a 3D point in the part coordinate system into a point on the sketch

        Args:
            x: X coordinate of 3D point
            y: Y coordinate of 3D point
            z: Z coordinate of 3D point

        Returns:
            Python list [x, y]
        """
        ...
    @overload
    def ImportSVG(self, FileName: str) -> None:
        """Imports an SVG into the sketch

        Args:
            FileName: Path and name of SVG file
        """
        ...
    @overload
    def ImportSVG(self, FileName: str, TranslateX: float, TranslateY: float, RotationAngle: float, TranslateThenRotate: bool, NativeFigures: bool) -> None:
        """Imports an SVG into the sketch

        Args:
            FileName: Path and name of SVG file
            TranslateX: Amount to translate in the X direction
            TranslateY: Amount to translate in the Y direction
            RotationAngle: Amount to rotate in degrees
            TranslateThenRotate: true to perform translation passed to this function before rotation passed to this function, false to reverse order
            NativeFigures: true to create native circles and arcs when possible, false to always use Bezier curves
        """
        ...
    def LoadXml(self, FileName: str) -> None:
        """Loads the sketch from an XML file

        Args:
            FileName: Path and name of file to load from
        """
        ...
    def PathObject(self) -> Any: ...
    def PointtoGlobal(self, x: float, y: float) -> List[Any]:
        """Converts a point on the sketch into a 3D point in the part coordinate system

        Args:
            x: X coordinate of point on sketch
            y: Y coordinate of point on sketch

        Returns:
            Python list [x, y, z]
        """
        ...
    def SavetoXml(self, FileName: str) -> None:
        """Saves the sketch to an XML file Does not support ellipses and elliptical arcs

        Args:
            FileName: Path and name of file to save to
        """
        ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def StartEditing(self) -> None: ...
    @overload
    def StartFaceMapping(self, EdgeVertex1: Optional[Vertex], EdgeVertex2: Optional[Vertex]) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0]

        Args:
            EdgeVertex1: Firrt vertex of edge
            EdgeVertex2: Second vertex of edge
        """
        ...
    @overload
    def StartFaceMapping(self, EdgeEndPoint1: List[Any], EdgeEndPoint2: List[Any]) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values

        Args:
            EdgeEndPoint1: First end point of edge [X, Y, Z]
            EdgeEndPoint2: Second end point of edge [X, Y, Z]
        """
        ...
    def StartMapping(self, Point1: List[Any], Point2: List[Any], PointAboveAxis: List[Any]) -> None:
        """Starts mapping the sketch so that the specified line is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values

        Args:
            Point1: First line end point [X, Y, Z]
            Point2: Second line end point [X, Y, Z]
            PointAboveAxis: Point to be located above the X-axis
        """
        ...
    def StopEditing(self) -> None: ...
    def StopFaceMapping(self) -> None:
        """Stops mapping the face"""
        ...
    def StopMapping(self) -> None:
        """Stops mapping the sketch"""
        ...
    def ToString(self) -> str: ...
    def ToXml(self) -> str:
        """Saves the sketch to an XML string Does not support ellipses and elliptical arcs

        Returns:
            XML string representing sketch
        """
        ...
    def VertextoPoint(self, Vert: Optional[Vertex]) -> Any: ...

class Sketch3D(ISelectableGeometry, ISweepPath):
    AutomaticStartEndEditing: bool
    _SelectionSession: Any
    _Sketch: Any
    Figures: List[Any]
    """A list of figures defines on the sketch, e.g. bspline (read-only)"""
    Name: str
    """Name of the sketch (read-only)"""
    def __init__(self, Sketch: Any) -> None: ...
    def AddArc(self, NewArc: Optional[CircularArc3D]) -> None:
        """Adds a circular arc to the sketch

        Args:
            NewArc: Arc to add
        """
        ...
    def AddArcCenterStartEnd(self, CenterX: float, CenterY: float, CenterZ: float, StartX: float, StartY: float, StartZ: float, EndX: float, EndY: float, EndZ: float) -> None:
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end

        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            CenterZ: Z coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            StartZ: Z coordinate for start
            EndX: X coordinate for end
            EndY: Y cordinate for end
            EndZ: Z coordnate for end
        """
        ...
    @overload
    def AddBspline(self, Points: List[Any]) -> Bspline3D:
        """Adds a Bspline to the sketch

        Args:
            Points: List of control points [X1, Y1, Z1, X2, Y2, Z2, ...]

        Returns:
            The Bspline object that was created
        """
        ...
    @overload
    def AddBspline(self, Bspline: Optional[Bspline3D]) -> None:
        """Adds a Bspline to the sketch

        Args:
            Bspline: Bspline to add
        """
        ...
    @overload
    def AddBspline(self, Points: Any) -> Bspline3D:
        """Adds a Bspline to the sketch

        Args:
            Points: List of control points [X1, Y1, Z1, X2, Y2, Z2, ...]

        Returns:
            The Bspline object that was created
        """
        ...
    @overload
    def AddLine(self, StartPoint: List[Any], EndPoint: List[Any]) -> None:
        """Adds a line to the sketch

        Args:
            StartPoint: Start of line [X, Y, Z]
            EndPoint: End of line [X, Y, Z]
        """
        ...
    @overload
    def AddLine(self, NewLine: Optional[Line3D]) -> None:
        """Adds a line to the sketch

        Args:
            NewLine: 3D line to add
        """
        ...
    @overload
    def AddLine(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float) -> None:
        """Adds a line to the sketch

        Args:
            X1: Start point X
            Y1: Start point Y
            Z1: Start point Z
            X2: End point X
            Y2: End point Y
            Z2: End point Z
        """
        ...
    def AddLines(self, Points: List[Any]) -> None:
        """Adds a polyline to the sketch

        Args:
            Points: Set of points [Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z, ...]
        """
        ...
    @overload
    def AddPoint(self, X: float, Y: float, Z: float) -> None:
        """Adds a point to the sketch

        Args:
            X: Point X coordinate
            Y: Point Y coordinate
            Z: Point Z coordinate
        """
        ...
    @overload
    def AddPoint(self, NewPoint: Optional[SketchPoint3D]) -> None:
        """Adds a point to the sketch

        Args:
            NewPoint: Point to add
        """
        ...
    def AddPolyline(self, Line: Optional[Polyline3D]) -> None:
        """Adds a polyline to the sketch

        Args:
            Line: Polyine to add
        """
        ...
    def FromXml(self, Xml: str) -> None:
        """Adds elements to the sketch from XML

        Args:
            Xml: XML to parse
        """
        ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Part that the sketch is defined on

        Returns:
            Part
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def LoadXml(self, FileName: str) -> None:
        """Loads the sketch from an XML file

        Args:
            FileName: Path and name of file to load from
        """
        ...
    def PathObject(self) -> Any: ...
    def SavetoXml(self, FileName: str) -> None:
        """Saves the sketch to an XML file

        Args:
            FileName: Path and name of file to save to
        """
        ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def StartEditing(self) -> None: ...
    def StopEditing(self) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> str:
        """Saves the sketch to an XML string

        Returns:
            XML string representing sketch
        """
        ...

class Plane(IConstrainable, IPlane, ISelectableGeometry, ISketchSurface):
    _Plane: Any
    _SelectionSession: Any
    Name: str
    """The name of the plane (read-only)"""
    def __init__(self, Plane: Any) -> None: ...
    def ConstraintObject(self) -> Any: ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Gets the part that defined this plane"""
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def Hide(self) -> None:
        """Hides the plane"""
        ...
    def IsParallel(self, OtherPlane: Optional[Plane]) -> bool:
        """Checks if another plane is parallel to this one

        Args:
            OtherPlane: The other plane to check

        Returns:
            true if the planes are parallel
        """
        ...
    def PlaneObject(self) -> Any: ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def Show(self) -> None:
        """Shows the plane"""
        ...
    def SurfaceObject(self) -> Any: ...
    def ToString(self) -> str: ...

class Axis(IAxis, IConstrainable, ISelectableGeometry):
    _Axis: Any
    _SelectionSession: Any
    Name: str
    """The name of the axis (read-only)"""
    def __init__(self, Axis: Any) -> None: ...
    def AxisObject(self) -> Any: ...
    def ConstraintObject(self) -> Any: ...
    def GetGeometry(self, Point: Any, Vector: Any) -> None: ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Gets the part that the axis is defined on

        Returns:
            Part that defines the axis
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def Hide(self) -> None:
        """Hides the axis"""
        ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def Show(self) -> None:
        """Shows the axis"""
        ...
    def ToString(self) -> str: ...

class Point(IConstrainable, IPoint, ISelectableGeometry):
    _Point: Any
    _SelectionSession: Any
    Name: str
    """Name of the point (read-only)"""
    X: float
    """Point X coordinate (read-only)"""
    Y: float
    """Point Y coordinate (read-only)"""
    Z: float
    """Point Z coordinate (read-only)"""
    def __init__(self, Point: Any) -> None: ...
    def ConstraintObject(self) -> Any: ...
    def CrossSectionObject(self) -> Any: ...
    def GetCoordinates(self) -> List[Any]:
        """Gets the coordiates of the point as a list [X, Y, Z]

        Returns:
            List of coordinates [X, Y, Z]
        """
        ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Gets the part that the point is defined in"""
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def Hide(self) -> None:
        """Hides the point"""
        ...
    def PointObject(self) -> Any: ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def Show(self) -> None:
        """Shows the point"""
        ...
    def ToString(self) -> str: ...

class Face(IChamferable, IConstrainable, IFilletable, IPlane, ISelectableGeometry, ISketchSurface):
    _SelectionSession: Any
    _Session: Any
    AdjoiningFaces: Any
    Coedges: Any
    Edges: Any
    Name: str
    """The name of the face (read-only)"""
    PartnerCoedges: Any
    Vertices: Any
    _Face: Any
    def __init__(self, Face: Any) -> None: ...
    def ChamferableObject(self) -> Any: ...
    def ConstraintObject(self) -> Any: ...
    def CrossSectionObject(self) -> Any: ...
    def DistanceTo(self, OtherFace: Optional[Face]) -> float:
        """Gets the distance from this face to another face

        Args:
            OtherFace: The other face to measure to

        Returns:
            The distance between faces
        """
        ...
    def FilletableObject(self) -> Any: ...
    def GetAdjoiningFaces(self) -> List[Any]:
        """Gets a list of the adjoining faces

        Returns:
            List of faces
        """
        ...
    def GetArea(self) -> float:
        """Gets the area of the face

        Returns:
            Area of face
        """
        ...
    def GetEdges(self) -> List[Any]:
        """Gets a list of the current edges in the face

        Returns:
            List of edges
        """
        ...
    def GetNormal(self) -> Any: ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Gets the part that the face is defined on

        Returns:
            Part that contains face
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def GetVertices(self) -> List[Any]:
        """Gets a list of the current vertices in the face

        Returns:
            List of vertices
        """
        ...
    def IsParallel(self, OtherFace: Optional[Face]) -> bool:
        """Checks if another face is parallel to this one

        Args:
            OtherFace: The other face to check

        Returns:
            true if the faces are parallel
        """
        ...
    def IsRectangle(self) -> bool:
        """Determines if the face is a rectangle

        Returns:
            true if face is a rectangle
        """
        ...
    def PlaneObject(self) -> Any: ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def SurfaceObject(self) -> Any: ...
    def ToString(self) -> str: ...

class Edge(IAxis, IChamferable, IConstrainable, IFilletable, ISelectableGeometry, ISweepPath):
    _SelectionSession: Any
    _Session: Any
    Diameter: float
    """The diameter of the edge, if it is a circle (read-only)"""
    Length: float
    """The length of the edge (read-only)"""
    Name: str
    """Name of the edge (read-only)"""
    Vertices: Any
    _Edge: Any
    def __init__(self, Edge: Any) -> None: ...
    def AxisObject(self) -> Any: ...
    def ChamferableObject(self) -> Any: ...
    def ConstraintObject(self) -> Any: ...
    def FilletableObject(self) -> Any: ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Gets the part that the edge is defined on

        Returns:
            Part that contains edge
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def GetVertices(self) -> List[Any]:
        """Gets a python list of the current vertices in the edge

        Returns:
            Python list of vertices
        """
        ...
    def PathObject(self) -> Any: ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def ToString(self) -> str: ...

class Vertex(IChamferable, IConstrainable, IPoint, ISelectableGeometry):
    _SelectionSession: Any
    _Session: Any
    Name: str
    """Name of the vertex (read-only)"""
    X: float
    """X-coordinate of vertex (read-only)"""
    Y: float
    """Y-coordinate of vertex (read-only)"""
    Z: float
    """Z-coordinate of vertex (read-only)"""
    _Vertex: Any
    def __init__(self, Vertex: Any) -> None: ...
    def ChamferableObject(self) -> Any: ...
    def ConstraintObject(self) -> Any: ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetPart(self) -> Part:
        """Part that the vertex is defined on

        Returns:
            Part
        """
        ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def PointObject(self) -> Any: ...
    def SelectableObject(self) -> Any: ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def ToString(self) -> str: ...

class Feature:
    _Feature: Any
    Name: str
    """Name of the feature (read-only)"""
    def __init__(self, Feature: Any) -> None: ...
    def GetColor(self) -> Any: ...
    @overload
    def SetColor(self, NewColor: Any) -> None:
        """Sets the color of the part"""
        ...
    @overload
    def SetColor(self, Red: int, Green: int, Blue: int) -> None:
        """Sets the color of the part

        Args:
            Red: Red component 0 - 255
            Green: Green component 0 - 255
            Blue: Blue component 0 - 255
        """
        ...
    def ToString(self) -> str: ...

class Configuration:
    _Configuration: Any
    _Occurrence: Any
    _Session: Any
    IsActive: bool
    """True if the configuration is currently active (read-only)"""
    Name: str
    """The name of the configuration (read-only)"""
    def __init__(self, Configuration: Any, Session: Any) -> None: ...
    def Activate(self) -> None:
        """Makes the configuration active"""
        ...
    def LockAll(self) -> None:
        """Applies all locks to the configuration"""
        ...
    def SetLocks(self, Locks: Optional[LockTypes]) -> None:
        """Sets the locks on the configuration

        Args:
            Locks: Locks to set
        """
        ...
    def ToString(self) -> str: ...
    def UnlockAll(self) -> None:
        """Removes all locks from the configuration"""
        ...

class Parameter:
    _Parameter: Any
    _Session: Any
    Comment: str
    """Comment for the parameter"""
    Equation: str
    """Equation of the parameter"""
    ExcelCell: str
    """Excel cell associated with the parameter, e.g. '$B$3' (read-only)"""
    ExcelSheet: str
    """Excel sheet associated with the parameter, e.g. 'Sheet1' (read-only)"""
    ExcelWorkbook: str
    """Excel workbook associated with the parameter e.g. 'Foo.xlsx' (read-only)"""
    Name: str
    """Name of the parameter"""
    RawValue: float
    """Raw value of the parameter"""
    Type: ParameterTypes
    """Type of the parameter (read-only)"""
    Units: ParameterUnits
    """Current units of the parameter"""
    Value: float
    """Current value of the parameter in script units (for mm, cm, in), or degrees for angles, or raw value for other units"""
    def __init__(self, Parameter: Any, Session: Any) -> None: ...
    def AttachToExcel(self, Document: str, Sheet: str, Cell: str, Units: Optional[UnitTypes]) -> None:
        """Attaches the parameter to a cell in an Ezcel spreadsheet

        Args:
            Document: Path and name of Excel spreadsheet
            Sheet: Name of sheet to use
            Cell: Cell to use
            Units: Units used in the cell
        """
        ...
    def ToString(self) -> str: ...

class Windows:
    ProductName: str
    @overload
    def __init__(self) -> None:
        """Creates a new Windows object allowing user interfaces to be constructed"""
        ...
    @overload
    def __init__(self, SessionIdentifier: str, ScriptFileName: str, ParentForm: Any) -> None: ...
    def CloseForm(self, SessionIdentifier: str) -> None:
        """Close all currently open forms for a specific session

        Args:
            SessionIdentifier: Identifier for session
        """
        ...
    def DisableInput(self, Index: int) -> None:
        """Disables an input

        Args:
            Index: Index of the input
        """
        ...
    def EnableInput(self, Index: int) -> None:
        """Enables an input

        Args:
            Index: Index of the input
        """
        ...
    def ErrorDialog(self, Message: str, Title: str) -> None:
        """Shows an error window

        Args:
            Message: Error message
            Title: Title of window
        """
        ...
    @staticmethod
    def GetDisplayedForm(SessionIdentifier: str) -> Any:
        """Gets the currently displayed form for a specific session

        Args:
            SessionIdentifier: Identifier of session

        Returns:
            Displayed form or null for none
        """
        ...
    def GetInputValue(self, Index: int) -> Any:
        """Gets the current value of an input

        Args:
            Index: Index of the input

        Returns:
            Current value
        """
        ...
    def InfoDialog(self, Message: str, Title: str) -> None:
        """Shows an information window

        Args:
            Message: Message to show
            Title: Title of window
        """
        ...
    def OpenFileDialog(self, Title: str, Filter: str, DefaultExtension: str) -> str:
        """Prompts user to select a file

        Args:
            Title: Title of dialog window
            Filter: File filter, example filter: 'Part Files|*.AD_PRT'
            DefaultExtension: Default file extension, e.g. '.AD_PRT'

        Returns:
            Path and name of selected file or empty string if canceled
        """
        ...
    @overload
    def OptionsDialog(self, Title: str, Inputs: List[Any], InputAreaWidth: int = ...) -> List[Any]:
        """Shows a dialog prompting the user to enter values

        Args:
            Title: Title of dialog window
            Inputs: List of input definitions [[Name, Type, DefaultValue], [...]]
            InputAreaWidth: Width of input area, optional

        Returns:
            List of entered values
        """
        ...
    @overload
    def OptionsDialog(self, Title: str, Inputs: List[Any], InputAreaWidth: int, InputChangedCallback: Any, UpdateUserInterfaceCallback: Any) -> List[Any]:
        """Shows a dialog prompting the user to enter values

        Args:
            Title: Title of dialog window
            Inputs: List of input definitions\n [[Name, Type, DefaultValue, OptionalSettings], [...]]\n Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
            InputAreaWidth: Width of input area
            InputChangedCallback: Function called when an input is changed
            UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog

        Returns:
            List of entered values
        """
        ...
    def QuestionDialog(self, Question: str, Title: str) -> bool:
        """Shows a question window

        Args:
            Question: Question to show
            Title: Title of window

        Returns:
            true if 'yes' was clicked, false if 'no' was clicked
        """
        ...
    def SaveFileDialog(self, Title: str, Filter: str, DefaultExtension: str) -> str:
        """Prompts user to save a file

        Args:
            Title: Title of dialog window
            Filter: File filter, example filter: 'Part Files|*.AD_PRT'
            DefaultExtension: Default file extension, e.g. '.AD_PRT'

        Returns:
            Path and name of selected file or empty string if canceled
        """
        ...
    def SelectFolderDialog(self, CurrentFolder: str, Description: str) -> str:
        """Prompts the user to select a folder

        Args:
            CurrentFolder: The current folder, if any
            Description: Description of what is being chosen, shown to user

        Returns:
            Path of selected folder or empty if canceled
        """
        ...
    def SetInputValue(self, Index: int, Value: Any) -> None:
        """Sets the current value for an input

        Args:
            Index: Index of the input
            Value: Value to show
        """
        ...
    def SetStringList(self, Index: int, Strings: Any) -> None:
        """Updates the list of strings for a stringlist input

        Args:
            Index: Index of the stringlist input
            Strings: New list of strings to show
        """
        ...
    @overload
    def UtilityDialog(self, Title: str, ActionButtonText: str, ActionButtonCallback: Any, InputChangedCallback: Any, Inputs: List[Any], InputAreaWidth: int = ...) -> None:
        """Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script

        Args:
            Title: Title of dialog window
            ActionButtonText: Text for action button
            ActionButtonCallback: Function called when the action button is clicked
            InputChangedCallback: Function called when an input is changed
            Inputs: List of input definitions [[Name, Type, DefaultValue, OptionalSettings], [...]]
            InputAreaWidth: Width of dialog input area, optional
        """
        ...
    @overload
    def UtilityDialog(self, Title: str, ActionButtonText: str, ActionButtonCallback: Any, InputChangedCallback: Any, Inputs: List[Any], InputAreaWidth: int, UpdateUserInterfaceCallback: Any) -> None:
        """Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script

        Args:
            Title: Title of dialog window
            ActionButtonText: Text for action button
            ActionButtonCallback: Function called when the action button is clicked
            InputChangedCallback: Function called when an input is changed
            Inputs: List of input definitions\n [[Name, Type, DefaultValue, OptionalSettings], [...]]\n Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
            InputAreaWidth: Width of dialog input area
            UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog
        """
        ...

class AssembledPart(IAssembled, Part):
    _SelectionSession: Any
    ConfigurationList: Any
    Configurations: List[Any]
    """List of configurations defined on the part (read-only)"""
    Edges: Any
    Faces: Any
    Name: str
    """Name of the assembled part (read-only)"""
    def __init__(self, PartSession: Any) -> None: ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex: Optional[IPoint], XOffset: float, YOffset: float, ZOffset: float) -> Point:
        """Adds a point at an offset to a point or a vertex

        Args:
            Name: Name of point
            PointOrVertex: Point or vertex
            XOffset: X offse
            YOffset: Y offset
            ZOffset: Z offset

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PointOrVertex1: Optional[IPoint], PointOrVertex2: Optional[IPoint], Ratio: float) -> Point:
        """Adds a point between two points/vertices

        Args:
            Name: Name of point
            PointOrVertex1: First point or vertex
            PointOrVertex2: Second point or vertex
            Ratio: Ratio of distance between points/vertices

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge1: Optional[IAxis], AxisOrEdge2: Optional[IAxis]) -> Point:
        """Adds a point at the intersection or two axes or edges

        Args:
            Name: Name of point
            AxisOrEdge1: First axis or edge
            AxisOrEdge2: Second axis or edge

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, PlaneOrFace1: Optional[IPlane], PlaneOrFace2: Optional[IPlane], PlaneOrFace3: Optional[IPlane]) -> Point:
        """Adds a point at the intersection of three planes or faces

        Args:
            Name: Name of point
            PlaneOrFace1: First plane or face
            PlaneOrFace2: Second plane or face
            PlaneOrFace3: Third plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, AxisOrEdge: Optional[IAxis], PlaneOrFace: Optional[IPlane]) -> Point:
        """Adds a point at the the intersection of a axis or edge and a plane or face

        Args:
            Name: Name of point
            AxisOrEdge: Axis or edge
            PlaneOrFace: Plane or face

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, SourcePointOrVertex: Optional[IPoint], TargetPlaneOrFace: Optional[IPlane], XOffset: float, YOffset: float) -> Point:
        """Adds a point by projecting a point or vertex onto a plane or face

        Args:
            Name: Name of point
            SourcePointOrVertex: Point or vertex to project
            TargetPlaneOrFace: Plane or face to project onto
            XOffset: X offset to apply to point once projected
            YOffset: Y offset to apply to point once projected

        Returns:
            The created point
        """
        ...
    @overload
    def AddPoint(self, Name: str, TargetEdge: Optional[Edge], Ratio: float) -> Point:
        """Adds a point on an edge

        Args:
            Name: Name of point
            TargetEdge: The edge to create the point on
            Ratio: Ratio along the edge from 0.0 -> 1.0

        Returns:
            The created point
        """
        ...
    def AddPointFromCircularEdge(self, Name: str, TargetEdge: Optional[Edge]) -> Point:
        """Adds a point at the center of a circular edge

        Args:
            Name: Name of point
            TargetEdge: The edge to use for creating the point

        Returns:
            The created point
        """
        ...
    def AddPointFromToroidalFace(self, Name: str, TargetFace: Optional[Face]) -> Point:
        """Adds a point at the center of a toroidal face

        Args:
            Name: Name of point
            TargetFace: Toroidal face to use in creating the point

        Returns:
            The created point
        """
        ...
    def AssemblyPointtoPartPoint(self, AssemblyPoint: List[Any]) -> List[Any]:
        """Converts a point in the assembly coordinate system into a point in the part coordinate system

        Args:
            AssemblyPoint: Point [X, Y, Z] in the assembly coordinate system

        Returns:
            Point [X, Y, Z] in the part coordinate system
        """
        ...
    def GetAssembledPath(self) -> Any: ...
    def GetAssembly(self) -> Assembly:
        """Gets the assembly for the part

        Returns:
            Assembly or None if no assembly
        """
        ...
    def GetAssemblyBoundingBox(self) -> List[Any]:
        """Gets the bounding box for the part as eight points in the assembly coordinate system

        Returns:
            Python list of eight points as [P1, P2, ... P8]. Each point is [X, Y, Z]
        """
        ...
    def GetAssemblyVertices(self) -> List[Any]:
        """Gets a python list of the current vertices in the part in the assembly coordinate system

        Returns:
            Python list of vertices in assembly coordinates [ [X1, Y1, Z1], ... [Xn, Yn, Zn] ]
        """
        ...
    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name

        Args:
            Name: Name of confguration

        Returns:
            Configuration object
        """
        ...
    def GetEdge(self, Name: str) -> Edge:
        """Gets an edge using it's name "Edge<n>"

        Args:
            Name: Name of edge

        Returns:
            Edge if found
        """
        ...
    def GetEdges(self) -> List[Any]:
        """Gets a python list of the current edges in the part

        Returns:
            Python list of edges
        """
        ...
    def GetFace(self, Name: str) -> Face:
        """Gets a face using it's name "Face<n>"

        Args:
            Name: Name of face

        Returns:
            Face if found
        """
        ...
    def GetFaces(self) -> List[Any]:
        """Gets a python list of the current faces in the part

        Returns:
            Python list of faces
        """
        ...
    def GetMappedOccurrence(self, Assembly: Any) -> Any:
        """Gets the occurrence of the part mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific assembly using the part

        Args:
            Assembly: Assembly for occurrence structure

        Returns:
            Mapped occurrence or null if not found
        """
        ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetSelectionAssembly(self) -> Assembly: ...
    def GetTransformation(self) -> Any: ...
    @overload
    def PartPointtoAssemblyPoint(self, PartPoint: List[Any]) -> List[Any]:
        """Converts a point in the part coordinate system into a point in the assembly coordinate system

        Args:
            PartPoint: Point [X, Y, Z] in the part coordinate system

        Returns:
            Point [X, Y, Z] in the assembly coordinate system
        """
        ...
    @overload
    def PartPointtoAssemblyPoint(self, X: float, Y: float, Z: float, AssemblyX: float, AssemblyY: float, AssemblyZ: float) -> None:
        """Converts a point in the part coordinate system into a point in the assembly coordinate system

        Returns:
            Point [X, Y, Z] in the assembly coordinate system
        """
        ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def ToString(self) -> str: ...

class AssembledSubAssembly(Assembly, IAssembled):
    _SelectionSession: Any
    ConfigurationList: Any
    Configurations: List[Any]
    """A list of configurations defined on the assembly (read-only)"""
    Name: str
    """Name of the subassembly (read-only)"""
    def __init__(self, AssemblySession: Any) -> None: ...
    def GetAssembledPath(self) -> Any: ...
    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name

        Args:
            Name: Name of confguration

        Returns:
            Configuration object
        """
        ...
    def GetMappedOccurrence(self, Assembly: Any) -> Any:
        """Gets the occurrence of the sub-assembly mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific sub-assembly using the part

        Args:
            Assembly: Assembly for occurrence structure

        Returns:
            Mapped occurrence or null if not found
        """
        ...
    def GetOccurrence(self) -> Any: ...
    def GetParentAssembly(self) -> Assembly: ...
    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on Only valid when a selection has been made

        Returns:
            Assembly or null for no assembly
        """
        ...
    def SetOccurrence(self, Occurrence: Any) -> None: ...
    def SetParentAssembly(self, ParentAssembly: Optional[Assembly]) -> None: ...
    def ToString(self) -> str: ...

class Bspline(ISketchFigure):
    ControlPoints: List[Any]
    """The control points [x1, y1, ..., xn, yn]"""
    IsReference: bool
    """True if the bspline is a reference bspline, false if it is a regular bspline"""
    KnotVectors: List[Any]
    """The knot vectors [k1, k2, ..., kn]"""
    Length: float
    """Gets the length of the Bspline (read-only)"""
    Order: int
    """The order of the bspline"""
    Weights: List[Any]
    """The weights [w1, w2, ..., wn]"""
    @overload
    def __init__(self, Bspline: Any) -> None: ...
    @overload
    def __init__(self, Order: int, ControlPoints: List[Any], KnotVectors: List[Any], Weights: List[Any], IsReference: bool) -> None:
        """Creates a bspline

        Args:
            Order: Order of the bspline
            ControlPoints: Value of control points [Point1X, Point1Y, ...]
            KnotVectors: Knot vectors [KnotVector1, KnotVector2, ...]
            Weights: Point weights [Weight1, Weight2, ...]
            IsReference: True if a reference bspline, false if a regular bspline
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> Bspline: ...
    def GetNormalAt(self, u: float) -> List[Any]:
        """Gets the normal vector at a point on the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Vector for point on the spline at the specified location (A, B)
        """
        ...
    def GetPointAt(self, u: float) -> List[Any]:
        """Gets a point on the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Point on the spline at the specified location [X, Y]
        """
        ...
    def GetX(self, u: float) -> float:
        """Gets the X value of the spline at a location along the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            X value of spline at the specified location
        """
        ...
    def GetY(self, u: float) -> float:
        """Gets the Y value of the spline at a location along the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Y value of spline at the specified location
        """
        ...
    def SetInstance(self, Figure: Any) -> None: ...
    def Subdivide(self, Segments: int) -> List[Any]:
        """Divides the Bspline up into segments

        Args:
            Segments: Number of segments to obtain

        Returns:
            List of points between segments [X1, Y1, X2, Y2, ...]
        """
        ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class Bspline3D:
    ControlPoints: List[Any]
    """The control points [x1, y1, ..., xn, yn]"""
    IsReference: bool
    """True if the bspline is a reference bspline, false if it is a regular bspline"""
    KnotVectors: List[Any]
    """The knot vectors [k1, k2, ..., kn]"""
    Length: float
    """Gets the length of the Bspline (read-only)"""
    Order: int
    """The order of the bspline"""
    Weights: List[Any]
    """The weights [w1, w2, ..., wn]"""
    @overload
    def __init__(self, Bspline: Any) -> None: ...
    @overload
    def __init__(self, Order: int, ControlPoints: List[Any], KnotVectors: List[Any], Weights: List[Any], IsReference: bool) -> None:
        """Creates a bspline

        Args:
            Order: Order of the bspline
            ControlPoints: Value of control points [Point1X, Point1Y, ...]
            KnotVectors: Knot vectors [KnotVector1, KnotVector2, ...]
            Weights: Point weights [Weight1, Weight2, ...]
            IsReference: True if a reference bspline, false if a regular bspline
        """
        ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(Xml: Any) -> Bspline3D: ...
    def GetNormalAt(self, u: float) -> List[Any]:
        """Gets the normal vector at a point on the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Vector for point on the spline at the specified location (A, B, C)
        """
        ...
    def GetPointAt(self, u: float) -> List[Any]:
        """Gets a point on the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Point on the spline at the specified location [X, Y, Z]
        """
        ...
    def GetX(self, u: float) -> float:
        """Gets the X value of the spline at a location along the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            X value of spline at the specified location
        """
        ...
    def GetY(self, u: float) -> float:
        """Gets the Y value of the spline at a location along the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Y value of spline at the specified location
        """
        ...
    def GetZ(self, u: float) -> float:
        """Gets the Z value of the spline at a location along the spline

        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end

        Returns:
            Y value of spline at the specified location
        """
        ...
    def Subdivide(self, Segments: int) -> List[Any]:
        """Divides the Bspline up into segments

        Args:
            Segments: Number of segments to obtain

        Returns:
            List of points between segments [X1, Y1, Z1, X2, Y2, Z2, ...]
        """
        ...
    def SubdivideGetNormals(self, Segments: int) -> List[Any]:
        """Divides the Bspline up into segments and gets the normal for each point

        Args:
            Segments: Number of segments to obtain

        Returns:
            List of points between segments and normals [X1, Y1, Z1, A1, B1, C1, X2, Y2, Z2, A2, B2, C2, ...]
        """
        ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class CSharp:
    class WriteHandler:
        def __init__(self, object: Any, method: Any) -> None: ...
        def BeginInvoke(self, Sender: Any, Text: str, callback: Any, object: Any) -> Any: ...
        def EndInvoke(self, result: Any) -> None: ...
        def Invoke(self, Sender: Any, Text: str) -> None: ...

    class WriteLineHandler:
        def __init__(self, object: Any, method: Any) -> None: ...
        def BeginInvoke(self, Sender: Any, Text: str, callback: Any, object: Any) -> Any: ...
        def EndInvoke(self, result: Any) -> None: ...
        def Invoke(self, Sender: Any, Text: str) -> None: ...

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, SessionIdentifier: str, ScriptFileName: str, ParentForm: Any) -> None: ...
    def Compile(self, Code: str) -> Any:
        """Compiles C# code

        Args:
            Code: Code to compile

        Returns:
            Compiled code object
        """
        ...
    @overload
    def CompileAndRun(self, Code: str) -> Dict[Any, Any]:
        """Compiles and runs C# code

        Args:
            Code: Code to compile and run

        Returns:
            Updated dictionary of variables
        """
        ...
    @overload
    def CompileAndRun(self, Code: str, Variables: Dict[Any, Any]) -> Dict[Any, Any]:
        """Compiles and runs C# code

        Args:
            Code: Code to compile and run
            Variables: Dictionary of variables

        Returns:
            Updated dictionary of variables
        """
        ...
    @overload
    def Run(self, Script: Any) -> Dict[Any, Any]:
        """Runs compiled C# code

        Args:
            Script: Compiled code object to run

        Returns:
            Updated dictionary of variables
        """
        ...
    @overload
    def Run(self, Script: Any, Variables: Dict[Any, Any]) -> Dict[Any, Any]:
        """Runs compiled C# code

        Args:
            Script: Compiled code object to run

        Returns:
            Updated dictionary of variables
        """
        ...

class Circle(ISketchFigure):
    Center: List[Any]
    """The center of the circle [x, y]"""
    CenterPoint: SketchPoint
    """The center of the circle as a sketch point (read-only)"""
    IsReference: bool
    """True if the circle is a reference circle, false if it is a regular circle"""
    Length: float
    """The length of the circle circumference in script units (read-only)"""
    Radius: float
    """Radius of the circle"""
    @overload
    def __init__(self, Circle: Any) -> None: ...
    @overload
    def __init__(self, Center: List[Any], Radius: float, IsReference: bool) -> None:
        """Creates a 2D circle which can be added to sketches

        Args:
            Center: Center of the circle as a python list [x, y]
            Radius: Radius of circle
            IsReference: True to create a reference circle
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> Circle: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class CircularArc(ISketchFigure):
    class ArcType:
        CenterStartAngle: CircularArc.ArcType
        CenterStartEnd: CircularArc.ArcType

    Angle: float
    """Angle of arc"""
    Center: List[Any]
    """The center of the arc [x, y]"""
    CenterPoint: SketchPoint
    """The center point as a sketchpoint object (read-only)"""
    End: SketchPoint
    """The end point as a sketchpoint object (read-only)"""
    EndPoint: List[Any]
    """The end point of the arc [x, y]"""
    IsReference: bool
    """True if the arc is a reference arc, false if it is a regular arc"""
    Radius: float
    """Radius of arc"""
    Start: SketchPoint
    """The start point as a sketchpoint object (read-only)"""
    StartPoint: List[Any]
    """The start point of the arc [x, y]"""
    Type: CircularArc.ArcType
    """Type of arc (read-only)"""
    @overload
    def __init__(self, Arc: Any) -> None: ...
    @overload
    def __init__(self, Center: List[Any], Start: List[Any], End: List[Any], IsReference: bool) -> None:
        """Creates an arc using the center, start point and end point

        Args:
            Center: Center of the arc
            Start: Start point of the arc
            End: End point of the arc
            IsReference: True to create a reference arc, false to create a regular arc
        """
        ...
    @overload
    def __init__(self, Center: List[Any], Start: List[Any], Angle: float, IsReference: bool) -> None:
        """Creates an arc using the center, start point and an angle

        Args:
            Center: Location of center of arc
            Start: Location of start of arc
            Angle: Angle of arc
            IsReference: True if a reference arc, false if a regular arc
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> CircularArc: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class CircularArc3D:
    class ArcType:
        CenterStartAngle: CircularArc3D.ArcType
        CenterStartEnd: CircularArc3D.ArcType

    Angle: float
    """Angle of arc"""
    Center: List[Any]
    """The center of the arc [x, y, z]"""
    EndPoint: List[Any]
    """The end point of the arc [x, y, z]"""
    IsReference: bool
    """True if the arc is a reference arc, false if it is a regular arc"""
    Radius: float
    """Radius of arc"""
    StartPoint: List[Any]
    """The start point of the arc [x, y, z]"""
    Type: CircularArc3D.ArcType
    """Type of arc (read-only)"""
    @overload
    def __init__(self, Arc: Any) -> None: ...
    @overload
    def __init__(self, Center: List[Any], Start: List[Any], End: List[Any], IsReference: bool) -> None:
        """Creates an arc using the center, start point and end point

        Args:
            Center: Center of the arc
            Start: Start point of the arc
            End: End point of the arc
            IsReference: True to create a reference arc, false to create a regular arc
        """
        ...
    @overload
    def __init__(self, Center: List[Any], Start: List[Any], Angle: float, IsReference: bool) -> None:
        """Creates an arc using the center, start point and an angle

        Args:
            Center: Location of center of arc
            Start: Location of start of arc
            Angle: Angle of arc
            IsReference: True if a reference arc, false if a regular arc
        """
        ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(Xml: Any) -> CircularArc3D: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class Ellipse(ISketchFigure):
    Center: List[Any]
    """The center of the ellipse [x, y]"""
    CenterPoint: SketchPoint
    """The center point as a sketchpoint object (read-only)"""
    IsReference: bool
    """True if the ellipse is a reference ellipse, false if it is a regular ellipse"""
    MajorAxisAngle: float
    """Angle of major axis"""
    MinorMajorRatio: float
    """Ratio of minor radius to major radius"""
    Radius: float
    """Radius on major axis"""
    @overload
    def __init__(self, Ellipse: Any) -> None: ...
    @overload
    def __init__(self, Center: List[Any], MajorRadius: float, MajorAxisAngle: float, MinorMajorRatio: float, IsReference: bool) -> None:
        """Creates an ellipse

        Args:
            Center: Center of the ellipse
            MajorRadius: Radius on the major axis
            MajorAxisAngle: Angle of the major axis in degrees
            MinorMajorRatio: Radius on the minor axis as a ratio of the major radius
            IsReference: True to create a reference arc, false to create a regular arc
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> Ellipse: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class EllipticalArc(ISketchFigure):
    Center: List[Any]
    """The center of the elliptical arc [x, y]"""
    CenterPoint: SketchPoint
    """The center point as a sketchpoint object (read-only)"""
    End: SketchPoint
    """The end point as a sketchpoint object (read-only)"""
    EndPoint: List[Any]
    """The end point of the arc [x, y]"""
    IsReference: bool
    """True if the elliptical arc is a reference elliptical arc, false if it is a regular elliptical arc"""
    MajorAxisAngle: float
    """Angle of major axis"""
    MinorMajorRatio: float
    """Ratio of minor radius to major radius"""
    Radius: float
    """Radius on major axis"""
    Start: SketchPoint
    """The start point as a sketchpoint object (read-only)"""
    StartPoint: List[Any]
    """The start point of the arc [x, y]"""
    @overload
    def __init__(self, ElArc: Any) -> None: ...
    @overload
    def __init__(self, Center: List[Any], Start: List[Any], End: List[Any], MajorRadius: float, MajorAxisAngle: float, MinorMajorRatio: float, IsReference: bool) -> None:
        """Creates an elliptical arc

        Args:
            Center: Center of the elliptical arc
            Start: The start point for the arc
            End: The end point for the arc
            MajorRadius: Radius on the major axis
            MajorAxisAngle: Angle of the major axis in degrees
            MinorMajorRatio: Radius on the minor axis as a ratio of the major radius
            IsReference: True to create a reference arc, false to create a regular arc
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> EllipticalArc: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class GearSketch(ISelectableGeometry, ISweepPath, Sketch):
    CenterX: float
    """X coordinate of gear center"""
    CenterY: float
    """Y coordinate of gear center"""
    DiametralPitch: float
    """Diametral pitch of gear in teeth per inch"""
    NumberofTeeth: int
    """Number of teeth in gear"""
    PitchDiameter: float
    """Pitch diameter of gear in script units"""
    PressureAngle: float
    """Pressure angle of gear"""
    @overload
    def __init__(self, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, DiametralPitch: float, SingleTooth: bool, CenterX: float, CenterY: float, InvolutePoints: int, ProfileShiftFactor: float, AddendumCoefficient: float, DedendumCoefficient: float, ClearanceCoefficient: float, Sketch: Any) -> None: ...
    @overload
    def __init__(self, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, DiametralPitch: float, ProfileShiftFactor: float, AddendumCoefficient: float, DedendumCoefficient: float, ClearanceCoefficient: float, PitchPointtoBase: float, Sketch: Any) -> None: ...
    def ToString(self) -> str: ...

class GlobalParameters:
    _GlobalParameters: Any
    ConfigurationList: Any
    Configurations: List[Any]
    """A list of configurations (read-only)"""
    Name: str
    """Name of the global parameters (read-only)"""
    ParameterList: Any
    Parameters: List[Any]
    """A list of parameters (read-only)"""
    @overload
    def __init__(self, Folder: str, Name: str) -> None:
        """Opens an existing global parameters set

        Args:
            Folder: Folder containing global parameters
            Name: Name of global parameters to open
        """
        ...
    @overload
    def __init__(self, Name: str) -> None:
        """Creates a new global parameters set

        Args:
            Name: Name of new global parameters set
        """
        ...
    @overload
    def __init__(self, Name: str, CreateNew: bool) -> None:
        """Creates a new global parameters set or accesses an already opened global parameters set

        Args:
            Name: Name of global parameters set to create or access
            CreateNew: True to create a new global parameters set, false to access an opened global parameters
        """
        ...
    @overload
    def __init__(self, GlobalParamSession: Any) -> None: ...
    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the global parameters set

        Args:
            Name: Name of configuration

        Returns:
            New configuration
        """
        ...
    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the global parameters set using another configuration as a base

        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use

        Returns:
            New configuration
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Value: float) -> Parameter:
        """Adds a parameter to the global parameters set

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter

        Returns:
            New parameter
        """
        ...
    @overload
    def AddParameter(self, Name: str, Type: Optional[ParameterTypes], Equation: str) -> Parameter:
        """Adds a parameter to the global parameters set

        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter

        Returns:
            New parameter
        """
        ...
    def Close(self) -> None:
        """Closes the global parameters set If it is unsaved then changes will be lost"""
        ...
    def GetActiveConfiguration(self) -> Configuration:
        """Gets the currently active configuration

        Returns:
            Configuration object
        """
        ...
    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name

        Args:
            Name: Name of confguration

        Returns:
            Configuration object
        """
        ...
    def GetParameter(self, Name: str) -> Parameter:
        """Gets a parameter with a specific name

        Args:
            Name: Name of parameter

        Returns:
            Parameter object
        """
        ...
    @overload
    def Save(self) -> None:
        """Saves the global parameters set using the current path and file name"""
        ...
    @overload
    def Save(self, Folder: str) -> None:
        """Saves the global parameters set to a specific folder

        Args:
            Folder: Folder to save to
        """
        ...
    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the global parameters set to a specific folder with a new name

        Args:
            Folder: Folder to save to
            NewName: New name for global parameters set
        """
        ...
    def ToString(self) -> str: ...

class GuideCurveTypes:
    """Type of guide curve"""
    Global: GuideCurveTypes
    Local: GuideCurveTypes
    Tangent: GuideCurveTypes

class Line(ISketchFigure):
    End: SketchPoint
    """The end point as a sketchpoint object (read-only)"""
    EndPoint: List[Any]
    """The end point of the line [x, y]"""
    IsReference: bool
    """True if the line is a reference line, false if it is a regular line"""
    Length: float
    """The length of the line in script units (read-only)"""
    Start: SketchPoint
    """The start point as a sketchpoint object (read-only)"""
    StartPoint: List[Any]
    """The start point of the line [x, y]"""
    @overload
    def __init__(self, Line: Any) -> None: ...
    @overload
    def __init__(self, StartPoint: List[Any], EndPoint: List[Any], IsReference: bool) -> None:
        """Creates a new 2D line

        Args:
            StartPoint: Location of the start point [x, y]
            EndPoint: Location of the end point [x, y]
            IsReference: True if a reference line
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> Line: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class Line3D:
    End: SketchPoint3D
    """The end point as a sketchpoint object (read-only)"""
    EndPoint: List[Any]
    """The end point of the line [x, y, z]"""
    IsReference: bool
    """True if the line is a reference line, false if it is a regular line"""
    Length: float
    """The length of the line in script units (read-only)"""
    Start: SketchPoint3D
    """The start point as a sketchpoint object (read-only)"""
    StartPoint: List[Any]
    """The start point of the line [x, y, z]"""
    @overload
    def __init__(self, Line: Any) -> None: ...
    @overload
    def __init__(self, StartPoint: List[Any], EndPoint: List[Any], IsReference: bool) -> None:
        """Creates a new 3D line

        Args:
            StartPoint: Location of the start point [x, y, z]
            EndPoint: Location of the end point [x, y, z]
            IsReference: True if a reference line
        """
        ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(Xml: Any) -> Line3D: ...
    def SetInstance(self, Line: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class LockTypes:
    """Type of configuration lock"""
    All: LockTypes
    HideNewAnnotations: LockTypes
    HideNewDesignGeometry: LockTypes
    HideNewInclusions: LockTypes
    HideNewSketches: LockTypes
    LockActiveSectionView: LockTypes
    LockColorProperties: LockTypes
    LockComponentConfig: LockTypes
    LockParameterValues: LockTypes
    LockPropertyValues: LockTypes
    None_: LockTypes
    SuppressNewComponents: LockTypes
    SuppressNewConstraints: LockTypes
    SuppressNewFeatures: LockTypes

class Material:
    ABS: float
    """Density for ABS plastic in kg/cm3"""
    PLA: float
    """Density for PLA plastic in kg/cm3"""
    def __init__(self) -> None: ...

class ParameterTypes:
    """Type of parameter"""
    Angle: ParameterTypes
    Count: ParameterTypes
    Distance: ParameterTypes
    Scale: ParameterTypes

class ParameterUnits:
    """Units of parameters"""
    Centimeters: ParameterUnits
    Degrees: ParameterUnits
    DegreesMinutes: ParameterUnits
    DegreesMinutesSeconds: ParameterUnits
    Feet: ParameterUnits
    FeetInches: ParameterUnits
    Grams: ParameterUnits
    Inches: ParameterUnits
    Kilograms: ParameterUnits
    Meters: ParameterUnits
    Millimeters: ParameterUnits
    Pounds: ParameterUnits
    Radians: ParameterUnits
    Unitless: ParameterUnits

class Polyline:
    Points: Any
    @overload
    def __init__(self) -> None:
        """Creates a new 2D polyline that can be later added to a 2D sketch"""
        ...
    @overload
    def __init__(self, Points: List[Any]) -> None:
        """Creates a new 2D polyline that can be later added to a 2D sketch

        Args:
            Points: List of points in the polyline [X1, Y1, X2, Y2, ...]
        """
        ...
    def AddArc(self, Center: Optional[PolylinePoint], Start: Optional[PolylinePoint], End: Optional[PolylinePoint], MinimumSegments: int) -> None:
        """Adds an arc to the polyline. The arc is approcimated with straight line segments

        Args:
            Center: Point defining center of arc
            Start: Point defining start of arc
            End: Point defining end of arc
            MinimumSegments: Minimum number of line segments to use to form arc
        """
        ...
    def AddCircle(self, CenterX: float, CenterY: float, Diameter: float, sides: int) -> None:
        """Adds a circle to the line

        Args:
            CenterX: X coordinate of circle center
            CenterY: Y coordinate of circle center
            Diameter: Diameter of circle
            sides: Number of sides to use to approximate circle
        """
        ...
    @overload
    def AddPoint(self, Point: Optional[PolylinePoint]) -> None:
        """Adds a new point to the polyline

        Args:
            Point: Point to add
        """
        ...
    @overload
    def AddPoint(self, X: float, Y: float) -> None:
        """Adds a new point to the polyline"""
        ...
    def AddPolyline(self, AppendLine: Optional[Polyline]) -> None:
        """Appends a line to the current line

        Args:
            AppendLine: Line to append
        """
        ...
    @overload
    def Clone(self) -> Polyline:
        """Creates an exact copy of the line

        Returns:
            Copy of line
        """
        ...
    @overload
    def Clone(self, StartIndex: int, EndIndex: int) -> Polyline:
        """Creates an exact copy of a section of the line

        Args:
            StartIndex: 0-based index of first point to include in copy
            EndIndex: 0-based index of last point to include in copy

        Returns:
            Copied line
        """
        ...
    @overload
    @staticmethod
    def FindIntersection(L1: Optional[Polyline], L2: Optional[Polyline]) -> PolylinePoint:
        """Finds the first intersection point between two lines

        Args:
            L1: First line
            L2: Second line

        Returns:
            First intersection point or null if none found
        """
        ...
    @overload
    @staticmethod
    def FindIntersection(A1: Optional[PolylinePoint], A2: Optional[PolylinePoint], B1: Optional[PolylinePoint], B2: Optional[PolylinePoint]) -> PolylinePoint:
        """Gets the intersection between the line segments A1A2 and B1B2

        Args:
            A1: First segment start point
            A2: First segment end point
            B1: Second segment start point
            B2: Second segment end point

        Returns:
            Intersection point or null if not found
        """
        ...
    @staticmethod
    def FindIntersectionWithCircle(L1: Optional[Polyline], CircleX: float, CircleY: float, Radius: float) -> PolylinePoint:
        """Finds first intersection of line with a circle

        Args:
            L1: Line to check
            CircleX: X-coordinate of circle center
            CircleY: Y-coordinate of circle center
            Radius: Radius of circle

        Returns:
            Intersection point or null if not found
        """
        ...
    def InsertPoint(self, Index: int, Point: Optional[PolylinePoint]) -> None:
        """Inserts a point at a specific location

        Args:
            Index: 0-based index of location to insert
            Point: Point to insert
        """
        ...
    @staticmethod
    def IsPointOnLine(A1: Optional[PolylinePoint], A2: Optional[PolylinePoint], Point: Optional[PolylinePoint], Tolerance: float) -> bool:
        """Determines if a point is on a line segment

        Args:
            A1: First point of line segment
            A2: Last point of line segment
            Point: Point to check
            Tolerance: Fudge factor

        Returns:
            True if point is on line
        """
        ...
    def Join(self, AppendLine: Optional[Polyline]) -> Polyline:
        """Joins a line onto the end of the current line and returns the new line

        Args:
            AppendLine: The line to join to the current line

        Returns:
            The new line created from this line plus the appended line
        """
        ...
    def Offset(self, OffsetX: float, OffsetY: float) -> None:
        """Applies an offset to all points on the line

        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
        """
        ...
    def RemoveDuplicates(self) -> None:
        """Removes duplicate points that are next to each other"""
        ...
    def RotateZ(self, CenterX: float, CenterY: float, Angle: float) -> None:
        """Rotates the polyline around the Z axis

        Args:
            CenterX: X coordinate of center of rotation
            CenterY: Y coordinate of center of rotation
            Angle: Number of degrees to rotate
        """
        ...
    def SplitAtPoint(self, SplitPoint: Optional[PolylinePoint], Tolerence: float) -> List[Polyline]:
        """Splits a polyline at a point, creating two polylines

        Args:
            SplitPoint: Point to split at
            Tolerence: Tolerance to determine if point is on/near line

        Returns:
            List of polylines [A, B]
        """
        ...

class Polyline3D:
    Points: Any
    @overload
    def __init__(self) -> None:
        """Creates a new 3D polyline that can be later added to a 3D sketch"""
        ...
    @overload
    def __init__(self, Points: List[Any]) -> None:
        """Creates a new 3D polyline that can be later added to a 3D sketch

        Args:
            Points: List of points in the polyline [X1, Y1, Z1, X2, Y2, Z2, ...]
        """
        ...
    @overload
    def AddPoint(self, Point: Optional[PolylinePoint3D]) -> None:
        """Adds a new point to the polyline

        Args:
            Point: Point to add
        """
        ...
    @overload
    def AddPoint(self, X: float, Y: float, Z: float) -> None:
        """Adds a new point to the polyline"""
        ...
    def AddPolyline(self, AppendLine: Optional[Polyline3D]) -> None:
        """Appends a line to the current line

        Args:
            AppendLine: Line to append
        """
        ...
    @overload
    def Clone(self) -> Polyline3D:
        """Creates an exact copy of the line

        Returns:
            Copy of line
        """
        ...
    @overload
    def Clone(self, StartIndex: int, EndIndex: int) -> Polyline3D:
        """Creates an exact copy of a section of the line

        Args:
            StartIndex: 0-based index of first point to include in copy
            EndIndex: 0-based index of last point to include in copy

        Returns:
            Copied line
        """
        ...
    def InsertPoint(self, Index: int, Point: Optional[PolylinePoint3D]) -> None:
        """Inserts a point at a specific location

        Args:
            Index: 0-based index of location to insert
            Point: Point to insert
        """
        ...
    @staticmethod
    def IsPointOnLine(A: Optional[PolylinePoint3D], B: Optional[PolylinePoint3D], P: Optional[PolylinePoint3D], Tolerance: float) -> bool:
        """Determines if a point is on a line segment

        Args:
            A: First point of line segment
            B: Last point of line segment
            P: Point to check
            Tolerance: Fudge factor

        Returns:
            True if point is on line
        """
        ...
    def Join(self, AppendLine: Optional[Polyline3D]) -> Polyline3D:
        """Joins a line onto the end of the current line and returns the new line

        Args:
            AppendLine: The line to join to the current line

        Returns:
            The new line created from this line plus the appended line
        """
        ...
    def Offset(self, OffsetX: float, OffsetY: float, OffsetZ: float) -> None:
        """Applies an offset to all points on the line

        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
        """
        ...
    def RemoveDuplicates(self) -> None:
        """Removes duplicate points that are next to each other"""
        ...
    def SplitAtPoint(self, SplitPoint: Optional[PolylinePoint3D], Tolerence: float) -> List[Polyline3D]:
        """Splits a polyline at a point, creating two polylines

        Args:
            SplitPoint: Point to split at
            Tolerence: Tolerance to determine if point is on/near line

        Returns:
            List of polylines [A, B]
        """
        ...

class PolylinePoint:
    X: float
    """X coordinate"""
    Y: float
    """Y coordinate"""
    @overload
    def __init__(self) -> None:
        """Creates a new polyline point"""
        ...
    @overload
    def __init__(self, X: float, Y: float) -> None:
        """Creates a new polyline point

        Args:
            X: X coordinate
            Y: Y coordinate
        """
        ...
    @staticmethod
    def CrossProduct(P1: Optional[PolylinePoint], P2: Optional[PolylinePoint]) -> float: ...
    def Equals(self, obj: Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Offset(self, X: float, Y: float) -> PolylinePoint:
        """Applies an offset to the point and creates a new point

        Args:
            X: X offset to apply
            Y: Y offset to apply

        Returns:
            New point with offset applied
        """
        ...
    def RotateZ(self, CenterX: float, CenterY: float, Angle: float) -> None:
        """Rotates the point around the Z axis

        Args:
            CenterX: X coordinate of center of rotation
            CenterY: Y coordinate of center of rotation
            Angle: Number of degrees to rotate
        """
        ...
    def Scale(self, ScaleOriginX: float, ScaleOriginY: float, ScaleFactor: float) -> PolylinePoint:
        """Scales the point location based on an origin for the scaling

        Args:
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleFactor: Factor for scaling as a percentage

        Returns:
            New point with scaling applied
        """
        ...
    def ToString(self) -> str: ...

class PolylinePoint3D:
    X: float
    """X coordinate"""
    Y: float
    """Y coordinate"""
    Z: float
    """Z coordinate"""
    @overload
    def __init__(self) -> None:
        """Creates a new polyline point"""
        ...
    @overload
    def __init__(self, X: float, Y: float, Z: float) -> None:
        """Creates a new 3D polyline point

        Args:
            X: X coordinate
            Y: Y coordinate
            Z: Z coordinate
        """
        ...
    def Equals(self, obj: Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Offset(self, X: float, Y: float, Z: float) -> PolylinePoint3D:
        """Applies an offset to the point and creates a new point

        Args:
            X: X offset to apply
            Y: Y offset to apply
            Z: Z offset to apply

        Returns:
            New point with offset applied
        """
        ...
    def Scale(self, ScaleOriginX: float, ScaleOriginY: float, ScaleOriginZ: float, ScaleFactor: float) -> PolylinePoint3D:
        """Scales the point location based on an origin for the scaling

        Args:
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleOriginZ: Z-coordinate for scaling origin
            ScaleFactor: Factor for scaling as a percentage

        Returns:
            New point with scaling applied
        """
        ...
    def ToString(self) -> str: ...

class SketchPoint(ISketchFigure):
    IsReference: bool
    """True if the point is a reference point, false if it is a regular point"""
    Point: Any
    X: float
    """X-coordinate of point"""
    Y: float
    """Y-coordinate of point"""
    @overload
    def __init__(self, Point: Any) -> None: ...
    @overload
    def __init__(self, X: float, Y: float, IsReference: bool) -> None:
        """Creates a new sketch point which can be added to sketches

        Args:
            X: X coordinate of sketch point
            Y: Y coordinate of sketch point
            IsReference: true to create a reference point, false to create a regular point
        """
        ...
    @overload
    def __init__(self) -> None: ...
    def FigureObject(self) -> Any: ...
    @staticmethod
    def FromXml(Xml: Any) -> SketchPoint: ...
    def SetInstance(self, Figure: Any) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class SketchPoint3D:
    IsReference: bool
    """True if the point is a reference point, false if it is a regular point"""
    X: float
    """X-coordinate of point"""
    Y: float
    """Y-coordinate of point"""
    Z: float
    """Z-coordinate of point"""
    @overload
    def __init__(self, Point: Any) -> None: ...
    @overload
    def __init__(self, X: float, Y: float, Z: float, IsReference: bool) -> None:
        """Creates a new 3D sketch point which can be added to sketches

        Args:
            X: X coordinate of point
            Y: Y coordinate of point
            Z: Z coordinate of point
            IsReference: true to create a reference point, false to create a regular point
        """
        ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(Xml: Any) -> SketchPoint3D: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> Any: ...

class ThreeD:
    class RotationDirections:
        X: ThreeD.RotationDirections
        Y: ThreeD.RotationDirections
        Z: ThreeD.RotationDirections

    def __init__(self) -> None: ...
    @staticmethod
    def CreateRotation(Angle: float, Direction: Optional[ThreeD.RotationDirections], GeomFactory: Any) -> Any: ...
    @staticmethod
    def CreateTransformation(OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool, GeomFactory: Any) -> Any: ...
    @staticmethod
    def CreateTranslation(x: float, y: float, z: float, GeomFactory: Any) -> Any: ...
    @staticmethod
    def DecomposeTransformation(Transformation: Any, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float) -> None: ...
    @staticmethod
    def GetMatrixFromTransformation(Transformation: Any) -> Any: ...
    def GetPerpendicularVector(self, Vector: List[Any]) -> List[Any]:
        """Gets a vector that is perpendicular to a vector

        Args:
            Vector: Vector [X, Y, Z]

        Returns:
            Vector that is perpendicular [X, Y, Z]
        """
        ...
    @staticmethod
    def TransformPoint(Point: List[float], Transformation: Any) -> List[float]: ...
    def TransformPointUsingVectors(self, SourceVector: List[Any], DestinationVector: List[Any], Point: List[Any]) -> List[Any]:
        """Transforms a point based on two vectors

        Args:
            SourceVector: Source vector [X, Y, Z]
            DestinationVector: Destination vector [X, Y, Z]
            Point: Point to transform [X, Y, Z]

        Returns:
            Transformed point [X, Y, Z]
        """
        ...
    @staticmethod
    def TransformVector(Vector: List[float], Transformation: Any) -> List[float]: ...
    @staticmethod
    def VectorTransform(Vector1: Any, Vector2: Any) -> Any: ...

class ThumbnailOptions:
    BiggerSizeOk: ThumbnailOptions
    IconOnly: ThumbnailOptions
    InCacheOnly: ThumbnailOptions
    InMemoryOnly: ThumbnailOptions
    None_: ThumbnailOptions
    ThumbnailOnly: ThumbnailOptions

class Trace:
    class LineTypes:
        API: Trace.LineTypes
        Internal: Trace.LineTypes
        ScriptFunc: Trace.LineTypes

    @staticmethod
    def Output(Text: str) -> None: ...
    @staticmethod
    def OutputLine(LineType: Optional[Trace.LineTypes], Text: str, Parameters: List[Any]) -> None: ...
    @staticmethod
    def Start(FileName: str) -> None: ...
    @staticmethod
    def Stop() -> None: ...

class TwoD:
    def __init__(self) -> None: ...
    def GetPerpendicularVector(self, Vector: List[Any]) -> List[Any]:
        """Gets a vector that is perpendicular to a vector

        Args:
            Vector: Vector [X, Y]

        Returns:
            Vector that is perpendicular [X, Y]
        """
        ...
    @staticmethod
    def IsPointInsidePolygon(Vertices: Any, Point: Any) -> bool: ...
    def NormalizeVector(self, Vector: List[Any]) -> List[Any]:
        """Normalizes a vector

        Args:
            Vector: Vector [X, Y]

        Returns:
            Normalized vector [X, Y]
        """
        ...
    def RotatePoint(self, Point: List[Any], Angle: float) -> List[Any]:
        """Rotates a point

        Args:
            Point: Point to rotate as [X, Y]
            Angle: Angle to rotate in degrees

        Returns:
            Rotated point as [RX, RY]
        """
        ...
    @staticmethod
    def TranslatePoint(Point: Any, XTranslation: float, YTranslation: float) -> Any: ...
    @staticmethod
    def _RotatePoint(Point: Any, Angle: float) -> Any: ...

class UnitTypes:
    """Supported units"""
    Centimeters: UnitTypes
    Inches: UnitTypes
    Millimeters: UnitTypes

class Units:
    Current: UnitTypes
    """The current units"""
    @staticmethod
    def FromADUnitType(ADUnit: Any) -> UnitTypes: ...
    @overload
    @staticmethod
    def FromADUnits(Value: float) -> float: ...
    @overload
    @staticmethod
    def FromADUnits(Value: float, CurrentUnits: Any) -> float: ...
    @overload
    @staticmethod
    def FromADUnits(ADValues: Any) -> Any: ...
    @staticmethod
    def FromInches(Value: float) -> float: ...
    @staticmethod
    def FromMillimeters(Value: float) -> float: ...
    @staticmethod
    def FromTeethPerInch(TeethPerInch: float) -> float: ...
    @overload
    @staticmethod
    def ToADUnits(Value: float) -> float: ...
    @overload
    @staticmethod
    def ToADUnits(Values: Any) -> Any: ...
    @overload
    @staticmethod
    def ToADUnits(Value: float, CurrentUnits: Any) -> float: ...
    @staticmethod
    def ToInches(Value: float) -> float: ...
    @staticmethod
    def ToMillimeters(Value: float) -> float: ...
    @staticmethod
    def ToTeethPerInch(TeethPerCurrentUnits: float) -> float: ...

class WindowsInputTypes:
    """Type of Windows input"""
    Assembly: WindowsInputTypes
    Axes: WindowsInputTypes
    Axis: WindowsInputTypes
    Boolean: WindowsInputTypes
    Edge: WindowsInputTypes
    Edges: WindowsInputTypes
    Face: WindowsInputTypes
    Faces: WindowsInputTypes
    File: WindowsInputTypes
    Folder: WindowsInputTypes
    Image: WindowsInputTypes
    Integer: WindowsInputTypes
    Label: WindowsInputTypes
    Part: WindowsInputTypes
    Plane: WindowsInputTypes
    Planes: WindowsInputTypes
    Point: WindowsInputTypes
    Points: WindowsInputTypes
    Real: WindowsInputTypes
    SaveFile: WindowsInputTypes
    Sketch: WindowsInputTypes
    Sketch3D: WindowsInputTypes
    Sketches: WindowsInputTypes
    String: WindowsInputTypes
    StringList: WindowsInputTypes
    Url: WindowsInputTypes
    Vertex: WindowsInputTypes
    Vertices: WindowsInputTypes

def CurrentPart() -> Part:
    """The part in the active window."""
    ...

def CurrentAssembly() -> Assembly:
    """The assembly in the active window."""
    ...

def CurrentParts() -> List[Part]:
    """Every open part."""
    ...

def CurrentAssemblies() -> List[Assembly]:
    """Every open assembly."""
    ...
