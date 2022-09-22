import xlwings as xw

wb = xw.Book('data.xlsx')

wks = xw.sheets # Viewing avaiable data in sheet

print("\nAvailable sheets :\n", wks)

ws = wks[0] # Selecting a sheet

val = ws.range("A1").value # Selecting a value "A1"

print("\nA value in sheet1 :", val)

columns = ws.range("A1:A4").value

print("\nA value in sheet1 :", columns)
