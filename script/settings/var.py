import os


workDir = os.getcwd()

ExcelSrc = workDir + "\\files\\src\\" + os.listdir(workDir + "\\files\\src\\")[0]
srcList = []  #Liste bestehend aus allen Zeilen des Excelfiles
repNummern = [] # Liste mit allen Reparaturnummern
duplicates = []