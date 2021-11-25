import csv

#<<<<<<< Hier wird das CSV File eingelesen und in Liste gespeichert>>>>>>>>>>>
def opencsv(srcFile, dstFile):
    with open(srcFile) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=';')
        for row in csvReader:
            dstFile.append(row)





    






    

