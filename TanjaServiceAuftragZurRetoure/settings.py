import os


workDir = os.getcwd()
srcBuHa=workDir + "\\" + "Mappe2.csv"
eingelesenBuHa=[] # BuHa src File als Liste - Basis für alle weiteren Aktionen
korrekteAuftragsnummer=[]
korrekteAuftragsnummerZir=[]
korrekteAuftragsnummerPP=[]
inkorrekteAuftragsnummern=[]


dstBO=[]  # BO src File als Liste - Basis für alle weiteren Aktionen
dstBOBuHa=[] #Speichert die rows aus dem BOFile die auch im BuHaFile vorhanden sind
dstBoBuHaSR=[] #speichert alle rows aus "dstBOBuHa" die in Spalte 5 eine SR Nummer enthalten
#BuHaInklSRNummer=[] # Speichert Tanjas Liste incl. SR Nummer
srcBO = workDir + "\\" + "Retoure_Infotext.csv"