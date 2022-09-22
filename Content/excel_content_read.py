import xlwings as xw

wb = xw.Book('Electrical_Standard_2022_10.xls')
wks = xw.sheets # Viewing avaiable data in sheet
print("\nAvailable sheets :\n", wks)
ws = wks[1] # Selecting a sheet [1] second sheet 

columns = ws.range("B4:B13").value
print("\nA value in sheet1 :", columns)

# automatic = ws.range("B4").expand().value
# print("Automatic Table :", automatic)
