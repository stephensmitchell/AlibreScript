# Part exporter script
# Demonstrates exporting a set of parts
# For use with Alibre Design
import fnmatch
import os
from os.path import expanduser
Win = Windows()
ScriptName = 'Part Exporter'
ExportTypes = ['STEP203', 'STEP214', 'STL', 'IGES', 'SAT', 'BMP']
Options = []
Options.append(['Folder containing parts', WindowsInputTypes.Folder, expanduser('~'), 'Choose a folder containing the parts.'])
Options.append(['Output folder', WindowsInputTypes.Folder, expanduser('~'), 'Choose a folder to put the exported files'])
Options.append(['Export type', WindowsInputTypes.StringList, ExportTypes, ExportTypes[0]])
Values = Win.OptionsDialog(ScriptName, Options, 300)
if Values == None:
  sys.exit()
# get the inputs
PartsFolder = Values[0]
OutputFolder = Values[1]
ExportType = ExportTypes[Values[2]]
# validate
if not PartsFolder:
  Win.ErrorDialog('No part folder selected', ScriptName)
  sys.exit();
if os.path.isdir(PartsFolder) == False:
  Win.ErrorDialog('Folder containing parts does not exist', ScriptName)
  sys.exit();
if not OutputFolder:
  Win.ErrorDialog('No output folder selected', ScriptName)
  sys.exit();
if os.path.isdir(OutputFolder) == False:
  Win.ErrorDialog('Output folder does not exist', ScriptName)
  sys.exit();
print "Searching for parts..."
# create empty lists
Parts = []
# perform the search
for Root, Dirnames, Filenames in os.walk(PartsFolder):
  for Filename in fnmatch.filter(Filenames, '*.AD_PRT'):
    Parts.append(os.path.join(Root, Filename))
# if no parts found...
if len(Parts) == 0:
  Win.ErrorDialog('No parts found', ScriptName)
  sys.exit();
# export each part
for PartFileName in Parts:
  print "Exporting {0}...".format(PartFileName)
  Folder = os.path.dirname(os.path.abspath(PartFileName))
  FileName = os.path.basename(PartFileName)
  FileNameNoExt, Ext = os.path.splitext(FileName)
  OutputFileName = OutputFolder + '\\' + FileNameNoExt
  # open, export, close
  P = Part(Folder, FileName)
  if ExportType == 'STEP203':
    P.ExportSTEP203(OutputFileName + '.stp')
    print "Created {0} (203)".format(OutputFileName + '.stp')
  elif ExportType == 'STEP214':
    P.ExportSTEP214(OutputFileName + ".stp")
    print "Created {0} (214)".format(OutputFileName + '.stp')
  elif ExportType == 'STL':
    P.ExportSTL(OutputFileName + ".stl")
    print "Created {0}".format(OutputFileName + '.stl')
  elif ExportType == 'IGES':
    P.ExportIGES(OutputFileName + ".igs")
    print "Created {0}".format(OutputFileName + '.igs')
  elif ExportType == 'SAT':
    P.ExportSAT(OutputFileName + ".sat", 18, True)
    print "Created {0}".format(OutputFileName + '.sat')
  elif ExportType == 'BMP':
    P.SaveSnapshot(OutputFileName + '.bmp', 800, 600, True, False)
    print "Created {0}".format(OutputFileName + '.bmp')
  P.Close()
Win.InfoDialog('Exported {0} parts'.format(len(Parts)), ScriptName)
