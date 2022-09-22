import xlwings as xw

ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[1]
ALL = xw.Book('ALL_STANDARD_2022_09.xlsx').sheets[0]

columns_ESS = ES.range("B1:B30").value
columns_ALL = ALL.range("B1:B3000").value

for columns_ES in columns_ESS:
	columns_ES_buffer = columns_ES
	try:
		columns_ES_buffer = ''.join(columns_ES_buffer.split())
		#print(columns_ES_buffer)
	except AttributeError:
		"1" # nothing happned
		
	for column in columns_ALL:
		column_buffer = column
		try:
			column_buffer = ''.join(column_buffer.split())
		except AttributeError:
			"1" # nothing happned
		if column_buffer == None:
			"1"
		elif column_buffer == columns_ES_buffer:
			print ('P')
			print(columns_ES_buffer)
		#print(column_buffer)
		#if column_buffer == columns_ES_buffer:
			#print ('P')
	
		





# for column in columns_ALL:
	# column_buffer = column
	# try:
		# column_buffer = ''.join(column_buffer.split())
	# except AttributeError:
		# "1" # nothing happned

	# if column_buffer == columns_ES:
		# print ('P')

