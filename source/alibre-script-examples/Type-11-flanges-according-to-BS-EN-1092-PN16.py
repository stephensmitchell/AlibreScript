#https://help.alibre.com/articles/#!alibre-help-v23/type-11-flanges-according-to-bs-en-1092-pn16
from math import cos,sin,radians
# Size of Flange TYPE 11 According to BS/EN-1092 PN16
#--- INPUT HERE ---#
print('Input DN Flange size: 10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600')
DN = int(Read())
#--- INPUT STOP ---#
# Measurements table D,C2,H2,H3,R,A,N1,d1,f1,K,L,N from here
#http://www.roymech.co.uk/Useful_Tables/Flanges/BSEN1092_16_Dimensions.html
DNData = {}
DNData[10] = [90,14,35,6,4,17.2,28,40,2,60,14,4]
DNData[15] = [95,14,35,6,4,21.3,32,45,2,65,14,4]
DNData[20] = [105,14,38,6,4,26.9,39,58,2,75,14,4]
DNData[25] = [115,16,38,6,4,33.7,46,68,2,85,14,4]
DNData[32] = [140,16,40,6,6,42.4,56,78,2,100,18,4]
DNData[40] = [150,16,42,7,6,48.3,64,88,2,110,18,4]
DNData[50] = [165,18,45,8,6,60.3,75,102,2,125,18,4]
DNData[65] = [185,18,45,10,6,76.1,90,122,2,145,18,4]
DNData[80] = [200,20,50,10,8,88.9,105,138,2,160,18,8]
DNData[100] = [220,20,52,12,8,114.3,131,158,2,180,18,8]
DNData[125] = [250,22,55,12,8,139.7,156,188,2,210,18,8]
DNData[150] = [285,22,55,12,10,168.3,192,212,2,240,22,8]
DNData[200] = [340,24,62,16,10,219.1,235,268,2,295,22,12]
DNData[250] = [405,26,70,16,12,273,292,320,2,355,26,12]
DNData[300] = [460,28,78,16,12,323.9,344,378,2,410,26,12]
DNData[350] = [520,30,82,16,12,355.6,390,438,2,470,26,16]
DNData[400] = [580,32,85,16,12,406.4,445,490,2,525,30,16]
DNData[450] = [640,40,87,16,12,457,490,550,2,585,30,20]
DNData[500] = [715,44,90,16,12,508,548,610,2,650,33,20]
DNData[600] = [840,54,95,18,12,610,652,725,2,770,36,20]
DNData[700] = [910,36,100,18,12,711,755,795,2,840,36,24]
DNData[800] = [1025,38,105,20,12,813,855,900,2,950,39,24]
DNData[900] = [1125,40,110,20,12,914,955,1000,2,1050,39,28]
DNData[1000] = [1255,42,120,22,16,1016,1058,1115,2,1170,42,28]
DNData[1200] = [1485,48,130,30,16,1219,1262,1330,2,1390,48,32]
DNData[1400] = [1685,52,145,30,16,1420,1465,1530,2,1590,48,36]
DNData[1600] = [1930,58,160,35,16,1620,1668,1750,2,1820,56,40]
D = DNData[DN][0]
C2 = DNData[DN][1]
H2 = DNData[DN][2]
H3 = DNData[DN][3]
R = DNData[DN][4]
A = DNData[DN][5]
N1 = DNData[DN][6]
d1 = DNData[DN][7]
f1 = DNData[DN][8]
K = DNData[DN][9]
L = DNData[DN][10]
N = DNData[DN][11]
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
# Create part
Flange = Part('DN%d Flange PN16' % (DN))
# body
Profile = Flange.AddSketch('Profile', Flange.GetPlane('XY-Plane'))
Line = Polyline()
Line.AddPoint(PolylinePoint(DN/2.,0))
Line.AddPoint(PolylinePoint(d1/2.,0))
Line.AddPoint(PolylinePoint(d1/2.,f1))
Line.AddPoint(PolylinePoint(D/2.,f1))
Line.AddPoint(PolylinePoint(D/2.,C2))
Line.AddPoint(PolylinePoint(N1/2.,C2))
Line.AddPoint(PolylinePoint(A/2.,H2-H3))
Line.AddPoint(PolylinePoint(A/2.,H2))
Line.AddPoint(PolylinePoint(DN/2.,H2))
Line.AddPoint(PolylinePoint(DN/2.,0))
Profile.AddPolyline(Line,False)
Flange.AddRevolveBoss('Body', Profile, Flange.GetAxis('Y-Axis'),360)
#Chamfer
Flange.AddChamfer('Chamfer<1>',Flange.GetFace('Face<2>'),1,False)
#Fillet
Flange.AddFillet('Fillet<1>',[Flange.GetEdge('Edge<6>'),Flange.GetEdge('Edge<7>')],R,False)
# Hole
Hole = Flange.AddSketch('Hole',Flange.GetFace('Face<8>'))
for i in xrange(N):
    Ang = (360/N)*i
    Hole.AddCircle(sin(radians(Ang))*K/2.,cos(radians(Ang))*K/2.,L,False)
Flange.AddExtrudeCut('Flange Hole',Hole,C2,True)
