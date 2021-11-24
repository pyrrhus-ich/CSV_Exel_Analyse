from var import *


def chForDup(src):
    a=len(src)
    b=len(set(src))
    if len(src) == len(set(src)):
        print("Keine Duplikate vorhanden")
        print("Länge src : " + str(a))
        print("Länge bereinigt Liste : " + str(b))
        print("Anzahl Duplikate : " + str(a-b))
    else:
        print("Anzahl der Duplikate : " + str(len(src) - len(set(src))))

def crDupList(src, dst):
    for val in src:
        for el in src:
            if val == el:
                dst.append(el)
