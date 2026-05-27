#https://help.alibre.com/articles/#!alibre-help-v23/assembly-constraints
# create a new empty assembly
Asm = Assembly("Test");
# add a part at the origin, replace path with your own
NewPart1 = Asm.AddPart(r'C:\Users\<username>\Desktop\PartA.AD_PRT', 0, 0, 0)
# duplicate the part
NewPart2 = Asm.DuplicatePart(NewPart1.Name, 0, 0, 0)
# anchor the original copy
Asm.AnchorPart(NewPart1.Name);
# at a mate constraint, separating the XY-planes of the two parts by 0mm
Asm.AddMateConstraint(0, NewPart1, NewPart1.GetPlane("XY-Plane"), NewPart2, NewPart2.GetPlane("XY-Plane"))
# add an alignment constraint, separating the parts by 0mm
Asm.AddAlignConstraint(0, NewPart1, NewPart1.GetPlane("YZ-Plane"), NewPart2, NewPart2.GetPlane("YZ-Plane"))