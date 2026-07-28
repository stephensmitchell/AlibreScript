# Python 2.7 compatible stub/mock API
## Gets a python list of the current vertices in the part in the assembly coordinate system
def GetAssemblyVertices():
    pass
## Gets the occurrence of the part mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific assembly using the part
def GetMappedOccurrence(Assembly):
    # Assembly: Assembly for occurrence structure
    pass
## Gets the assembly for the part
def GetAssembly():
    pass
## Gets a configuration with a specific name
def GetConfiguration(Name):
    # Name: Name of confguration
    pass
## Gets the bounding box for the part as eight points in the assembly coordinate system
def GetAssemblyBoundingBox():
    pass
## Converts a point in the part coordinate system into a point in the assembly coordinate system
def PartPointtoAssemblyPoint(PartPoint):
    # PartPoint: Point [X, Y, Z] in the part coordinate system
    pass
## Converts a point in the assembly coordinate system into a point in the part coordinate system
def AssemblyPointtoPartPoint(AssemblyPoint):
    # AssemblyPoint: Point [X, Y, Z] in the assembly coordinate system
    pass
## Gets a face using it's name "Face<n>"
def GetFace(Name):
    # Name: Name of face
    pass
## Gets an edge using it's name "Edge<n>"
def GetEdge(Name):
    # Name: Name of edge
    pass
## Gets a python list of the current edges in the part
def GetEdges():
    pass
## Gets a python list of the current faces in the part
def GetFaces():
    pass
## Adds a point at an offset to a point or a vertex
def AddPoint(Name, PointOrVertex, XOffset, YOffset, ZOffset):
    # Name: Name of point
    # PointOrVertex: Point or vertex
    # XOffset: X offse
    # YOffset: Y offset
    # ZOffset: Z offset
    pass
## Adds a point between two points/vertices
def AddPoint(Name, PointOrVertex1, PointOrVertex2, Ratio):
    # Name: Name of point
    # PointOrVertex1: First point or vertex
    # PointOrVertex2: Second point or vertex
    # Ratio: Ratio of distance between points/vertices
    pass
## Adds a point at the intersection or two axes or edges
def AddPoint(Name, AxisOrEdge1, AxisOrEdge2):
    # Name: Name of point
    # AxisOrEdge1: First axis or edge
    # AxisOrEdge2: Second axis or edge
    pass
## Adds a point at the intersection of three planes or faces
def AddPoint(Name, PlaneOrFace1, PlaneOrFace2, PlaneOrFace3):
    # Name: Name of point
    # PlaneOrFace1: First plane or face
    # PlaneOrFace2: Second plane or face
    # PlaneOrFace3: Third plane or face
    pass
## Adds a point at the the intersection of a axis or edge and a plane or face
def AddPoint(Name, AxisOrEdge, PlaneOrFace):
    # Name: Name of point
    # AxisOrEdge: Axis or edge
    # PlaneOrFace: Plane or face
    pass
## Adds a point by projecting a point or vertex onto a plane or face
def AddPoint(Name, SourcePointOrVertex, TargetPlaneOrFace, XOffset, YOffset):
    # Name: Name of point
    # SourcePointOrVertex: Point or vertex to project
    # TargetPlaneOrFace: Plane or face to project onto
    # XOffset: X offset to apply to point once projected
    # YOffset: Y offset to apply to point once projected
    pass
## Adds a point on an edge
def AddPoint(Name, TargetEdge, Ratio):
    # Name: Name of point
    # TargetEdge: The edge to create the point on
    # Ratio: Ratio along the edge from 0.0 -> 1.0
    pass
## Adds a point at the center of a circular edge
def AddPointFromCircularEdge(Name, TargetEdge):
    # Name: Name of point
    # TargetEdge: The edge to use for creating the point
    pass
## Adds a point at the center of a toroidal face
def AddPointFromToroidalFace(Name, TargetFace):
    # Name: Name of point
    # TargetFace: Toroidal face to use in creating the point
    pass
## Removes a point from the part
def RemovePoint(Point):
    # Point: Point to remove
    pass
## Removes a plane from the part
def RemovePlane(Plane):
    # Plane: Plane to remove
    pass
## Removes a sketch from the part
def RemoveSketch(Name):
    # Name: Name of sketch to remove
    pass
## Removes a sketch from the part
def RemoveSketch(Sketch):
    # Sketch: Sketch to remove
    pass
## Creates a new 3D sketch
def Add3DSketch(Name):
    # Name: Name of sketch
    pass
## Adds a gear sketch to the part
def AddGear(Name, NumberofTeeth, PitchDiameter, PressureAngle, DiametralPitch, SingleTooth, CenterX, CenterY, InvolutePoints, Plane):
    # Name: Name of gear sketch
    # NumberofTeeth: Number of teeth
    # PitchDiameter: Diameter of pitch circle in current units
    # PressureAngle: Pressure angle (14.5 is typical)
    # DiametralPitch: Diametral angle (tooth size) (25.4/module) in teeth per inch
    # SingleTooth: true to create only a single tooth profile
    # CenterX: X-coordinate of gear center
    # CenterY: Y-coordinate of gear center
    # InvolutePoints: Number of points for involute curve. Decreasing this makes Cubify/Geomagic faster. Increasing makes tooth profiles more accurate and allows gears with more teeth to be generated.
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using number of teeth and pitch diameter
def AddGearNP(Name, NumberofTeeth, PitchDiameter, PressureAngle, CenterX, CenterY, Plane):
    # Name: Name of gear sketch
    # NumberofTeeth: Number of teeth
    # PitchDiameter: Diameter of pitch circle
    # PressureAngle: Pressure angle (14.5 is typical)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using number of teeth and pitch diameter
def AddGearNP(Name, NumberofTeeth, PitchDiameter, PressureAngle, CenterX, CenterY, SingleTooth, Plane):
    # Name: Name of gear sketch
    # NumberofTeeth: Number of teeth
    # PitchDiameter: Diameter of pitch circle
    # PressureAngle: Pressure angle (14.5 is typical)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # SingleTooth: True to generate a single tooth
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using diametral pitch and pitch diameter
def AddGearDP(Name, PitchDiameter, PressureAngle, DiametralPitch, CenterX, CenterY, Plane):
    # Name: Name of gear sketch
    # PitchDiameter: Diameter of pitch circle
    # PressureAngle: Pressure angle (14.5 is typical)
    # DiametralPitch: Diametral angle (tooth size) (1/module)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using diametral pitch and pitch diameter
def AddGearDP(Name, PitchDiameter, PressureAngle, DiametralPitch, CenterX, CenterY, SingleTooth, Plane):
    # Name: Name of gear sketch
    # PitchDiameter: Diameter of pitch circle
    # PressureAngle: Pressure angle (14.5 is typical)
    # DiametralPitch: Diametral angle (tooth size) (1/module)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # SingleTooth: True to generate a single tooth
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using diametral pitch and number of teeth
def AddGearDN(Name, NumberofTeeth, PressureAngle, DiametralPitch, CenterX, CenterY, Plane):
    # Name: Name of gear sketch
    # NumberofTeeth: Number of teeth
    # PressureAngle: Pressure angle (14.5 is typical)
    # DiametralPitch: Diametral angle (tooth size) (1/module)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # Plane: Plane or face to create gear sketch on
    pass
## Adds a gear sketch to the part using diametral pitch and number of teeth
def AddGearDN(Name, NumberofTeeth, PressureAngle, DiametralPitch, CenterX, CenterY, SingleTooth, Plane):
    # Name: Name of gear sketch
    # NumberofTeeth: Number of teeth
    # PressureAngle: Pressure angle (14.5 is typical)
    # DiametralPitch: Diametral angle (tooth size) (1/module)
    # CenterX: X-coordinate of center of gear
    # CenterY: Y-coordinate of center of gear
    # SingleTooth: True to generate a single tooth
    # Plane: Plane or face to create gear sketch on
    pass
## Creates an axis based on the intersection of two planes/faces
def AddAxis(Name, Plane1, Plane2):
    # Name: Name of axis
    # Plane1: First plane/face
    # Plane2: Second plane/face
    pass
## Creates an axis based on two points
def AddAxis(Name, PointA, PointB):
    # Name: Name of axis
    # PointA: First point object
    # PointB: Second point object
    pass
## Creates an axis for a cylindrical face
def AddAxis(Name, CylindricalFace):
    # Name: Name of axis
    # CylindricalFace: Cylindrical face
    pass
## Creates an axis based on two points
def AddAxis(Name, Point1, Point2):
    # Name: Name of axis
    # Point1: First point [X, Y, Z]
    # Point2: Second point [X, Y, Z]
    pass
## Adds a point to the part
def AddPoint(Name, Point):
    # Name: Name of the new point
    # Point: Point location [x, y, z]
    pass
## Adds a point to the part
def AddPoint(Name, Point):
    # Name: Name of the point
    # Point: Point to add
    pass
## Adds a point to the part
def AddPoint(Name, X, Y, Z):
    # Name: Name of new point
    # X: X coordinate
    # Y: Y coordinate
    # Z: Z coordinate
    pass
## Adds a set of points to the part
def AddPoints(Prefix, Points):
    # Prefix: Prefix for the point names
    # Points: List of points [x1,y1,z1, ..., xn,yn,zn]
    pass
## Regenerates the part
def Regenerate():
    pass
## Adds a simple extrude boss to a specific depth
def AddExtrudeBoss(Name, Sketch, Depth, IsReversed):
    # Name: Name of extrusion
    # Sketch: Sketch to extrude
    # Depth: Extrusion distance
    # IsReversed: True if extrusion direction is reversed
    pass
## Adds an extrude feature
def AddExtrudeBoss(Name, Sketch, Depth, IsReversed, EndCondition, EndPlane, EndOffset, Direction, SweepPath, DraftAngle, OutwardDraft):
    # Name: Name of extrusion
    # Sketch: Sketch to extrude
    # Depth: Depth of extrusion
    # IsReversed: true if direction is reversed
    # EndCondition: End condition for extrusion
    # EndPlane: Face or plane to terminate extrusion
    # EndOffset: Offset from face or plane to terminate extrusion
    # Direction: Direction of extrusion
    # SweepPath: Sketch or edge to follow when extruding
    # DraftAngle: Angle of draft
    # OutwardDraft: true if outward draft
    pass
## Adds a simple extrude cut to a specific depth
def AddExtrudeCut(Name, Sketch, Depth, IsReversed):
    # Name: Name of extrusion
    # Sketch: Sketch to extrude
    # Depth: Extrusion distance
    # IsReversed: True if extrusion direction is reversed
    pass
## Adds an extrude cut feature
def AddExtrudeCut(Name, Sketch, Depth, IsReversed, EndCondition, EndPlane, EndOffset, Direction, SweepPath, DraftAngle, OutwardDraft):
    # Name: Name of extrusion
    # Sketch: Sketch to extrude
    # Depth: Depth of extrusion
    # IsReversed: true if direction is reversed
    # EndCondition: End condition for extrusion
    # EndPlane: Face or plane to terminate extrusion
    # EndOffset: Offset from face or plane to terminate extrusion
    # Direction: Direction of extrusion
    # SweepPath: Sketch or edge to follow when extruding
    # DraftAngle: Angle of draft
    # OutwardDraft: true if outward draft
    pass
## Creates a revolve boss feature
def AddRevolveBoss(Name, Sketch, Axis, Angle):
    # Name: Name of feature
    # Sketch: Sketch to revolve
    # Axis: Axis to rotate around
    # Angle: Rotation angle in degrees
    pass
## Creates a revolve cut feature
def AddRevolveCut(Name, Sketch, Axis, Angle):
    # Name: Name of feature
    # Sketch: Sketch to revolve
    # Axis: Axis to rotate around
    # Angle: Rotation angle in degrees
    pass
## Adds a loft extrusion
def AddLoftBoss(Name, CrossSections, MinimizeTwist, MinimizeCurvature, SimplifySurface, ConnectEnds):
    # Name: Name of loft
    # CrossSections: Python list of cross sections (faces, 2D sketches, design points)
    # MinimizeTwist: True to minimize twist
    # MinimizeCurvature: True to minimize curvature
    # SimplifySurface: True to simplify the loft surface
    # ConnectEnds: True to connect the start of the loft with the end
    pass
## Adds a loft extrusion using guide curves
def AddLoftBoss(Name, CrossSections, GuideCurves, GuideType, MinimizeTwist, MinimizeCurvature, SimplifySurface, ConnectEnds):
    # Name: Name of loft
    # CrossSections: Python list of cross sections (faces, 2D sketches, design points)
    # GuideCurves: Python list of guide curves (3D sketches)
    # GuideType: Type of guide curve
    # MinimizeTwist: True to minimize twist
    # MinimizeCurvature: True to minimize curvature
    # SimplifySurface: True to simplify the loft surface
    # ConnectEnds: True to connect the start of the loft with the end
    pass
## Adds a loft cut
def AddLoftCut(Name, CrossSections, MinimizeTwist, MinimizeCurvature, SimplifySurface, ConnectEnds):
    # Name: Name of loft
    # CrossSections: Python list of cross sections (faces, 2D sketches, design points)
    # MinimizeTwist: True to minimize twist
    # MinimizeCurvature: True to minimize curvature
    # SimplifySurface: True to simplify the loft surface
    # ConnectEnds: True to connect the start of the loft with the end
    pass
## Adds a loft cut using guide curves
def AddLoftCut(Name, CrossSections, GuideCurves, GuideType, MinimizeTwist, MinimizeCurvature, SimplifySurface, ConnectEnds):
    # Name: Name of loft
    # CrossSections: Python list of cross sections (faces, 2D sketches, design points)
    # GuideCurves: Python list of guide curves (3D sketches)
    # GuideType: Type of guide curve
    # MinimizeTwist: True to minimize twist
    # MinimizeCurvature: True to minimize curvature
    # SimplifySurface: True to simplify the loft surface
    # ConnectEnds: True to connect the start of the loft with the end
    pass
## Adds a sweep extrude feature
def AddSweepBoss(Name, ProfileSketch, PathSketch, IsRigid, EndCondition, EndPlane, EndOffset, DraftAngle, OutwardDraft):
    # Name: Name of extrusion
    # ProfileSketch: Sketch to extrude
    # PathSketch: Sketch or edge to sweep along
    # IsRigid: true if path is parallel to profile
    # EndCondition: End condition for extrusion
    # EndPlane: Face or plane to terminate extrusion
    # EndOffset: Offset from face or plane to terminate extrusion
    # DraftAngle: Angle of draft
    # OutwardDraft: true if outward draft
    pass
## Adds a sweep extrude cut feature
def AddSweepCut(Name, ProfileSketch, PathSketch, IsRigid, EndCondition, EndPlane, EndOffset, DraftAngle, OutwardDraft):
    # Name: Name of extrusion
    # ProfileSketch: Sketch to extrude
    # PathSketch: Sketch or edge to sweep along
    # IsRigid: true if path is parallel to profile
    # EndCondition: End condition for extrusion
    # EndPlane: Face or plane to terminate extrusion
    # EndOffset: Offset from face or plane to terminate extrusion
    # DraftAngle: Angle of draft
    # OutwardDraft: true if outward draft
    pass
## Adds a constant radius fillet to a face or edge
def AddFillet(Name, Item, Radius, TangentPropagate):
    # Name: Name of fillet
    # Item: Face or edge to fillet
    # Radius: Radius of fillet
    # TangentPropagate: True to propagate the fillet along connected edges
    pass
## Adds a constant radius fillet to a set of faces and edges
def AddFillet(Name, Items, Radius, TangentPropagate):
    # Name: Name of fillet
    # Items: Faces and edges to fillet
    # Radius: Radius of fillet
    # TangentPropagate: True to propagate the fillet along connected edges
    pass
## Adds a variable radius fillet to a set of faces and edges
def AddFillet(Name, Items, StartRadii, EndRadii, TangentPropagate):
    # Name: Name of fillet
    # Items: Faces and edges to fillet
    # StartRadii: Start radii of fillets
    # EndRadii: End radii of fillets
    # TangentPropagate: True to propagate the fillet along connected edges
    pass
## Uniform scaling of the part
def Scale(Name, ScaleAboutCenter, ScaleFactor):
    # Name: Name of the scaling
    # ScaleAboutCenter: true to scale around the center of the part
    # ScaleFactor: Scale factor
    pass
## Non-uniform scaling of the part
def NonUniformScale(Name, ScaleAboutCenter, ScaleFactorX, ScaleFactorY, ScaleFactorZ):
    # Name: Name of the scaling
    # ScaleAboutCenter: true to scale around the center of the part
    # ScaleFactorX: X scale factor
    # ScaleFactorY: Y scale factor
    # ScaleFactorZ: Z scale factor
    pass
## Adds a chamfer to a face or edge
def AddChamfer(Name, Item, Distance1, Distance2, TangentPropagate):
    # Name: Name of chamfer
    # Item: Face or edge to chamfer
    # Distance1: First chamfer distance
    # Distance2: Second chamfer distance
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Adds a chamfer to a set of faces and edges
def AddChamfer(Name, Items, Distance1, Distance2, TangentPropagate):
    # Name: Name of chamfer
    # Items: Faces and edges to chamfer
    # Distance1: First chamfer distance
    # Distance2: Second chamfer distance
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Adds a chamfer to a face or edge
def AddChamfer(Name, Item, Distance, TangentPropagate):
    # Name: Name of chamfer
    # Item: Face or edge to chamfer
    # Distance: Chamfer distance
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Gets a python list of the current edges in the part
def GetEdges():
    pass
## Gets a python list of the current faces in the part
def GetFaces():
    pass
## Gets a python list of the current vertices in the part
def GetVertices():
    pass
## Gets the bounding box for the part as eight points
def GetBoundingBox():
    pass
## Adds a chamfer to a set of faces and edges
def AddChamfer(Name, Items, Distance, TangentPropagate):
    # Name: Name of chamfer
    # Items: Faces and edges to chamfer
    # Distance: Chamfer distance
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Adds a chamfer to a face or edge
def AddChamferAngle(Name, Item, Distance, Angle, TangentPropagate):
    # Name: Name of chamfer
    # Item: Face or edge to chamfer
    # Distance: Chamfer distance
    # Angle: Chamfer angle
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Adds a chamfer to a set of faces and edges
def AddChamferAngle(Name, Items, Distance, Angle, TangentPropagate):
    # Name: Name of chamfer
    # Items: Faces and edges to chamfer
    # Distance: Chamfer distance
    # Angle: Chamfer angle
    # TangentPropagate: True to propagate the chamfer along connected edges
    pass
## Adds a chamfer to a vertex
def AddVertexChamfer(Name, Item, Distance1, Distance2, Distance3):
    # Name: Name of chamfer
    # Item: Vertex to chamfer
    # Distance1: First chamfer distance
    # Distance2: Second chamfer distance
    # Distance3: Third chamfer distance
    pass
## Adds a chamfer to a set of vertices
def AddVertexChamfer(Name, Items, Distance1, Distance2, Distance3):
    # Name: Name of chamfer
    # Items: Vertices to chamfer
    # Distance1: First chamfer distance
    # Distance2: Second chamfer distance
    # Distance3: Third chamfer distance
    pass
## Saves the part using the current path and file name
def Save():
    pass
## Saves the part to a specific folder
def Save(Folder):
    # Folder: Folder to save to
    pass
## Saves the part to a specific folder with a new name
def SaveAs(Folder, NewName):
    # Folder: Folder to save to
    # NewName: New name for part
    pass
## Closes the part If it is unsaved then changes will be lost
def Close():
    pass
## Exports the part as an STL file
def ExportSTL(FileName):
    # FileName: Path and name of STL file
    pass
## Exports the part as an STL rotated so that a specific face is on the bottom
def ExportRotatedSTL(FileName, BottomFace, ForcetoMillimeters, UseCustomSettings, MaxCellSize, NormalDeviation, SurfaceDeviation):
    # FileName: Path and name of STL file
    # BottomFace: Face to use as bottom of part
    # ForcetoMillimeters: true to output STL in millimeters regardless of part units
    # UseCustomSettings: true to use custom STL settings, false to use settings in system properties
    # MaxCellSize: Custom max cell size
    # NormalDeviation: Custom normal deviation
    # SurfaceDeviation: Custom surface deviation
    pass
## Gets the display units for the part
def DisplayUnits():
    pass
## Exports the part as a STEP 203 file
def ExportSTEP203(FileName):
    # FileName: Path and name of STEP 203 file
    pass
## Exports the part as a STEP 214 file
def ExportSTEP214(FileName):
    # FileName: Path and name of STEP 214 file
    pass
## Exports the part as a IGES file
def ExportIGES(FileName):
    # FileName: Path and name of IGES file
    pass
## Exports the part as a SAT file
def ExportSAT(FileName, Version, SaveColors):
    # FileName: Path and name of SAT file
    # Version: Exported SAT file version
    # SaveColors: true to preseve colors
    pass
## Exports a keyshot file
def ExportBIP(FileName):
    # FileName: Path and name of keyshot file
    pass
## Sets the color of the part
def SetColor(Red, Green, Blue):
    # Red: Red component 0 - 255
    # Green: Green component 0 - 255
    # Blue: Blue component 0 - 255
    pass
## Saves the current view as a bitmap image
def SaveSnapshot(FileName, Width, Height, UseAspectRatio, UseWidthandHeight):
    # FileName: Path and name of file to save to
    # Width: Width in pixels
    # Height: Height in pixels
    # UseAspectRatio: if true uses greater of width/height along with current aspect ratio
    # UseWidthandHeight: if true uses current width/height of view
    pass
## Saves a thumbnail image of the part
def SaveThumbnail(FileName, Width, Height):
    # FileName: Path and name of file to save to
    # Width: Width of thumbnail in pixels
    # Height: Height of thumbnail in pixels
    pass
## Selects a face, edge, vertex, point, axis, plane, sketch
def Select(FaceorEdge):
    # FaceorEdge: Face, edge, vertex, point, axis plane or sketch to select
    pass
## Selects a group of faces, edges, vertices, points, axes, planes and sketches
def Select(FacesEdgesList):
    # FacesEdgesList: List of Faces, edges, vertices, points, axes, planes and sketches to select [FaceA, FaceB, EdgeA, EdgeB, ...]
    pass
## Sets user data
def SetUserData(Name, Dict):
    # Name: Data name of the format companyname.projectname.dataname
    # Dict: Python dictionary of data to store
    pass
## Gets user data
def GetUserData(Name):
    # Name: Name of data to get
    pass
## Pauses updating the part user interface
def PauseUpdating():
    pass
## Resumes updating the part user interface
def ResumeUpdating():
    pass
## The assembly that the part was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Add a point at an offset to a point or a vertex
def AddPoint(Name, PointOrVertex, XOffset, YOffset, ZOffset):
    # Name: Name of point
    # PointOrVertex: Point or vertex
    # XOffset: X offse
    # YOffset: Y offset
    # ZOffset: Z offset
    pass
## Add a point between two points/vertices
def AddPoint(Name, PointOrVertex1, PointOrVertex2, Ratio):
    # Name: Name of point
    # PointOrVertex1: First point or vertex
    # PointOrVertex2: Second point or vertex
    # Ratio: Ratio of distance between points/vertices
    pass
## Add a point at the intersection or two axes or edges
def AddPoint(Name, AxisOrEdge1, AxisOrEdge2):
    # Name: Name of point
    # AxisOrEdge1: First axis or edge
    # AxisOrEdge2: Second axis or edge
    pass
## Add a point at the intersection of three planes or faces
def AddPoint(Name, PlaneOrFace1, PlaneOrFace2, PlaneOrFace3):
    # Name: Name of point
    # PlaneOrFace1: First plane or face
    # PlaneOrFace2: Second plane or face
    # PlaneOrFace3: Third plane or face
    pass
## Add a point at the the intersection of a axis or edge and a plane or face
def AddPoint(Name, AxisOrEdge, PlaneOrFace):
    # Name: Name of point
    # AxisOrEdge: Axis or edge
    # PlaneOrFace: Plane or face
    pass
## Add a point by projecting a point or vertex onto a plane or face
def AddPoint(Name, SourcePointOrVertex, TargetPlaneOrFace, XOffset, YOffset):
    # Name: Name of point
    # SourcePointOrVertex: Point or vertex to project
    # TargetPlaneOrFace: Plane or face to project onto
    # XOffset: X offset to apply to point once projected
    # YOffset: Y offset to apply to point once projected
    pass
## Add a point on an edge
def AddPoint(Name, TargetEdge, Ratio):
    # Name: Name of point
    # TargetEdge: The edge to create the point on
    # Ratio: Ratio along the edge from 0.0 -> 1.0
    pass
## Adds a point at the center of a circular edge
def AddPointFromCircularEdge(Name, TargetEdge):
    # Name: Name of point
    # TargetEdge: The edge to use for creating the point
    pass
## Adds a point at the center of a toroidal face
def AddPointFromToroidalFace(Name, TargetFace):
    # Name: Name of point
    # TargetFace: Toroidal face to use in creating the point
    pass
## Checks if the part is opened
def IsOpen():
    pass
## Gets a feature on the part
def GetFeature(Name):
    # Name: Name of the feature to get
    pass
## Removes a feature from the part
def RemoveFeature(Name):
    # Name: Name of the feature to remove
    pass
## Removes a feature from the part
def RemoveFeature(Feature):
    # Feature: Feature to remove
    pass
## Suppresses a feature on the part
def SuppressFeature(Name):
    # Name: Name of the feature to suppress
    pass
## Suppresses a feature on the part
def SuppressFeature(Feature):
    # Feature: Feature to suppress
    pass
## Unsuppresses a feature on the part
def UnsuppressFeature(Name):
    # Name: Name of the feature to unsuppress
    pass
## Unsuppresses a feature on the part
def UnsuppressFeature(Feature):
    # Feature: Feature to unsuppress
    pass
## Hides a feature on the part
def HideFeature(Name):
    # Name: Name of the feature to hide
    pass
## Hides a feature on the part
def HideFeature(Feature):
    # Feature: Feature to hide
    pass
## Shows a feature on the part
def ShowFeature(Name):
    # Name: Name of the feature to show
    pass
## Shows a feature on the part
def ShowFeature(Feature):
    # Feature: Feature to show
    pass
## Gets a plane using the name of the plane
def GetPlane(Name):
    # Name: Name of plane to find
    pass
## Gets an axis from an axis name
def GetAxis(Name):
    # Name: Name of axis to find
    pass
## Gets a point on the part using the point name. The point must have been created in a script
def GetPoint(Name):
    # Name: Name of point to get
    pass
## Gets a sketch using the name of the sketch
def GetSketch(Name):
    # Name: Name of sketch
    pass
## Gets a sketch using the name of the sketch
def Get3DSketch(Name):
    # Name: Name of sketch
    pass
## Gets a face using it's name "Face<n>"
def GetFace(Name):
    # Name: Name of face
    pass
## Gets an edge using it's name "Edge<n>"
def GetEdge(Name):
    # Name: Name of edge
    pass
## Gets a vertex using it's name "Vertex<n>"
def GetVertex(Name):
    # Name: Name of vertex
    pass
## Gets a parameter with a specific name
def GetParameter(Name):
    # Name: Name of parameter
    pass
## Gets the value of a custonm property
def GetCustomProperty(Name):
    # Name: Name of the custom property
    pass
## Sets the value of a custom property The custom property must already be defined on the part or defined on the user's PC
def SetCustomProperty(Name, Value):
    # Name: Name of the custom property
    # Value: New value for the custom property
    pass
## Gets a configuration with a specific name
def GetConfiguration(Name):
    # Name: Name of confguration
    pass
## Gets the currently active configuration
def GetActiveConfiguration():
    pass
## Creates a plane based on the offset from an existing plane
def AddPlane(Name, SourcePlane, Offset):
    # Name: Name of plane
    # SourcePlane: Plane/face to use as basis
    # Offset: Offset from basis plane in currently chosen units
    pass
## Adds a plane using a normal vector and a point on the plane
def AddPlane(Name, NormalVector, PointonPlane):
    # Name: Name of plane to add
    # NormalVector: Normal vector as a list [nx, ny, nz]. Does not need to be a unit vector
    # PointonPlane: A point on the plane as a list [px, py, pz]
    pass
## Creates a new plane contaning an axis and a point
def AddPlane(Name, Axis, Point):
    # Name: Name of new plane
    # Axis: Axis that lies on plane
    # Point: Point that lies on plane
    pass
## Creates a new plane at an angle to an existing plane
def AddPlane(Name, SourcePlane, RotationAxis, Angle):
    # Name: Name of new plane
    # SourcePlane: Plane/face to use as basis for new plane
    # RotationAxis: Axis of rotation for new plane
    # Angle: Angle of new plane in degrees
    pass
## Adds a cm/mm/in/deg parameter to the part
def AddParameter(Name, Type, Value):
    # Name: Name of parameter
    # Type: Type of parameter
    # Value: Value for parameter
    pass
## Adds a parameter to the part with specific units
def AddParameter(Name, Type, UnitstoUse, Value):
    # Name: Name of parameter
    # Type: Type of parameter
    # UnitstoUse: Units to use
    # Value: Value for parameter
    pass
## NOTE: DOESN'T SEEM TO WORK IN GD V16 - THROWS EXCEPTION ABOUT TRANSACTION ALREADY BEING OPEN. Adds a parameter to the part
def AddParameter(Name, Type, Equation):
    # Name: Name of parameter
    # Type: Type of parameter
    # Equation: Equation for parameter
    pass
## Adds a configuration to the part
def AddConfiguration(Name):
    # Name: Name of configuration
    pass
## Adds a configuration to the part using another configuration as a base
def AddConfiguration(Name, BaseConfigurationName):
    # Name: Name of configuration
    # BaseConfigurationName: Name of base configuration to use
    pass
## Creates a plane using three points. Each point is defined as list of [x, y, z]
def AddPlane(Name, Point1, Point2, Point3):
    # Name: Name of plane
    # Point1: Point on plane
    # Point2: Point on plane
    # Point3: Point on plane
    pass
## Creates a new sketch using a plane/face
def AddSketch(Name, Plane):
    # Name: Name of sketch
    # Plane: Plane/face to use for sketch
    pass
## Name of the assembled part
def Name():
    pass
## List of configurations defined on the part
def Configurations():
    pass
## List of parameters defined on the part
def Parameters():
    pass
## Density of the part
def Density():
    pass
## Material of the part
def Material():
    pass
## Description of the part
def Description():
    pass
## User-defined number for the part
def Number():
    pass
## Mass of the part
def Mass():
    pass
## Comment property
def Comment():
    pass
## Cost center property
def CostCenter():
    pass
## Created By property
def CreatedBy():
    pass
## Created Date property
def CreatedDate():
    pass
## Creating Application property
def CreatingApplication():
    pass
## Document Number property
def DocumentNumber():
    pass
## Engineering Approval Date property
def EngineeringApprovalDate():
    pass
## Engineering Approved By property
def EngineeringApprovedBy():
    pass
## Estimated Cost property
def EstimatedCost():
    pass
## Keywords property
def Keywords():
    pass
## Last Author property
def LastAuthor():
    pass
## Last Update Date property
def LastUpdateDate():
    pass
## Material (extended information) property
def ExtendedMaterialInformation():
    pass
## Manufacturing Approved By property
def ManufacturingApprovedBy():
    pass
## Product property
def ManufacturingApprovedDate():
    pass
## Modified Information property
def ModifiedInformation():
    pass
## Product property
def Product():
    pass
## Received From property
def ReceivedFrom():
    pass
## Revision property
def Revision():
    pass
## Stock Size property
def StockSize():
    pass
## Supplier property
def Supplier():
    pass
## Title property
def Title():
    pass
## Vendor property
def Vendor():
    pass
## Web Link property
def WebLink():
    pass
## Path and filename of the part
def FileName():
    pass
## Gets the XY-plane (language independent)
def XYPlane():
    pass
## Gets the YZ-plane (language independent)
def YZPlane():
    pass
## Gets the ZX-plane (language independent)
def ZXPlane():
    pass
## Gets the X-axis (language independent)
def XAxis():
    pass
## Gets the Y-axis (language independent)
def YAxis():
    pass
## Gets the Z-axis (language independent)
def ZAxis():
    pass
## Gets the origin (language independent)
def Origin():
    pass
## Gets the currently selected items as [ItemA, ItemB, ...] Supports faces, edges, vertices, planes, axes and points
def Selections():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Gets the occurrence of the sub-assembly mapped into the occurrence structure of a specific assembly This occurrence can be used to create constraints in the specific sub-assembly using the part
def GetMappedOccurrence(Assembly):
    # Assembly: Assembly for occurrence structure
    pass
## Gets a configuration with a specific name
def GetConfiguration(Name):
    # Name: Name of confguration
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(FileName, OffsetX, OffsetY, OffsetZ):
    # FileName: Path and name of sub-assembly to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(FileName, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # FileName: Path and name of sub-asembly to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Adds a simple mate constraint between two planes/faces/axes/edges/points
def AddMateConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB):
    # Distance: Mate distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    pass
## Adds a simple mate constraint between two planes/faces/axes/edges/points
def AddMateConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # Distance: Mate distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds a mate constraint between two planes/faces/axes/edges/points Uses bounds type
def AddMateConstraint2(Distance1, Distance2, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name, BoundsType):
    # Distance1: Mate distance
    # Distance2: Second distance for 'between' bounds type or zero if not used
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    # BoundsType: The bounds type to use
    pass
## Adds a fastner constraint
def AddFastenerConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # Distance: Fastener to surface mate distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds a fastner constraint
def AddFastenerConstraint2(Distance1, Distance2, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name, BoundsType):
    # Distance1: Fastener to surface mate distance
    # Distance2: Second distance for 'between' bounds type or zero if not used
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    # BoundsType: The bounds type to use
    pass
## Adds a simple alignment constraint between two planes/faces/axes/edges/points
def AddAlignConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB):
    # Distance: Alignment distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    pass
## Adds a simple alignment constraint between two planes/faces/axes/edges/points
def AddAlignConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # Distance: Alignment distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds an alignment constraint between two planes/faces/axes/edges/points Uses bounds type
def AddAlignConstraint2(Distance1, Distance2, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name, BoundsType):
    # Distance1: Align distance
    # Distance2: Second distance for 'between' bounds type or zero if not used
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    # BoundsType: The bounds type to use
    pass
## Adds an orient constraint between two planes/faces/axes/edges/points
def AddOrientConstraint(Value, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB):
    # Value: Value
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    pass
## Adds an orient constraint between two planes/faces/axes/edges/points
def AddOrientConstraint(Value, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # Value: Value
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds an angle constraint between two planes/faces/axes/edges/points
def AddAngleConstraint(Angle, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB):
    # Angle: Angle in degrees
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    pass
## Adds a simple angle constraint between two planes/faces/axes/edges/points
def AddAngleConstraint(Angle, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # Angle: Angle in degrees
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds an angle constraint between two planes/faces/axes/edges/points Uses bounds type
def AddAngleConstraint2(Angle1, Angle2, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name, BoundsType):
    # Angle1: Angle for constraint
    # Angle2: Second angle for 'between' bounds type or zero if not used
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    # BoundsType: The bounds type to use
    pass
## Adds a gear constraint using ratio RatioA:RatioB
def AddGearConstraint(RatioA, RatioB, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # RatioA: First value in gear ratio
    # RatioB: Second value in gear ratio
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds a rack and pinion constraint
def AddRackAndPinionConstraint(PitchDiameter, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # PitchDiameter: Pitch diameter
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds a screw constraint
def AddScrewConstraint(ThreadPitch, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, IsReversed, Name):
    # ThreadPitch: Pitch of thread
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Adds a tangent constraint between two planes/faces/axes/edges/points
def AddTangentConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, Outside):
    # Distance: Alignment distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # Outside: true for an outside tangent constraint, false for an inside tangent constraint
    pass
## Adds a tangent constraint between two planes/faces/axes/edges/points
def AddTangentConstraint(Distance, PartorAssemblyA, ItemA, PartorAssemblyB, ItemB, Outside, IsReversed, Name):
    # Distance: Alignment distance
    # PartorAssemblyA: First part/assembly to constrain
    # ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
    # PartorAssemblyB: Second part/assembly to constrain
    # ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
    # Outside: true for an outside tangent constraint, false for an inside tangent constraint
    # IsReversed: true to reverse constraint
    # Name: Name of constraint
    pass
## Creates a unique name that can be used to safely add a part or subassembly to the assembly if the names used in the assembly are not known in advance
def CreateUniqueName(BaseName):
    # BaseName: Base name to use
    pass
## Exports the assembly as an STL file
def ExportSTL(FileName):
    # FileName: Path and name of STL file
    pass
## Exports the assembly as a STEP 203 file
def ExportSTEP203(FileName):
    # FileName: Path and name of STEP 203 file
    pass
## Exports the assembly as a STEP 214 file
def ExportSTEP214(FileName):
    # FileName: Path and name of STEP 214 file
    pass
## Exports the assembly as a IGES file
def ExportIGES(FileName):
    # FileName: Path and name of IGES file
    pass
## Exports the assembly as a SAT file
def ExportSAT(FileName, Version, SaveColors):
    # FileName: Path and name of SAT file
    # Version: Exported SAT file version
    # SaveColors: true to preseve colors
    pass
## Exports a keyshot file
def ExportBIP(FileName):
    # FileName: Path and name of keyshot file
    pass
## Sets user data
def SetUserData(Name, Dict):
    # Name: Data name of the format companyname.projectname.dataname
    # Dict: Python dictionary of data to store
    pass
## Gets user data
def GetUserData(Name):
    # Name: Name of data to get
    pass
## Pauses updating the assembly user interface
def PauseUpdating():
    pass
## Resumes updating the assembly user interface
def ResumeUpdating():
    pass
## Add a point at an offset to a point or a vertex
def AddPoint(Name, PointOrVertex, XOffset, YOffset, ZOffset):
    # Name: Name of point
    # PointOrVertex: Point or vertex
    # XOffset: X offse
    # YOffset: Y offset
    # ZOffset: Z offset
    pass
## Add a point between two points/vertices
def AddPoint(Name, PointOrVertex1, PointOrVertex2, Ratio):
    # Name: Name of point
    # PointOrVertex1: First point or vertex
    # PointOrVertex2: Second point or vertex
    # Ratio: Ratio of distance between points/vertices
    pass
## Add a point at the intersection or two axes or edges
def AddPoint(Name, AxisOrEdge1, AxisOrEdge2):
    # Name: Name of point
    # AxisOrEdge1: First axis or edge
    # AxisOrEdge2: Second axis or edge
    pass
## Add a point at the intersection of three planes or faces
def AddPoint(Name, PlaneOrFace1, PlaneOrFace2, PlaneOrFace3):
    # Name: Name of point
    # PlaneOrFace1: First plane or face
    # PlaneOrFace2: Second plane or face
    # PlaneOrFace3: Third plane or face
    pass
## Add a point at the the intersection of a axis or edge and a plane or face
def AddPoint(Name, AxisOrEdge, PlaneOrFace):
    # Name: Name of point
    # AxisOrEdge: Axis or edge
    # PlaneOrFace: Plane or face
    pass
## Add a point by projecting a point or vertex onto a plane or face
def AddPoint(Name, SourcePointOrVertex, TargetPlaneOrFace, XOffset, YOffset):
    # Name: Name of point
    # SourcePointOrVertex: Point or vertex to project
    # TargetPlaneOrFace: Plane or face to project onto
    # XOffset: X offset to apply to point once projected
    # YOffset: Y offset to apply to point once projected
    pass
## Add a point on an edge
def AddPoint(Name, TargetEdge, Ratio):
    # Name: Name of point
    # TargetEdge: The edge to create the point on
    # Ratio: Ratio along the edge from 0.0 -> 1.0
    pass
## Adds a point at the center of a circular edge
def AddPointFromCircularEdge(Name, TargetEdge):
    # Name: Name of point
    # TargetEdge: The edge to use for creating the point
    pass
## Adds a point at the center of a toroidal face
def AddPointFromToroidalFace(Name, TargetFace):
    # Name: Name of point
    # TargetFace: Toroidal face to use in creating the point
    pass
## Gets a plane using the name of the plane
def GetPlane(Name):
    # Name: Name of plane to find
    pass
## Gets an axis from an axis name
def GetAxis(Name):
    # Name: Name of axis to find
    pass
## Gets a point on the assembly using the point name. The point must have been created in a script
def GetPoint(Name):
    # Name: Name of point to get
    pass
## Gets a parameter with a specific name
def GetParameter(Name):
    # Name: Name of parameter
    pass
## Gets the value of a custonm property
def GetCustomProperty(Name):
    # Name: Name of the custom property
    pass
## Sets the value of a custom property The custom property must already be defined on the assembly or defined on the user's PC
def SetCustomProperty(Name, Value):
    # Name: Name of the custom property
    # Value: New value for the custom property
    pass
## Gets a configuration with a specific name
def GetConfiguration(Name):
    # Name: Name of confguration
    pass
## Gets the currently active configuration
def GetActiveConfiguration():
    pass
## Creates a plane based on the offset from an existing plane
def AddPlane(Name, SourcePlane, Offset):
    # Name: Name of plane
    # SourcePlane: Plane/face to use as basis
    # Offset: Offset from basis plane in currently chosen units
    pass
## Adds a plane using a normal vector and a point on the plane
def AddPlane(Name, NormalVector, PointonPlane):
    # Name: Name of plane to add
    # NormalVector: Normal vector as a list [nx, ny, nz]. Does not need to be a unit vector
    # PointonPlane: A point on the plane as a list [px, py, pz]
    pass
## Creates a new plane at an angle to an existing plane
def AddPlane(Name, SourcePlane, RotationAxis, Angle):
    # Name: Name of new plane
    # SourcePlane: Plane/face to use as basis for new plane
    # RotationAxis: Axis of rotation for new plane
    # Angle: Angle of new plane in degrees
    pass
## Adds a parameter to the assembly
def AddParameter(Name, Type, Value):
    # Name: Name of parameter
    # Type: Type of parameter
    # Value: Value for parameter
    pass
## NOTE: DOESN'T SEEM TO WORK IN GD V16 - THROWS EXCEPTION ABOUT TRANSACTION ALREADY BEING OPEN. Adds a parameter to the assembly
def AddParameter(Name, Type, Equation):
    # Name: Name of parameter
    # Type: Type of parameter
    # Equation: Equation for parameter
    pass
## Adds a configuration to the assembly
def AddConfiguration(Name):
    # Name: Name of configuration
    pass
## Adds a configuration to the assembly using another configuration as a base
def AddConfiguration(Name, BaseConfigurationName):
    # Name: Name of configuration
    # BaseConfigurationName: Name of base configuration to use
    pass
## Creates a plane using three points
def AddPlane(Name, Point1, Point2, Point3):
    # Name: Name of plane
    # Point1: Point on plane
    # Point2: Point on plane
    # Point3: Point on plane
    pass
## Creates an axis based on the intersection of two planes/faces
def AddAxis(Name, Plane1, Plane2):
    # Name: Name of axis
    # Plane1: First plane/face
    # Plane2: Second plane/face
    pass
## Creates an axis based on two points
def AddAxis(Name, Point1, Point2):
    # Name: Name of axis
    # Point1: First point
    # Point2: Second point
    pass
## Adds a point to the assembly
def AddPoint(Name, X, Y, Z):
    # Name: Name of new point
    # X: X coordinate
    # Y: Y coordinate
    # Z: Z coordinate
    pass
## Adds a set of points to the part
def AddPoints(Prefix, Points):
    # Prefix: Prefix for the point names
    # Points: List of points [x1,y1,z1, ..., xn,yn,zn]
    pass
## Regenerates the assembly
def Regenerate():
    pass
## Saves the assembly using the current path and file name
def Save():
    pass
## Saves the assembly to a specific folder
def Save(Folder):
    # Folder: Folder to save to
    pass
## Saves the assembly to a specific folder with a new name
def SaveAs(Folder, NewName):
    # Folder: Folder to save to
    # NewName: New name for assembly
    pass
## Save the assembly and all parts/sub-assemblies to a folder
def SaveAll(Folder):
    # Folder: Folder to save to
    pass
## Saves the current view as a bitmap image
def SaveSnapshot(FileName, Width, Height, UseAspectRatio, UseWidthandHeight):
    # FileName: Path and mame of file to save to
    # Width: Width in pixels
    # Height: Height in pixels
    # UseAspectRatio: if true uses greater of width/height along with current aspect ratio
    # UseWidthandHeight: if true uses current width/height of view
    pass
## Closes the assembly If it is unsaved then changes will be lost
def Close():
    pass
## Saves a thumbnail image of the assembly
def SaveThumbnail(FileName, Width, Height):
    # FileName: Path and name of file to save to
    # Width: Width of thumbnail in pixels
    # Height: Height of thumbnail in pixels
    pass
## Adds a part to the assembly at the origin
def AddPart(Folder, Name):
    # Folder: Folder containing part
    # Name: Name of part to open
    pass
## Adds a part to the assembly
def AddPart(Folder, Name, OffsetX, OffsetY, OffsetZ):
    # Folder: Folder containing part
    # Name: Name of part to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a part to the assembly
def AddPart(Folder, Name, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Folder: Folder containing part
    # Name: Name of part to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Adds a part to the assembly at the origin
def AddPart(Part):
    # Part: Part to add
    pass
## Adds a part to the assembly
def AddPart(Part, OffsetX, OffsetY, OffsetZ):
    # Part: Part to add
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a part to the assembly at the origin
def AddPart(FileName):
    # FileName: Path and name of part to open
    pass
## Adds a part to the assembly
def AddPart(FileName, OffsetX, OffsetY, OffsetZ):
    # FileName: Path and name of part to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a part to the assembly
def AddPart(FileName, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # FileName: Path and name of part to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Gets the orientation of a part in an assembly
def GetPartOrientation(Part):
    # Part: Part in an assembly
    pass
## Gets the orientation of a part in an assembly
def GetPartOrientation(PartName):
    # PartName: Name of part to get orientation
    pass
## Gets the display units for the assembly
def DisplayUnits():
    pass
## Adds a part to the assembly
def AddPart(Part, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Part: Part to add
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Adds a new part to the assembly
def AddNewPart(Name, X, Y, Z):
    # Name: Name of the new part
    # X: X location of part
    # Y: Y location of part
    # Z: Z location of part
    pass
## Gets a part in the assembly
def GetPart(Name):
    # Name: Name of part instance to get
    pass
## Gets a sub-assembly in the assembly
def GetSubAssembly(Name):
    # Name: Name of sub-assembly instance to get
    pass
## Duplicates a part in the assembly
def DuplicatePart(Name, OffsetX, OffsetY, OffsetZ):
    # Name: Name of part to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Duplicates a part in the assembly
def DuplicatePart(Part, OffsetX, OffsetY, OffsetZ):
    # Part: Part to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Duplicates a part in the assembly
def DuplicatePart(Name, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Name: Name of part to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Duplicates a part in the assembly
def DuplicatePart(Part, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Part: Part to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Duplicates a sub-assembly in the assembly
def DuplicateSubAssembly(SubAssembly, OffsetX, OffsetY, OffsetZ):
    # SubAssembly: Sub-assembly to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Duplicates a sub-assembly in the assembly
def DuplicateSubAssembly(Name, OffsetX, OffsetY, OffsetZ):
    # Name: Name of sub-assembly to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Duplicates a sub-assembly in the assembly
def DuplicateSubAssembly(SubAssembly, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # SubAssembly: Sub-assembly to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Duplicates a sub-assembly in the assembly
def DuplicateSubAssembly(Name, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Name: Name of sub-assembly to duplicate
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Anchors a part
def AnchorPart(Name):
    # Name: Name of part to anchor
    pass
## Anchors a part
def AnchorPart(Part):
    # Part: Part to anchor
    pass
## Anchors a sub-assembly
def AnchorSubAssembly(Name):
    # Name: Name of sub-assembly to anchor
    pass
## Un-anchors a part
def UnanchorPart(Name):
    # Name: Name of part to un-anchor
    pass
## Un-anchors a part
def UnanchorPart(Part):
    # Part: Part to un-anchor
    pass
## Un-anchors a sub-assembly
def UnanchorSubAssembly(Name):
    # Name: Name of sub-assembly to un-anchor
    pass
## Hides a part
def HidePart(Name):
    # Name: Name of part to hide
    pass
## Hides a part
def HidePart(Part):
    # Part: Part to hide
    pass
## Hides a sub-assembly
def HideSubAssembly(Name):
    # Name: Name of sub-assembly to hide
    pass
## Shows a part
def ShowPart(Name):
    # Name: Name of part to show
    pass
## Shows a part
def ShowPart(Part):
    # Part: Part to show
    pass
## Shows a sub-assembly
def ShowSubAssembly(Name):
    # Name: Name of sub-assembly to show
    pass
## Suppresses a part
def SuppressPart(Name):
    # Name: Name of part to suppress
    pass
## Suppresses a part
def SuppressPart(Part):
    # Part: Part to suppress
    pass
## Suppresses a sub-assembly
def SuppressSubAssembly(Name):
    # Name: Name of sub-assembly to suppress
    pass
## Un-suppresses a part
def UnsuppressPart(Name):
    # Name: Name of part to un-suppress
    pass
## Un-suppresses a part
def UnsuppressPart(Part):
    # Part: Part to un-suppress
    pass
## Un-suppresses a sub-assembly
def UnsuppressSubAssembly(Name):
    # Name: Name of sub-assembly to un-suppress
    pass
## Moves a part
def MovePart(Name, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # Name: Name of part to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Moves a part
def MovePart(Part, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # Part: Part to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Moves a sub-assembly
def MoveSubAssembly(Name, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # Name: Name of sub-assembly to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Moves a sub-assembly
def MoveSubAssembly(SubAssembly, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # SubAssembly: Sub-assembly to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Moves a set of parts
def MoveParts(Names, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # Names: Names of parts to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Moves a set of sub-assemblies
def MoveSubAssemblies(Names, OffsetX, OffsetY, OffsetZ, ApplyConstraints):
    # Names: Names of sub-assemblies to move
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a part
def RotatePart(Name, AngleX, AngleY, AngleZ, ApplyConstraints):
    # Name: Name of part to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a part
def RotatePart(Part, AngleX, AngleY, AngleZ, ApplyConstraints):
    # Part: Part to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a sub-assembly
def RotateSubAssembly(Name, AngleX, AngleY, AngleZ, ApplyConstraints):
    # Name: Name of sub-assembly to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a sub-assembly
def RotateSubAssembly(SubAssembly, AngleX, AngleY, AngleZ, ApplyConstraints):
    # SubAssembly: Sub-assembly to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a sub-assembly
def RotateSubAssembly(AssemOcc, AngleX, AngleY, AngleZ, ApplyConstraints):
    # AssemOcc: Occurence of sub-assembly to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a set of parts
def RotateParts(Names, AngleX, AngleY, AngleZ, ApplyConstraints):
    # Names: Names of parts to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Rotates a set of sub-assemblies
def RotateSubAssemblies(Names, AngleX, AngleY, AngleZ, ApplyConstraints):
    # Names: Names of sub-assemblies to rotate
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # ApplyConstraints: true to apply constraints
    pass
## Adds a new sub-assembly to the assembly
def AddNewSubAssembly(Name, X, Y, Z):
    # Name: Name of the new assembly
    # X: X location of assembly
    # Y: Y location of assembly
    # Z: Z location of assembly
    pass
## Adds a sub-assembly to the assembly at the origin
def AddSubAssembly(Assembly):
    # Assembly: Assembly to add
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(Assembly, OffsetX, OffsetY, OffsetZ):
    # Assembly: Assembly to add
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(Assembly, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Assembly: Sub-assembly to add
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Adds a sub-assembly to the assembly at the origin
def AddSubAssembly(Folder, Name):
    # Folder: Folder containing sub-assembly
    # Name: Name of sub-assembly to open
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(Folder, Name, OffsetX, OffsetY, OffsetZ):
    # Folder: Folder containing sub-assembly
    # Name: Name of sub-assembly to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    pass
## Adds a sub-assembly to the assembly
def AddSubAssembly(Folder, Name, OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ, TranslationFirst):
    # Folder: Folder containing sub-assembly
    # Name: Name of sub-assembly to open
    # OffsetX: X offset
    # OffsetY: Y offset
    # OffsetZ: Z offset
    # AngleX: X rotation angle in degrees
    # AngleY: Y rotation angle in degrees
    # AngleZ: Z rotation angle in degrees
    # TranslationFirst: if true translation occurs before rotation, if false rotation occurs before translation
    pass
## Adds a sub-assembly to the assembly at the origin
def AddSubAssembly(FileName):
    # FileName: Path and name of sub-assembly to open
    pass
## Name of the subassembly
def Name():
    pass
## A list of configurations defined on the assembly
def Configurations():
    pass
## A list of parameters defined on the assembly
def Parameters():
    pass
## A list of parts defined on the assembly
def Parts():
    pass
## A list of subassemblies defined on the assembly
def SubAssemblies():
    pass
## Path and filename of the assembly
def FileName():
    pass
## Gets the XY-plane (language independent)
def XYPlane():
    pass
## Gets the YZ-plane (language independent)
def YZPlane():
    pass
## Gets the ZX-plane (language independent)
def ZXPlane():
    pass
## Gets the X-axis (language independent)
def XAxis():
    pass
## Gets the Y-axis (language independent)
def YAxis():
    pass
## Gets the Z-axis (language independent)
def ZAxis():
    pass
## Gets the origin (language independent)
def Origin():
    pass
## Gets the currently selected items as [ItemA, ItemB, ...] Supports subassemblies, parts, faces, edges, vertices, planes, axes and points
def Selections():
    pass
## Comment property
def Comment():
    pass
## Cost center property
def CostCenter():
    pass
## Created By property
def CreatedBy():
    pass
## Created Date property
def CreatedDate():
    pass
## Creating Application property
def CreatingApplication():
    pass
## Document Number property
def DocumentNumber():
    pass
## Engineering Approval Date property
def EngineeringApprovalDate():
    pass
## Engineering Approved By property
def EngineeringApprovedBy():
    pass
## Estimated Cost property
def EstimatedCost():
    pass
## Keywords property
def Keywords():
    pass
## Last Author property
def LastAuthor():
    pass
## Last Update Date property
def LastUpdateDate():
    pass
## Material (extended information) property
def ExtendedMaterialInformation():
    pass
## Manufacturing Approved By property
def ManufacturingApprovedBy():
    pass
## Product property
def ManufacturingApprovedDate():
    pass
## Modified Information property
def ModifiedInformation():
    pass
## Product property
def Product():
    pass
## Received From property
def ReceivedFrom():
    pass
## Revision property
def Revision():
    pass
## Stock Size property
def StockSize():
    pass
## Supplier property
def Supplier():
    pass
## Title property
def Title():
    pass
## Vendor property
def Vendor():
    pass
## Web Link property
def WebLink():
    pass
## Density of the part
def Density():
    pass
## Material of the part
def Material():
    pass
## Description of the part
def Description():
    pass
## User-defined number for the part
def Number():
    pass
## Gets the part that the axis is defined on
def GetPart():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Hides the axis
def Hide():
    pass
## Shows the axis
def Show():
    pass
## The name of the axis
def Name():
    pass
## Gets the X value of the spline at a location along the spline
def GetX(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets the Y value of the spline at a location along the spline
def GetY(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets the Z value of the spline at a location along the spline
def GetZ(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets a point on the spline
def GetPointAt(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets the normal vector at a point on the spline
def GetNormalAt(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Divides the Bspline up into segments
def Subdivide(Segments):
    # Segments: Number of segments to obtain
    pass
## Divides the Bspline up into segments and gets the normal for each point
def SubdivideGetNormals(Segments):
    # Segments: Number of segments to obtain
    pass
## Creates a bspline
def #ctor(Order, ControlPoints, KnotVectors, Weights, IsReference):
    # Order: Order of the bspline
    # ControlPoints: Value of control points [Point1X, Point1Y, ...]
    # KnotVectors: Knot vectors [KnotVector1, KnotVector2, ...]
    # Weights: Point weights [Weight1, Weight2, ...]
    # IsReference: True if a reference bspline, false if a regular bspline
    pass
## The control points [x1, y1, ..., xn, yn]
def ControlPoints():
    pass
## The weights [w1, w2, ..., wn]
def Weights():
    pass
## The knot vectors [k1, k2, ..., kn]
def KnotVectors():
    pass
## True if the bspline is a reference bspline, false if it is a regular bspline
def IsReference():
    pass
## The order of the bspline
def Order():
    pass
## Gets the length of the Bspline
def Length():
    pass
## Gets the X value of the spline at a location along the spline
def GetX(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets the Y value of the spline at a location along the spline
def GetY(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets a point on the spline
def GetPointAt(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Gets the normal vector at a point on the spline
def GetNormalAt(u):
    # u: Location along the spline. 0.0 = start, 1.0 = end
    pass
## Divides the Bspline up into segments
def Subdivide(Segments):
    # Segments: Number of segments to obtain
    pass
## Creates a bspline
def #ctor(Order, ControlPoints, KnotVectors, Weights, IsReference):
    # Order: Order of the bspline
    # ControlPoints: Value of control points [Point1X, Point1Y, ...]
    # KnotVectors: Knot vectors [KnotVector1, KnotVector2, ...]
    # Weights: Point weights [Weight1, Weight2, ...]
    # IsReference: True if a reference bspline, false if a regular bspline
    pass
## The control points [x1, y1, ..., xn, yn]
def ControlPoints():
    pass
## The weights [w1, w2, ..., wn]
def Weights():
    pass
## The knot vectors [k1, k2, ..., kn]
def KnotVectors():
    pass
## True if the bspline is a reference bspline, false if it is a regular bspline
def IsReference():
    pass
## The order of the bspline
def Order():
    pass
## Gets the length of the Bspline
def Length():
    pass
## Creates a 2D circle which can be added to sketches
def #ctor(Center, Radius, IsReference):
    # Center: Center of the circle as a python list [x, y]
    # Radius: Radius of circle
    # IsReference: True to create a reference circle
    pass
## The center of the circle as a sketch point
def CenterPoint():
    pass
## The center of the circle [x, y]
def Center():
    pass
## Radius of the circle
def Radius():
    pass
## True if the circle is a reference circle, false if it is a regular circle
def IsReference():
    pass
## The length of the circle circumference in script units
def Length():
    pass
## Creates an arc using the center, start point and end point
def #ctor(Center, Start, End, IsReference):
    # Center: Center of the arc
    # Start: Start point of the arc
    # End: End point of the arc
    # IsReference: True to create a reference arc, false to create a regular arc
    pass
## Creates an arc using the center, start point and an angle
def #ctor(Center, Start, Angle, IsReference):
    # Center: Location of center of arc
    # Start: Location of start of arc
    # Angle: Angle of arc
    # IsReference: True if a reference arc, false if a regular arc
    pass
## The center of the arc [x, y, z]
def Center():
    pass
## The start point of the arc [x, y, z]
def StartPoint():
    pass
## The end point of the arc [x, y, z]
def EndPoint():
    pass
## Radius of arc
def Radius():
    pass
## Angle of arc
def Angle():
    pass
## Type of arc
def Type():
    pass
## True if the arc is a reference arc, false if it is a regular arc
def IsReference():
    pass
## Types of circular arcs
def ArcType():
    pass
## Creates an arc using the center, start point and end point
def #ctor(Center, Start, End, IsReference):
    # Center: Center of the arc
    # Start: Start point of the arc
    # End: End point of the arc
    # IsReference: True to create a reference arc, false to create a regular arc
    pass
## Creates an arc using the center, start point and an angle
def #ctor(Center, Start, Angle, IsReference):
    # Center: Location of center of arc
    # Start: Location of start of arc
    # Angle: Angle of arc
    # IsReference: True if a reference arc, false if a regular arc
    pass
## The center of the arc [x, y]
def Center():
    pass
## The start point of the arc [x, y]
def StartPoint():
    pass
## The end point of the arc [x, y]
def EndPoint():
    pass
## The start point as a sketchpoint object
def Start():
    pass
## The end point as a sketchpoint object
def End():
    pass
## The center point as a sketchpoint object
def CenterPoint():
    pass
## Radius of arc
def Radius():
    pass
## Angle of arc
def Angle():
    pass
## Type of arc
def Type():
    pass
## True if the arc is a reference arc, false if it is a regular arc
def IsReference():
    pass
## Types of circular arcs
def ArcType():
    pass
## Compiles and runs C# code
def CompileAndRun(Code):
    # Code: Code to compile and run
    pass
## Compiles and runs C# code
def CompileAndRun(Code, Variables):
    # Code: Code to compile and run
    # Variables: Dictionary of variables
    pass
## Compiles C# code
def Compile(Code):
    # Code: Code to compile
    pass
## Runs compiled C# code
def Run(Script):
    # Script: Compiled code object to run
    pass
## Runs compiled C# code
def Run(Script, Variables):
    # Script: Compiled code object to run
    # Variables: Dictionary of variables or None for no variables
    pass
## Creates an ellipse
def #ctor(Center, MajorRadius, MajorAxisAngle, MinorMajorRatio, IsReference):
    # Center: Center of the ellipse
    # MajorRadius: Radius on the major axis
    # MajorAxisAngle: Angle of the major axis in degrees
    # MinorMajorRatio: Radius on the minor axis as a ratio of the major radius
    # IsReference: True to create a reference arc, false to create a regular arc
    pass
## The center of the ellipse [x, y]
def Center():
    pass
## The center point as a sketchpoint object
def CenterPoint():
    pass
## Radius on major axis
def Radius():
    pass
## Angle of major axis
def MajorAxisAngle():
    pass
## Ratio of minor radius to major radius
def MinorMajorRatio():
    pass
## True if the ellipse is a reference ellipse, false if it is a regular ellipse
def IsReference():
    pass
## Creates an elliptical arc
def #ctor(Center, Start, End, MajorRadius, MajorAxisAngle, MinorMajorRatio, IsReference):
    # Center: Center of the elliptical arc
    # Start: The start point for the arc
    # End: The end point for the arc
    # MajorRadius: Radius on the major axis
    # MajorAxisAngle: Angle of the major axis in degrees
    # MinorMajorRatio: Radius on the minor axis as a ratio of the major radius
    # IsReference: True to create a reference arc, false to create a regular arc
    pass
## The center of the elliptical arc [x, y]
def Center():
    pass
## The start point of the arc [x, y]
def StartPoint():
    pass
## The end point of the arc [x, y]
def EndPoint():
    pass
## The center point as a sketchpoint object
def CenterPoint():
    pass
## The start point as a sketchpoint object
def Start():
    pass
## The end point as a sketchpoint object
def End():
    pass
## Radius on major axis
def Radius():
    pass
## Angle of major axis
def MajorAxisAngle():
    pass
## Ratio of minor radius to major radius
def MinorMajorRatio():
    pass
## True if the elliptical arc is a reference elliptical arc, false if it is a regular elliptical arc
def IsReference():
    pass
## Gets a parameter with a specific name
def GetParameter(Name):
    # Name: Name of parameter
    pass
## Gets a configuration with a specific name
def GetConfiguration(Name):
    # Name: Name of confguration
    pass
## Gets the currently active configuration
def GetActiveConfiguration():
    pass
## Adds a parameter to the global parameters set
def AddParameter(Name, Type, Value):
    # Name: Name of parameter
    # Type: Type of parameter
    # Value: Value for parameter
    pass
## Adds a parameter to the global parameters set
def AddParameter(Name, Type, Equation):
    # Name: Name of parameter
    # Type: Type of parameter
    # Equation: Equation for parameter
    pass
## Adds a configuration to the global parameters set
def AddConfiguration(Name):
    # Name: Name of configuration
    pass
## Adds a configuration to the global parameters set using another configuration as a base
def AddConfiguration(Name, BaseConfigurationName):
    # Name: Name of configuration
    # BaseConfigurationName: Name of base configuration to use
    pass
## Saves the global parameters set using the current path and file name
def Save():
    pass
## Saves the global parameters set to a specific folder
def Save(Folder):
    # Folder: Folder to save to
    pass
## Saves the global parameters set to a specific folder with a new name
def SaveAs(Folder, NewName):
    # Folder: Folder to save to
    # NewName: New name for global parameters set
    pass
## Closes the global parameters set If it is unsaved then changes will be lost
def Close():
    pass
## Opens an existing global parameters set
def #ctor(Folder, Name):
    # Folder: Folder containing global parameters
    # Name: Name of global parameters to open
    pass
## Creates a new global parameters set
def #ctor(Name):
    # Name: Name of new global parameters set
    pass
## Creates a new global parameters set or accesses an already opened global parameters set
def #ctor(Name, CreateNew):
    # Name: Name of global parameters set to create or access
    # CreateNew: True to create a new global parameters set, false to access an opened global parameters
    pass
## Name of the global parameters
def Name():
    pass
## A list of parameters
def Parameters():
    pass
## A list of configurations
def Configurations():
    pass
## Gets the part occurrence for this instance
def GetOccurrence():
    pass
## Gets the part occurrence for this instance
def GetOccurrence():
    pass
## Low level object that represents the point
def PointObject():
    pass
## Gets the part occurrence for this instance
def GetOccurrence():
    pass
## Creates a new 3D line
def #ctor(StartPoint, EndPoint, IsReference):
    # StartPoint: Location of the start point [x, y, z]
    # EndPoint: Location of the end point [x, y, z]
    # IsReference: True if a reference line
    pass
## The start point of the line [x, y, z]
def StartPoint():
    pass
## The end point of the line [x, y, z]
def EndPoint():
    pass
## True if the line is a reference line, false if it is a regular line
def IsReference():
    pass
## The length of the line in script units
def Length():
    pass
## The start point as a sketchpoint object
def Start():
    pass
## The end point as a sketchpoint object
def End():
    pass
## Adds a new point to the polyline
def AddPoint(Point):
    # Point: Point to add
    pass
## Inserts a point at a specific location
def InsertPoint(Index, Point):
    # Index: 0-based index of location to insert
    # Point: Point to insert
    pass
## Appends a line to the current line
def AddPolyline(AppendLine):
    # AppendLine: Line to append
    pass
## Determines if a point is on a line segment
def IsPointOnLine(A, B, P, Tolerance):
    # A: First point of line segment
    # B: Last point of line segment
    # P: Point to check
    # Tolerance: Fudge factor
    pass
## Splits a polyline at a point, creating two polylines
def SplitAtPoint(SplitPoint, Tolerence):
    # SplitPoint: Point to split at
    # Tolerence: Tolerance to determine if point is on/near line
    pass
## Creates an exact copy of the line
def Clone():
    pass
## Creates an exact copy of a section of the line
def Clone(StartIndex, EndIndex):
    # StartIndex: 0-based index of first point to include in copy
    # EndIndex: 0-based index of last point to include in copy
    pass
## Joins a line onto the end of the current line and returns the new line
def Join(AppendLine):
    # AppendLine: The line to join to the current line
    pass
## Applies an offset to all points on the line
def Offset(OffsetX, OffsetY, OffsetZ):
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    # OffsetZ: Z offset to apply
    pass
## Removes duplicate points that are next to each other
def RemoveDuplicates():
    pass
## Creates a new 3D polyline that can be later added to a 3D sketch
def #ctor():
    pass
## Creates a new 3D polyline that can be later added to a 3D sketch
def #ctor(Points):
    # Points: List of points in the polyline [X1, Y1, Z1, X2, Y2, Z2, ...]
    pass
## Applies an offset to the point and creates a new point
def Offset(X, Y, Z):
    # X: X offset to apply
    # Y: Y offset to apply
    # Z: Z offset to apply
    pass
## Scales the point location based on an origin for the scaling
def Scale(ScaleOriginX, ScaleOriginY, ScaleOriginZ, ScaleFactor):
    # ScaleOriginX: X-coordinate for scaling origin
    # ScaleOriginY: Y-coordinate for scaling origin
    # ScaleOriginZ: Z-coordinate for scaling origin
    # ScaleFactor: Factor for scaling as a percentage
    pass
## Creates a new polyline point
def #ctor():
    pass
## Creates a new 3D polyline point
def #ctor(X, Y, Z):
    # X: X coordinate
    # Y: Y coordinate
    # Z: Z coordinate
    pass
## X coordinate
def X():
    pass
## Y coordinate
def Y():
    pass
## Z coordinate
def Z():
    pass
## Rotates a point
def RotatePoint(Point, Angle):
    # Point: Point to rotate as [X, Y]
    # Angle: Angle to rotate in degrees
    pass
## Gets a vector that is perpendicular to a vector
def GetPerpendicularVector(Vector):
    # Vector: Vector [X, Y]
    pass
## Normalizes a vector
def NormalizeVector(Vector):
    # Vector: Vector [X, Y]
    pass
## Type of Windows input
def WindowsInputTypes():
    pass
## Close all currently open forms for a specific session
def CloseForm(SessionIdentifier):
    # SessionIdentifier: Identifier for session
    pass
## Gets the currently displayed form for a specific session
def GetDisplayedForm(SessionIdentifier):
    # SessionIdentifier: Identifier of session
    pass
## Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script
def UtilityDialog(Title, ActionButtonText, ActionButtonCallback, InputChangedCallback, Inputs, InputAreaWidth):
    # Title: Title of dialog window
    # ActionButtonText: Text for action button
    # ActionButtonCallback: Function called when the action button is clicked
    # InputChangedCallback: Function called when an input is changed
    # Inputs: List of input definitions [[Name, Type, DefaultValue, OptionalSettings], [...]]
    # InputAreaWidth: Width of dialog input area, optional
    pass
## Shows a dialog prompting the user to enter values The dialog remains open until the user clicks on the close button A callback function is called to give the input values to the script
def UtilityDialog(Title, ActionButtonText, ActionButtonCallback, InputChangedCallback, Inputs, InputAreaWidth, UpdateUserInterfaceCallback):
    # Title: Title of dialog window
    # ActionButtonText: Text for action button
    # ActionButtonCallback: Function called when the action button is clicked
    # InputChangedCallback: Function called when an input is changed
    # Inputs: List of input definitions [[Name, Type, DefaultValue, OptionalSettings], [...]] Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
    # InputAreaWidth: Width of dialog input area
    # UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog
    pass
## Shows a dialog prompting the user to enter values
def OptionsDialog(Title, Inputs, InputAreaWidth):
    # Title: Title of dialog window
    # Inputs: List of input definitions [[Name, Type, DefaultValue], [...]]
    # InputAreaWidth: Width of input area, optional
    pass
## Shows a dialog prompting the user to enter values
def OptionsDialog(Title, Inputs, InputAreaWidth, InputChangedCallback, UpdateUserInterfaceCallback):
    # Title: Title of dialog window
    # Inputs: List of input definitions [[Name, Type, DefaultValue, OptionalSettings], [...]] Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
    # InputAreaWidth: Width of input area
    # InputChangedCallback: Function called when an input is changed
    # UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog
    pass
## Disables an input
def DisableInput(Index):
    # Index: Index of the input
    pass
## Enables an input
def EnableInput(Index):
    # Index: Index of the input
    pass
## Gets the current value of an input
def GetInputValue(Index):
    # Index: Index of the input
    pass
## Updates the list of strings for a stringlist input
def SetStringList(Index, Strings):
    # Index: Index of the stringlist input
    # Strings: New list of strings to show
    pass
## Sets the current value for an input
def SetInputValue(Index, Value):
    # Index: Index of the input
    # Value: Value to show
    pass
## Prompts user to select a file
def OpenFileDialog(Title, Filter, DefaultExtension):
    # Title: Title of dialog window
    # Filter: File filter, example filter: 'Part Files|*.AD_PRT'
    # DefaultExtension: Default file extension, e.g. '.AD_PRT'
    pass
## Prompts user to save a file
def SaveFileDialog(Title, Filter, DefaultExtension):
    # Title: Title of dialog window
    # Filter: File filter, example filter: 'Part Files|*.AD_PRT'
    # DefaultExtension: Default file extension, e.g. '.AD_PRT'
    pass
## Prompts the user to select a folder
def SelectFolderDialog(CurrentFolder, Description):
    # CurrentFolder: The current folder, if any
    # Description: Description of what is being chosen, shown to user
    pass
## Shows an information window
def InfoDialog(Message, Title):
    # Message: Message to show
    # Title: Title of window
    pass
## Shows an error window
def ErrorDialog(Message, Title):
    # Message: Error message
    # Title: Title of window
    pass
## Shows a question window
def QuestionDialog(Question, Title):
    # Question: Question to show
    # Title: Title of window
    pass
## Creates a new Windows object allowing user interfaces to be constructed
def #ctor():
    pass
## Type of configuration lock
def LockTypes():
    pass
## Sets the locks on the configuration
def SetLocks(Locks):
    # Locks: Locks to set
    pass
## Applies all locks to the configuration
def LockAll():
    pass
## Removes all locks from the configuration
def UnlockAll():
    pass
## Makes the configuration active
def Activate():
    pass
## The name of the configuration
def Name():
    pass
## True if the configuration is currently active
def IsActive():
    pass
## Opens an existing assembly
def #ctor(Folder, Name):
    # Folder: Folder containing assembly
    # Name: Name of assembly to open
    pass
## Opens an existing assembly, optionally hiding the editor
def #ctor(Folder, Name, HideEditor):
    # Folder: Folder containing assembly
    # Name: Name of assembly to open
    # HideEditor: True to hide the editor
    pass
## Creates a new assembly
def #ctor(Name):
    # Name: Name of new assembly
    pass
## Creates a new assembly or accesses an already opened assembly
def #ctor(Name, CreateNew):
    # Name: Name of assembly to create or access
    # CreateNew: True to create a new assembly, false to access an opened assembly
    pass
## Creates a new assembly or accesses an already opened assembly, optionally hiding the editor
def #ctor(Name, CreateNew, HideEditor):
    # Name: Name of assembly to create or access
    # CreateNew: True to create a new assembly, false to access an opened assembly
    # HideEditor: True to hide the editor (only valid if assembly is not already open)
    pass
## Name of the assembly
def Name():
    pass
## A list of configurations defined on the assembly
def Configurations():
    pass
## Assembly constraint bounds types
def ConstraintBoundsType():
    pass
## Gets the part that the edge is defined on
def GetPart():
    pass
## Gets a python list of the current vertices in the edge
def GetVertices():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Name of the edge
def Name():
    pass
## The diameter of the edge, if it is a circle
def Diameter():
    pass
## The length of the edge
def Length():
    pass
## Gets the part that the face is defined on
def GetPart():
    pass
## Determines if the face is a rectangle
def IsRectangle():
    pass
## Gets a list of the current edges in the face
def GetEdges():
    pass
## Gets a list of the adjoining faces
def GetAdjoiningFaces():
    pass
## Gets a list of the current vertices in the face
def GetVertices():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Checks if another face is parallel to this one
def IsParallel(OtherFace):
    # OtherFace: The other face to check
    pass
## Gets the distance from this face to another face
def DistanceTo(OtherFace):
    # OtherFace: The other face to measure to
    pass
## Gets the area of the face
def GetArea():
    pass
## The name of the face
def Name():
    pass
## Sets the color of the part
def SetColor(Red, Green, Blue):
    # Red: Red component 0 - 255
    # Green: Green component 0 - 255
    # Blue: Blue component 0 - 255
    pass
## Name of the feature
def Name():
    pass
## Part that the sketch is defined on
def GetPart():
    pass
## Gets the surface that the sketch was created on, e.g. a design plane or a face
def GetSurface():
    pass
## Adds a constraint to the sketch
def AddConstraint(Figure, Constraint):
    # Figure: Figure to constrain (e.g. Line)
    # Constraint: Constraint to apply
    pass
## Adds a constraint to the sketch
def AddConstraint(Figures, Constraint):
    # Figures: List of Sketch figures to constrain [Figure1, Figure2, ...] (Circle, Line, CircularArc, etc.)
    # Constraint: Constraint to apply
    pass
## Adds a line to the sketch
def AddLine(StartPoint, EndPoint, IsReference):
    # StartPoint: Start of line [X, Y]
    # EndPoint: End of line [X, Y]
    # IsReference: true if line is a reference line
    pass
## Adds a line to the sketch
def AddLine(NewLine):
    # NewLine: 2D line to add
    pass
## Adds a line to the sketch
def AddLine(X1, Y1, X2, Y2, IsReference):
    # X1: Start point X
    # Y1: Start point Y
    # X2: End point X
    # Y2: End point Y
    # IsReference: true to create a reference line
    pass
## Adds a point to the sketch
def AddPoint(X, Y):
    # X: Point X coordinate
    # Y: Point Y coordinate
    pass
## Adds a point to the sketch [DEPRECATED - DO NOT USE]
def AddPoint(X, Y, IsReference):
    # X: Point X coordinate
    # Y: Point Y coordinate
    # IsReference: Set to false
    pass
## Adds a point to the sketch
def AddPoint(NewPoint):
    # NewPoint: Point to add
    pass
## Adds a polyline to the sketch
def AddLines(Points, IsReference):
    # Points: Set of points [Point1X, Point1Y, Point2X, Point2Y, ...]
    # IsReference: true if line is a reference line
    pass
## Adds a polyline to the sketch
def AddPolyline(Line, IsReference):
    # Line: Polyine to add
    # IsReference: true if line is a reference line
    pass
## Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end
def AddArcCenterStartEnd(CenterX, CenterY, StartX, StartY, EndX, EndY, IsReference):
    # CenterX: X coordinate for center
    # CenterY: Y coordinate for center
    # StartX: X coordinate for start
    # StartY: Y coordinate for start
    # EndX: X coordinate for end
    # EndY: Y cordinate for end
    # IsReference: True if arc is a reference figure
    pass
## Adds a circular arc using center, start and angle Arc goes anti-clockwise from start
def AddArcCenterStartAngle(CenterX, CenterY, StartX, StartY, Angle, IsReference):
    # CenterX: X coordinate for center
    # CenterY: Y coordinate for center
    # StartX: X coordinate for start
    # StartY: Y coordinate for start
    # Angle: Arc angle in degrees
    # IsReference: True if arc is a reference figure
    pass
## Adds an ellipse to the sketch using three points
def AddEllipse(CenterX, CenterY, MajorX, MajorY, MinorX, MinorY, IsReference):
    # CenterX: X coordinate of ellipse center
    # CenterY: Y coordinate of ellipse center
    # MajorX: X coordinate of ellipse on major axis
    # MajorY: Y coordinate of ellipse on major axis
    # MinorX: X coordinate of ellipse on minor axis
    # MinorY: Y coordinate of ellipse on minor axis
    # IsReference: True to create a reference ellipse
    pass
## Adds an ellipse to the sketch
def AddEllipse(CenterX, CenterY, MajorAxisDiameter, MinorMajorRatio, MajorAxisAngle, IsReference):
    # CenterX: X coordinate of ellipse center
    # CenterY: Y coordinate of ellipse center
    # MajorAxisDiameter: Diameter of ellipse on major axis
    # MinorMajorRatio: Ratio of minor diameter to major diameter
    # MajorAxisAngle: Angle of major axis
    # IsReference: True to create a reference ellipse
    pass
## Adds an ellipse to the sketch
def AddEllipse(NewEllipse):
    # NewEllipse: Ellipse to add
    pass
## Adds an elliptical arc to the sketch
def AddEllipticalArc(CenterX, CenterY, StartX, StartY, EndX, EndY, MajorAxisDiameter, MinorMajorRatio, MajorAxisAngle, IsReference):
    # CenterX: X coordinate of arc center
    # CenterY: Y coordinate of arc center
    # StartX: X coorindate of arc start
    # StartY: Y coordinate of arc start
    # EndX: X coordinate of arc end
    # EndY: Y coordinate of arc end
    # MajorAxisDiameter: Diameter of ellipse on major axis
    # MinorMajorRatio: Ratio of minor diameter to major diameter
    # MajorAxisAngle: Angle of major axis
    # IsReference: True to create a reference elliptical arc
    pass
## Adds an elliptical arc to the sketch
def AddEllipticalArc(NewEllipticalArc):
    # NewEllipticalArc: Elliptical arc to add
    pass
## Adds a circular arc to the sketch
def AddArc(NewArc):
    # NewArc: Arc to add
    pass
## Adds a rectangle to the sketch
def AddRectangle(BottomLeftX, BottomLeftY, TopRightX, TopRightY, IsReference):
    # BottomLeftX: X coordinate of bottom left corner
    # BottomLeftY: Y coordinate of bottom left corner
    # TopRightX: X coordinate of top right
    # TopRightY: Y coordinate of top right
    # IsReference: True to create a reference rectangle
    pass
## Adds a circle to the sketch
def AddCircle(CenterX, CenterY, Diameter, IsReference):
    # CenterX: X coordinate of circle center
    # CenterY: Y coordinate of circle center
    # Diameter: Circle diameter
    # IsReference: True to create a reference circle
    pass
## Adds a circle to the sketch
def AddCircle(NewCircle):
    # NewCircle: Circle to add to sketch
    pass
## Adds a Bspline to the sketch
def AddBspline(Order, ControlPoints, KnotVectors, Weights, IsReference):
    # Order: Order of the Bspline (Degree - 1)
    # ControlPoints: List of control points
    # KnotVectors: List of knot vectors
    # Weights: List of control point weights
    # IsReference: True to create a reference bspline
    pass
## Adds a Bspline to the sketch through a set of points
def AddBspline(Points, IsReference):
    # Points: List of points
    # IsReference: True to create a reference bspline
    pass
## Adds a figure to the sketch
def AddFigure(NewFigure):
    # NewFigure: Figure to add
    pass
## Adds a new bspline to the sketch
def AddBspline(NewBspline):
    # NewBspline: Bspline to add to the sketch
    pass
## Adds a regular polygon to the sketch
def AddPolygon(CenterX, CenterY, Diameter, Sides, IsReference):
    # CenterX: X coordinate for polygon center
    # CenterY: Y coordinate for polygon center
    # Diameter: Diameter of polygon
    # Sides: Number of sides
    # IsReference: True to create a reference polygon
    pass
## Adds a polyhole to the sketch Create a "circle" whose size should be accurate regardless of the 3D printing method See: http://hydraraptor.blogspot.co.uk/2011/02/polyholes.html
def AddPolyhole(CenterX, CenterY, Diameter, IsReference):
    # CenterX: X coordinate for hole center
    # CenterY: Y coordinate for hole center
    # Diameter: Diameter of hole
    # IsReference: true if line is a reference line
    pass
## Copies a sketch into this sketch
def CopyFrom(Source):
    # Source: Sketch to copy from
    pass
## Copies a sketch into this sketch
def CopyFrom(Source, Angle, RotationCenterX, RotationCenterY, TranslateX, TranslateY, ScaleOriginX, ScaleOriginY, ScaleFactor):
    # Source: Sketch to copy from
    # Angle: Rotation angle
    # RotationCenterX: X-coodinate for center of rotation
    # RotationCenterY: Y-coordinate for center of rotation
    # TranslateX: Amount to move sketch in X direction
    # TranslateY: Amount to move sketch in Y direction
    # ScaleOriginX: X-coordinate for scaling origin
    # ScaleOriginY: Y-coordinate for scaling origin
    # ScaleFactor: Factor for scaling as a percentage
    pass
## Converts a point on the sketch into a 3D point in the part coordinate system
def PointtoGlobal(x, y):
    # x: X coordinate of point on sketch
    # y: Y coordinate of point on sketch
    pass
## Projects a 3D point in the part coordinate system into a point on the sketch
def GlobaltoPoint(x, y, z):
    # x: X coordinate of 3D point
    # y: Y coordinate of 3D point
    # z: Z coordinate of 3D point
    pass
## The assembly that the sketch was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Adds a dimension to the sketch between two points
def AddDimension(P1, P2):
    # P1: First point
    # P2: Second point
    pass
## Adds a dimension to the radius of a circle
def AddDimension(Circle):
    # Circle: Circle to dimension
    pass
## Adds a dimension to the radius of an arc
def AddDimension(Arc):
    # Arc: Arc to dimension
    pass
## Saves the sketch to an XML file Does not support ellipses and elliptical arcs
def SavetoXml(FileName):
    # FileName: Path and name of file to save to
    pass
## Saves the sketch to an XML string Does not support ellipses and elliptical arcs
def ToXml():
    pass
## Loads the sketch from an XML file
def LoadXml(FileName):
    # FileName: Path and name of file to load from
    pass
## Adds elements to the sketch from XML
def FromXml(Xml):
    # Xml: XML to parse
    pass
## Starts mapping the face so that the specified edge is at [0, 0]
def StartFaceMapping(EdgeVertex1, EdgeVertex2):
    # EdgeVertex1: Firrt vertex of edge
    # EdgeVertex2: Second vertex of edge
    pass
## Starts mapping the face so that the specified edge is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values
def StartFaceMapping(EdgeEndPoint1, EdgeEndPoint2):
    # EdgeEndPoint1: First end point of edge [X, Y, Z]
    # EdgeEndPoint2: Second end point of edge [X, Y, Z]
    pass
## Stops mapping the face
def StopFaceMapping():
    pass
## Starts mapping the sketch so that the specified line is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values
def StartMapping(Point1, Point2, PointAboveAxis):
    # Point1: First line end point [X, Y, Z]
    # Point2: Second line end point [X, Y, Z]
    # PointAboveAxis: Point to be located above the X-axis
    pass
## Stops mapping the sketch
def StopMapping():
    pass
## Imports an SVG into the sketch
def ImportSVG(FileName):
    # FileName: Path and name of SVG file
    pass
## Imports an SVG into the sketch
def ImportSVG(FileName, TranslateX, TranslateY, RotationAngle, TranslateThenRotate, NativeFigures):
    # FileName: Path and name of SVG file
    # TranslateX: Amount to translate in the X direction
    # TranslateY: Amount to translate in the Y direction
    # RotationAngle: Amount to rotate in degrees
    # TranslateThenRotate: true to perform translation passed to this function before rotation passed to this function, false to reverse order
    # NativeFigures: true to create native circles and arcs when possible, false to always use Bezier curves
    pass
## Exports the sketch to an SVG
def ExportSVG(FileName):
    # FileName: Path and name of SVG file to export to
    pass
## Exports the sketch to an SVG
def ExportSVG(FileName, IncludeReferences):
    # FileName: Path and name of SVG file to export to
    # IncludeReferences: true to include reference figures in export
    pass
## Exports the sketch to an SVG with specific styling
def ExportSVG(FileName, IncludeReferences, StrokeWidth, StrokeColor, StrokeLineCap, StrokeDashed, StrokeDashLength, ReferenceStrokeWidth, ReferenceStrokeColor, ReferenceStrokeLineCap, ReferenceStrokeDashed, ReferenceStrokeDashLength):
    # FileName: Path and name of SVG file to export to
    # IncludeReferences: true to include reference figures in export
    # StrokeWidth: Stroke width
    # StrokeColor: String containing name of stroke color
    # StrokeLineCap: String containing name of stroke line cap type
    # StrokeDashed: true if stroke dashed, false if solid
    # StrokeDashLength: Length of stroke dashes if dashed
    # ReferenceStrokeWidth: Reference stroke width
    # ReferenceStrokeColor: String containing name of reference stroke color
    # ReferenceStrokeLineCap: String containing name of reference stroke line cap type, can be: butt, round, square
    # ReferenceStrokeDashed: true if reference stroke dashed, false if solid
    # ReferenceStrokeDashLength: Length of reference stroke dashes if dashed
    pass
## Name of the sketch
def Name():
    pass
## A list of figures (line, circle, circulararc, bspline, ellipse, elliptical arc) defined on the sketch
def Figures():
    pass
## The point that defines the origin
def Origin():
    pass
## Number of teeth in gear
def NumberofTeeth():
    pass
## Pitch diameter of gear in script units
def PitchDiameter():
    pass
## Pressure angle of gear
def PressureAngle():
    pass
## Diametral pitch of gear in teeth per inch
def DiametralPitch():
    pass
## X coordinate of gear center
def CenterX():
    pass
## Y coordinate of gear center
def CenterY():
    pass
## Creates a new 2D line
def #ctor(StartPoint, EndPoint, IsReference):
    # StartPoint: Location of the start point [x, y]
    # EndPoint: Location of the end point [x, y]
    # IsReference: True if a reference line
    pass
## The start point of the line [x, y]
def StartPoint():
    pass
## The end point of the line [x, y]
def EndPoint():
    pass
## True if the line is a reference line, false if it is a regular line
def IsReference():
    pass
## The length of the line in script units
def Length():
    pass
## The start point as a sketchpoint object
def Start():
    pass
## The end point as a sketchpoint object
def End():
    pass
## Density for ABS plastic in kg/cm3
def ABS():
    pass
## Density for PLA plastic in kg/cm3
def PLA():
    pass
## Type of parameter
def ParameterTypes():
    pass
## Units of parameters
def ParameterUnits():
    pass
## Attaches the parameter to a cell in an Ezcel spreadsheet
def AttachToExcel(Document, Sheet, Cell, Units):
    # Document: Path and name of Excel spreadsheet
    # Sheet: Name of sheet to use
    # Cell: Cell to use
    # Units: Units used in the cell
    pass
## Name of the parameter
def Name():
    pass
## Comment for the parameter
def Comment():
    pass
## Equation of the parameter
def Equation():
    pass
## Excel workbook associated with the parameter e.g. 'Foo.xlsx'
def ExcelWorkbook():
    pass
## Excel sheet associated with the parameter, e.g. 'Sheet1'
def ExcelSheet():
    pass
## Excel cell associated with the parameter, e.g. '$B$3'
def ExcelCell():
    pass
## Type of the parameter
def Type():
    pass
## Current units of the parameter
def Units():
    pass
## Current value of the parameter in script units (for mm, cm, in), or degrees for angles, or raw value for other units
def Value():
    pass
## Raw value of the parameter
def RawValue():
    pass
## Opens an existing part
def #ctor(Folder, Name):
    # Folder: Folder containing part
    # Name: Name of part to open
    pass
## Opens an existing part, optionally hiding the editor
def #ctor(Folder, Name, HideEditor):
    # Folder: Folder containing part
    # Name: Name of part to open
    # HideEditor: True to hide the editor (only valid if part is not already open)
    pass
## Creates a new part
def #ctor(Name):
    # Name: Name of new part
    pass
## Creates a new part or accesses an already opened part
def #ctor(Name, CreateNew):
    # Name: Name of part to create or access
    # CreateNew: True to create a new part, false to access an opened part
    pass
## Creates a new part or accesses an already opened part, optionally hiding the editor
def #ctor(Name, CreateNew, HideEditor):
    # Name: Name of part to create or access
    # CreateNew: True to create a new part, false to access an opened part
    # HideEditor: True to hide the editor (only valid if CreateNew is true)
    pass
## Opens or imports an existing file for editing
def #ctor(FileName, Type):
    # FileName: Name of file to open
    # Type: Type of file (GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
    pass
## Opens or imports an existing file for editing, optionally hiding the editor
def #ctor(FileName, Type, HideEditor):
    # FileName: Name of file to open
    # Type: Type of file (GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
    # HideEditor: True to hide the editor
    pass
## Name of the part
def Name():
    pass
## List of configurations defined on the part
def Configurations():
    pass
## Extrusion end conditions - extrude until...
def EndCondition():
    pass
## Extrusion directions - extrude along...
def DirectionType():
    pass
## Supported file types
def FileTypes():
    pass
## Gets the part that defined this plane
def GetPart():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Checks if another plane is parallel to this one
def IsParallel(OtherPlane):
    # OtherPlane: The other plane to check
    pass
## Hides the plane
def Hide():
    pass
## Shows the plane
def Show():
    pass
## The name of the plane
def Name():
    pass
## Gets the part that the point is defined in
def GetPart():
    pass
## Gets the coordiates of the point as a list [X, Y, Z]
def GetCoordinates():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Hides the point
def Hide():
    pass
## Shows the point
def Show():
    pass
## Name of the point
def Name():
    pass
## Point X coordinate
def X():
    pass
## Point Y coordinate
def Y():
    pass
## Point Z coordinate
def Z():
    pass
## Adds a new point to the polyline
def AddPoint(Point):
    # Point: Point to add
    pass
## Inserts a point at a specific location
def InsertPoint(Index, Point):
    # Index: 0-based index of location to insert
    # Point: Point to insert
    pass
## Adds a circle to the line
def AddCircle(CenterX, CenterY, Diameter, sides):
    # CenterX: X coordinate of circle center
    # CenterY: Y coordinate of circle center
    # Diameter: Diameter of circle
    # sides: Number of sides to use to approximate circle
    pass
## Adds an arc to the polyline. The arc is approcimated with straight line segments
def AddArc(Center, Start, End, MinimumSegments):
    # Center: Point defining center of arc
    # Start: Point defining start of arc
    # End: Point defining end of arc
    # MinimumSegments: Minimum number of line segments to use to form arc
    pass
## Appends a line to the current line
def AddPolyline(AppendLine):
    # AppendLine: Line to append
    pass
## Finds the first intersection point between two lines
def FindIntersection(L1, L2):
    # L1: First line
    # L2: Second line
    pass
## Finds first intersection of line with a circle
def FindIntersectionWithCircle(L1, CircleX, CircleY, Radius):
    # L1: Line to check
    # CircleX: X-coordinate of circle center
    # CircleY: Y-coordinate of circle center
    # Radius: Radius of circle
    pass
## Gets the intersection between the line segments A1A2 and B1B2
def FindIntersection(A1, A2, B1, B2):
    # A1: First segment start point
    # A2: First segment end point
    # B1: Second segment start point
    # B2: Second segment end point
    pass
## Determines if a point is on a line segment
def IsPointOnLine(A1, A2, Point, Tolerance):
    # A1: First point of line segment
    # A2: Last point of line segment
    # Point: Point to check
    # Tolerance: Fudge factor
    pass
## Splits a polyline at a point, creating two polylines
def SplitAtPoint(SplitPoint, Tolerence):
    # SplitPoint: Point to split at
    # Tolerence: Tolerance to determine if point is on/near line
    pass
## Creates an exact copy of the line
def Clone():
    pass
## Creates an exact copy of a section of the line
def Clone(StartIndex, EndIndex):
    # StartIndex: 0-based index of first point to include in copy
    # EndIndex: 0-based index of last point to include in copy
    pass
## Joins a line onto the end of the current line and returns the new line
def Join(AppendLine):
    # AppendLine: The line to join to the current line
    pass
## Rotates the polyline around the Z axis
def RotateZ(CenterX, CenterY, Angle):
    # CenterX: X coordinate of center of rotation
    # CenterY: Y coordinate of center of rotation
    # Angle: Number of degrees to rotate
    pass
## Applies an offset to all points on the line
def Offset(OffsetX, OffsetY):
    # OffsetX: X offset to apply
    # OffsetY: Y offset to apply
    pass
## Removes duplicate points that are next to each other
def RemoveDuplicates():
    pass
## Creates a new 2D polyline that can be later added to a 2D sketch
def #ctor():
    pass
## Creates a new 2D polyline that can be later added to a 2D sketch
def #ctor(Points):
    # Points: List of points in the polyline [X1, Y1, X2, Y2, ...]
    pass
## Applies an offset to the point and creates a new point
def Offset(X, Y):
    # X: X offset to apply
    # Y: Y offset to apply
    pass
## Scales the point location based on an origin for the scaling
def Scale(ScaleOriginX, ScaleOriginY, ScaleFactor):
    # ScaleOriginX: X-coordinate for scaling origin
    # ScaleOriginY: Y-coordinate for scaling origin
    # ScaleFactor: Factor for scaling as a percentage
    pass
## Rotates the point around the Z axis
def RotateZ(CenterX, CenterY, Angle):
    # CenterX: X coordinate of center of rotation
    # CenterY: Y coordinate of center of rotation
    # Angle: Number of degrees to rotate
    pass
## Creates a new polyline point
def #ctor():
    pass
## Creates a new polyline point
def #ctor(X, Y):
    # X: X coordinate
    # Y: Y coordinate
    pass
## X coordinate
def X():
    pass
## Y coordinate
def Y():
    pass
## Supported sketch constraints
def Constraints():
    pass
## Type of guide curve
def GuideCurveTypes():
    pass
## Part that the sketch is defined on
def GetPart():
    pass
## Adds a line to the sketch
def AddLine(StartPoint, EndPoint):
    # StartPoint: Start of line [X, Y, Z]
    # EndPoint: End of line [X, Y, Z]
    pass
## Adds a line to the sketch
def AddLine(NewLine):
    # NewLine: 3D line to add
    pass
## Adds a point to the sketch
def AddPoint(X, Y, Z):
    # X: Point X coordinate
    # Y: Point Y coordinate
    # Z: Point Z coordinate
    pass
## Adds a point to the sketch
def AddPoint(NewPoint):
    # NewPoint: Point to add
    pass
## Adds a line to the sketch
def AddLine(X1, Y1, Z1, X2, Y2, Z2):
    # X1: Start point X
    # Y1: Start point Y
    # Z1: Start point Z
    # X2: End point X
    # Y2: End point Y
    # Z2: End point Z
    pass
## Adds a polyline to the sketch
def AddLines(Points):
    # Points: Set of points [Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z, ...]
    pass
## Adds a polyline to the sketch
def AddPolyline(Line):
    # Line: Polyine to add
    pass
## Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end
def AddArcCenterStartEnd(CenterX, CenterY, CenterZ, StartX, StartY, StartZ, EndX, EndY, EndZ):
    # CenterX: X coordinate for center
    # CenterY: Y coordinate for center
    # CenterZ: Z coordinate for center
    # StartX: X coordinate for start
    # StartY: Y coordinate for start
    # StartZ: Z coordinate for start
    # EndX: X coordinate for end
    # EndY: Y cordinate for end
    # EndZ: Z coordnate for end
    pass
## Adds a circular arc to the sketch
def AddArc(NewArc):
    # NewArc: Arc to add
    pass
## Adds a Bspline to the sketch
def AddBspline(Points):
    # Points: List of control points [X1, Y1, Z1, X2, Y2, Z2, ...]
    pass
## Adds a Bspline to the sketch
def AddBspline(Bspline):
    # Bspline: Bspline to add
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Saves the sketch to an XML file
def SavetoXml(FileName):
    # FileName: Path and name of file to save to
    pass
## Saves the sketch to an XML string
def ToXml():
    pass
## Loads the sketch from an XML file
def LoadXml(FileName):
    # FileName: Path and name of file to load from
    pass
## Adds elements to the sketch from XML
def FromXml(Xml):
    # Xml: XML to parse
    pass
## Name of the sketch
def Name():
    pass
## A list of figures defines on the sketch, e.g. bspline
def Figures():
    pass
## Creates a new sketch point which can be added to sketches
def #ctor(X, Y, IsReference):
    # X: X coordinate of sketch point
    # Y: Y coordinate of sketch point
    # IsReference: true to create a reference point, false to create a regular point
    pass
## X-coordinate of point
def X():
    pass
## Y-coordinate of point
def Y():
    pass
## True if the point is a reference point, false if it is a regular point
def IsReference():
    pass
## Creates a new 3D sketch point which can be added to sketches
def #ctor(X, Y, Z, IsReference):
    # X: X coordinate of point
    # Y: Y coordinate of point
    # Z: Z coordinate of point
    # IsReference: true to create a reference point, false to create a regular point
    pass
## X-coordinate of point
def X():
    pass
## Y-coordinate of point
def Y():
    pass
## Z-coordinate of point
def Z():
    pass
## True if the point is a reference point, false if it is a regular point
def IsReference():
    pass
## Gets a vector that is perpendicular to a vector
def GetPerpendicularVector(Vector):
    # Vector: Vector [X, Y, Z]
    pass
## Transforms a point based on two vectors
def TransformPointUsingVectors(SourceVector, DestinationVector, Point):
    # SourceVector: Source vector [X, Y, Z]
    # DestinationVector: Destination vector [X, Y, Z]
    # Point: Point to transform [X, Y, Z]
    pass
## Supported units
def UnitTypes():
    pass
## The current units
def Current():
    pass
## Part that the vertex is defined on
def GetPart():
    pass
## The assembly that the edge was selected on Only valid when a selection has been made
def GetSelectionAssembly():
    pass
## Name of the vertex
def Name():
    pass
## X-coordinate of vertex
def X():
    pass
## Y-coordinate of vertex
def Y():
    pass
## Z-coordinate of vertex
def Z():
    pass
