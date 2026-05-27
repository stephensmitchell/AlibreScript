#https://help.alibre.com/articles/#!alibre-help-v23/importing-files
# replace paths used with your own
# import a step file
MyPart1 = Part(r'c:\mycadfiles\Corner.stp', Part.FileTypes.STEP)
# import an IGES file
MyPart3 = Part(r'c:\mycadfiles\wave washer.igs', Part.FileTypes.IGES)
