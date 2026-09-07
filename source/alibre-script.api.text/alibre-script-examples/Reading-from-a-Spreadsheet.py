#https://help.alibre.com/articles/#!alibre-help-v23/reading-from-a-spreadsheet
from openpyxl import load_workbook
# open a workbook, replace with your own path
wb = load_workbook(filename = 'C:\\Users\\<username>\\Downloads\\Book1.xlsx')
# get access to the sheet
Sheet1 = wb['Sheet1']
# get the value in cell C3
print Sheet1['C3'].value