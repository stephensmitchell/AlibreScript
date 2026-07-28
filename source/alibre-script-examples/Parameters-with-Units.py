#https://help.alibre.com/articles/#!alibre-help-v23/parameters-with-units
# this script uses inches for it's units
Units.Current = UnitTypes.Inches
MyPart = Part('Foo')
# create parameter using current script units
LengthParam = MyPart.AddParameter('Length', ParameterTypes.Distance, 123.4)
# parameter value reads back in current script units
print 'Value in script units =', LengthParam.Value
# cteate parameter in degrees
RotationParam = MyPart.AddParameter('Rotation', ParameterTypes.Angle, 34.2)
# parameter reads back in degrees
print 'Value in degrees = ', RotationParam.Value
# create parameter with specific units
WidthParam = MyPart.AddParameter('Width', ParameterTypes.Distance, ParameterUnits.Centimeters, 7.32)
# reads back in current script units
print 'Value in script units = ', WidthParam.Value
# reads back the actual value we wrote
print 'Value we wrote = ', WidthParam.RawValue
# create parameter with specific units
WidthParam2 = MyPart.AddParameter('Width2', ParameterTypes.Distance, ParameterUnits.Inches, 1.0)
# reads back in current script units
print 'Value in script units = ', WidthParam2.Value
# reads back the actual value we wrote
print 'Value we wrote = ', WidthParam2.RawValue
# create parameter with no units
Count = MyPart.AddParameter('Count', ParameterTypes.Count, ParameterUnits.Unitless, 45)
# reads back value
print 'Count value = ', Count.Value
