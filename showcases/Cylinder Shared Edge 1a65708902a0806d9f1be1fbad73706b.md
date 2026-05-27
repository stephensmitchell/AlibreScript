# Cylinder Shared Edge

ID: A7246742B-27
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: February 25, 2025 9:51 PM
AI summary: Python function to find a shared edge between two faces in a 3D model using Alibre Script and IronPython, returning the edge if found or indicating none exists.

```python
def GetSharedEdge(FaceA, FaceB):
    EdgesA = FaceA.GetEdges()
    EdgesB = FaceB.GetEdges()

    for EdgeA in EdgesA:
        for EdgeB in EdgesB:

            VerticesA = EdgeA.GetVertices()
            VerticesB = EdgeB.GetVertices()

            VerticesASet = {(v.X, v.Y, v.Z) for v in VerticesA}
            VerticesBSet = {(v.X, v.Y, v.Z) for v in VerticesB}

            if VerticesASet == VerticesBSet:
                return EdgeA

    return None
P = CurrentPart()

Face1 = P.GetFace("Face<1>")
Face2 = P.GetFace("Face<2>")

SharedEdge = GetSharedEdge(Face1, Face2)

if SharedEdge:
    print("Shared Edge Found:", SharedEdge.Name)
else:
    print("No shared edge between the faces.")
```