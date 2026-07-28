import math
from AlibreScript import *
# Initialize the part session
part = CurrentPart()
# Assuming you have a part with an edge to chamfer.
# The edge can be obtained in various ways, depending on the context.
# Here's a generic way to get an edge, replace this with your specific method.
edges = part.GetEdges()
edge_to_chamfer = edges[0]  # Assuming you want to chamfer the first edge in the list
# Define chamfer parameters
distance1 = 1  # The first chamfer distance
distance2 = 1  # The second chamfer distance (for unequal chamfer, otherwise set same as distance1)
# Add chamfer to the selected edge
part.AddChamfer("ChamferName", edge_to_chamfer, distance1, distance2, False)
# Regenerate the part to update the view
part.Regenerate()