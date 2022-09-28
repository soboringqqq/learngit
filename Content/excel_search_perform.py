import xlwings as xw
import excel_search_sub
import excel_select


def excel_search(E_sheet, A_sheet):
	"""Return Result"""
	global E_Contents
	E_Contents = [] # dic for Electrical Standard
	E_Content_flag = 0 
	Column_temp = [] # temp store found Electrical Standard
	E_Found = [] # Found Electrical Standard
	E_NotFound = [] # Not Found Electrical Standard
	E_NotFoundC = []
	
	columns_ESS, columns_ESS_Name = excel_select.excel_select_E(E_sheet)
	columns_ALL = excel_select.excel_select_A(A_sheet)
	
	
	
	
	Column_temp, E_Content_flag, E_Contents = excel_search_sub.excel_search_s(columns_ESS, columns_ESS_Name, columns_ALL)
	
	
	
	E_Found, E_NotFound = excel_search_sub.excel_print(Column_temp, E_Content_flag, E_Contents)
	
	
	# if Flag == True:
		# for i in range(len(E_NotFound)):
			# E_NotFoundC = excel_search_sub.excel_search_ss(E_NotFound[i]['Code'], columns_ALL)
			# print(E_NotFound[i]['Code'])
		
		# print(123)
	
# excel_search
	return E_NotFound
	
def excel_search_NotF(E_NotFound, columns_ALL):
	"""Search Not Found"""
	E_Found = []
	for column in columns_ALL:
		column_buffer= column
		try:
			column_buffer = ''.join(column_buffer.split())
		except AttributeError:
			"1" # nothing happned
		# if column_buffer == None:
			# "1"
		# elif column_buffer == columns_ES_buffer:
				
			# Column_temp.append(columns_ES_buffer)
		for i in range(len(E_NotFound)):
			if E_NotFound[i]['Code'] == column_buffer:
				E_Found.append(column_buffer)
	print(E_Found)
			
