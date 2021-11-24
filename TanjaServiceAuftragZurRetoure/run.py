from re import search
from listenVergleichen import compareLists
from regex import searchSR
from settings import *
from csv_einlesen import *
from listeBearbeiten import *
from csv_create_and_write import *

opencsv(srcBO, dstBO)
opencsv(srcBuHa, dstBuHa)
retZusammengesetzt(dstBuHa)
createNewCsv('1_BuHaSourceFileinclZusammengesetzterRetourenNummer.csv', dstBuHa)
retZusammengesetzt(dstBO)
compareLists(dstBuHa, dstBO, dstBOBuHa)
print(dstBOBuHa[1])
searchSR(dstBOBuHa)
createNewCsv('2_Retoure_incl_SR_.csv',dstBoBuHaSR)
buHaFileInklSrNummer(dstBuHa, dstBoBuHaSR)
createNewCsv('3_BuHaSrcFileInclSR.csv', dstBuHa)
for el in dstBuHa:
    print(el)
