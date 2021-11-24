import os


workDir = os.getcwd()

ExcelSrc = workDir + "\\src\\" + os.listdir(workDir + "\\src\\")[0]
srcList = []  #Liste bestehend aus allen Zeilen des Excelfiles
repNummern = [] # Liste mit allen Reparaturnummern
wgrNames=[] # Liste mit den Namen der Warengruppen
lstWgr=set(wgrNames)
duplicates = []