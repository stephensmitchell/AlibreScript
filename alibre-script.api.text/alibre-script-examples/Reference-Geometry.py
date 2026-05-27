#https://help.alibre.com/articles/#!alibre-help-v23/default-reference-geometry
# create a new part
P = Part("Test")
# access reference geometry
print P.XYPlane
print P.YZPlane
print P.ZXPlane
print P.XAxis
print P.YAxis
print P.ZAxis
print P.Origin
