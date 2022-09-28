import xlwings as xw

# global E_Contents

def excel_select_E(sheet):
	"""Return search result."""
	
	ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[int(sheet)]
	columns_ESS = ES.range("B4:B30").value
	columns_ESS_Name = ES.range("C4:C30").value
	
	return columns_ESS, columns_ESS_Name
	
def excel_select_A(sheet):
	"""Return search result."""
	
	ALL = xw.Book('ALL_STANDARD_2022_09.xlsx').sheets[int(sheet)]
	columns_ALL = ALL.range("B1:B3000").value
	
	return columns_ALL
	


# qwe = excel_select(0)
# print(qwe)
# print(columns_ESS)
# qwe = excel_select(0)
# print(qwe)
