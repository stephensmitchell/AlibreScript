#https://help.alibre.com/articles/#!alibre-help-v23/creating-and-manipulating-assemblies
# create a new empty assembly
Asm = Assembly("Test");
# add an existing part, located at the origin, replace path with your own
NewPart1 = Asm.AddPart(r'C:\Users\Brian\Desktop\PartA.AD_PRT', 0, 0, 0, 0, 0, 0, True)
# duplicate the part, translate it to x = 5, y = 10, z = 15 and rotate it x 30 deg, y 40 deg, z 50 deg
NewPart2 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, True)
# duplicate the part, rotate it x 30 deg, y 40 deg, z 50 deg and translate it x = 5, y = 10, z = 15
NewPart3 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, False)
# anchor the original part
Asm.AnchorPart(NewPart1);
# get the part (this is an 'assembled part')
P = Asm.GetPart(NewPart1.Name)
# show the faces on the part
print P.Faces