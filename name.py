import xlrd
file_location="names.xlsx"
workbook=xlrd.open(file_location)
sheet=workbook.sheet_by_index(0)
