import sys
import math
# Assuming Windows, WindowsInputTypes, and CurrentPart are predefined in your environment
Win = Windows()
Options = []
Options.append(['Radius', WindowsInputTypes.Real, 10.0])
Options.append(['Pitch', WindowsInputTypes.Real, 5.0])
Options.append(['Total Turns', WindowsInputTypes.Integer, 10])
Options.append(['Angle Increment', WindowsInputTypes.Real, 0.1])
Options.append(['Segment Angle', WindowsInputTypes.Integer, 30])  # Option for segment angle
Values = Win.OptionsDialog('Helix Parameters', Options)
if Values is None:
    sys.exit('User cancelled')
Radius = Values[0]
Pitch = Values[1]
TotalTurns = Values[2]
AngleIncrement = Values[3]
SegmentAngle = Values[4]  # Angle for each segment
print('Radius = %f' % Radius)
print('Pitch = %f' % Pitch)
print('Total Turns = %d' % TotalTurns)
print('Angle Increment = %f' % AngleIncrement)
print('Segment Angle = %d' % SegmentAngle)
# Calculate the total number of segments based on total turns and segment angle
Segments = int((TotalTurns * 360) / SegmentAngle)
for Segment in range(Segments):
    Points = []
    # Calculate the start and end angles for the current segment in radians
    StartAngle = Segment * SegmentAngle * (math.pi / 180.0)
    EndAngle = StartAngle + (SegmentAngle * (math.pi / 180.0))
    # Adjust the starting Z coordinate based on the segment's position in the overall helix
    StartZ = Pitch * (StartAngle / (2 * math.pi))
    Angle = StartAngle
    while Angle < EndAngle:
        X = Radius * math.cos(Angle)
        Y = Radius * math.sin(Angle)
        # Calculate Z using the adjusted start Z for the segment and the angle's progression
        Z = StartZ + Pitch * ((Angle - StartAngle) / (2 * math.pi))
        Points.extend([X, Y, Z])
        Angle += AngleIncrement * (math.pi / 180.0)  # Convert angle increment to radians for consistent progression
    # Assuming CurrentPart() and Add3DSketch are part of your CAD API
    Helix = CurrentPart()
    PathName = 'Path_Segment_%d' % (Segment + 1)
    Path = Helix.Add3DSketch(PathName)
    Path.AddBspline(Points)
