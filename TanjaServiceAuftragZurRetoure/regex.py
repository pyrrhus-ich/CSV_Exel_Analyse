import re
from settings import dstBOBuHa, dstBoBuHaSR
list = ["M037-190480843", "FrMank","S027-196841645", "M199-Frank" ]

#Sucht alle 
def searchSR(src):
    for el in src:
        if len(el[5]) == 13:
            #print("el[5] = " +el[5])
            el[5] = el[5].replace("-T-","-")
            dstBoBuHaSR.append(el)
            #print("el[5] replaced : " + el[5])

        
                
        
        

