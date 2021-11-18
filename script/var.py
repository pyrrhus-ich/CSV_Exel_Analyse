import os


workDir = os.getcwd()

ExcelSrc = workDir + "\\src\\" + os.listdir(workDir + "\\src\\")[0]
srcList = []  #Liste bestehend aus allen Zeilen des Excelfiles
repNummern = [] # Liste mit allen Reparaturnummern
duplicates = []