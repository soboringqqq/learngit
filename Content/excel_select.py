import xlwings as xw

# global E_Contents

def excel_select(sheet):
	"""Return search result."""
	
	ES = xw.Book('Electrical_Standard_2022_10.xls').sheets[int(sheet)]
	
	return sheet
	


# qwe = excel_select(0)
# print(qwe)
# print(columns_ESS)
# qwe = excel_select(0)
# print(qwe)
