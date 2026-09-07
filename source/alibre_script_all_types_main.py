# pyright: reportRedeclaration=false, reportAttributeAccessIssue=false, reportCallIssue=false
# Fully self-contained Alibre Script type harness.
# Type declarations generated from:
#   Alibre-Script-Stub-Files/generated/package/AlibreScript/__init__.pyi
#
# Target runtime: Alibre Script add-on, IronPython 2.7.10.
# This file can also run outside Alibre because it contains fallback mocks.

_RUNNING_IN_ALIBRE_SCRIPT = (
    'CurrentPart' in globals() or
    'CurrentAssembly' in globals() or
    'ScriptFolder' in globals()
)

if not _RUNNING_IN_ALIBRE_SCRIPT:
    ScriptFileName = ''
    ScriptFolder = ''

    class _StubBase(object):
        pass
        def __init__(self, *args, **kwargs):
            pass

    class Part(_StubBase):
        pass
        class DirectionType:
            pass
            Normal = None
        class EndCondition:
            pass
            ToDepth = None
            ThroughAll = None
            MidPlane = None
            EntirePath = None
        class FileTypes:
            pass
            GeomagicDesignPart = None
            AlibreDesignPart = None
            STEP = None
            IGES = None
            ThreeDM = None
            SAT = None
            STL_in = None
            STL_cm = None
            STL_mm = None
        Comment = None
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
        Mass = None
        Material = None
        ModifiedInformation = None
        Name = None
        Number = None
        Origin = None
        Parameters = None
        Product = None
        ReceivedFrom = None
        Revision = None
        Selections = None
        StockSize = None
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
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def __init__(self, value, value_2, value_3):
            return None
        # @overload
        def __init__(self, value):
            return None
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def __init__(self, value, value_2, value_3):
            return None
        # @overload
        def __init__(self, value, part_file_types):
            return None
        # @overload
        def __init__(self, value, part_file_types, value_2):
            return None
        def Add3DSketch(self, name):
            return None
        # @overload
        def AddAxis(self, name, plane1, plane2):
            return None
        # @overload
        def AddAxis(self, name, point_a, point_b):
            return None
        # @overload
        def AddAxis(self, name, cylindrical_face):
            return None
        # @overload
        def AddAxis(self, name, point1, point2):
            return None
        # @overload
        def AddChamfer(self, name, item, distance1, distance2, tangent_propagate):
            return None
        # @overload
        def AddChamfer(self, name, items, distance1, distance2, tangent_propagate):
            return None
        # @overload
        def AddChamfer(self, name, item, distance, tangent_propagate):
            return None
        # @overload
        def AddChamfer(self, name, items, distance, tangent_propagate):
            return None
        # @overload
        def AddChamferAngle(self, name, item, distance, angle, tangent_propagate):
            return None
        # @overload
        def AddChamferAngle(self, name, items, distance, angle, tangent_propagate):
            return None
        # @overload
        def AddConfiguration(self, name):
            return None
        # @overload
        def AddConfiguration(self, name, base_configuration_name):
            return None
        # @overload
        def AddExtrudeBoss(self, name, sketch, depth, is_reversed):
            return None
        # @overload
        def AddExtrudeBoss(self, name, sketch, depth, is_reversed, end_condition, end_plane, end_offset, direction, sweep_path, draft_angle, outward_draft):
            return None
        # @overload
        def AddExtrudeCut(self, name, sketch, depth, is_reversed):
            return None
        # @overload
        def AddExtrudeCut(self, name, sketch, depth, is_reversed, end_condition, end_plane, end_offset, direction, sweep_path, draft_angle, outward_draft):
            return None
        # @overload
        def AddFillet(self, name, item, radius, tangent_propagate):
            return None
        # @overload
        def AddFillet(self, name, items, radius, tangent_propagate):
            return None
        # @overload
        def AddFillet(self, name, items, start_radii, end_radii, tangent_propagate):
            return None
        def AddGear(self, name, diametral_pitch, numberof_teeth, pitch_diameter, pressure_angle, single_tooth, center_x, center_y, involute_points, plane):
            return None
        # @overload
        def AddGearDN(self, name, diametral_pitch, numberof_teeth, pressure_angle, center_x, center_y, plane):
            return None
        # @overload
        def AddGearDN(self, name, diametral_pitch, numberof_teeth, pressure_angle, center_x, center_y, single_tooth, plane):
            return None
        # @overload
        def AddGearDP(self, name, diametral_pitch, pitch_diameter, pressure_angle, center_x, center_y, plane):
            return None
        # @overload
        def AddGearDP(self, name, diametral_pitch, pitch_diameter, pressure_angle, center_x, center_y, single_tooth, plane):
            return None
        # @overload
        def AddGearNP(self, name, numberof_teeth, pitch_diameter, pressure_angle, center_x, center_y, plane):
            return None
        # @overload
        def AddGearNP(self, name, numberof_teeth, pitch_diameter, pressure_angle, center_x, center_y, single_tooth, plane):
            return None
        # @overload
        def AddLoftBoss(self, name, cross_sections, minimize_twist, minimize_curvature, simplify_surface, connect_ends):
            return None
        # @overload
        def AddLoftBoss(self, name, cross_sections, guide_curves, guide_type, minimize_twist, minimize_curvature, simplify_surface, connect_ends):
            return None
        # @overload
        def AddLoftCut(self, name, cross_sections, minimize_twist, minimize_curvature, simplify_surface, connect_ends):
            return None
        # @overload
        def AddLoftCut(self, name, cross_sections, guide_curves, guide_type, minimize_twist, minimize_curvature, simplify_surface, connect_ends):
            return None
        # @overload
        def AddParameter(self, name, type, value):
            return None
        # @overload
        def AddParameter(self, name, type, unitsto_use, value):
            return None
        # @overload
        def AddParameter(self, name, type, equation):
            return None
        # @overload
        def AddPlane(self, name, source_plane, offset):
            return None
        # @overload
        def AddPlane(self, name, normal_vector, pointon_plane):
            return None
        # @overload
        def AddPlane(self, name, axis, point):
            return None
        # @overload
        def AddPlane(self, name, source_plane, rotation_axis, angle):
            return None
        # @overload
        def AddPlane(self, name, point1, point2, point3):
            return None
        # @overload
        def AddPoint(self, name, point):
            return None
        # @overload
        def AddPoint(self, name, point):
            return None
        # @overload
        def AddPoint(self, name, x, y, z):
            return None
        # @overload
        def AddPoint(self, name, point_or_vertex, x_offset, y_offset, z_offset):
            return None
        # @overload
        def AddPoint(self, name, point_or_vertex1, point_or_vertex2, ratio):
            return None
        # @overload
        def AddPoint(self, name, axis_or_edge1, axis_or_edge2):
            return None
        # @overload
        def AddPoint(self, name, plane_or_face1, plane_or_face2, plane_or_face3):
            return None
        # @overload
        def AddPoint(self, name, axis_or_edge, plane_or_face):
            return None
        # @overload
        def AddPoint(self, name, source_point_or_vertex, target_plane_or_face, x_offset, y_offset):
            return None
        # @overload
        def AddPoint(self, name, target_edge, ratio):
            return None
        def AddPointFromCircularEdge(self, name, target_edge):
            return None
        def AddPointFromToroidalFace(self, name, target_face):
            return None
        def AddPoints(self, prefix, points):
            return None
        def AddRevolveBoss(self, name, sketch, axis, angle):
            return None
        def AddRevolveCut(self, name, sketch, axis, angle):
            return None
        def AddSketch(self, name, plane):
            return None
        def AddSweepBoss(self, name, profile_sketch, path_sketch, is_rigid, end_condition, end_plane, end_offset, draft_angle, outward_draft):
            return None
        def AddSweepCut(self, name, profile_sketch, path_sketch, is_rigid, end_condition, end_plane, end_offset, draft_angle, outward_draft):
            return None
        # @overload
        def AddVertexChamfer(self, name, item, distance1, distance2, distance3):
            return None
        # @overload
        def AddVertexChamfer(self, name, items, distance1, distance2, distance3):
            return None
        def Close(self):
            return None
        def DisplayUnits(self):
            return None
        def ExportBIP(self, file_name):
            return None
        def ExportIGES(self, file_name):
            return None
        def ExportRotatedSTL(self, file_name, bottom_face, forceto_millimeters, use_custom_settings, max_cell_size, normal_deviation, surface_deviation):
            return None
        def ExportSAT(self, file_name, version, save_colors):
            return None
        def ExportSTEP203(self, file_name):
            return None
        def ExportSTEP214(self, file_name):
            return None
        def ExportSTL(self, file_name):
            return None
        def Get3DSketch(self, name):
            return None
        def GetActiveConfiguration(self):
            return None
        def GetAxis(self, name):
            return None
        def GetBoundingBox(self):
            return None
        def GetConfiguration(self, name):
            return None
        def GetCustomProperty(self, name):
            return None
        def GetEdge(self, name):
            return None
        def GetEdges(self):
            return None
        def GetFace(self, name):
            return None
        def GetFaces(self):
            return None
        def GetFeature(self, name):
            return None
        def GetParameter(self, name):
            return None
        def GetPlane(self, name):
            return None
        def GetPoint(self, name):
            return None
        def GetSelectionAssembly(self):
            return None
        def GetSketch(self, name):
            return None
        def GetUserData(self, name):
            return None
        def GetVertex(self, name):
            return None
        def GetVertices(self):
            return None
        # @overload
        def HideFeature(self, name):
            return None
        # @overload
        def HideFeature(self, feature):
            return None
        def IsOpen(self):
            return None
        def NonUniformScale(self, name, scale_about_center, scale_factor_x, scale_factor_y, scale_factor_z):
            return None
        def PauseUpdating(self):
            return None
        def Regenerate(self):
            return None
        # @overload
        def RemoveFeature(self, name):
            return None
        # @overload
        def RemoveFeature(self, feature):
            return None
        def RemovePlane(self, plane):
            return None
        def RemovePoint(self, point):
            return None
        # @overload
        def RemoveSketch(self, name):
            return None
        # @overload
        def RemoveSketch(self, sketch):
            return None
        def ResumeUpdating(self):
            return None
        # @overload
        def Save(self):
            return None
        # @overload
        def Save(self, folder):
            return None
        def SaveAs(self, folder, new_name):
            return None
        def SaveSnapshot(self, file_name, width, height, use_aspect_ratio, use_widthand_height):
            return None
        def SaveThumbnail(self, file_name, width, height):
            return None
        def Scale(self, name, scale_about_center, scale_factor):
            return None
        # @overload
        def Select(self, faceor_edge):
            return None
        # @overload
        def Select(self, faces_edges_list):
            return None
        def SetColor(self, red, green, blue):
            return None
        def SetCustomProperty(self, name, value):
            return None
        def SetUserData(self, name, dict):
            return None
        # @overload
        def ShowFeature(self, name):
            return None
        # @overload
        def ShowFeature(self, feature):
            return None
        # @overload
        def SuppressFeature(self, name):
            return None
        # @overload
        def SuppressFeature(self, feature):
            return None
        # @overload
        def UnsuppressFeature(self, name):
            return None
        # @overload
        def UnsuppressFeature(self, feature):
            return None

    class Assembly(_StubBase):
        pass
        class ConstraintBoundsType:
            pass
    # Unconverted stub line:         pass
        Comment = None
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
        Parameters = None
        Parts = None
        Product = None
        ReceivedFrom = None
        Revision = None
        Selections = None
        StockSize = None
        SubAssemblies = None
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
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def __init__(self, value, value_2, value_3):
            return None
        # @overload
        def __init__(self, value):
            return None
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def __init__(self, value, value_2, value_3):
            return None
        # @overload
        def AddAlignConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b):
            return None
        # @overload
        def AddAlignConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        def AddAlignConstraint2(self, distance1, distance2, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name, bounds_type):
            return None
        # @overload
        def AddAngleConstraint(self, angle, partor_assembly_a, item_a, partor_assembly_b, item_b):
            return None
        # @overload
        def AddAngleConstraint(self, angle, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        def AddAngleConstraint2(self, angle1, angle2, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name, bounds_type):
            return None
        # @overload
        def AddAxis(self, name, plane1, plane2):
            return None
        # @overload
        def AddAxis(self, name, point1, point2):
            return None
        # @overload
        def AddConfiguration(self, name):
            return None
        # @overload
        def AddConfiguration(self, name, base_configuration_name):
            return None
        def AddFastenerConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        def AddFastenerConstraint2(self, distance1, distance2, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name, bounds_type):
            return None
        def AddGearConstraint(self, ratio_a, ratio_b, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        # @overload
        def AddMateConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b):
            return None
        # @overload
        def AddMateConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        def AddMateConstraint2(self, distance1, distance2, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name, bounds_type):
            return None
        def AddNewPart(self, name, x, y, z):
            return None
        def AddNewSubAssembly(self, name, x, y, z):
            return None
        # @overload
        def AddOrientConstraint(self, value, partor_assembly_a, item_a, partor_assembly_b, item_b):
            return None
        # @overload
        def AddOrientConstraint(self, value, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        # @overload
        def AddParameter(self, name, type, value):
            return None
        # @overload
        def AddParameter(self, name, type, equation):
            return None
        # @overload
        def AddPart(self, folder, name):
            return None
        # @overload
        def AddPart(self, folder, name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddPart(self, folder, name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddPart(self, part):
            return None
        # @overload
        def AddPart(self, part, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddPart(self, file_name):
            return None
        # @overload
        def AddPart(self, file_name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddPart(self, file_name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddPart(self, part, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddPlane(self, name, source_plane, offset):
            return None
        # @overload
        def AddPlane(self, name, normal_vector, pointon_plane):
            return None
        # @overload
        def AddPlane(self, name, source_plane, rotation_axis, angle):
            return None
        # @overload
        def AddPlane(self, name, point1, point2, point3):
            return None
        # @overload
        def AddPoint(self, name, point_or_vertex, x_offset, y_offset, z_offset):
            return None
        # @overload
        def AddPoint(self, name, point_or_vertex1, point_or_vertex2, ratio):
            return None
        # @overload
        def AddPoint(self, name, axis_or_edge1, axis_or_edge2):
            return None
        # @overload
        def AddPoint(self, name, plane_or_face1, plane_or_face2, plane_or_face3):
            return None
        # @overload
        def AddPoint(self, name, axis_or_edge, plane_or_face):
            return None
        # @overload
        def AddPoint(self, name, source_point_or_vertex, target_plane_or_face, x_offset, y_offset):
            return None
        # @overload
        def AddPoint(self, name, target_edge, ratio):
            return None
        # @overload
        def AddPoint(self, name, x, y, z):
            return None
        def AddPointFromCircularEdge(self, name, target_edge):
            return None
        def AddPointFromToroidalFace(self, name, target_face):
            return None
        def AddPoints(self, prefix, points):
            return None
        def AddRackAndPinionConstraint(self, pitch_diameter, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        def AddScrewConstraint(self, thread_pitch, partor_assembly_a, item_a, partor_assembly_b, item_b, is_reversed, name):
            return None
        # @overload
        def AddSubAssembly(self, file_name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddSubAssembly(self, file_name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddSubAssembly(self, assembly):
            return None
        # @overload
        def AddSubAssembly(self, assembly, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddSubAssembly(self, assembly, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddSubAssembly(self, folder, name):
            return None
        # @overload
        def AddSubAssembly(self, folder, name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def AddSubAssembly(self, folder, name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def AddSubAssembly(self, file_name):
            return None
        # @overload
        def AddTangentConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b, outside):
            return None
        # @overload
        def AddTangentConstraint(self, distance, partor_assembly_a, item_a, partor_assembly_b, item_b, outside, is_reversed, name):
            return None
        # @overload
        def AnchorPart(self, name):
            return None
        # @overload
        def AnchorPart(self, assembled_part):
            return None
        def AnchorSubAssembly(self, name):
            return None
        def Close(self):
            return None
        def CreateUniqueName(self, base_name):
            return None
        def DisplayUnits(self):
            return None
        # @overload
        def DuplicatePart(self, name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def DuplicatePart(self, assembled_part, value, value_2, value_3):
            return None
        # @overload
        def DuplicatePart(self, name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def DuplicatePart(self, assembled_part, value, value_2, value_3, value_4, value_5, value_6, value_7):
            return None
        # @overload
        def DuplicateSubAssembly(self, sub_assembly, offset_x, offset_y, offset_z):
            return None
        # @overload
        def DuplicateSubAssembly(self, name, offset_x, offset_y, offset_z):
            return None
        # @overload
        def DuplicateSubAssembly(self, sub_assembly, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        # @overload
        def DuplicateSubAssembly(self, name, offset_x, offset_y, offset_z, angle_x, angle_y, angle_z, translation_first):
            return None
        def ExportBIP(self, file_name):
            return None
        def ExportIGES(self, file_name):
            return None
        def ExportSAT(self, file_name, version, save_colors):
            return None
        def ExportSTEP203(self, file_name):
            return None
        def ExportSTEP214(self, file_name):
            return None
        def ExportSTL(self, file_name):
            return None
        def GetActiveConfiguration(self):
            return None
        def GetAxis(self, name):
            return None
        def GetConfiguration(self, name):
            return None
        def GetCustomProperty(self, name):
            return None
        def GetParameter(self, name):
            return None
        def GetPart(self, name):
            return None
        # @overload
        def GetPartOrientation(self, assembled_part):
            return None
        # @overload
        def GetPartOrientation(self, part_name):
            return None
        def GetPlane(self, name):
            return None
        def GetPoint(self, name):
            return None
        def GetSubAssembly(self, name):
            return None
        def GetUserData(self, name):
            return None
        # @overload
        def HidePart(self, name):
            return None
        # @overload
        def HidePart(self, assembled_part):
            return None
        def HideSubAssembly(self, name):
            return None
        # @overload
        def MovePart(self, name, offset_x, offset_y, offset_z, apply_constraints):
            return None
        # @overload
        def MovePart(self, assembled_part, value, value_2, value_3, value_4):
            return None
        def MoveParts(self, names, offset_x, offset_y, offset_z, apply_constraints):
            return None
        def MoveSubAssemblies(self, names, offset_x, offset_y, offset_z, apply_constraints):
            return None
        # @overload
        def MoveSubAssembly(self, name, offset_x, offset_y, offset_z, apply_constraints):
            return None
        # @overload
        def MoveSubAssembly(self, sub_assembly, offset_x, offset_y, offset_z, apply_constraints):
            return None
        def PauseUpdating(self):
            return None
        def Regenerate(self):
            return None
        def ResumeUpdating(self):
            return None
        # @overload
        def RotatePart(self, name, angle_x, angle_y, angle_z, apply_constraints):
            return None
        # @overload
        def RotatePart(self, assembled_part, value, value_2, value_3, value_4):
            return None
        def RotateParts(self, names, angle_x, angle_y, angle_z, apply_constraints):
            return None
        def RotateSubAssemblies(self, names, angle_x, angle_y, angle_z, apply_constraints):
            return None
        # @overload
        def RotateSubAssembly(self, name, angle_x, angle_y, angle_z, apply_constraints):
            return None
        # @overload
        def RotateSubAssembly(self, sub_assembly, angle_x, angle_y, angle_z, apply_constraints):
            return None
        # @overload
        def RotateSubAssembly(self, alibre_x_iad_occurrence, value, value_2, value_3, value_4):
            return None
        # @overload
        def Save(self):
            return None
        # @overload
        def Save(self, folder):
            return None
        def SaveAll(self, folder):
            return None
        def SaveAs(self, folder, new_name):
            return None
        def SaveSnapshot(self, file_name, width, height, use_aspect_ratio, use_widthand_height):
            return None
        def SaveThumbnail(self, file_name, width, height):
            return None
        def SetCustomProperty(self, name, value):
            return None
        def SetUserData(self, name, dict):
            return None
        # @overload
        def ShowPart(self, name):
            return None
        # @overload
        def ShowPart(self, assembled_part):
            return None
        def ShowSubAssembly(self, name):
            return None
        # @overload
        def SuppressPart(self, name):
            return None
        # @overload
        def SuppressPart(self, assembled_part):
            return None
        def SuppressSubAssembly(self, name):
            return None
        # @overload
        def UnanchorPart(self, name):
            return None
        # @overload
        def UnanchorPart(self, assembled_part):
            return None
        def UnanchorSubAssembly(self, name):
            return None
        # @overload
        def UnsuppressPart(self, name):
            return None
        # @overload
        def UnsuppressPart(self, assembled_part):
            return None
        def UnsuppressSubAssembly(self, name):
            return None

    class AssembledPart(_StubBase):
        pass
        Configurations = None
        Name = None
        def __init__(self):
            return None
        # @overload
        def AddPoint(self, value, i_point, value_2, value_3, value_4):
            return None
        # @overload
        def AddPoint(self, value, i_point, i_point_2, value_2):
            return None
        # @overload
        def AddPoint(self, value, i_axis, i_axis_2):
            return None
        # @overload
        def AddPoint(self, value, i_plane, i_plane_2, i_plane_3):
            return None
        # @overload
        def AddPoint(self, value, i_axis, i_plane):
            return None
        # @overload
        def AddPoint(self, value, i_point, i_plane, value_2, value_3):
            return None
        # @overload
        def AddPoint(self, value, edge, value_2):
            return None
        def AddPointFromCircularEdge(self, value, edge):
            return None
        def AddPointFromToroidalFace(self, value, face):
            return None
        def AssemblyPointtoPartPoint(self, list):
            return None
        def GetAssembly(self):
            return None
        def GetAssemblyBoundingBox(self):
            return None
        def GetAssemblyVertices(self):
            return None
        def GetConfiguration(self, value):
            return None
        def GetEdge(self, value):
            return None
        def GetEdges(self):
            return None
        def GetFace(self, value):
            return None
        def GetFaces(self):
            return None
        def GetMappedOccurrence(self, alibre_x_iad_assembly_session):
            return None
        def PartPointtoAssemblyPoint(self, list):
            return None

    class AssembledSubAssembly(_StubBase):
        pass
        Configurations = None
        Name = None
        def __init__(self):
            return None
        def GetConfiguration(self, name):
            return None
        def GetMappedOccurrence(self, iad_assembly_session_assembly):
            return None
        def GetSelectionAssembly(self):
            return None

    class Sketch(_StubBase):
        pass
        class Constraints:
            pass
            Coincident = None
            Collinear = None
            Equal = None
            Horizontal = None
            Parallel = None
            Perpendicular = None
            Tangent = None
            Vertical = None
        Figures = None
        Name = None
        Origin = None
        def __init__(self):
            return None
        def AddArc(self, new_arc):
            return None
        def AddArcCenterStartAngle(self, center_x, center_y, start_x, start_y, angle, is_reference):
            return None
        def AddArcCenterStartEnd(self, center_x, center_y, start_x, start_y, end_x, end_y, is_reference):
            return None
        # @overload
        def AddBspline(self, order, control_points, knot_vectors, weights, is_reference):
            return None
        # @overload
        def AddBspline(self, points, is_reference):
            return None
        # @overload
        def AddBspline(self, new_bspline):
            return None
        # @overload
        def AddCircle(self, center_x, center_y, diameter, is_reference):
            return None
        # @overload
        def AddCircle(self, new_circle):
            return None
        # @overload
        def AddConstraint(self, i_sketch_figure, sketch_constraints):
            return None
        # @overload
        def AddConstraint(self, list, sketch_constraints):
            return None
        # @overload
        def AddDimension(self, p1, p2):
            return None
        # @overload
        def AddDimension(self, circle):
            return None
        # @overload
        def AddDimension(self, arc):
            return None
        # @overload
        def AddEllipse(self, center_x, center_y, major_x, major_y, minor_x, minor_y, is_reference):
            return None
        # @overload
        def AddEllipse(self, center_x, center_y, major_axis_diameter, minor_major_ratio, major_axis_angle, is_reference):
            return None
        # @overload
        def AddEllipse(self, new_ellipse):
            return None
        # @overload
        def AddEllipticalArc(self, center_x, center_y, start_x, start_y, end_x, end_y, major_axis_diameter, minor_major_ratio, major_axis_angle, is_reference):
            return None
        # @overload
        def AddEllipticalArc(self, new_elliptical_arc):
            return None
        def AddFigure(self, new_figure):
            return None
        # @overload
        def AddLine(self, start_point, end_point, is_reference):
            return None
        # @overload
        def AddLine(self, new_line):
            return None
        # @overload
        def AddLine(self, x1, y1, x2, y2, is_reference):
            return None
        def AddLines(self, points, is_reference):
            return None
        # @overload
        def AddPoint(self, x, y):
            return None
        # @overload
        def AddPoint(self, x, y, is_reference):
            return None
        # @overload
        def AddPoint(self, new_point):
            return None
        def AddPolygon(self, center_x, center_y, diameter, sides, is_reference):
            return None
        def AddPolyhole(self, center_x, center_y, diameter, is_reference):
            return None
        def AddPolyline(self, line, is_reference):
            return None
        def AddRectangle(self, bottom_left_x, bottom_left_y, top_right_x, top_right_y, is_reference):
            return None
        # @overload
        def CopyFrom(self, source):
            return None
        # @overload
        def CopyFrom(self, source, angle, rotation_center_x, rotation_center_y, translate_x, translate_y, scale_origin_x, scale_origin_y, scale_factor):
            return None
        # @overload
        def ExportSVG(self, file_name):
            return None
        # @overload
        def ExportSVG(self, file_name, include_references):
            return None
        # @overload
        def ExportSVG(self, file_name, include_references, stroke_width, stroke_color, stroke_line_cap, stroke_dashed, stroke_dash_length, reference_stroke_width, reference_stroke_color, reference_stroke_line_cap, reference_stroke_dashed, reference_stroke_dash_length):
            return None
        def FromXml(self, xml):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def GetSurface(self):
            return None
        def GlobaltoPoint(self, x, y, z):
            return None
        # @overload
        def ImportSVG(self, file_name):
            return None
        # @overload
        def ImportSVG(self, file_name, translate_x, translate_y, rotation_angle, translate_then_rotate, native_figures):
            return None
        def LoadXml(self, file_name):
            return None
        def PointtoGlobal(self, x, y):
            return None
        def SavetoXml(self, file_name):
            return None
        # @overload
        def StartFaceMapping(self, edge_vertex1, edge_vertex2):
            return None
        # @overload
        def StartFaceMapping(self, edge_end_point1, edge_end_point2):
            return None
        def StartMapping(self, point1, point2, point_above_axis):
            return None
        def StopFaceMapping(self):
            return None
        def StopMapping(self):
            return None
        def ToXml(self):
            return None

    class Sketch3D(_StubBase):
        pass
        Figures = None
        Name = None
        def __init__(self):
            return None
        def AddArc(self, new_arc):
            return None
        def AddArcCenterStartEnd(self, center_x, center_y, center_z, start_x, start_y, start_z, end_x, end_y, end_z):
            return None
        # @overload
        def AddBspline(self, points):
            return None
        # @overload
        def AddBspline(self, bspline):
            return None
        # @overload
        def AddLine(self, start_point, end_point):
            return None
        # @overload
        def AddLine(self, new_line):
            return None
        # @overload
        def AddLine(self, x1, y1, z1, x2, y2, z2):
            return None
        def AddLines(self, points):
            return None
        # @overload
        def AddPoint(self, x, y, z):
            return None
        # @overload
        def AddPoint(self, new_point):
            return None
        def AddPolyline(self, line):
            return None
        def FromXml(self, xml):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def LoadXml(self, file_name):
            return None
        def SavetoXml(self, file_name):
            return None
        def ToXml(self):
            return None

    class Plane(_StubBase):
        pass
        Name = None
        def __init__(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def Hide(self):
            return None
        def IsParallel(self, other_plane):
            return None
        def Show(self):
            return None

    class Axis(_StubBase):
        pass
        Name = None
        def __init__(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def Hide(self):
            return None
        def Show(self):
            return None

    class Point(_StubBase):
        pass
        Name = None
        X = None
        Y = None
        Z = None
        def __init__(self):
            return None
        def GetCoordinates(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def Hide(self):
            return None
        def Show(self):
            return None

    class Face(_StubBase):
        pass
        Name = None
        def __init__(self):
            return None
        def DistanceTo(self, other_face):
            return None
        def GetAdjoiningFaces(self):
            return None
        def GetArea(self):
            return None
        def GetEdges(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def GetVertices(self):
            return None
        def IsParallel(self, other_face):
            return None
        def IsRectangle(self):
            return None

    class Edge(_StubBase):
        pass
        Diameter = None
        Length = None
        Name = None
        def __init__(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None
        def GetVertices(self):
            return None

    class Vertex(_StubBase):
        pass
        Name = None
        X = None
        Y = None
        Z = None
        def __init__(self):
            return None
        def GetPart(self):
            return None
        def GetSelectionAssembly(self):
            return None

    class Feature(_StubBase):
        pass
        Name = None
        def __init__(self):
            return None
        def SetColor(self, red, green, blue):
            return None

    class Windows(_StubBase):
        pass
        def __init__(self):
            return None
        def CloseForm(self, session_identifier):
            return None
        def DisableInput(self, index):
            return None
        def EnableInput(self, index):
            return None
        def ErrorDialog(self, message, title):
            return None
        def GetDisplayedForm(self, session_identifier):
            return None
        def GetInputValue(self, index):
            return None
        def InfoDialog(self, message, title):
            return None
        def OpenFileDialog(self, title, filter, default_extension):
            return None
        # @overload
        def OptionsDialog(self, title, inputs, input_area_width):
            return None
        # @overload
        def OptionsDialog(self, title, inputs, input_area_width, input_changed_callback, update_user_interface_callback):
            return None
        def QuestionDialog(self, question, title):
            return None
        def SaveFileDialog(self, title, filter, default_extension):
            return None
        def SelectFolderDialog(self, current_folder, description):
            return None
        def SetInputValue(self, index, value):
            return None
        def SetStringList(self, index, strings):
            return None
        # @overload
        def UtilityDialog(self, title, action_button_text, action_button_callback, input_changed_callback, inputs, input_area_width):
            return None
        # @overload
        def UtilityDialog(self, title, action_button_text, action_button_callback, input_changed_callback, inputs, input_area_width, update_user_interface_callback):
            return None

    class Bspline(_StubBase):
        pass
        ControlPoints = None
        IsReference = None
        KnotVectors = None
        Length = None
        Order = None
        Weights = None
        def __init__(self, value, list, list_2, list_3, value_2):
            return None
        def GetNormalAt(self, u):
            return None
        def GetPointAt(self, u):
            return None
        def GetX(self, u):
            return None
        def GetY(self, u):
            return None
        def Subdivide(self, segments):
            return None

    class Bspline3D(_StubBase):
        pass
        ControlPoints = None
        IsReference = None
        KnotVectors = None
        Length = None
        Order = None
        Weights = None
        def __init__(self, value, list, list_2, list_3, value_2):
            return None
        def GetNormalAt(self, u):
            return None
        def GetPointAt(self, u):
            return None
        def GetX(self, u):
            return None
        def GetY(self, u):
            return None
        def GetZ(self, u):
            return None
        def Subdivide(self, segments):
            return None
        def SubdivideGetNormals(self, segments):
            return None

    class CSharp(_StubBase):
        pass
        def __init__(self):
            return None
        def Compile(self, code):
            return None
        # @overload
        def CompileAndRun(self, code):
            return None
        # @overload
        def CompileAndRun(self, code, variables):
            return None
        # @overload
        def Run(self, script_script):
            return None
        # @overload
        def Run(self, script_script, variables):
            return None

    class Circle(_StubBase):
        pass
        Center = None
        CenterPoint = None
        IsReference = None
        Length = None
        Radius = None
        def __init__(self, list, value, value_2):
            return None

    class CircularArc(_StubBase):
        pass
        class ArcType:
            pass
    # Unconverted stub line:         pass
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
        # @overload
        def __init__(self, list, list_2, list_3, value):
            return None
        # @overload
        def __init__(self, list, list_2, value, value_2):
            return None

    class CircularArc3D(_StubBase):
        pass
        class ArcType:
            pass
    # Unconverted stub line:         pass
        Angle = None
        Center = None
        EndPoint = None
        IsReference = None
        Radius = None
        StartPoint = None
        Type = None
        # @overload
        def __init__(self, list, list_2, list_3, value):
            return None
        # @overload
        def __init__(self, list, list_2, value, value_2):
            return None

    class Configuration(_StubBase):
        pass
        IsActive = None
        Name = None
        def __init__(self):
            return None
        def Activate(self):
            return None
        def LockAll(self):
            return None
        def SetLocks(self, locks):
            return None
        def UnlockAll(self):
            return None

    class Ellipse(_StubBase):
        pass
        Center = None
        CenterPoint = None
        IsReference = None
        MajorAxisAngle = None
        MinorMajorRatio = None
        Radius = None
        def __init__(self, list, value, value_2, value_3, value_4):
            return None

    class EllipticalArc(_StubBase):
        pass
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
        def __init__(self, list, list_2, list_3, value, value_2, value_3, value_4):
            return None

    class GearSketch(_StubBase):
        pass
        CenterX = None
        CenterY = None
        DiametralPitch = None
        NumberofTeeth = None
        PitchDiameter = None
        PressureAngle = None
        def __init__(self):
            return None

    class GlobalParameters(_StubBase):
        pass
        Configurations = None
        Name = None
        Parameters = None
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def __init__(self, value):
            return None
        # @overload
        def __init__(self, value, value_2):
            return None
        # @overload
        def AddConfiguration(self, name):
            return None
        # @overload
        def AddConfiguration(self, name, base_configuration_name):
            return None
        # @overload
        def AddParameter(self, name, type, value):
            return None
        # @overload
        def AddParameter(self, name, type, equation):
            return None
        def Close(self):
            return None
        def GetActiveConfiguration(self):
            return None
        def GetConfiguration(self, name):
            return None
        def GetParameter(self, name):
            return None
        # @overload
        def Save(self):
            return None
        # @overload
        def Save(self, folder):
            return None
        def SaveAs(self, folder, new_name):
            return None

    class GuideCurveTypes(_StubBase):
        pass
    # Unconverted stub line:     """Type of guide curve"""
        Global = None
        Local = None
        def __init__(self):
            return None

    class IAxis(_StubBase):
        pass
        def __init__(self):
            return None
        def GetOccurrence(self):
            return None

    class IPlane(_StubBase):
        pass
        def __init__(self):
            return None
        def GetOccurrence(self):
            return None

    class IPoint(_StubBase):
        pass
        def __init__(self):
            return None
        def GetOccurrence(self):
            return None
        def PointObject(self):
            return None

    class Line(_StubBase):
        pass
        End = None
        EndPoint = None
        IsReference = None
        Length = None
        Start = None
        StartPoint = None
        def __init__(self, list, list_2, value):
            return None

    class Line3D(_StubBase):
        pass
        End = None
        EndPoint = None
        IsReference = None
        Length = None
        Start = None
        StartPoint = None
        def __init__(self, list, list_2, value):
            return None

    class LockTypes(_StubBase):
        pass
    # Unconverted stub line:     """Type of configuration lock"""
        SuppressNewFeatures = None
        LockColorProperties = None
        def __init__(self):
            return None

    class Material(_StubBase):
        pass
        ABS = None
        PLA = None
        def __init__(self):
            return None

    class Parameter(_StubBase):
        pass
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
        def __init__(self):
            return None
        def AttachToExcel(self, document, sheet, cell, units):
            return None

    class ParameterTypes(_StubBase):
        pass
    # Unconverted stub line:     """Type of parameter"""
        Distance = None
        Angle = None
        Count = None
        def __init__(self):
            return None

    class ParameterUnits(_StubBase):
        pass
    # Unconverted stub line:     """Units of parameters"""
        Unitless = None
        Millimeters = None
        Centimeters = None
        Inches = None
        Degrees = None
        def __init__(self):
            return None

    class Polyline(_StubBase):
        pass
        # @overload
        def __init__(self):
            return None
        # @overload
        def __init__(self, list):
            return None
        def AddArc(self, center, start, end, minimum_segments):
            return None
        def AddCircle(self, center_x, center_y, diameter, sides):
            return None
        def AddPoint(self, point):
            return None
        def AddPolyline(self, append_line):
            return None
        # @overload
        def Clone(self):
            return None
        # @overload
        def Clone(self, start_index, end_index):
            return None
        # @overload
        def FindIntersection(self, l1, l2):
            return None
        # @overload
        def FindIntersection(self, a1, a2, b1, b2):
            return None
        def FindIntersectionWithCircle(self, l1, circle_x, circle_y, radius):
            return None
        def InsertPoint(self, index, point):
            return None
        def IsPointOnLine(self, a1, a2, point, tolerance):
            return None
        def Join(self, append_line):
            return None
        def Offset(self, offset_x, offset_y):
            return None
        def RemoveDuplicates(self):
            return None
        def RotateZ(self, center_x, center_y, angle):
            return None
        def SplitAtPoint(self, split_point, tolerence):
            return None

    class Polyline3D(_StubBase):
        pass
        # @overload
        def __init__(self):
            return None
        # @overload
        def __init__(self, list):
            return None
        def AddPoint(self, point):
            return None
        def AddPolyline(self, append_line):
            return None
        # @overload
        def Clone(self):
            return None
        # @overload
        def Clone(self, start_index, end_index):
            return None
        def InsertPoint(self, index, point):
            return None
        def IsPointOnLine(self, a, b, p, tolerance):
            return None
        def Join(self, append_line):
            return None
        def Offset(self, offset_x, offset_y, offset_z):
            return None
        def RemoveDuplicates(self):
            return None
        def SplitAtPoint(self, split_point, tolerence):
            return None

    class PolylinePoint(_StubBase):
        pass
        X = None
        Y = None
        # @overload
        def __init__(self):
            return None
        # @overload
        def __init__(self, value, value_2):
            return None
        def Offset(self, x, y):
            return None
        def RotateZ(self, center_x, center_y, angle):
            return None
        def Scale(self, scale_origin_x, scale_origin_y, scale_factor):
            return None

    class PolylinePoint3D(_StubBase):
        pass
        X = None
        Y = None
        Z = None
        # @overload
        def __init__(self):
            return None
        # @overload
        def __init__(self, value, value_2, value_3):
            return None
        def Offset(self, x, y, z):
            return None
        def Scale(self, scale_origin_x, scale_origin_y, scale_origin_z, scale_factor):
            return None

    class SketchPoint(_StubBase):
        pass
        IsReference = None
        X = None
        Y = None
        def __init__(self, value, value_2, value_3):
            return None

    class SketchPoint3D(_StubBase):
        pass
        IsReference = None
        X = None
        Y = None
        Z = None
        def __init__(self, value, value_2, value_3, value_4):
            return None

    class ThreeD(_StubBase):
        pass
        def __init__(self):
            return None
        def GetPerpendicularVector(self, vector):
            return None
        def TransformPointUsingVectors(self, source_vector, destination_vector, point):
            return None

    class TwoD(_StubBase):
        pass
        def __init__(self):
            return None
        def GetPerpendicularVector(self, vector):
            return None
        def NormalizeVector(self, vector):
            return None
        def RotatePoint(self, point, angle):
            return None

    class UnitTypes(_StubBase):
        pass
    # Unconverted stub line:     """Supported units"""
        Millimeters = None
        Inches = None
        Centimeters = None
        def __init__(self):
            return None

    class Units(_StubBase):
        pass
        Current = None
        def __init__(self):
            return None

    class WindowsInputTypes(_StubBase):
        pass
    # Unconverted stub line:     """Type of Windows input"""
        Boolean = None
        Edge = None
        Face = None
        File = None
        Folder = None
        Image = None
        Integer = None
        Part = None
        Plane = None
        Real = None
        SaveFile = None
        Sketch = None
        Sketch3D = None
        String = None
        StringList = None
        def __init__(self):
            return None

    def CurrentPart():
        return None
    def CurrentAssembly():
        return None
    def CurrentParts():
        return None
    def CurrentAssemblies():
        return None

    def _stub_get_plane(self, name):
        return Plane()

    def _stub_get_axis(self, name):
        return Axis()

    def _stub_get_point(self, name):
        return Point()

    def _stub_get_configuration(self):
        return Configuration()

    def _stub_get_parameter(self, *args):
        return Parameter()

    def _stub_get_list(self):
        return []

    def _stub_get_bounding_box(self):
        return []

    def _stub_add_point(self, *args):
        return Point()

    def _stub_add_axis(self, *args):
        return Axis()

    def _stub_add_plane(self, *args):
        return Plane()

    def _stub_add_parameter(self, *args):
        return Parameter()

    def _stub_add_sketch(self, *args):
        return Sketch()

    def _stub_add_3d_sketch(self, *args):
        return Sketch3D()

    def _stub_sketch_point(self, *args):
        return SketchPoint()

    def _stub_sketch_figure(self, *args):
        return Feature()

    def _stub_sketch3d_point(self, *args):
        return SketchPoint3D()

    def _stub_sketch3d_figure(self, *args):
        return Feature()

    def _stub_init(self, *args, **kwargs):
        pass

    for _stub_type in (Part, Assembly, AssembledPart, AssembledSubAssembly, Sketch, Sketch3D, Plane, Axis, Point, Face, Edge, Vertex, Feature, Windows, Bspline, Bspline3D, CSharp, Circle, CircularArc, CircularArc3D, Configuration, Ellipse, EllipticalArc, GearSketch, GlobalParameters, GuideCurveTypes, IAxis, IPlane, IPoint, Line, Line3D, LockTypes, Material, Parameter, ParameterTypes, ParameterUnits, Polyline, Polyline3D, PolylinePoint, PolylinePoint3D, SketchPoint, SketchPoint3D, ThreeD, TwoD, UnitTypes, Units, WindowsInputTypes):
        _stub_type.__init__ = _stub_init

    Part.GetPlane = _stub_get_plane
    Part.GetAxis = _stub_get_axis
    Part.GetPoint = _stub_get_point
    Part.GetActiveConfiguration = _stub_get_configuration
    Part.GetParameter = _stub_get_parameter
    Part.GetEdges = _stub_get_list
    Part.GetFaces = _stub_get_list
    Part.GetVertices = _stub_get_list
    Part.GetBoundingBox = _stub_get_bounding_box
    Part.AddPoint = _stub_add_point
    Part.AddAxis = _stub_add_axis
    Part.AddPlane = _stub_add_plane
    Part.AddParameter = _stub_add_parameter
    Part.AddSketch = _stub_add_sketch
    Part.Add3DSketch = _stub_add_3d_sketch

    Assembly.GetPlane = _stub_get_plane
    Assembly.GetAxis = _stub_get_axis
    Assembly.GetPoint = _stub_get_point

    Sketch.AddPoint = _stub_sketch_point
    Sketch.AddLine = _stub_sketch_figure
    Sketch.AddCircle = _stub_sketch_figure
    Sketch.AddRectangle = _stub_sketch_figure
    Sketch3D.AddPoint = _stub_sketch3d_point
    Sketch3D.AddLine = _stub_sketch3d_figure
    Sketch3D.AddLines = _stub_sketch3d_figure
    Sketch3D.AddArcCenterStartEnd = _stub_sketch3d_figure
    Sketch3D.AddBspline = _stub_sketch3d_figure

    def CurrentPart():
        return Part()

    def CurrentAssembly():
        return Assembly()

    def CurrentParts():
        return [Part()]

    def CurrentAssemblies():
        return [Assembly()]

RUN_ON_LOAD = True
CREATE_TEST_GEOMETRY = True
RUN_PARAMETER_SHOWCASE_TEST = True
RUN_3D_SKETCH_TEST = True
RUN_3D_SKETCH_SIX_SCALAR_LINE_TEST = True

ALIBRE_SCRIPT_TYPE_NAMES = ('Part', 'Assembly', 'AssembledPart', 'AssembledSubAssembly', 'Sketch', 'Sketch3D', 'Plane', 'Axis', 'Point', 'Face', 'Edge', 'Vertex', 'Feature', 'Windows', 'Bspline', 'Bspline3D', 'CSharp', 'Circle', 'CircularArc', 'CircularArc3D', 'Configuration', 'Ellipse', 'EllipticalArc', 'GearSketch', 'GlobalParameters', 'GuideCurveTypes', 'IAxis', 'IPlane', 'IPoint', 'Line', 'Line3D', 'LockTypes', 'Material', 'Parameter', 'ParameterTypes', 'ParameterUnits', 'Polyline', 'Polyline3D', 'PolylinePoint', 'PolylinePoint3D', 'SketchPoint', 'SketchPoint3D', 'ThreeD', 'TwoD', 'UnitTypes', 'Units', 'WindowsInputTypes')
NESTED_TYPE_NAMES = ('Part.DirectionType', 'Part.EndCondition', 'Part.FileTypes', 'Assembly.ConstraintBoundsType', 'Sketch.Constraints', 'CircularArc.ArcType', 'CircularArc3D.ArcType')
COMMON_CONSTANT_PATHS = ('Part.DirectionType.Normal', 'Part.EndCondition.ToDepth', 'Part.EndCondition.ThroughAll', 'Part.EndCondition.MidPlane', 'Part.EndCondition.EntirePath', 'Part.FileTypes.GeomagicDesignPart', 'Part.FileTypes.AlibreDesignPart', 'Part.FileTypes.STEP', 'Part.FileTypes.IGES', 'Part.FileTypes.ThreeDM', 'Part.FileTypes.SAT', 'Part.FileTypes.STL_in', 'Part.FileTypes.STL_cm', 'Part.FileTypes.STL_mm', 'Part.Comment', 'Part.Configurations', 'Part.CostCenter', 'Part.CreatedBy', 'Part.CreatedDate', 'Part.CreatingApplication', 'Part.Density', 'Part.Description', 'Part.DocumentNumber', 'Part.EngineeringApprovalDate', 'Part.EngineeringApprovedBy', 'Part.EstimatedCost', 'Part.ExtendedMaterialInformation', 'Part.FileName', 'Part.Keywords', 'Part.LastAuthor', 'Part.LastUpdateDate', 'Part.ManufacturingApprovedBy', 'Part.ManufacturingApprovedDate', 'Part.Mass', 'Part.Material', 'Part.ModifiedInformation', 'Part.Name', 'Part.Number', 'Part.Origin', 'Part.Parameters', 'Part.Product', 'Part.ReceivedFrom', 'Part.Revision', 'Part.Selections', 'Part.StockSize', 'Part.Supplier', 'Part.Title', 'Part.Vendor', 'Part.WebLink', 'Part.XAxis', 'Part.XYPlane', 'Part.YAxis', 'Part.YZPlane', 'Part.ZAxis', 'Part.ZXPlane', 'Assembly.Comment', 'Assembly.Configurations', 'Assembly.CostCenter', 'Assembly.CreatedBy', 'Assembly.CreatedDate', 'Assembly.CreatingApplication', 'Assembly.Density', 'Assembly.Description', 'Assembly.DocumentNumber', 'Assembly.EngineeringApprovalDate', 'Assembly.EngineeringApprovedBy', 'Assembly.EstimatedCost', 'Assembly.ExtendedMaterialInformation', 'Assembly.FileName', 'Assembly.Keywords', 'Assembly.LastAuthor', 'Assembly.LastUpdateDate', 'Assembly.ManufacturingApprovedBy', 'Assembly.ManufacturingApprovedDate', 'Assembly.Material', 'Assembly.ModifiedInformation', 'Assembly.Name', 'Assembly.Number', 'Assembly.Origin', 'Assembly.Parameters', 'Assembly.Parts', 'Assembly.Product', 'Assembly.ReceivedFrom', 'Assembly.Revision', 'Assembly.Selections', 'Assembly.StockSize', 'Assembly.SubAssemblies', 'Assembly.Supplier', 'Assembly.Title', 'Assembly.Vendor', 'Assembly.WebLink', 'Assembly.XAxis', 'Assembly.XYPlane', 'Assembly.YAxis', 'Assembly.YZPlane', 'Assembly.ZAxis', 'Assembly.ZXPlane', 'AssembledPart.Configurations', 'AssembledPart.Name', 'AssembledSubAssembly.Configurations', 'AssembledSubAssembly.Name', 'Sketch.Constraints.Coincident', 'Sketch.Constraints.Collinear', 'Sketch.Constraints.Equal', 'Sketch.Constraints.Horizontal', 'Sketch.Constraints.Parallel', 'Sketch.Constraints.Perpendicular', 'Sketch.Constraints.Tangent', 'Sketch.Constraints.Vertical', 'Sketch.Figures', 'Sketch.Name', 'Sketch.Origin', 'Sketch3D.Figures', 'Sketch3D.Name', 'Plane.Name', 'Axis.Name', 'Point.Name', 'Point.X', 'Point.Y', 'Point.Z', 'Face.Name', 'Edge.Diameter', 'Edge.Length', 'Edge.Name', 'Vertex.Name', 'Vertex.X', 'Vertex.Y', 'Vertex.Z', 'Feature.Name', 'Bspline.ControlPoints', 'Bspline.IsReference', 'Bspline.KnotVectors', 'Bspline.Length', 'Bspline.Order', 'Bspline.Weights', 'Bspline3D.ControlPoints', 'Bspline3D.IsReference', 'Bspline3D.KnotVectors', 'Bspline3D.Length', 'Bspline3D.Order', 'Bspline3D.Weights', 'Circle.Center', 'Circle.CenterPoint', 'Circle.IsReference', 'Circle.Length', 'Circle.Radius', 'CircularArc.Angle', 'CircularArc.Center', 'CircularArc.CenterPoint', 'CircularArc.End', 'CircularArc.EndPoint', 'CircularArc.IsReference', 'CircularArc.Radius', 'CircularArc.Start', 'CircularArc.StartPoint', 'CircularArc.Type', 'CircularArc3D.Angle', 'CircularArc3D.Center', 'CircularArc3D.EndPoint', 'CircularArc3D.IsReference', 'CircularArc3D.Radius', 'CircularArc3D.StartPoint', 'CircularArc3D.Type', 'Configuration.IsActive', 'Configuration.Name', 'Ellipse.Center', 'Ellipse.CenterPoint', 'Ellipse.IsReference', 'Ellipse.MajorAxisAngle', 'Ellipse.MinorMajorRatio', 'Ellipse.Radius', 'EllipticalArc.Center', 'EllipticalArc.CenterPoint', 'EllipticalArc.End', 'EllipticalArc.EndPoint', 'EllipticalArc.IsReference', 'EllipticalArc.MajorAxisAngle', 'EllipticalArc.MinorMajorRatio', 'EllipticalArc.Radius', 'EllipticalArc.Start', 'EllipticalArc.StartPoint', 'GearSketch.CenterX', 'GearSketch.CenterY', 'GearSketch.DiametralPitch', 'GearSketch.NumberofTeeth', 'GearSketch.PitchDiameter', 'GearSketch.PressureAngle', 'GlobalParameters.Configurations', 'GlobalParameters.Name', 'GlobalParameters.Parameters', 'GuideCurveTypes.Global', 'GuideCurveTypes.Local', 'Line.End', 'Line.EndPoint', 'Line.IsReference', 'Line.Length', 'Line.Start', 'Line.StartPoint', 'Line3D.End', 'Line3D.EndPoint', 'Line3D.IsReference', 'Line3D.Length', 'Line3D.Start', 'Line3D.StartPoint', 'LockTypes.SuppressNewFeatures', 'LockTypes.LockColorProperties', 'Material.ABS', 'Material.PLA', 'Parameter.Comment', 'Parameter.Equation', 'Parameter.ExcelCell', 'Parameter.ExcelSheet', 'Parameter.ExcelWorkbook', 'Parameter.Name', 'Parameter.RawValue', 'Parameter.Type', 'Parameter.Units', 'Parameter.Value', 'ParameterTypes.Distance', 'ParameterTypes.Angle', 'ParameterTypes.Count', 'ParameterUnits.Unitless', 'ParameterUnits.Millimeters', 'ParameterUnits.Centimeters', 'ParameterUnits.Inches', 'ParameterUnits.Degrees', 'PolylinePoint.X', 'PolylinePoint.Y', 'PolylinePoint3D.X', 'PolylinePoint3D.Y', 'PolylinePoint3D.Z', 'SketchPoint.IsReference', 'SketchPoint.X', 'SketchPoint.Y', 'SketchPoint3D.IsReference', 'SketchPoint3D.X', 'SketchPoint3D.Y', 'SketchPoint3D.Z', 'UnitTypes.Millimeters', 'UnitTypes.Inches', 'UnitTypes.Centimeters', 'Units.Current', 'WindowsInputTypes.Boolean', 'WindowsInputTypes.Edge', 'WindowsInputTypes.Face', 'WindowsInputTypes.File', 'WindowsInputTypes.Folder', 'WindowsInputTypes.Image', 'WindowsInputTypes.Integer', 'WindowsInputTypes.Part', 'WindowsInputTypes.Plane', 'WindowsInputTypes.Real', 'WindowsInputTypes.SaveFile', 'WindowsInputTypes.Sketch', 'WindowsInputTypes.Sketch3D', 'WindowsInputTypes.String', 'WindowsInputTypes.StringList')
GLOBAL_VALUE_NAMES = ('ScriptFileName', 'ScriptFolder')
GLOBAL_FUNCTION_NAMES = (
    'CurrentPart',
    'CurrentAssembly',
    'CurrentParts',
    'CurrentAssemblies',
)

_MISSING = object()
_RESULT_COUNTS = {
    'error': 0,
    'miss': 0,
    'warn': 0,
    'skip': 0,
    'na': 0,
}

def _value_type_name(value):
    try:
        return type(value).__name__
    except Exception:
        return '<type unavailable>'

def _error_text(error):
    return error.__class__.__name__ + ': ' + str(error)

def _reset_result_counts():
    for key in _RESULT_COUNTS:
        _RESULT_COUNTS[key] = 0

def _status_prefix(status):
    return (status + '       ')[:7]

def _print_status(status, message):
    if status == 'ERROR':
        _RESULT_COUNTS['error'] += 1
    elif status == 'MISS':
        _RESULT_COUNTS['miss'] += 1
    elif status == 'WARN':
        _RESULT_COUNTS['warn'] += 1
    elif status == 'SKIP':
        _RESULT_COUNTS['skip'] += 1
    elif status == 'N/A':
        _RESULT_COUNTS['na'] += 1
    print(_status_prefix(status) + message)

def _global_value(name):
    return globals().get(name, _MISSING)

def _resolve_path(path):
    parts = path.split('.')
    value = _global_value(parts[0])
    if value is _MISSING:
        return _MISSING
    for part in parts[1:]:
        try:
            value = getattr(value, part)
        except Exception:
            return _MISSING
    return value

def _call_global(name):
    fn = _global_value(name)
    if fn is _MISSING:
        return False, 'missing global function', None
    try:
        return True, 'OK', fn()
    except Exception as error:
        return False, _error_text(error), None

def _call_method(obj, method_name, args):
    try:
        method = getattr(obj, method_name)
    except Exception as error:
        return False, 'missing method ' + method_name + ': ' + _error_text(error), None
    try:
        return True, 'OK', method(*args)
    except Exception as error:
        return False, _error_text(error), None

def _expected_workspace_mismatch(name, detail):
    lower = detail.lower()
    if name == 'CurrentAssembly' and 'not an assembly' in lower:
        return True
    if name == 'CurrentPart' and 'not a part' in lower:
        return True
    return False

def _print_section(title):
    print('')
    print('== ' + title + ' ==')

def _print_result(label, ok, detail, value):
    if ok:
        _print_status('OK', '{0} -> {1}'.format(label, _value_type_name(value)))
    else:
        _print_status('ERROR', '{0}: {1}'.format(label, detail))

def _report_paths(title, paths):
    found = 0
    missing = 0
    _print_section(title)
    for path in paths:
        value = _resolve_path(path)
        if value is _MISSING:
            missing += 1
            _print_status('MISS', path)
        else:
            found += 1
            _print_status('OK', '{0} -> {1}'.format(path, _value_type_name(value)))
    print('Summary: {0} found, {1} missing'.format(found, missing))

def _get_current_documents():
    documents = {}
    _print_section('Built-In Globals')
    for name in GLOBAL_VALUE_NAMES:
        value = _global_value(name)
        if value is _MISSING:
            _print_status('MISS', name)
        else:
            _print_status('OK', '{0} = {1}'.format(name, repr(value)))

    _print_section('Current Document Functions')
    for name in GLOBAL_FUNCTION_NAMES:
        ok, detail, value = _call_global(name)
        if not ok and _expected_workspace_mismatch(name, detail):
            _print_status('N/A', '{0}(): {1}'.format(name, detail))
            value = None
        else:
            _print_result(name + '()', ok, detail, value)
        documents[name] = value
    return documents

def _exercise_part_read_api(part):
    _print_section('CurrentPart Read API')
    calls = (
        ('GetPlane', ('XY-Plane',)),
        ('GetPlane', ('YZ-Plane',)),
        ('GetPlane', ('ZX-Plane',)),
        ('GetAxis', ('X-Axis',)),
        ('GetAxis', ('Y-Axis',)),
        ('GetAxis', ('Z-Axis',)),
        ('GetPoint', ('Origin',)),
        ('GetActiveConfiguration', ()),
        ('GetEdges', ()),
        ('GetFaces', ()),
        ('GetVertices', ()),
        ('GetBoundingBox', ()),
    )
    for method_name, args in calls:
        label = method_name + '(' + ', '.join([repr(arg) for arg in args]) + ')'
        ok, detail, value = _call_method(part, method_name, args)
        _print_result(label, ok, detail, value)

def _exercise_new_part_3d_sketch_api():
    _print_section('New Part 3D Sketch API')

    part_name = 'new3dSketch'
    sketch_name = 'My3DSketch'

    try:
        my_part = Part(part_name)
        _print_status('OK', "my_part = Part('{0}') -> {1}".format(part_name, _value_type_name(my_part)))
    except Exception as error:
        _print_status('ERROR', "my_part = Part('{0}'): {1}".format(part_name, _error_text(error)))
        return

    ok, detail, value = _call_method(my_part, 'Regenerate', ())
    if ok:
        _print_result("Part('{0}').Regenerate()".format(part_name), ok, detail, value)
    else:
        _print_status('WARN', "Part('{0}').Regenerate(): {1}".format(part_name, detail))

    ok, detail, sketch_3d = _call_method(my_part, 'Add3DSketch', (sketch_name,))
    _print_result("Part('{0}').Add3DSketch('{1}')".format(part_name, sketch_name), ok, detail, sketch_3d)
    if not ok or sketch_3d is None:
        _print_status('NOTE', "Expected call path: my_part = Part('new3dSketch'); sketch_3d = my_part.Add3DSketch('My3DSketch')")
        return

    bspline_points = [
        0.0, 10.0, 0.0,
        5.0, 15.0, 5.0,
        10.0, 15.0, 0.0,
        15.0, 20.0, 10.0,
    ]
    polyline_points = [
        20.0, 0.0, 0.0,
        25.0, 5.0, 5.0,
        30.0, 0.0, 10.0,
        35.0, 5.0, 15.0,
    ]

    showcase_calls = (
        ('Sketch3D.AddBspline', 'AddBspline', (bspline_points,)),
        ('Sketch3D.AddLine.list_points', 'AddLine', ([0.0, 0.0, 0.0], [10.0, 0.0, 5.0])),
        ('Sketch3D.AddArcCenterStartEnd', 'AddArcCenterStartEnd', (15.0, 0.0, 0.0, 10.0, 0.0, 5.0, 15.0, 5.0, 5.0)),
        ('Sketch3D.AddLines', 'AddLines', (polyline_points,)),
        ('Sketch3D.AddPoint', 'AddPoint', (25.0, 10.0, 5.0)),
    )
    for label, method_name, args in showcase_calls:
        ok, detail, value = _call_method(sketch_3d, method_name, args)
        _print_result(label, ok, detail, value)

    if RUN_3D_SKETCH_SIX_SCALAR_LINE_TEST:
        ok, detail, value = _call_method(sketch_3d, 'AddLine', (0.0, 0.0, 0.0, 10.0, 0.0, 10.0))
        _print_result('Sketch3D.AddLine.six_scalars', ok, detail, value)
    else:
        _print_status('SKIP', 'Sketch3D.AddLine.six_scalars: disabled by RUN_3D_SKETCH_SIX_SCALAR_LINE_TEST')

def _exercise_part_create_api(part):
    _print_section('CurrentPart Create API')
    ok, detail, xy_plane = _call_method(part, 'GetPlane', ('XY-Plane',))
    if not ok:
        _print_result('GetPlane("XY-Plane")', ok, detail, xy_plane)
        return

    tests = (
        ('AddPoint', ('ZZ_TypeTest_Point', [0.0, 0.0, 0.0])),
        ('AddAxis', ('ZZ_TypeTest_Axis', [0.0, 0.0, 0.0], [0.0, 0.0, 25.0])),
        ('AddPlane', ('ZZ_TypeTest_Plane', [0.0, 0.0, 1.0], [0.0, 0.0, 5.0])),
        ('AddSketch', ('ZZ_TypeTest_Sketch', xy_plane)),
    )

    created = {}
    for method_name, args in tests:
        if _MISSING in args:
            _print_status('SKIP', '{0}: missing enum/type argument'.format(method_name))
            continue
        ok, detail, value = _call_method(part, method_name, args)
        _print_result(method_name, ok, detail, value)
        created[method_name] = value

    sketch = created.get('AddSketch')
    if sketch is not None:
        for method_name, args in (
            ('AddPoint', (1.0, 1.0)),
            ('AddLine', (0.0, 0.0, 25.0, 0.0, False)),
            ('AddCircle', (10.0, 10.0, 5.0, False)),
            ('AddRectangle', (0.0, 0.0, 10.0, 5.0, False)),
        ):
            ok, detail, value = _call_method(sketch, method_name, args)
            _print_result('Sketch.' + method_name, ok, detail, value)

def _make_suffix():
    try:
        import time
        return str(int(time.time()))
    except Exception:
        return 'Manual'

def _exercise_parameter_showcase():
    _print_section('Parameter Showcase Transaction API')

    suffix = _make_suffix()
    part_name = 'ZZ_Parameter_Showcase_' + suffix

    try:
        param_part = Part(part_name)
    except Exception as error:
        _print_status('ERROR', 'Part({0!r}): {1}'.format(part_name, _error_text(error)))
        return

    tests = (
        ('Width', ('Width', ParameterTypes.Distance, 50.0)),
        ('Height', ('Height', ParameterTypes.Distance, ParameterUnits.Centimeters, 5.0)),
        ('Angle', ('Angle', ParameterTypes.Angle, 30.0)),
        ('EquationParam', ('EquationParam', ParameterTypes.Distance, 'Width/2')),
    )

    for label, args in tests:
        ok, detail, value = _call_method(param_part, 'AddParameter', args)
        _print_result('AddParameter.' + label, ok, detail, value)

    ok, detail, width_param = _call_method(param_part, 'GetParameter', ('Width',))
    _print_result('GetParameter.Width', ok, detail, width_param)
    if ok and width_param is not None:
        try:
            width_param.Value = 75.0
            _print_status('OK', 'Width.Value = 75.0')
        except Exception as error:
            _print_status('ERROR', 'Width.Value update: ' + _error_text(error))

    ok, detail, equation_param = _call_method(param_part, 'GetParameter', ('EquationParam',))
    _print_result('GetParameter.EquationParam', ok, detail, equation_param)
    if ok and equation_param is not None:
        try:
            equation_param.Equation = 'Height * 2'
            _print_status('OK', "EquationParam.Equation = 'Height * 2'")
        except Exception as error:
            _print_status('ERROR', 'EquationParam.Equation update: ' + _error_text(error))

    try:
        parameters = getattr(param_part, 'Parameters', None)
        if parameters is None:
            parameters = []
        count = len(parameters)
        _print_status('OK', 'Parameters count -> ' + str(count))
    except Exception as error:
        _print_status('ERROR', 'Parameters count: ' + _error_text(error))

def _exercise_assembly_read_api(assembly):
    _print_section('CurrentAssembly Read API')
    for method_name, args in (
        ('GetPlane', ('XY-Plane',)),
        ('GetPlane', ('YZ-Plane',)),
        ('GetPlane', ('ZX-Plane',)),
        ('GetAxis', ('X-Axis',)),
        ('GetAxis', ('Y-Axis',)),
        ('GetAxis', ('Z-Axis',)),
        ('GetPoint', ('Origin',)),
    ):
        label = method_name + '(' + ', '.join([repr(arg) for arg in args]) + ')'
        ok, detail, value = _call_method(assembly, method_name, args)
        _print_result(label, ok, detail, value)

def _print_verification_summary():
    _print_section('Verification Summary')
    print('Errors: ' + str(_RESULT_COUNTS['error']))
    print('Missing: ' + str(_RESULT_COUNTS['miss']))
    print('Warnings: ' + str(_RESULT_COUNTS['warn']))
    print('Skipped: ' + str(_RESULT_COUNTS['skip']))
    print('Not applicable: ' + str(_RESULT_COUNTS['na']))
    if _RESULT_COUNTS['error'] == 0 and _RESULT_COUNTS['miss'] == 0:
        print('RESULT PASS')
    else:
        print('RESULT FAIL')

def main():
    _reset_result_counts()
    print('Alibre Script all-types main() test')
    print('Self-contained fallback mocks: ' + str(not _RUNNING_IN_ALIBRE_SCRIPT))
    print('Create test geometry: ' + str(CREATE_TEST_GEOMETRY))
    print('Parameter showcase test: ' + str(RUN_PARAMETER_SHOWCASE_TEST))
    print('3D sketch test: ' + str(RUN_3D_SKETCH_TEST))
    print('3D sketch six-scalar line test: ' + str(RUN_3D_SKETCH_SIX_SCALAR_LINE_TEST))

    documents = _get_current_documents()
    _report_paths('Top-Level Types From __init__.pyi', ALIBRE_SCRIPT_TYPE_NAMES)
    _report_paths('Nested Types From __init__.pyi', NESTED_TYPE_NAMES)
    _report_paths('Constants And Fields From __init__.pyi', COMMON_CONSTANT_PATHS)

    part = documents.get('CurrentPart')
    if part is not None:
        _exercise_part_read_api(part)
        if CREATE_TEST_GEOMETRY:
            _exercise_part_create_api(part)
            if RUN_3D_SKETCH_TEST:
                _exercise_new_part_3d_sketch_api()
            else:
                print('')
                _print_status('SKIP', 'New Part 3D Sketch API: disabled by RUN_3D_SKETCH_TEST')

    if RUN_PARAMETER_SHOWCASE_TEST:
        _exercise_parameter_showcase()
    else:
        print('')
        _print_status('SKIP', 'Parameter showcase: disabled by RUN_PARAMETER_SHOWCASE_TEST')

    assembly = documents.get('CurrentAssembly')
    if assembly is not None:
        _exercise_assembly_read_api(assembly)

    _print_verification_summary()

    print('')
    print('main() complete')

if RUN_ON_LOAD:
    main()
