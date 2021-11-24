from excel.excel_lesen import readSrcFile, readSrcFileColumn
from excel.duplikateSuchen import *
from settings.var import *

readSrcFileColumn(ExcelSrc, repNummern, 2)

#print(repNummern)

chForDup(repNummern)
