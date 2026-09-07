#https://help.alibre.com/articles/#!alibre-help-v23/list-all-parts-in-an-assembly-and-sub-assemblies
# list all the parts in an assembly and it's sub-assemblies
def ListPartsinAssembly(Assem):
  for P in Assem.Parts:
    print '%s in %s' % (P, Assem)
  for SA in Assem.SubAssemblies:
    ListPartsinAssembly(SA)
# top-level assembly, replace with your own path
Assem = Assembly(r'C:\Users\<username>\Downloads\ASM', 'Main ASM.AD_ASM')
ListPartsinAssembly(Assem)
Assem.Close()