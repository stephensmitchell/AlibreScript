import math

from math import pi, sin, cos, radians

# Prompt user for blade parameters

Win = Windows()

Options = []

Options.append(['Number of Blades', WindowsInputTypes.Integer, 3])

Options.append(['Radius Start (mm)', WindowsInputTypes.Real, 100.0])

Options.append(['Radius End (mm)', WindowsInputTypes.Real, 10.0])

Options.append(['Blade Height Increment (mm)', WindowsInputTypes.Real, 50])

Options.append(['Points per Blade', WindowsInputTypes.Integer, 200])


# Display the dialog and get values

Values = Win.OptionsDialog('Fibonacci Propeller Blade Generator', Options)

if Values is None:

    sys.exit("Operation canceled by the user.")


# Extract the values

num_blades = Values[0]

radius_start = Values[1]

radius_end = Values[2]

height_increment = Values[3]

points_per_blade = Values[4]



# Constants

golden_angle = radians(137.5)  # Golden angle in radians

radius_step = (radius_end - radius_start) / points_per_blade



PropellerPart = CurrentPart()



# Loop through each blade

for blade in range(num_blades):

    angle_offset = golden_angle * blade  # Offset each blade by the golden angle

    Points = []

    

    # Generate points for the blade

    for i in range(points_per_blade + 1):

        angle = i * (2 * pi / points_per_blade) + angle_offset

        radius = radius_start + i * radius_step

        x = radius * cos(angle)

        y = radius * sin(angle)

        z = i * (height_increment / points_per_blade)

        Points.extend([x, y, z])

    

    # Add the blade spline to the 3D sketch

    BladeSketch = PropellerPart.Add3DSketch('Blade_' + str(blade + 1))

    BladeSketch.AddBspline(Points)



Win.InfoDialog('Done.',"Fibonacci Propeller Blade Generator")
