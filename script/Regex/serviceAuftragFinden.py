import re


text = """Wir versuchen M444-1234 zu finden oder M555-12345 oder M666-123456 oder M777-1234567
        und M666125894/1900  und M555123458 oder MM23-12345  oder R123-12345 auszuschliessen"""
x = text.split() # splittet den Text in elemente auf über die iteriert werden kann
for el in x: print("Element an Index {} ist : -{}".format(x.index(el), el))
reparaturAuftragsnummer = r"^[M|S]{1}[0-9]{3,3}-[0-9]{5,6}" # definiert die Suchkriterien

														   
# ^[M|S]{1}  - startet mit großem M oder S genau 1 x
# [0-9]{3,3} - Zahlen zwischen 0 und 9 mindestens 3 und maximal 3 mal
# - Bindestrich an 4. Stelle
# [0-9]{5,6} wenigstens 5 mal maximal 6 mal

# Problem : der letzte Step funktioniert insofern, das zwar Elemente kürzer 5 nicht ausgegeben werden
# Elemente gößer 6 aber abgeschnitten und dann ausgegeben werden Das umgehe ich in der for Schleife
# indem ich vorher abfrage das Länge Element <= 11 ist. (10-ZIR, 11-PP)

				

for el in x:
    if len(el) <=11:
        y = re.findall(reparaturAuftragsnummer, el)
        if y:
            print("Folgende Nr. wurde gefunden : {}".format(y))
