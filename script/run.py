from excel_lesen import readSrcFile, readSrcFileColumn
from duplikateSuchen import *
from var import *

readSrcFileColumn(ExcelSrc, repNummern, 2)

#print(repNummern)

chForDup(repNummern)
