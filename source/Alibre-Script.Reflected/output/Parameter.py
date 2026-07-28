class Parameter:
    def __init__(self, Name, Comment, Equation, ExcelWorkbook, ExcelSheet, ExcelCell, Type, Units, Value, RawValue):
        pass
        self.Name = Name
        self.Comment = Comment
        self.Equation = Equation
        self.ExcelWorkbook = ExcelWorkbook
        self.ExcelSheet = ExcelSheet
        self.ExcelCell = ExcelCell
        self.Type = Type
        self.Units = Units
        self.Value = Value
        self.RawValue = RawValue
    def AttachToExcel(self,StringDocument,StringSheet,StringCell,UnitTypesUnits):
        pass
