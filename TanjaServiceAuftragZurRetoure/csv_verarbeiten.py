import csv

#<<<<<<< Hier wird das CSV File eingelesen und in Liste gespeichert>>>>>>>>>>>
def opencsv(basisDatei, zielListe):
    with open(basisDatei) as csvFile:
        csvReader = csv.reader(csvFile, delimiter='R')
        for row in csvReader:
            zielListe.append(row)


# erstellt das Zielfile (ohne Kopfzeile) und schreibt Zeile für Zeile die korrekte Nummer rein
def createAndWriteCsv(basisListe, zieldatei):
    with open(zieldatei,'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        kopfzeile=["Zir Auftragsnummer"]
        writer.writerow(kopfzeile)
        for auftragsNummer in basisListe:
            zeile=[]
            zeile.append(auftragsNummer)
            writer.writerow(zeile)









    






    

