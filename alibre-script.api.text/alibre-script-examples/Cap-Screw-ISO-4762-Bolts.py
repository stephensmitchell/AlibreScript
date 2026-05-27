#https://help.alibre.com/articles/#!alibre-help-v23/cap-screw-iso-4762-bolts
# Creates a metric socket cap screw using ISO 4762
# See: http://practicalmaintenance.wordpress.com/2009/01/30/socket-head-cap-screws-article-13/
# Size of screw
Diameter = 3.0
Length = 30.0
# Measurements table containing H, F, E, T, C from web page
MetricData = {}
MetricData[1.6]  = [3.14,  2.0,  1.73,  0.7, 0.16]
MetricData[2.0]  = [3.98,  2.6,  1.73,  1.0, 0.2]
MetricData[2.5]  = [4.68,  3.1,  2.3,   1.1, 0.25]
MetricData[3.0]  = [5.68,  3.6,  2.87,  1.3, 0.3]
MetricData[4.0]  = [7.22,  4.7,  3.44,  2.0, 0.4]
MetricData[5.0]  = [8.72,  5.7,  4.58,  2.5, 0.5]
MetricData[6.0]  = [10.22, 6.8,  5.72,  3.0, 0.6]
MetricData[8.0]  = [13.27, 9.2,  6.86,  4.0, 0.8]
MetricData[10.0] = [16.27, 11.2, 9.15,  5.0, 1.0]
MetricData[12.0] = [18.27, 13.7, 11.43, 6.0, 1.2]
MetricData[16.0] = [24.33, 17.7, 16.0,  8.0, 1.6]
MetricData[20.0] = [30.33, 22.4, 19.44, 10.0, 2.0]
MetricData[24.0] = [36.39, 26.4, 21.73, 12.0, 2.4]
MetricData[30.0] = [45.39, 33.4, 25.15, 15.5, 3.0]
MetricData[36.0] = [54.46, 39.4, 30.85, 19.0, 3.6]
MetricData[42.0] = [63.46, 45.6, 36.57, 24.0, 4.2]
MetricData[48.0] = [72.46, 52.6, 41.13, 28.0, 4.8]
MetricData[56.0] = [84.54, 63.0, 46.83, 34.0, 5.6]
MetricData[64.0] = [96.54, 71.0, 52.53, 38.0, 6.4]
CapDiameter = MetricData[Diameter][0]
FilletTransitionDiameter = MetricData[Diameter][1]
HexHoleDiameter = MetricData[Diameter][2]
HexHoleDepth = MetricData[Diameter][3]
RimFilletRadius = MetricData[Diameter][4]
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
# Create part
Screw = Part('Cap Screw M%dx%d' % (Diameter, Length))
# body
Profile = Screw.AddSketch('Profile', Screw.GetPlane('XY-Plane'))
Line = Polyline()
Line.AddPoint(PolylinePoint(0, 0))
Line.AddPoint(PolylinePoint(0, CapDiameter / 2))
Line.AddPoint(PolylinePoint(Diameter, CapDiameter / 2))
Line.AddPoint(PolylinePoint(Diameter, Diameter / 2))
Line.AddPoint(PolylinePoint(Diameter + Length, Diameter / 2))
Line.AddPoint(PolylinePoint(Diameter + Length, 0))
Line.AddPoint(PolylinePoint(0, 0))
Profile.AddPolyline(Line, False)
Screw.AddRevolveBoss('Body', Profile, Screw.GetAxis('X-Axis'), 360)
# hex hole
HexHole = Screw.AddSketch('Hole', Screw.GetFace('Face<5>'))
HexHole.AddPolygon(0, 0, HexHoleDiameter, 6, False)
Screw.AddExtrudeCut('Hex Hole', HexHole, HexHoleDepth + ((FilletTransitionDiameter - Diameter) / 2.0), True)
# fillet from cap to shaft
Screw.AddFillet('Cap Joint', Screw.GetEdge('Edge<21>'), (FilletTransitionDiameter - Diameter) / 2.0, False)
# fillet at bottom of hex hole
Screw.AddFillet('Hex Hole Bottom', [Screw.GetEdge('Edge<5>'), Screw.GetEdge('Edge<9>'), Screw.GetEdge('Edge<12>'), Screw.GetEdge('Edge<21>'), Screw.GetEdge('Edge<18>'), Screw.GetEdge('Edge<15>')], (FilletTransitionDiameter - Diameter) / 2.0, False)
# fillet on rim
Screw.AddFillet('Cap Rim', Screw.GetEdge('Edge<35>'), RimFilletRadius, False)
