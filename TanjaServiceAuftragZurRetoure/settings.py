import os


workDir = os.getcwd()
srcBO = workDir + "\\" + "Retoure_Infotext.csv"
srcBuHa=workDir + "\\" + "822644_11.11.2021_SAP_BA.csv"

dstBO=[]  # BO src File als Liste - Basis für alle weiteren Aktionen
dstBuHa=[] # BuHa src File als Liste - Basis für alle weiteren Aktionen
dstBOBuHa=[] #Speichert die rows aus dem BOFile die auch im BuHaFile vorhanden sind
dstBoBuHaSR=[] #speichert alle rows aus "dstBOBuHa" die in Spalte 5 eine SR Nummer enthalten
#BuHaInklSRNummer=[] # Speichert Tanjas Liste incl. SR Nummer
