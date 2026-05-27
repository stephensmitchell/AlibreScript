#https://help.alibre.com/articles/#!alibre-help-v23/geodesic-dome-reference-geometry
# tessellates a sphere into triangles and generates a reference point at each vertex
# adapted from
# http://musingsofninjarat.wordpress.com/spheres-through-triangle-tessellation/
from math import *
A = 0.525731112119133606
B = 0.850650808352039932
icosa_indices = [0 for x in xrange(20)]
icosa_indices[0]  = [0,4,1]
icosa_indices[1]  = [0,9,4]
icosa_indices[2]  = [9,5,4]
icosa_indices[3]  = [4,5,8]
icosa_indices[4]  = [4,8,1]
icosa_indices[5]  = [8,10,1]
icosa_indices[6]  = [8,3,10]
icosa_indices[7]  = [5,3,8]
icosa_indices[8]  = [5,2,3]
icosa_indices[9]  = [2,7,3]
icosa_indices[10] = [7,10,3]
icosa_indices[11] = [7,6,10]
icosa_indices[12] = [7,11,6]
icosa_indices[13] = [11,0,6]
icosa_indices[14] = [0,1,6]
icosa_indices[15] = [6,1,10]
icosa_indices[16] = [9,0,11]
icosa_indices[17] = [9,11,2]
icosa_indices[18] = [9,2,5]
icosa_indices[19] = [7,2,11]
icosa_verts = [0 for x in xrange(12)]
icosa_verts[0]  = [A,0.0,-B]
icosa_verts[1]  = [-A,0.0,-B]
icosa_verts[2]  = [A,0.0,B]
icosa_verts[3]  = [-A,0.0,B]
icosa_verts[4]  = [0.0,-B,-A]
icosa_verts[5]  = [0.0,-B,A]
icosa_verts[6]  = [0.0,B,-A]
icosa_verts[7]  = [0.0,B,A]
icosa_verts[8]  = [-B,-A,0.0]
icosa_verts[9]  = [B,-A,0.0]
icosa_verts[10] = [-B,A,0.0]
icosa_verts[11] = [B,A,0.0]
def normalize_vert(a):
  d = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
  a[0] = a[0] / d
  a[1] = a[1] / d
  a[2] = a[2] / d
  return a
def draw_recursive_tri(a, b, c, div, r, vertices):
  if div == 0:
    v1 = (a[0]*r, a[1]*r, a[2]*r)
    v2 = (b[0]*r, b[1]*r, b[2]*r)
    v3 = (c[0]*r, c[1]*r, c[2]*r)
    vertices.add(v1)
    vertices.add(v2)
    vertices.add(v3)
  else:
    ab = [0, 0, 0]
    ac = [0, 0, 0]
    bc = [0, 0, 0]
    for i in range(0, 3):
      ab[i] = (a[i] + b[i]) / 2.0
      ac[i] = (a[i] + c[i]) / 2.0
      bc[i] = (b[i] + c[i]) / 2.0
    ab = normalize_vert(ab)
    ac = normalize_vert(ac)
    bc = normalize_vert(bc)
    draw_recursive_tri(a, ab, ac, div - 1, r, vertices)
    draw_recursive_tri(b, bc, ab, div - 1, r, vertices)
    draw_recursive_tri(c, ac, bc, div - 1, r, vertices)
    draw_recursive_tri(ab, bc, ac, div - 1, r, vertices)
# calculates the triangle vertices for a given sphere and level of detail
def calculate_sphere(detail, radius):
  # we use a set because each vertex must be unique and sets can only contain unique values
  vertices = set()
  for i in range(0, 20):
    draw_recursive_tri(icosa_verts[icosa_indices[i][0]], icosa_verts[icosa_indices[i][1]], icosa_verts[icosa_indices[i][2]], detail, radius, vertices);
  return vertices
# use a low level of detail - increasing this value drastically increases the number of triangles
# warning - must be zero or a positive integer
Detail = 1
# radius of sphere in millimeters
Radius = 10
# generate a set of triangle vertices
Vertices = calculate_sphere(Detail, Radius)
# create a new part
MyPart = Part('Geodesic Sphere')
# add the reference points to the part
Number = 0
for Vertex in Vertices:
  MyPart.AddPoint('Geodesic ' + str(Number), Vertex[0], Vertex[1], Vertex[2])
  Number = Number + 1
