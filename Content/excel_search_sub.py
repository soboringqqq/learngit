import xlwings as xw
# import excel_select

def excel_search_s(columns_ESS, columns_ESS_Name, columns_ALL):
	"""Return Result"""
	global E_Contents
	E_Contents = [] # dic for Electrical Standard
	E_Content_flag = 0 
	Column_temp = [] # temp store found Electrical Standard
	E_Found = [] # Found Electrical Standard
	E_NotFound = [] # Not Found Electrical Standard
	
	
	for E_Content_number in range(len(columns_ESS_Name)): # Create empty dic
		new_E_Content = {'Code': 'place', 'Name': 'place', 'Expired': 'place'} # two element
		E_Contents.append(new_E_Content)
	
	
	
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
			column_buffer= column
			try:
				column_buffer = ''.join(column_buffer.split())
			except AttributeError:
				"1" # nothing happned
			if column_buffer == None:
				"1"
			elif column_buffer == columns_ES_buffer:
				
				Column_temp.append(columns_ES_buffer)
			
	
	return Column_temp, E_Content_flag, E_Contents

# excel_search

def excel_print(Column_temp, E_Content_flag, E_Contents):
	"""Print Result"""
	E_Found = [] # Found Electrical Standard
	E_NotFound = [] # Not Found Electrical Standard
	print("""==============================================================================""")
	print("\n             Found Electrical Standard\n")
	for i in range(E_Content_flag):
		if E_Contents[i]['Code'] in Column_temp:
			# print(E_Contents[i])
			E_Contents[i]['Expired'] = 'F'
			E_Found.append(E_Contents[i])
		else:
			# print(E_Contents[i])
			E_Contents[i]['Expired'] = 'T'
			E_NotFound.append(E_Contents[i])
	
	# print("\n", Column_temp_Not)
	
	
	for i in range(len(E_Found)):
		print(E_Found[i])
	
	print("""==============================================================================""")
	print("\n            Not Found Electrical Standard\n")
	
	for i in range(len(E_NotFound)):
		print(E_NotFound[i])
		
	return E_Found, E_NotFound



def excel_search_ss(columns_ES_buffer, columns_ALL):
	"""Return Result"""
	Column_temp = []
	for column in columns_ALL:
		column_buffer = column
		try:
			column_buffer = ''.join(column_buffer.split())
		except AttributeError:
			"1" # nothing happned
		if column_buffer == None:
			"1"
		elif column_buffer == columns_ES_buffer:

			Column_temp.append(columns_ES_buffer)
			
	return Column_temp
