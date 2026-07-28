#https://help.alibre.com/articles/#!alibre-help-v23/scaling-a-sketch
Units.Current = UnitTypes.Inches
TestRoom = Part('TEST ROOM Scaled', False)
OriginalSketch = TestRoom.GetSketch('Sketch<1>')
# currently 8.25' wide, need it to be 4.125'
ScaleFactor = 4.125 / 8.25 * 100.0
ScaledSketch = TestRoom.AddSketch('Scaled', TestRoom.GetFace('Face<6>'))
ScaledSketch.CopyFrom(OriginalSketch, 0, 0, 0, 8.25, 0, 0, 0, ScaleFactor)