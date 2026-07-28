class GlobalParameters:
    def __init__(
        self, Name, ParameterList, ConfigurationList, Parameters, Configurations
    ):
        pass
        self.Name = Name
        self.ParameterList = ParameterList
        self.ConfigurationList = ConfigurationList
        self.Parameters = Parameters
        self.Configurations = Configurations
    def GetParameter(self, StringName):
        pass
    def GetConfiguration(self, StringName):
        pass
    def GetActiveConfiguration(
        self,
    ):
        pass
    def AddParameter(self, StringName, ParameterTypesType, DoubleValue):
        pass
    def AddParameter(self, StringName, ParameterTypesType, StringEquation):
        pass
    def AddConfiguration(self, StringName):
        pass
    def AddConfiguration(self, StringName, StringBaseConfigurationName):
        pass
    def Save(
        self,
    ):
        pass
    def Save(self, StringFolder):
        pass
    def SaveAs(self, StringFolder, StringNewName):
        pass
    def Close(
        self,
    ):
        pass
