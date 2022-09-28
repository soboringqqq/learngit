import xlwings as xw
import excel_select
import excel_search_perform as excel_s

E_NotFound = excel_s.excel_search(1, 0)

columns_ALL = excel_select.excel_select_A( 2 )
excel_s.excel_search_NotF(E_NotFound ,columns_ALL)
