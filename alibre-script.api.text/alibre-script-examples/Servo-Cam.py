#https://help.alibre.com/articles/#!alibre-help-v23/servo-cam
majorwidth  = 13.763
minorwidth  = 6.260
height      = 7.000
slotwidth   = 3.000
baseheight  = 2.000
servoheight = 4.000
servoinside = 4.200
GripperCam = Part('GripperCam')
Base = GripperCam.AddSketch('Base', GripperCam.GetPlane('XY-Plane'))
Base.AddLine([-majorwidth / 2, -height / 2], [majorwidth / 2, -height / 2], False)
Base.AddLine([-majorwidth / 2,  height / 2], [majorwidth / 2,  height / 2], False)
Base.AddArcCenterStartEnd( majorwidth / 2, 0,  majorwidth / 2, -height / 2,  majorwidth / 2,  height / 2, False)
Base.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  height / 2, -majorwidth / 2, -height / 2, False)
Base.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
Base.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
Base.AddArcCenterStartEnd(majorwidth / 2, 0, majorwidth / 2, -slotwidth / 2, majorwidth / 2,  slotwidth / 2, False)
Base.AddArcCenterStartEnd(minorwidth / 2, 0, minorwidth / 2,  slotwidth / 2, minorwidth / 2, -slotwidth / 2, False)
Base.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
Base.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
Base.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  slotwidth / 2, -majorwidth / 2, -slotwidth / 2, False)
Base.AddArcCenterStartEnd(-minorwidth / 2, 0, -minorwidth / 2, -slotwidth / 2, -minorwidth / 2,  slotwidth / 2, False)
GripperCam.AddExtrudeBoss('Base', Base, baseheight, False)
Servo = GripperCam.AddSketch('Servo', GripperCam.GetFace('Face<13>'))
Servo.AddCircle(0, 0, 9, False)
Servo.AddCircle(0, 0, servoinside, False)
GripperCam.AddExtrudeBoss('Servo', Servo, servoheight, False)
Holes = GripperCam.AddSketch('Holes', GripperCam.GetPlane('XY-Plane'))
Holes.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
Holes.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
Holes.AddArcCenterStartEnd(majorwidth / 2, 0, majorwidth / 2, -slotwidth / 2, majorwidth / 2,  slotwidth / 2, False)
Holes.AddArcCenterStartEnd(minorwidth / 2, 0, minorwidth / 2,  slotwidth / 2, minorwidth / 2, -slotwidth / 2, False)
Holes.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
Holes.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
Holes.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  slotwidth / 2, -majorwidth / 2, -slotwidth / 2, False)
Holes.AddArcCenterStartEnd(-minorwidth / 2, 0, -minorwidth / 2, -slotwidth / 2, -minorwidth / 2,  slotwidth / 2, False)
GripperCam.AddExtrudeCut('Holes', Holes, baseheight + servoheight, False)