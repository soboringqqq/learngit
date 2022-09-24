import xlwings as xw
# import excel_select

global E_Contents
E_Contents = [] # dic for Electrical Standard
E_Content_flag = 0 
Column_temp = [] # temp store found Electrical Standard
E_Found = [] # Found Electrical Standard
E_NotFound = [] # Not Found Electrical Standard

ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[1]
ALL = xw.Book('ALL_STANDARD_2022_09.xlsx').sheets[0]

columns_ESS = ES.range("B4:B30").value
columns_ESS_Name = ES.range("C4:C30").value
columns_ALL = ALL.range("B1:B3000").value

# print(columns_ESS_Name)

# E_Contents = {'Code': 'qwe', 'Name': 'asd'} 
# print(E_Contents['Code'])

# print(len(columns_ESS_Name))

for E_Content_number in range(len(columns_ESS_Name)): # Create empty dic
	new_E_Content = {'Code': 'place', 'Name': 'place'} # two element
	E_Contents.append(new_E_Content)

# for E in E_Contents[:5]:
	# print(E)
# print(len(E_Contents))


for columns_ES in columns_ESS:
	columns_ES_buffer = columns_ES
	
	try:
		columns_ES_buffer = ''.join(columns_ES_buffer.split())
		# print(columns_ES_buffer)
		E_Contents[E_Content_flag]['Code'] = columns_ES_buffer # add Code 
		E_Contents[E_Content_flag]['Name'] = columns_ESS_Name[E_Content_flag] # add Name
		E_Content_flag = E_Content_flag + 1
	except AttributeError: # This is only for preventing program to crash
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
			# print(columns_ES_buffer)
			Column_temp.append(columns_ES_buffer)
		
				
		# elif column_buffer != columns_ES_buffer and column_buffer != None:
			# Column_temp_Not.append(columns_ES_buffer)
			# # print(Column_temp_Not)
			


print("""==============================================================================""")
print("\n             Found Electrical Standard\n")
for i in range(E_Content_flag):
	if E_Contents[i]['Code'] in Column_temp:
		# print(E_Contents[i])
		E_Found.append(E_Contents[i])
	else:
		# print(E_Contents[i])
		E_NotFound.append(E_Contents[i])

# print("\n", Column_temp_Not)


for i in range(len(E_Found)):
	print(E_Found[i])

print("""==============================================================================""")
print("\n            Not Found Electrical Standard\n")

for i in range(len(E_NotFound)):
	print(E_NotFound[i])



