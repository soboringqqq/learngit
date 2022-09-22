import xlwings as xw

ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[1]
#ESS = xw.sheets # Viewing avaiable data in sheet

ALL = xw.Book('ALL_STANDARD_2022_09.xlsx').sheets[1]
print("\nAvailable sheets :\n", ES)
print("\nAvailable sheets :\n", ALL)
# ws = ESS[1] # Selecting a sheet [1] second sheet Only read current excel file

#columns = ES.range("B:B").value
#print("\nA value in sheet1 :", columns)

# automatic = ws.range("B4").expand().value
# print("Automatic Table :", automatic)

columns = ALL.range("B2:B3000").value
#print("\nA value in sheet 1 :", columns)
#columns = ''.join(columns.split()) # remove space between string

for column in columns:
	column_buffer = column
	try:
		column_buffer = ''.join(column_buffer.split())
	except AttributeError:
		"1" # nothing happned

	if column_buffer == 'DL/T666-2012':
		print ('P')
