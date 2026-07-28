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
