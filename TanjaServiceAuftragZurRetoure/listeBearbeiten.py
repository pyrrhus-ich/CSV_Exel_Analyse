from settings import *


#durchsucht die eingelesene Liste nach Übereinstimmungen mit ZIR SR Nummern
def sortiereAuftragsnummernZIR(ursprungsListe, korrekteAufträge, inkorrekteAufträge):
    for el in ursprungsListe:
        if el[0][0] == "S" or el[0][0]=="M" and len(el[0]) <= 11:
            var = el[0]
            if var.endswith("-"):
                zirEl = var.rstrip("-")
                korrekteAufträge.append(zirEl)
            else:
                inkorrekteAufträge.append(el)

def durchsucheInkorrekteAufträge(urprungsliste, korrekteAufträge):
    for el in urprungsliste:
        if el[0][0] == "S" or el[0][0]=="M" and len(el[0]) == 10:
            if el[0][4]== "-":
                korrekteAufträge.append(el[0])
                inkorrekteAuftragsnummern.remove(el)












# Baut die eindeutige Retourennummer im Format M199-12345687 zusammen und fügt sie am index 2 in 
# das entsprechende List element ein
def retZusammengesetzt(src):
    for el in src:
        dst_el=""
        if len(el[0])==4:
            dst_el=str(el[0]) + "-"+ str(el[1])
            el.insert(2, dst_el)
        else: # Wenn der SAP Code nicht M199 sondern M1990000 ist
            el[0]=el[0][0:4] # schneidet M1990000 zu M199
            dst_el=str(el[0]) + "-"+ str(el[1])
            el.insert(2, dst_el)

def buHaFileInklSrNummer(srcBuHa, srcBO):
    for el in srcBuHa:
        for ele in srcBO:
            if el[2] == ele[2]:
                if len(el) == 4:
                    print(el)
                else:
                    if len(ele[5]) == 11:
                            #print(len(ele[5]))
                            #print(ele[5])
                            el.append(ele[5])
                    else:
                        el.append("-")

    


