class Windows:
    def __init__(
        self,
    ):
        pass
    def CloseForm(self, StringSessionIdentifier):
        pass
    def GetDisplayedForm(self, StringSessionIdentifier):
        pass
    def UtilityDialog(
        self,
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
    ):
        pass
    def UtilityDialog(
        self,
        StringTitle,
        StringActionButtonText,
        ObjectActionButtonCallback,
        ObjectInputChangedCallback,
        ListInputs,
        Int32InputAreaWidth,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def OptionsDialog(self, StringTitle, ListInputs, Int32InputAreaWidth):
        pass
    def OptionsDialog(
        self,
        StringTitle,
        ListInputs,
        Int32InputAreaWidth,
        ObjectInputChangedCallback,
        ObjectUpdateUserInterfaceCallback,
    ):
        pass
    def DisableInput(self, Int32Index):
        pass
    def EnableInput(self, Int32Index):
        pass
    def GetInputValue(self, Int32Index):
        pass
    def SetStringList(self, Int32Index, ObjectStrings):
        pass
    def SetInputValue(self, Int32Index, ObjectValue):
        pass
    def OpenFileDialog(self, StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SaveFileDialog(self, StringTitle, StringFilter, StringDefaultExtension):
        pass
    def SelectFolderDialog(self, StringCurrentFolder, StringDescription):
        pass
    def InfoDialog(self, StringMessage, StringTitle):
        pass
    def ErrorDialog(self, StringMessage, StringTitle):
        pass
    def QuestionDialog(self, StringQuestion, StringTitle):
        pass
