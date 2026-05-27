# python-headaches-with-decimals-and-alibre-lofting-error

ID: A7246742B-30
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Research
Reviewed: No
Created time: April 14, 2025 6:58 PM
AI summary: Python script for processing 3D point data from a TXT file, creating multiple splines, and generating reference points and planes in Alibre using IronPython. Includes functions for reading input, defining point ranges, and adding sketches to the current part.

```python
import fpformat
Win = Windows()
CurrentPart = CurrentPart()

txtfile = Win.OpenFileDialog('Select 3D Pojnts in TXT,mm',
                             'TXT files(*.*)|*.txt*',
                             '.txt')
f = open(txtfile, 'r')
datareader2 = f.read()
f.close()

data_into_list = datareader2.replace('\n', ',').split(",")
Points_Full = data_into_list

print 'Input Number of Guide Curves (typ - 10), then press ENTER'
NumberOfSections = int(Read())

length = (len(Points_Full) // (NumberOfSections * 3))
print(length)

# Break with While Loop
# Point Ranges
Points_1_range  = range(0,           (length*3))
Points_2_range  = range(length*3,    (3*2*length))
Points_3_range  = range(3*2*length, (3*3*length))
Points_4_range  = range(3*3*length, (3*4*length))
Points_5_range  = range(3*4*length, (3*5*length))
Points_6_range  = range(3*5*length, (3*6*length))
Points_7_range  = range(3*6*length, (3*7*length))
Points_8_range  = range(3*7*length, (3*8*length))
Points_9_range  = range(3*8*length, (3*9*length))
Points_10_range = range(3*9*length, (3*10*length))

# Convert to floats directly
Points_1  = [float(Points_Full[w])   for w in Points_1_range]
Points_2  = [float(Points_Full[ww])  for ww in Points_2_range]
Points_3  = [float(Points_Full[www]) for www in Points_3_range]
Points_4  = [float(Points_Full[xxxx]) for xxxx in Points_4_range]
Points_5  = [float(Points_Full[xxxxx]) for xxxxx in Points_5_range]
Points_6  = [float(Points_Full[xxxxxx]) for xxxxxx in Points_6_range]
Points_7  = [float(Points_Full[xxxxxxx]) for xxxxxxx in Points_7_range]
Points_8  = [float(Points_Full[xxxxxxxx]) for xxxxxxxx in Points_8_range]
Points_9  = [float(Points_Full[xxxxxxxxx]) for xxxxxxxxx in Points_9_range]
Points_10 = [float(Points_Full[xxxxxxxxxx]) for xxxxxxxxxx in Points_10_range]

cycle = range(length)

###############################################################################
# Helper function: "fix to 4 decimals, then back to float"
# If you don't need the decimal trimming, you can skip fpformat.fix(...) entirely.
###############################################################################
def to_float4(value):
    # Convert 'value' to a string with 4 decimals, then back to float
    return float(fpformat.fix(value, 4))

###############################################################################
# 1st Spline
###############################################################################
Path1 = CurrentPart.Add3DSketch('Spline1')
Points1 = []
for i in cycle:
    ix = i*3
    X11 = to_float4(Points_1[ix])
    Y11 = to_float4(Points_1[ix+1])
    Z11 = to_float4(Points_1[ix+2])
    Points1.extend([X11, Y11, Z11])

Path1.AddBspline(Points1)

# sample points for planes or references
SP1  = [Points1[0],   Points1[1],   Points1[2]]
SP11 = [Points1[150], Points1[151], Points1[152]]
SP21 = [Points1[300], Points1[301], Points1[302]]

CurrentPart.AddPoint('SP1',  SP1[0],  SP1[1],  SP1[2])
CurrentPart.AddPoint('SP11', SP11[0], SP11[1], SP11[2])
CurrentPart.AddPoint('SP21', SP21[0], SP21[1], SP21[2])

###############################################################################
# 2nd Spline
###############################################################################
Path2 = CurrentPart.Add3DSketch('Spline2')
Points2 = []
for i in cycle:
    ix = i*3
    X12 = to_float4(Points_2[ix])
    Y12 = to_float4(Points_2[ix+1])
    Z12 = to_float4(Points_2[ix+2])
    Points2.extend([X12, Y12, Z12])

Path2.AddBspline(Points2)

SP2  = [Points2[0],   Points2[1],   Points2[2]]
SP12 = [Points2[150], Points2[151], Points2[152]]
SP22 = [Points2[300], Points2[301], Points2[302]]

CurrentPart.AddPoint('SP2',  SP2[0],  SP2[1],  SP2[2])
CurrentPart.AddPoint('SP12', SP12[0], SP12[1], SP12[2])
CurrentPart.AddPoint('SP22', SP22[0], SP22[1], SP22[2])

###############################################################################
# 3rd Spline
###############################################################################
Path3 = CurrentPart.Add3DSketch('Spline3')
Points3 = []
for i in cycle:
    ix = i*3
    X13 = to_float4(Points_3[ix])
    Y13 = to_float4(Points_3[ix+1])
    Z13 = to_float4(Points_3[ix+2])
    Points3.extend([X13, Y13, Z13])

Path3.AddBspline(Points3)

SP3  = [Points3[0],   Points3[1],   Points3[2]]
SP13 = [Points3[150], Points3[151], Points3[152]]
SP23 = [Points3[300], Points3[301], Points3[302]]

CurrentPart.AddPoint('SP3',  SP3[0],  SP3[1],  SP3[2])
CurrentPart.AddPoint('SP13', SP13[0], SP13[1], SP13[2])
CurrentPart.AddPoint('SP23', SP23[0], SP23[1], SP23[2])

###############################################################################
# 4th Spline
###############################################################################
Path4 = CurrentPart.Add3DSketch('Spline4')
Points4 = []
for i in cycle:
    ix = i*3
    X14 = to_float4(Points_4[ix])
    Y14 = to_float4(Points_4[ix+1])
    Z14 = to_float4(Points_4[ix+2])
    Points4.extend([X14, Y14, Z14])

Path4.AddBspline(Points4)

SP4  = [Points4[0],   Points4[1],   Points4[2]]
SP14 = [Points4[150], Points4[151], Points4[152]]
SP24 = [Points4[300], Points4[301], Points4[302]]

CurrentPart.AddPoint('SP4',  SP4[0],  SP4[1],  SP4[2])
CurrentPart.AddPoint('SP14', SP14[0], SP14[1], SP14[2])
CurrentPart.AddPoint('SP24', SP24[0], SP24[1], SP24[2])

###############################################################################
# 5th Spline
###############################################################################
Path5 = CurrentPart.Add3DSketch('Spline5')
Points5 = []
for i in cycle:
    ix = i*3
    X15 = to_float4(Points_5[ix])
    Y15 = to_float4(Points_5[ix+1])
    Z15 = to_float4(Points_5[ix+2])
    Points5.extend([X15, Y15, Z15])

Path5.AddBspline(Points5)

SP5  = [Points5[0],   Points5[1],   Points5[2]]
SP15 = [Points5[150], Points5[151], Points5[152]]
SP25 = [Points5[300], Points5[301], Points5[302]]

CurrentPart.AddPoint('SP5',  SP5[0],  SP5[1],  SP5[2])
CurrentPart.AddPoint('SP15', SP15[0], SP15[1], SP15[2])
CurrentPart.AddPoint('SP25', SP25[0], SP25[1], SP25[2])

###############################################################################
# 6th Spline
###############################################################################
Path6 = CurrentPart.Add3DSketch('Spline6')
Points6 = []
for i in cycle:
    ix = i*3
    X16 = to_float4(Points_6[ix])
    Y16 = to_float4(Points_6[ix+1])
    Z16 = to_float4(Points_6[ix+2])
    Points6.extend([X16, Y16, Z16])

Path6.AddBspline(Points6)

SP6  = [Points6[0],   Points6[1],   Points6[2]]
SP16 = [Points6[150], Points6[151], Points6[152]]
SP26 = [Points6[300], Points6[301], Points6[302]]

CurrentPart.AddPoint('SP6',  SP6[0],  SP6[1],  SP6[2])
CurrentPart.AddPoint('SP16', SP16[0], SP16[1], SP16[2])
CurrentPart.AddPoint('SP26', SP26[0], SP26[1], SP26[2])

###############################################################################
# 7th Spline
###############################################################################
Path7 = CurrentPart.Add3DSketch('Spline7')
Points7 = []
for i in cycle:
    ix = i*3
    X17 = to_float4(Points_7[ix])
    Y17 = to_float4(Points_7[ix+1])
    Z17 = to_float4(Points_7[ix+2])
    Points7.extend([X17, Y17, Z17])

Path7.AddBspline(Points7)

SP7  = [Points7[0],   Points7[1],   Points7[2]]
SP17 = [Points7[150], Points7[151], Points7[152]]
SP27 = [Points7[300], Points7[301], Points7[302]]

CurrentPart.AddPoint('SP7',  SP7[0],  SP7[1],  SP7[2])
CurrentPart.AddPoint('SP17', SP17[0], SP17[1], SP17[2])
CurrentPart.AddPoint('SP27', SP27[0], SP27[1], SP27[2])

###############################################################################
# 8th Spline
###############################################################################
Path8 = CurrentPart.Add3DSketch('Spline8')
Points8 = []
for i in cycle:
    ix = i*3
    X18 = to_float4(Points_8[ix])
    Y18 = to_float4(Points_8[ix+1])
    Z18 = to_float4(Points_8[ix+2])
    Points8.extend([X18, Y18, Z18])

Path8.AddBspline(Points8)

SP8  = [Points8[0],   Points8[1],   Points8[2]]
SP18 = [Points8[150], Points8[151], Points8[152]]
SP28 = [Points8[300], Points8[301], Points8[302]]

CurrentPart.AddPoint('SP8',  SP8[0],  SP8[1],  SP8[2])
CurrentPart.AddPoint('SP18', SP18[0], SP18[1], SP18[2])
CurrentPart.AddPoint('SP28', SP28[0], SP28[1], SP28[2])

###############################################################################
# 9th Spline
###############################################################################
Path9 = CurrentPart.Add3DSketch('Spline9')
Points9 = []
for i in cycle:
    ix = i*3
    X19 = to_float4(Points_9[ix])
    Y19 = to_float4(Points_9[ix+1])
    Z19 = to_float4(Points_9[ix+2])
    Points9.extend([X19, Y19, Z19])

Path9.AddBspline(Points9)

SP9  = [Points9[0],   Points9[1],   Points9[2]]
SP19 = [Points9[150], Points9[151], Points9[152]]
SP29 = [Points9[300], Points9[301], Points9[302]]

CurrentPart.AddPoint('SP9',  SP9[0],  SP9[1],  SP9[2])
CurrentPart.AddPoint('SP19', SP19[0], SP19[1], SP19[2])
CurrentPart.AddPoint('SP29', SP29[0], SP29[1], SP29[2])

###############################################################################
# 10th Spline
###############################################################################
Path10 = CurrentPart.Add3DSketch('Spline10')
Points10 = []
for i in cycle:
    ix = i*3
    X110 = to_float4(Points_10[ix])
    Y110 = to_float4(Points_10[ix+1])
    Z110 = to_float4(Points_10[ix+2])
    Points10.extend([X110, Y110, Z110])

Path10.AddBspline(Points10)

SP10 = [Points10[0],   Points10[1],   Points10[2]]
SP20 = [Points10[150], Points10[151], Points10[152]]
SP30 = [Points10[300], Points10[301], Points10[302]]

CurrentPart.AddPoint('SP10', SP10[0], SP10[1], SP10[2])
CurrentPart.AddPoint('SP20', SP20[0], SP20[1], SP20[2])
CurrentPart.AddPoint('SP30', SP30[0], SP30[1], SP30[2])

###############################################################################
# Make Planes from Points
###############################################################################
Plane1 = CurrentPart.AddPlane('FirstPlane', SP1, SP2, SP3)
Plane2 = CurrentPart.AddPlane('MiddlePlane', SP11, SP12, SP13)
Plane3 = CurrentPart.AddPlane('LastPlane', SP21, SP22, SP23)

S1 = CurrentPart.AddSketch('FirstSketch',  Plane1)
S2 = CurrentPart.AddSketch('MiddleSketch', Plane2)
S3 = CurrentPart.AddSketch('LastSketch',   Plane3)

# Combine your first three sets into one set for each plane
First_Sketch = SP1 + SP2 + SP3 + SP4 + SP5 + SP6 + SP7 + SP8 + SP9 + SP10
Mid_Sketch   = SP11 + SP12 + SP13 + SP14 + SP15 + SP16 + SP17 + SP18 + SP19 + SP20
End_Sketch   = SP21 + SP22 + SP23 + SP24 + SP25 + SP26 + SP27 + SP28 + SP29 + SP30

print(First_Sketch)

###############################################################################
# Convert to local 2D coordinates and draw lines for each plane’s sketch
###############################################################################
SketchPoints_1 = []
SketchPoints_2 = []
SketchPoints_3 = []

# Each set (SP*) above has 10 triplets => 30 elements
def chunk_triplets(dat):
    return [dat[i:i+3] for i in range(0, len(dat), 3)]

# Convert First_Sketch
trip_1 = chunk_triplets(First_Sketch)  # 10 sets of [X,Y,Z]
for (xx, yy, zz) in trip_1:
    uv = S1.GlobaltoPoint(xx, yy, zz)
    SketchPoints_1.append(uv)

# Convert Mid_Sketch
trip_2 = chunk_triplets(Mid_Sketch)
for (xx, yy, zz) in trip_2:
    uv = S2.GlobaltoPoint(xx, yy, zz)
    SketchPoints_2.append(uv)

# Convert End_Sketch
trip_3 = chunk_triplets(End_Sketch)
for (xx, yy, zz) in trip_3:
    uv = S3.GlobaltoPoint(xx, yy, zz)
    SketchPoints_3.append(uv)

# Flatten so that AddLines(...) sees them as [x1,y1, x2,y2, x3,y3, ...]
def flatten_and_close(pts2d):
    flattened = []
    for xy in pts2d:
        flattened.append(xy[0])
        flattened.append(xy[1])
    # Close the profile: add the first point again
    flattened.append(flattened[0])
    flattened.append(flattened[1])
    return flattened

SketchPoints1 = flatten_and_close(SketchPoints_1)
SketchPoints2 = flatten_and_close(SketchPoints_2)
SketchPoints3 = flatten_and_close(SketchPoints_3)

S1.AddLines(SketchPoints1, False)
S2.AddLines(SketchPoints2, False)
S3.AddLines(SketchPoints3, False)
```

<aside>
📢

Original source code with AI cleanup tasks applied 

[SplineScript_AI_Clean_01.py.txt](SplineScript_AI_Clean_01.py.txt)

- SplineScript_AI_Clean_01.py.txt
    
    ```python
    import fpformat
    
    def read_input_file():
        """
        Prompts the user to select a 3D-points TXT file.
        Reads the file contents into a list of strings.
        Returns:
            txtfile (str): file path
            Points_Full (list of str): list of point coordinates as strings
        """
        Win = Windows()
        CurrentPartVar = CurrentPart()
    
        txtfile = Win.OpenFileDialog('Select 3D Pojnts in TXT,mm','TXT files(*.*)|*.txt*','.txt')
        f = open(txtfile, 'r')
        datareader2 = f.read()
        f.close()
    
        # Convert file lines into a list of coordinate strings
        data_into_list = datareader2.replace('\n', ',').split(',')
        Points_Full = data_into_list
    
        return txtfile, Points_Full
    
    def get_number_of_sections():
        """
        Prompts the user for the number of guide curves and returns it as an integer.
        """
        print 'Input Number of Guide Curves (typ - 10), then press ENTER'
        NumberOfSections = int(Read())
        return NumberOfSections
    
    def define_point_ranges(length):
        """
        Given the number of points (length) for each spline, 
        returns 10 range objects. This part remains 
        hard-coded to handle exactly 10 guide curves.
        """
        Points_1_range  = range(0, ((length*3)))
        Points_2_range  = range(length*3, ((3*2*length)))
        Points_3_range  = range((3*2*length), ((3*3*length)))
        Points_4_range  = range((3*3*length), ((3*4*length)))
        Points_5_range  = range((3*4*length), ((3*5*length)))
        Points_6_range  = range((3*5*length), ((3*6*length)))
        Points_7_range  = range((3*6*length), ((3*7*length)))
        Points_8_range  = range((3*7*length), ((3*8*length)))
        Points_9_range  = range((3*8*length), ((3*9*length)))
        Points_10_range = range((3*9*length), ((3*10*length)))
        
        return (
            Points_1_range, Points_2_range, Points_3_range,
            Points_4_range, Points_5_range, Points_6_range,
            Points_7_range, Points_8_range, Points_9_range,
            Points_10_range
        )
    
    def extract_float_points(Points_Full, index_range):
        """
        Converts a sub-range of Points_Full into a list of floats.
        """
        return [float(Points_Full[i]) for i in index_range]
    
    def create_spline_sketch(sketch_name, float_points):
        """
        Creates a 3D sketch for a spline:
        - Loops over the float_points in sets of three,
          fixes them to 4 decimals, and accumulates them.
        - Adds a B-spline to the sketch.
        - Returns (Path object, some sample points) for plane creation, etc.
        """
        Path = CurrentPart().Add3DSketch(sketch_name)
        PointsList = []
        cycle = range(len(float_points)//3)
    
        # Build the array for AddBspline
        for aaa in cycle:
            IncX = aaa * 3
            IncY = (aaa*3) + 1
            IncZ = (aaa*3) + 2
            
            X_val = fpformat.fix(float_points[IncX], 4)
            Y_val = fpformat.fix(float_points[IncY], 4)
            Z_val = fpformat.fix(float_points[IncZ], 4)
            
            PointsList.extend([X_val, Y_val, Z_val])
        
        # Create the B-spline from the points
        Path.AddBspline(PointsList)
        
        # Return sample points for plane references (SP, SP1, SP2 etc.)
        # Hard-coded offsets: 0, 150, 300 (just as in the original).
        # Note: Make sure the float_points array has enough points.
        SP  = [
            fpformat.fix(float(PointsList[0]),4),
            fpformat.fix(float(PointsList[1]),4),
            fpformat.fix(float(PointsList[2]),4)
        ]
        SP1 = [
            fpformat.fix(float(PointsList[150]),4),
            fpformat.fix(float(PointsList[151]),4),
            fpformat.fix(float(PointsList[152]),4)
        ]
        SP2 = [
            fpformat.fix(float(PointsList[300]),4),
            fpformat.fix(float(PointsList[301]),4),
            fpformat.fix(float(PointsList[302]),4)
        ]
        
        return Path, SP, SP1, SP2
    
    def create_reference_points_on_part(SP_name, sp_coords):
        """
        Adds a reference point in the current part at the location of sp_coords.
        sp_coords should be [x, y, z] as strings or floats convertible to strings.
        """
        # Convert each to float if needed, then fix to 4 decimals again
        x_str = fpformat.fix(float(sp_coords[0]),4)
        y_str = fpformat.fix(float(sp_coords[1]),4)
        z_str = fpformat.fix(float(sp_coords[2]),4)
        CurrentPart().AddPoint(SP_name, [x_str, y_str, z_str])
    
    def create_planes_and_sketches(SP1, SP2, SP3, SP11, SP12, SP13, SP21, SP22, SP23):
        """
        Creates 3 planes from sets of points:
            Plane1 from SP1, SP2, SP3
            Plane2 from SP11, SP12, SP13
            Plane3 from SP21, SP22, SP23
        Then creates 2D sketches (S1, S2, S3) on those planes.
        Returns:
            (Plane1, Plane2, Plane3, S1, S2, S3)
        """
        Plane1 = CurrentPart().AddPlane('FirstPlane',  SP1,  SP2,  SP3)
        Plane2 = CurrentPart().AddPlane('MiddlePlane', SP11, SP12, SP13)
        Plane3 = CurrentPart().AddPlane('LastPlane',   SP21, SP22, SP23)
        
        S1 = CurrentPart().AddSketch('FirstSketch',  Plane1)
        S2 = CurrentPart().AddSketch('MiddleSketch', Plane2)
        S3 = CurrentPart().AddSketch('LastSketch',   Plane3)
        
        return Plane1, Plane2, Plane3, S1, S2, S3
    
    def create_2D_points_and_lines(S1, S2, S3, First_Sketch, Mid_Sketch, End_Sketch):
        """
        Takes the 3 sets of global points (First_Sketch, Mid_Sketch, End_Sketch),
        projects them onto the local plane sketches (S1, S2, S3),
        then adds lines connecting them in each 2D sketch.
        """
        SketchPoints_1 = []
        SketchPoints_2 = []
        SketchPoints_3 = []
    
        # Project 10 sets of points into S1
        for aaa in range(10):
            IncX = aaa*3
            IncY = (aaa*3)+1
            IncZ = (aaa*3)+2
            
            X11 = First_Sketch[IncX]
            Y11 = First_Sketch[IncY]
            Z11 = First_Sketch[IncZ]
            
            UV1 = S1.GlobaltoPoint(X11, Y11, Z11)
            SketchPoints_1.append(UV1)
    
        # Project 10 sets of points into S2
        for bbb in range(10):
            IncX = bbb*3
            IncY = (bbb*3)+1
            IncZ = (bbb*3)+2
            
            X22 = fpformat.fix(float(Mid_Sketch[IncX]),4)
            Y22 = fpformat.fix(float(Mid_Sketch[IncY]),4)
            Z22 = fpformat.fix(float(Mid_Sketch[IncZ]),4)
            
            UV2 = S2.GlobaltoPoint(X22, Y22, Z22)
            SketchPoints_2.append(UV2)
    
        # Project 10 sets of points into S3
        for ccc in range(10):
            IncX = ccc*3
            IncY = (ccc*3)+1
            IncZ = (ccc*3)+2
            
            X33 = fpformat.fix(float(End_Sketch[IncX]),4)
            Y33 = fpformat.fix(float(End_Sketch[IncY]),4)
            Z33 = fpformat.fix(float(End_Sketch[IncZ]),4)
            
            UV3 = S3.GlobaltoPoint(X33, Y33, Z33)
            SketchPoints_3.append(UV3)
    
        # Flatten the lists for AddLines(), and repeat the first point to close
        SketchPoints1 = [element for innerList in SketchPoints_1 for element in innerList]
        SketchPoints1.extend([SketchPoints1[0], SketchPoints1[1]])
    
        SketchPoints2 = [element for innerList in SketchPoints_2 for element in innerList]
        SketchPoints2.extend([SketchPoints2[0], SketchPoints2[1]])
    
        SketchPoints3 = [element for innerList in SketchPoints_3 for element in innerList]
        SketchPoints3.extend([SketchPoints3[0], SketchPoints3[1]])
    
        # Finally, add lines to each sketch
        S1.AddLines(SketchPoints1, False)
        S2.AddLines(SketchPoints2, False)
        S3.AddLines(SketchPoints3, False)
    
    def main():
        # -------------------
        # Step 1: Read file and parse data
        # -------------------
        txtfile, Points_Full = read_input_file()
        NumberOfSections = get_number_of_sections()
    
        length = (len(Points_Full)/(NumberOfSections*3))
        print(length)  # Just to match the original code's debug
    
        # -------------------
        # Step 2: Define index ranges for each group
        # -------------------
        (Points_1_range, Points_2_range, Points_3_range,
         Points_4_range, Points_5_range, Points_6_range,
         Points_7_range, Points_8_range, Points_9_range,
         Points_10_range) = define_point_ranges(length)
    
        # -------------------
        # Step 3: Build float-lists for each group
        # -------------------
        Points_1  = extract_float_points(Points_Full, Points_1_range)
        Points_2  = extract_float_points(Points_Full, Points_2_range)
        Points_3  = extract_float_points(Points_Full, Points_3_range)
        Points_4  = extract_float_points(Points_Full, Points_4_range)
        Points_5  = extract_float_points(Points_Full, Points_5_range)
        Points_6  = extract_float_points(Points_Full, Points_6_range)
        Points_7  = extract_float_points(Points_Full, Points_7_range)
        Points_8  = extract_float_points(Points_Full, Points_8_range)
        Points_9  = extract_float_points(Points_Full, Points_9_range)
        Points_10 = extract_float_points(Points_Full, Points_10_range)
    
        # -------------------
        # Step 4: Create 3D splines (Paths) from each group
        #         Also add reference points for each set
        # -------------------
        Path1,  SP1,  SP11,  SP21  = create_spline_sketch('Spline1',  Points_1)
        Path2,  SP2,  SP12,  SP22  = create_spline_sketch('Spline2',  Points_2)
        Path3,  SP3,  SP13,  SP23  = create_spline_sketch('Spline3',  Points_3)
        Path4,  SP4,  SP14,  SP24  = create_spline_sketch('Spline4',  Points_4)
        Path5,  SP5,  SP15,  SP25  = create_spline_sketch('Spline5',  Points_5)
        Path6,  SP6,  SP16,  SP26  = create_spline_sketch('Spline6',  Points_6)
        Path7,  SP7,  SP17,  SP27  = create_spline_sketch('Spline7',  Points_7)
        Path8,  SP8,  SP18,  SP28  = create_spline_sketch('Spline8',  Points_8)
        Path9,  SP9,  SP19,  SP29  = create_spline_sketch('Spline9',  Points_9)
        Path10, SP10, SP20,  SP30  = create_spline_sketch('Spline10', Points_10)
    
        # Add those reference points in the current part (SP1, SP11, etc.)
        # Original code: CurrentPart.AddPoint('SP1', SP1) ...
        # Here we simply replicate it in a small loop:
        create_reference_points_on_part('SP1',  SP1)
        create_reference_points_on_part('SP11', SP11)
        create_reference_points_on_part('SP21', SP21)
    
        create_reference_points_on_part('SP2',  SP2)
        create_reference_points_on_part('SP12', SP12)
        create_reference_points_on_part('SP22', SP22)
    
        create_reference_points_on_part('SP3',  SP3)
        create_reference_points_on_part('SP13', SP13)
        create_reference_points_on_part('SP23', SP23)
    
        create_reference_points_on_part('SP4',  SP4)
        create_reference_points_on_part('SP14', SP14)
        create_reference_points_on_part('SP24', SP24)
    
        create_reference_points_on_part('SP5',  SP5)
        create_reference_points_on_part('SP15', SP15)
        create_reference_points_on_part('SP25', SP25)
    
        create_reference_points_on_part('SP6',  SP6)
        create_reference_points_on_part('SP16', SP16)
        create_reference_points_on_part('SP26', SP26)
    
        create_reference_points_on_part('SP7',  SP7)
        create_reference_points_on_part('SP17', SP17)
        create_reference_points_on_part('SP27', SP27)
    
        create_reference_points_on_part('SP8',  SP8)
        create_reference_points_on_part('SP18', SP18)
        create_reference_points_on_part('SP28', SP28)
    
        create_reference_points_on_part('SP9',  SP9)
        create_reference_points_on_part('SP19', SP19)
        create_reference_points_on_part('SP29', SP29)
    
        create_reference_points_on_part('SP10', SP10)
        create_reference_points_on_part('SP20', SP20)
        create_reference_points_on_part('SP30', SP30)
    
        # -------------------
        # Step 5: Make Planes from the first, middle, last points 
        #         across the first 3 splines
        #         (Matches your original code exactly)
        # -------------------
        (Plane1, Plane2, Plane3, 
         S1, S2, S3) = create_planes_and_sketches(SP1, SP2, SP3,
                                                 SP11, SP12, SP13,
                                                 SP21, SP22, SP23)
    
        # -------------------
        # Step 6: Create point lists for 2D sketches (First, Mid, End)
        #         Then project them onto the sketches as lines
        # -------------------
        First_Sketch = SP1 + SP2 + SP3 + SP4 + SP5 + SP6 + SP7 + SP8 + SP9 + SP10
        Mid_Sketch   = SP11 + SP12 + SP13 + SP14 + SP15 + SP16 + SP17 + SP18 + SP19 + SP20
        End_Sketch   = SP21 + SP22 + SP23 + SP24 + SP25 + SP26 + SP27 + SP28 + SP29 + SP30
    
        print(First_Sketch)  # Matches original code
    
        create_2D_points_and_lines(S1, S2, S3, First_Sketch, Mid_Sketch, End_Sketch)
    
    # -------------------------------
    # Entry Point
    # -------------------------------
    main()
    
    ```
    
    ```
    >>>
    Input Number of Guide Curves (typ - 10), then press ENTER
    10
    101
    ['1224.7348', '1039.3295', '173.5912', '1219.8444', '1041.3338', '172.0690', '1219.7922', '1046.2421', '178.6999', '1216.2133', '1047.7089', '177.5859', '1216.1981', '1049.1405', '179.5199', '1217.8986', '1048.4435', '180.0492', '1217.9008', '1048.2390', '179.7730', '1222.9689', '1046.1618', '181.3505', '1222.9668', '1046.3663', '181.6267', '1224.6673', '1045.6693', '182.1560']
    Traceback (most recent call last):
      File "<string>", line 322, in <module>
      File "<string>", line 316, in main
      File "<string>", line 162, in create_2D_points_and_lines
    TypeError: expected float, got str
    >>>
    ```
    
</aside>

<aside>
📎

[davex7637.AD_PKG](davex7637.ad_pkg)

</aside>