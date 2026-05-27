#https://help.alibre.com/articles/#!alibre-help-v23/creating-a-3d-sketch-with-a-spline-and-an-arc
Units.Current = UnitTypes.Inches
P = Part('My Part')
# create 3d spline from a set of interpolation points
Path = P.Add3DSketch('Path')
Points = [0.6, -0.6625, 0.0]
Points.extend([0.6, -0.6625, -0.2175])
Points.extend([0.6, -0.8125, -0.6795])
Path.AddBspline(Points)
# arcs are counter clockwise, so to get a clockwise arc the start and end points are swapped
Path.AddArcCenterStartEnd(-5.6634, -3.92, -0.6795, 0.6, -7.0275, -0.6795, 0.6, -0.8125, -0.6795)