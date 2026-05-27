#https://help.alibre.com/articles/#!alibre-help-v23/create-and-modify-global-parameters
# create a new global parameters set
Params = GlobalParameters('Test')
# add a distance parameter in millimeters
Params.AddParameter('Width', ParameterTypes.Distance, 4.56)
# save and close, replace with your own path
Params.Save(r'C:\Users\<username>\Downloads\temp')
Params.Close()
# open global parameters, replace with your own path
Params2 = GlobalParameters(r'C:\Users\<username>\Downloads\temp', 'Test')
# get access to a parameter and display the current value
Width = Params2.GetParameter('Width')
print Width.Value
# change the value of the parameter
Width.Value = 12.34