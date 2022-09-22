import xlwings as xw

wb = xw.Book('data.xlsx')
wks = xw.sheets # Viewing avaiable data in sheet
print("\nAvailable sheets :\n", wks)
ws = wks[0] # Selecting a sheet
columns = ws.range("A1:A4").value
print("\nA value in sheet1 :", columns)

for column in columns:

	if column == 'a':
		print ('P')
	else:
		print ('F')
		
	if column == 'geeks.com':
		print ('P')
		print('\nCurrent Value is = ', column)
	else:
		print ('F')
		


ws.range("B2").value = ["asd"] # Write value into a single cell

columns = ws.range("A:A").value
print("\nA value in sheet1 :", columns)
