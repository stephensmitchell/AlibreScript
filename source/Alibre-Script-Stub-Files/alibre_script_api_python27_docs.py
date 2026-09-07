class Part:
    """Generated stub class"""
    def RemovePoint(self, AlibreScript_API_Point):
        """Removes a point from the part"""
        pass
    def RemovePlane(self, AlibreScript_API_Plane):
        """Removes a plane from the part"""
        pass
    def RemoveSketch(self, System_String):
        """Removes a sketch from the part"""
        pass
    def RemoveSketch(self, AlibreScript_API_Sketch):
        """Removes a sketch from the part"""
        pass
    def Add3DSketch(self, System_String):
        """Creates a new 3D sketch"""
        pass
    def AddGear(self, System_String,System_Double,System_Int32,System_Double,System_Double,System_Boolean,System_Double,System_Double,System_Int32,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part"""
        pass
    def AddGearNP(self, System_String,System_Int32,System_Double,System_Double,System_Double,System_Double,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using number of teeth and pitch diameter"""
        pass
    def AddGearNP(self, System_String,System_Int32,System_Double,System_Double,System_Double,System_Double,System_Boolean,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using number of teeth and pitch diameter"""
        pass
    def AddGearDP(self, System_String,System_Double,System_Double,System_Double,System_Double,System_Double,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using diametral pitch and pitch diameter"""
        pass
    def AddGearDP(self, System_String,System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using diametral pitch and pitch diameter"""
        pass
    def AddGearDN(self, System_String,System_Double,System_Int32,System_Double,System_Double,System_Double,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using diametral pitch and number of teeth"""
        pass
    def AddGearDN(self, System_String,System_Double,System_Int32,System_Double,System_Double,System_Double,System_Boolean,AlibreScript_API_ISketchSurface):
        """Adds a gear sketch to the part using diametral pitch and number of teeth"""
        pass
    def AddAxis(self, System_String,AlibreScript_API_ISketchSurface,AlibreScript_API_ISketchSurface):
        """Creates an axis based on the intersection of two planes/faces"""
        pass
    def AddAxis(self, System_String,AlibreScript_API_Point,AlibreScript_API_Point):
        """Creates an axis based on two points"""
        pass
    def AddAxis(self, System_String,AlibreScript_API_Face):
        """Creates an axis for a cylindrical face"""
        pass
    def AddAxis(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List):
        """Creates an axis based on two points"""
        pass
    def AddPoint(self, System_String,IronPython_Runtime_List):
        """Adds a point to the part"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_Point):
        """Adds a point to the part"""
        pass
    def AddPoint(self, System_String,System_Double,System_Double,System_Double):
        """Adds a point to the part"""
        pass
    def AddPoints(self, System_String,IronPython_Runtime_List):
        """Adds a set of points to the part"""
        pass
    def AddExtrudeBoss(self, System_String,AlibreScript_API_Sketch,System_Double,System_Boolean):
        """Adds a simple extrude boss to a specific depth"""
        pass
    def AddExtrudeBoss(self, System_String,AlibreScript_API_Sketch,System_Double,System_Boolean,AlibreScript_API_Part_EndCondition,AlibreScript_API_ISketchSurface,System_Double,AlibreScript_API_Part_DirectionType,AlibreScript_API_ISweepPath,System_Double,System_Boolean):
        """Adds an extrude feature"""
        pass
    def AddExtrudeCut(self, System_String,AlibreScript_API_Sketch,System_Double,System_Boolean):
        """Adds a simple extrude cut to a specific depth"""
        pass
    def AddExtrudeCut(self, System_String,AlibreScript_API_Sketch,System_Double,System_Boolean,AlibreScript_API_Part_EndCondition,AlibreScript_API_ISketchSurface,System_Double,AlibreScript_API_Part_DirectionType,AlibreScript_API_ISweepPath,System_Double,System_Boolean):
        """Adds an extrude cut feature"""
        pass
    def AddRevolveBoss(self, System_String,AlibreScript_API_Sketch,AlibreScript_API_Axis,System_Double):
        """Creates a revolve boss feature"""
        pass
    def AddRevolveCut(self, System_String,AlibreScript_API_Sketch,AlibreScript_API_Axis,System_Double):
        """Creates a revolve cut feature"""
        pass
    def AddLoftBoss(self, System_String,IronPython_Runtime_List,System_Boolean,System_Boolean,System_Boolean,System_Boolean):
        """Adds a loft extrusion"""
        pass
    def AddLoftBoss(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List,AlibreScript_API_GuideCurveTypes,System_Boolean,System_Boolean,System_Boolean,System_Boolean):
        """Adds a loft extrusion using guide curves"""
        pass
    def AddLoftCut(self, System_String,IronPython_Runtime_List,System_Boolean,System_Boolean,System_Boolean,System_Boolean):
        """Adds a loft cut"""
        pass
    def AddLoftCut(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List,AlibreScript_API_GuideCurveTypes,System_Boolean,System_Boolean,System_Boolean,System_Boolean):
        """Adds a loft cut using guide curves"""
        pass
    def AddSweepBoss(self, System_String,AlibreScript_API_Sketch,AlibreScript_API_ISweepPath,System_Boolean,AlibreScript_API_Part_EndCondition,AlibreScript_API_ISketchSurface,System_Double,System_Double,System_Boolean):
        """Adds a sweep extrude feature"""
        pass
    def AddSweepCut(self, System_String,AlibreScript_API_Sketch,AlibreScript_API_ISweepPath,System_Boolean,AlibreScript_API_Part_EndCondition,AlibreScript_API_ISketchSurface,System_Double,System_Double,System_Boolean):
        """Adds a sweep extrude cut feature"""
        pass
    def AddFillet(self, System_String,AlibreScript_API_IFilletable,System_Double,System_Boolean):
        """Adds a constant radius fillet to a face or edge"""
        pass
    def AddFillet(self, System_String,IronPython_Runtime_List,System_Double,System_Boolean):
        """Adds a constant radius fillet to a set of faces and edges"""
        pass
    def AddFillet(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List,IronPython_Runtime_List,System_Boolean):
        """Adds a variable radius fillet to a set of faces and edges"""
        pass
    def Scale(self, System_String,System_Boolean,System_Double):
        """Uniform scaling of the part"""
        pass
    def NonUniformScale(self, System_String,System_Boolean,System_Double,System_Double,System_Double):
        """Non-uniform scaling of the part"""
        pass
    def AddChamfer(self, System_String,AlibreScript_API_IChamferable,System_Double,System_Double,System_Boolean):
        """Adds a chamfer to a face or edge"""
        pass
    def AddChamfer(self, System_String,IronPython_Runtime_List,System_Double,System_Double,System_Boolean):
        """Adds a chamfer to a set of faces and edges"""
        pass
    def AddChamfer(self, System_String,AlibreScript_API_IChamferable,System_Double,System_Boolean):
        """Adds a chamfer to a face or edge"""
        pass
    def AddChamfer(self, System_String,IronPython_Runtime_List,System_Double,System_Boolean):
        """Adds a chamfer to a set of faces and edges"""
        pass
    def AddChamferAngle(self, System_String,AlibreScript_API_IChamferable,System_Double,System_Double,System_Boolean):
        """Adds a chamfer to a face or edge"""
        pass
    def AddChamferAngle(self, System_String,IronPython_Runtime_List,System_Double,System_Double,System_Boolean):
        """Adds a chamfer to a set of faces and edges"""
        pass
    def AddVertexChamfer(self, System_String,AlibreScript_API_Vertex,System_Double,System_Double,System_Double):
        """Adds a chamfer to a vertex"""
        pass
    def AddVertexChamfer(self, System_String,IronPython_Runtime_List,System_Double,System_Double,System_Double):
        """Adds a chamfer to a set of vertices"""
        pass
    def Save(self, System_String):
        """Saves the part to a specific folder"""
        pass
    def SaveAs(self, System_String,System_String):
        """Saves the part to a specific folder with a new name"""
        pass
    def ExportSTL(self, System_String):
        """Exports the part as an STL file"""
        pass
    def ExportRotatedSTL(self, System_String,AlibreScript_API_Face,System_Boolean,System_Boolean,System_Double,System_Double,System_Double):
        """Exports the part as an STL rotated so that a specific face is on the bottom"""
        pass
    def ExportSTEP203(self, System_String):
        """Exports the part as a STEP 203 file"""
        pass
    def ExportSTEP214(self, System_String):
        """Exports the part as a STEP 214 file"""
        pass
    def ExportIGES(self, System_String):
        """Exports the part as a IGES file"""
        pass
    def ExportSAT(self, System_String,System_Int32,System_Boolean):
        """Exports the part as a SAT file"""
        pass
    def ExportBIP(self, System_String):
        """Exports a keyshot file"""
        pass
    def SetColor(self, System_Byte,System_Byte,System_Byte):
        """Sets the color of the part"""
        pass
    def SaveSnapshot(self, System_String,System_Int32,System_Int32,System_Boolean,System_Boolean):
        """Saves the current view as a bitmap image"""
        pass
    def SaveThumbnail(self, System_String,System_Int32,System_Int32):
        """Saves a thumbnail image of the part"""
        pass
    def Select(self, AlibreScript_API_ISelectableGeometry):
        """Selects a face, edge, vertex, point, axis, plane, sketch"""
        pass
    def Select(self, IronPython_Runtime_List):
        """Selects a group of faces, edges, vertices, points, axes, planes and sketches"""
        pass
    def SetUserData(self, System_String,IronPython_Runtime_PythonDictionary):
        """Sets user data"""
        pass
    def GetUserData(self, System_String):
        """Gets user data"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IPoint,System_Double,System_Double,System_Double):
        """Add a point at an offset to a point or a vertex"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IPoint,AlibreScript_API_IPoint,System_Double):
        """Add a point between two points/vertices"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IAxis,AlibreScript_API_IAxis):
        """Add a point at the intersection or two axes or edges"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IPlane,AlibreScript_API_IPlane,AlibreScript_API_IPlane):
        """Add a point at the intersection of three planes or faces"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IAxis,AlibreScript_API_IPlane):
        """Add a point at the the intersection of a axis or edge and a plane or face"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_IPoint,AlibreScript_API_IPlane,System_Double,System_Double):
        """Add a point by projecting a point or vertex onto a plane or face"""
        pass
    def AddPoint(self, System_String,AlibreScript_API_Edge,System_Double):
        """Add a point on an edge"""
        pass
    def AddPointFromCircularEdge(self, System_String,AlibreScript_API_Edge):
        """Adds a point at the center of a circular edge"""
        pass
    def AddPointFromToroidalFace(self, System_String,AlibreScript_API_Face):
        """Adds a point at the center of a toroidal face"""
        pass
    def GetFeature(self, System_String):
        """Gets a feature on the part"""
        pass
    def RemoveFeature(self, System_String):
        """Removes a feature from the part"""
        pass
    def RemoveFeature(self, AlibreScript_API_Feature):
        """Removes a feature from the part"""
        pass
    def SuppressFeature(self, System_String):
        """Suppresses a feature on the part"""
        pass
    def SuppressFeature(self, AlibreScript_API_Feature):
        """Suppresses a feature on the part"""
        pass
    def UnsuppressFeature(self, System_String):
        """Unsuppresses a feature on the part"""
        pass
    def UnsuppressFeature(self, AlibreScript_API_Feature):
        """Unsuppresses a feature on the part"""
        pass
    def HideFeature(self, System_String):
        """Hides a feature on the part"""
        pass
    def HideFeature(self, AlibreScript_API_Feature):
        """Hides a feature on the part"""
        pass
    def ShowFeature(self, System_String):
        """Shows a feature on the part"""
        pass
    def ShowFeature(self, AlibreScript_API_Feature):
        """Shows a feature on the part"""
        pass
    def GetPlane(self, System_String):
        """Gets a plane using the name of the plane"""
        pass
    def GetAxis(self, System_String):
        """Gets an axis from an axis name"""
        pass
    def GetPoint(self, System_String):
        """Gets a point on the part using the point name_ The point must have been created in a script"""
        pass
    def GetSketch(self, System_String):
        """Gets a sketch using the name of the sketch"""
        pass
    def Get3DSketch(self, System_String):
        """Gets a sketch using the name of the sketch"""
        pass
    def GetFace(self, System_String):
        """Gets a face using it's name Face<n>"""""
        pass
    def GetEdge(self, System_String):
        """Gets an edge using it's name Edge<n>"""""
        pass
    def GetVertex(self, System_String):
        """Gets a vertex using it's name Vertex<n>"""""
        pass
    def GetParameter(self, System_String):
        """Gets a parameter with a specific name"""
        pass
    def GetCustomProperty(self, System_String):
        """Gets the value of a custonm property"""
        pass
    def SetCustomProperty(self, System_String,System_String):
        """Sets the value of a custom property The custom property must already be defined on the part or defined on the user's PC"""
        pass
    def GetConfiguration(self, System_String):
        """Gets a configuration with a specific name"""
        pass
    def AddPlane(self, System_String,AlibreScript_API_ISketchSurface,System_Double):
        """Creates a plane based on the offset from an existing plane"""
        pass
    def AddPlane(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List):
        """Adds a plane using a normal vector and a point on the plane"""
        pass
    def AddPlane(self, System_String,AlibreScript_API_Axis,AlibreScript_API_Point):
        """Creates a new plane contaning an axis and a point"""
        pass
    def AddPlane(self, System_String,AlibreScript_API_ISketchSurface,AlibreScript_API_Axis,System_Double):
        """Creates a new plane at an angle to an existing plane"""
        pass
    def AddParameter(self, System_String,AlibreScript_API_ParameterTypes,System_Double):
        """Adds a cm/mm/in/deg parameter to the part"""
        pass
    def AddParameter(self, System_String,AlibreScript_API_ParameterTypes,AlibreScript_API_ParameterUnits,System_Double):
        """Adds a parameter to the part with specific units"""
        pass
    def AddParameter(self, System_String,AlibreScript_API_ParameterTypes,System_String):
        """Adds a parameter to the part"""
        pass
    def AddConfiguration(self, System_String):
        """Adds a configuration to the part"""
        pass
    def AddConfiguration(self, System_String,System_String):
        """Adds a configuration to the part using another configuration as a base"""
        pass
    def AddPlane(self, System_String,IronPython_Runtime_List,IronPython_Runtime_List,IronPython_Runtime_List):
        """Creates a plane using three points_ Each point is defined as list of [x, y, z]"""
        pass
    def AddSketch(self, System_String,AlibreScript_API_ISketchSurface):
        """Creates a new sketch using a plane/face"""
        pass
class Bspline3D:
    """Generated stub class"""
    def GetX(self, System_Double):
        """Gets the X value of the spline at a location along the spline"""
        pass
    def GetY(self, System_Double):
        """Gets the Y value of the spline at a location along the spline"""
        pass
    def GetZ(self, System_Double):
        """Gets the Z value of the spline at a location along the spline"""
        pass
    def GetPointAt(self, System_Double):
        """Gets a point on the spline"""
        pass
    def GetNormalAt(self, System_Double):
        """Gets the normal vector at a point on the spline"""
        pass
    def Subdivide(self, System_Int32):
        """Divides the Bspline up into segments"""
        pass
    def SubdivideGetNormals(self, System_Int32):
        """Divides the Bspline up into segments and gets the normal for each point"""
        pass
class Bspline:
    """Generated stub class"""
    def GetX(self, System_Double):
        """Gets the X value of the spline at a location along the spline"""
        pass
    def GetY(self, System_Double):
        """Gets the Y value of the spline at a location along the spline"""
        pass
    def GetPointAt(self, System_Double):
        """Gets a point on the spline"""
        pass
    def GetNormalAt(self, System_Double):
        """Gets the normal vector at a point on the spline"""
        pass
    def Subdivide(self, System_Int32):
        """Divides the Bspline up into segments"""
        pass
class Circle:
    """Generated stub class"""
class CircularArc3D:
    """Generated stub class"""
class CircularArc:
    """Generated stub class"""
class Ellipse:
    """Generated stub class"""
class EllipticalArc:
    """Generated stub class"""
class Line3D:
    """Generated stub class"""
class Polyline3D:
    """Generated stub class"""
    def AddPoint(self, AlibreScript_API_PolylinePoint3D):
        """Adds a new point to the polyline"""
        pass
    def InsertPoint(self, System_Int32,AlibreScript_API_PolylinePoint3D):
        """Inserts a point at a specific location"""
        pass
    def AddPolyline(self, AlibreScript_API_Polyline3D):
        """Appends a line to the current line"""
        pass
    def IsPointOnLine(self, AlibreScript_API_PolylinePoint3D,AlibreScript_API_PolylinePoint3D,AlibreScript_API_PolylinePoint3D,System_Double):
        """Determines if a point is on a line segment"""
        pass
    def SplitAtPoint(self, AlibreScript_API_PolylinePoint3D,System_Double):
        """Splits a polyline at a point, creating two polylines"""
        pass
    def Clone(self, System_Int32,System_Int32):
        """Creates an exact copy of a section of the line"""
        pass
    def Join(self, AlibreScript_API_Polyline3D):
        """Joins a line onto the end of the current line and returns the new line"""
        pass
    def Offset(self, System_Double,System_Double,System_Double):
        """Applies an offset to all points on the line"""
        pass
class Sketch:
    """Generated stub class"""
    def AddConstraint(self, AlibreScript_API_ISketchFigure,AlibreScript_API_Sketch_Constraints):
        """Adds a constraint to the sketch"""
        pass
    def AddConstraint(self, IronPython_Runtime_List,AlibreScript_API_Sketch_Constraints):
        """Adds a constraint to the sketch"""
        pass
    def AddLine(self, IronPython_Runtime_List,IronPython_Runtime_List,System_Boolean):
        """Adds a line to the sketch"""
        pass
    def AddLine(self, AlibreScript_API_Line):
        """Adds a line to the sketch"""
        pass
    def AddLine(self, System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds a line to the sketch"""
        pass
    def AddPoint(self, System_Double,System_Double):
        """Adds a point to the sketch"""
        pass
    def AddPoint(self, System_Double,System_Double,System_Boolean):
        """Adds a point to the sketch [DEPRECATED - DO NOT USE]"""
        pass
    def AddPoint(self, AlibreScript_API_SketchPoint):
        """Adds a point to the sketch"""
        pass
    def AddLines(self, IronPython_Runtime_List,System_Boolean):
        """Adds a polyline to the sketch"""
        pass
    def AddPolyline(self, AlibreScript_API_Polyline,System_Boolean):
        """Adds a polyline to the sketch"""
        pass
    def AddArcCenterStartEnd(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end"""
        pass
    def AddArcCenterStartAngle(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds a circular arc using center, start and angle Arc goes anti-clockwise from start"""
        pass
    def AddEllipse(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds an ellipse to the sketch using three points"""
        pass
    def AddEllipse(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds an ellipse to the sketch"""
        pass
    def AddEllipse(self, AlibreScript_API_Ellipse):
        """Adds an ellipse to the sketch"""
        pass
    def AddEllipticalArc(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds an elliptical arc to the sketch"""
        pass
    def AddEllipticalArc(self, AlibreScript_API_EllipticalArc):
        """Adds an elliptical arc to the sketch"""
        pass
    def AddArc(self, AlibreScript_API_CircularArc):
        """Adds a circular arc to the sketch"""
        pass
    def AddRectangle(self, System_Double,System_Double,System_Double,System_Double,System_Boolean):
        """Adds a rectangle to the sketch"""
        pass
    def AddCircle(self, System_Double,System_Double,System_Double,System_Boolean):
        """Adds a circle to the sketch"""
        pass
    def AddCircle(self, AlibreScript_API_Circle):
        """Adds a circle to the sketch"""
        pass
    def AddBspline(self, System_Int32,IronPython_Runtime_List,IronPython_Runtime_List,IronPython_Runtime_List,System_Boolean):
        """Adds a Bspline to the sketch"""
        pass
    def AddBspline(self, IronPython_Runtime_List,System_Boolean):
        """Adds a Bspline to the sketch through a set of points"""
        pass
    def AddFigure(self, AlibreScript_API_ISketchFigure):
        """Adds a figure to the sketch"""
        pass
    def AddBspline(self, AlibreScript_API_Bspline):
        """Adds a new bspline to the sketch"""
        pass
    def AddPolygon(self, System_Double,System_Double,System_Double,System_Int32,System_Boolean):
        """Adds a regular polygon to the sketch"""
        pass
    def AddPolyhole(self, System_Double,System_Double,System_Double,System_Boolean):
        """Adds a polyhole to the sketch Create a circle" whose size should be accurate regardless of the 3D printing method See: http://hydraraptor_blogspot_co_uk/2011/02/polyholes_html""""
        pass
    def CopyFrom(self, AlibreScript_API_Sketch):
        """Copies a sketch into this sketch"""
        pass
    def CopyFrom(self, AlibreScript_API_Sketch,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double):
        """Copies a sketch into this sketch"""
        pass
    def PointtoGlobal(self, System_Double,System_Double):
        """Converts a point on the sketch into a 3D point in the part coordinate system"""
        pass
    def GlobaltoPoint(self, System_Double,System_Double,System_Double):
        """Projects a 3D point in the part coordinate system into a point on the sketch"""
        pass
    def AddDimension(self, AlibreScript_API_SketchPoint,AlibreScript_API_SketchPoint):
        """Adds a dimension to the sketch between two points"""
        pass
    def AddDimension(self, AlibreScript_API_Circle):
        """Adds a dimension to the radius of a circle"""
        pass
    def AddDimension(self, AlibreScript_API_CircularArc):
        """Adds a dimension to the radius of an arc"""
        pass
    def SavetoXml(self, System_String):
        """Saves the sketch to an XML file Does not support ellipses and elliptical arcs"""
        pass
    def LoadXml(self, System_String):
        """Loads the sketch from an XML file"""
        pass
    def FromXml(self, System_String):
        """Adds elements to the sketch from XML"""
        pass
    def StartFaceMapping(self, AlibreScript_API_Vertex,AlibreScript_API_Vertex):
        """Starts mapping the face so that the specified edge is at [0, 0]"""
        pass
    def StartFaceMapping(self, IronPython_Runtime_List,IronPython_Runtime_List):
        """Starts mapping the face so that the specified edge is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values"""
        pass
    def StartMapping(self, IronPython_Runtime_List,IronPython_Runtime_List,IronPython_Runtime_List):
        """Starts mapping the sketch so that the specified line is at [0, 0] Affects only the operation of the AddXXX functions and the GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values"""
        pass
    def ImportSVG(self, System_String):
        """Imports an SVG into the sketch"""
        pass
    def ImportSVG(self, System_String,System_Double,System_Double,System_Double,System_Boolean,System_Boolean):
        """Imports an SVG into the sketch"""
        pass
    def ExportSVG(self, System_String):
        """Exports the sketch to an SVG"""
        pass
    def ExportSVG(self, System_String,System_Boolean):
        """Exports the sketch to an SVG"""
        pass
    def ExportSVG(self, System_String,System_Boolean,System_Double,System_String,System_String,System_Boolean,System_Double,System_Double,System_String,System_String,System_Boolean,System_Double):
        """Exports the sketch to an SVG with specific styling"""
        pass
class Polyline:
    """Generated stub class"""
    def AddPoint(self, AlibreScript_API_PolylinePoint):
        """Adds a new point to the polyline"""
        pass
    def InsertPoint(self, System_Int32,AlibreScript_API_PolylinePoint):
        """Inserts a point at a specific location"""
        pass
    def AddCircle(self, System_Double,System_Double,System_Double,System_Int32):
        """Adds a circle to the line"""
        pass
    def AddArc(self, AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,System_Int32):
        """Adds an arc to the polyline_ The arc is approcimated with straight line segments"""
        pass
    def AddPolyline(self, AlibreScript_API_Polyline):
        """Appends a line to the current line"""
        pass
    def FindIntersection(self, AlibreScript_API_Polyline,AlibreScript_API_Polyline):
        """Finds the first intersection point between two lines"""
        pass
    def FindIntersectionWithCircle(self, AlibreScript_API_Polyline,System_Double,System_Double,System_Double):
        """Finds first intersection of line with a circle"""
        pass
    def FindIntersection(self, AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint):
        """Gets the intersection between the line segments A1A2 and B1B2"""
        pass
    def IsPointOnLine(self, AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,AlibreScript_API_PolylinePoint,System_Double):
        """Determines if a point is on a line segment"""
        pass
    def SplitAtPoint(self, AlibreScript_API_PolylinePoint,System_Double):
        """Splits a polyline at a point, creating two polylines"""
        pass
    def Clone(self, System_Int32,System_Int32):
        """Creates an exact copy of a section of the line"""
        pass
    def Join(self, AlibreScript_API_Polyline):
        """Joins a line onto the end of the current line and returns the new line"""
        pass
    def RotateZ(self, System_Double,System_Double,System_Double):
        """Rotates the polyline around the Z axis"""
        pass
    def Offset(self, System_Double,System_Double):
        """Applies an offset to all points on the line"""
        pass
class PolylinePoint:
    """Generated stub class"""
    def Offset(self, System_Double,System_Double):
        """Applies an offset to the point and creates a new point"""
        pass
    def Scale(self, System_Double,System_Double,System_Double):
        """Scales the point location based on an origin for the scaling"""
        pass
    def RotateZ(self, System_Double,System_Double,System_Double):
        """Rotates the point around the Z axis"""
        pass
class Sketch3D:
    """Generated stub class"""
    def AddLine(self, IronPython_Runtime_List,IronPython_Runtime_List):
        """Adds a line to the sketch"""
        pass
    def AddLine(self, AlibreScript_API_Line3D):
        """Adds a line to the sketch"""
        pass
    def AddPoint(self, System_Double,System_Double,System_Double):
        """Adds a point to the sketch"""
        pass
    def AddPoint(self, AlibreScript_API_SketchPoint3D):
        """Adds a point to the sketch"""
        pass
    def AddLine(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Double):
        """Adds a line to the sketch"""
        pass
    def AddLines(self, IronPython_Runtime_List):
        """Adds a polyline to the sketch"""
        pass
    def AddPolyline(self, AlibreScript_API_Polyline3D):
        """Adds a polyline to the sketch"""
        pass
    def AddArcCenterStartEnd(self, System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double,System_Double):
        """Adds a circular arc using three points - center, start and end Arc goes anti-clockwise from start to end"""
        pass
    def AddArc(self, AlibreScript_API_CircularArc3D):
        """Adds a circular arc to the sketch"""
        pass
    def AddBspline(self, IronPython_Runtime_List):
        """Adds a Bspline to the sketch"""
        pass
    def AddBspline(self, AlibreScript_API_Bspline3D):
        """Adds a Bspline to the sketch"""
        pass
    def SavetoXml(self, System_String):
        """Saves the sketch to an XML file"""
        pass
    def LoadXml(self, System_String):
        """Loads the sketch from an XML file"""
        pass
    def FromXml(self, System_String):
        """Adds elements to the sketch from XML"""
        pass
class SketchPoint:
    """Generated stub class"""
class SketchPoint3D:
    """Generated stub class"""
class ThreeD:
    """Generated stub class"""
    def GetPerpendicularVector(self, IronPython_Runtime_List):
        """Gets a vector that is perpendicular to a vector"""
        pass
    def TransformPointUsingVectors(self, IronPython_Runtime_List,IronPython_Runtime_List,IronPython_Runtime_List):
        """Transforms a point based on two vectors"""
        pass
