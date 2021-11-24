from settings import *


def compareLists(srcBuHa, srcBO, dstVar):
    cnt = 0
    print(len(srcBuHa))
    print(len(srcBO))
    for el in srcBuHa:
        for ele in srcBO:
            if el[2] == ele[2]:
                cnt+=1
                dstVar.append(ele)
    print(cnt)




