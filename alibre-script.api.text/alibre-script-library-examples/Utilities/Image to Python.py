# Image to Python Converter
# (c) Alibre, LLC 2019, All Rights Reserved
# Version 1.00
from array import array
import os
Win = Windows()
ScriptName = "Image to Python Converter"
Options = []
Options.append(['Image', WindowsInputTypes.File, None, 'Choose an image', 'PNG Files|*.png|JPEG Files|*.jpg|Bitmap Files|*.bmp|All Files|*.*'])
Options.append(['Python Output', WindowsInputTypes.SaveFile, None, 'Python File to Generate', 'Python Files|*.py|All Files|*.*', '.py'])
Values = Win.OptionsDialog(ScriptName, Options)
if Values == None:
  sys.exit()
ImageFile = Values[0]
OutputFile = Values[1]
# get some details about the image file
ImageSize = os.path.getsize(ImageFile)
ImageName = os.path.splitext(os.path.basename(ImageFile))[0]
ImageName = "Img_" + ImageName.Replace(' ', '_')
# load image into binary array
data = array('B')
with open(ImageFile, 'rb') as f:
    data.fromfile(f, ImageSize)
Out = open(OutputFile, 'w')
Out.write('%s = [\n' % ImageName)
Line = ''
Offset = 0
for b in range(0, ImageSize):
  Line += '0x%2.2X, ' % data[b]
  Offset += 1
  if Offset % 20 == 0:
    Out.write('  ' + Line + '\n')
    Line = ''
if len(Line) > 0: Out.write('  ' + Line)
Out.write(']\n')
Out.close()
Win.InfoDialog('Python file generated', ScriptName)
