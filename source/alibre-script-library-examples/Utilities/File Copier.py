# File Copier script
# Demonstrates copying a set of parts and assemblies
# For use with Alibre Design
import fnmatch
import os
from os.path import expanduser
Win = Windows()
ScriptName = 'File Copier'
CopyTypes = ['Only parts', 'Assemblies, sub-assemblies and parts in assemblies']
Options = []
Options.append(['Source folder', WindowsInputTypes.Folder, expanduser('~'), 'Choose the folder containing the items to copy'])
Options.append(['Destination folder', WindowsInputTypes.Folder, expanduser('~'), 'Choose the folder to place the copies'])
Options.append(['Copy', WindowsInputTypes.StringList, CopyTypes, CopyTypes[0]])
Values = Win.OptionsDialog(ScriptName, Options, 300)
if Values == None:
  sys.exit()
# get the inputs
SourceFolder = Values[0]
DestinationFolder = Values[1]
CopyType = Values[2]
# validate
if not SourceFolder:
  Win.ErrorDialog('No source folder selected', ScriptName)
  sys.exit();
if os.path.isdir(SourceFolder) == False:
  Win.ErrorDialog('Source folder does not exist', ScriptName)
  sys.exit();
if not DestinationFolder:
  Win.ErrorDialog('No destination folder selected', ScriptName)
  sys.exit();
if os.path.isdir(DestinationFolder) == False:
  Win.ErrorDialog('Destination folder does not exist', ScriptName)
  sys.exit();
if CopyType == 0:
  print "Searching for parts..."
else:
  print "Searching for assemblies..."
# create empty lists
Parts = []
Assemblies = []
# perform the search
for Root, Dirnames, Filenames in os.walk(SourceFolder):
  if CopyType == 0:
    for Filename in fnmatch.filter(Filenames, '*.AD_PRT'):
      Parts.append(os.path.join(Root, Filename))
  else:
    for Filename in fnmatch.filter(Filenames, '*.AD_ASM'):
      Assemblies.append(os.path.join(Root, Filename))
# if no parts or assemblies found...
if len(Parts) == 0 and len(Assemblies) == 0:
  Win.ErrorDialog('No parts or assemblies found', ScriptName)
  sys.exit();
# copy each part
for PartFileName in Parts:
  print "Copying {0}...".format(PartFileName)
  Folder = os.path.dirname(os.path.abspath(PartFileName))
  FileName = os.path.basename(PartFileName)
  FileNameNoExt, Ext = os.path.splitext(FileName)
  OutputFileName = DestinationFolder + '\\' + FileName
  # open, save, close
  P = Part(Folder, FileName)
  P.SaveAs(DestinationFolder, FileNameNoExt)
  P.Close()
  print "  -> {0}".format(OutputFileName)
# copy each assembly
for AssemblyFileName in Assemblies:
  print "Copying {0}...".format(AssemblyFileName)
  # open, save, close
  Folder = os.path.dirname(os.path.abspath(AssemblyFileName))
  FileName = os.path.basename(AssemblyFileName)
  OutputFileName = DestinationFolder + '\\' + FileName
  A = Assembly(Folder, Filename)
  A.SaveAll(DestinationFolder)
  A.Close()
  print "  -> {0}".format(OutputFileName)
if CopyType == 0:
  Win.InfoDialog('Copied {0} part{1}'.format(len(Parts), '' if len(Parts) == 1 else 's'), ScriptName)
else:
  Win.InfoDialog('Copied {0} assembl{1}'.format(len(Assemblies), 'y' if len(Assemblies) == 1 else 'ies'), ScriptName)
