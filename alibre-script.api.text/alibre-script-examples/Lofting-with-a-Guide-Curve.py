#https://help.alibre.com/articles/#!alibre-help-v23/lofting-with-a-guide-curve
# create part
P = Part('foo')
# create sketch for bottom of loft
Bottom = P.AddSketch('Bottom', P.GetPlane('XY-Plane'))
Bottom.AddRectangle(0, 0, 10, 10, False)
# create sketch for top of loft
TopPlane = P.AddPlane('Top Plane', P.GetPlane('XY-Plane'), 30)
Top = P.AddSketch('Top', TopPlane)
Top.AddRectangle(0, 0, 50, 50, False)
# create guide curve
Guide = P.Add3DSketch('Guide')
Guide.AddBspline([10,10,0, 20,20,5, 45,45,15, 50,50,30])
# create loft using guide curve
P.AddLoftBoss('Loft Test', [Bottom, Top], [Guide], GuideCurveTypes.Global, True, False, False, False)