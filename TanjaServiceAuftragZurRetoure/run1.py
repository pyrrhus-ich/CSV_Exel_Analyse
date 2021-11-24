from settings import *
from csv_verarbeiten import *
from listeBearbeiten import *


print(srcBuHa)
opencsv(srcBuHa,eingelesenBuHa )
print("Anzahl Zeilen Ursprungsfile {}".format(len(eingelesenBuHa)))
sortiereAuftragsnummernZIR(eingelesenBuHa, korrekteAuftragsnummer, inkorrekteAuftragsnummern)
print("Anzahl Zeilen Ursprungsfile {}".format(len(eingelesenBuHa)))
print("Anzahl Zeilen korrekteAuftragsnummern {}".format(len(korrekteAuftragsnummer)))
print("Anzahl Zeilen inkorrekteAuftragsnummern {}".format(len(inkorrekteAuftragsnummern)))
durchsucheInkorrekteAufträge(inkorrekteAuftragsnummern, korrekteAuftragsnummer, 10)
print("Anzahl Zeilen korrekteAuftragsnummern {}".format(len(korrekteAuftragsnummer)))
print("Anzahl Zeilen inkorrekteAuftragsnummern {}".format(len(inkorrekteAuftragsnummern)))
createAndWriteCsv(korrekteAuftragsnummer, "ZIR_korrekte_Auftragsnummer_aus_Mappe2.csv")
durchsucheInkorrekteAufträge(inkorrekteAuftragsnummern, korrekteAuftragsnummer, 11)
print("Anzahl Zeilen korrekteAuftragsnummern {}".format(len(korrekteAuftragsnummer)))
print("Anzahl Zeilen inkorrekteAuftragsnummern {}".format(len(inkorrekteAuftragsnummern)))
#print(inkorrekteAuftragsnummern)