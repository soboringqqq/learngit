import xlwings as xw

global E_Contents
E_Contents = [] # dic for Electrical Standard
E_Content_flag = 0 
Column_temp = [] # temp store found Electrical Standard

ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[1]
ALL = xw.Book('ALL_STANDARD_2022_09.xlsx').sheets[0]

columns_ESS = ES.range("B4:B30").value
columns_ESS_Name = ES.range("C4:C30").value
columns_ALL = ALL.range("B1:B3000").value

print(columns_ESS_Name)

# E_Contents = {'Code': 'qwe', 'Name': 'asd'} 
# print(E_Contents['Code'])

# print(len(columns_ESS_Name))

for E_Content_number in range(len(columns_ESS_Name)):
	new_E_Content = {'Code': 'place', 'Name': 'place'}
	E_Contents.append(new_E_Content)

for E in E_Contents[:5]:
	print(E)
print(len(E_Contents))


for columns_ES in columns_ESS:
	columns_ES_buffer = columns_ES
	
	try:
		columns_ES_buffer = ''.join(columns_ES_buffer.split())
		# print(columns_ES_buffer)
		E_Contents[E_Content_flag]['Code'] = columns_ES_buffer
		E_Contents[E_Content_flag]['Name'] = columns_ESS_Name[E_Content_flag]
		E_Content_flag = E_Content_flag + 1
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
			# print ('P')
			print(columns_ES_buffer)
			Column_temp.append(columns_ES_buffer)


print("""==============================================================================""")
print("\n             Found Electrical Standard\n")
for i in range(E_Content_flag):
	if E_Contents[i]['Code'] in Column_temp:
		print(E_Contents[i])
	



