from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt




def getOneFile(inputFile):
    result = []
    inf = open(inputFile)
    line = inf.readline()
    i = 0
    while line:
        line = line.strip()
        if i == 1:
            result.append(dealLine(line))
        if line.find('coveredNum')  >= 0:
            i = 1
        else:
            i = 0
        line = inf.readline()
    inf.close()
    return result

def dealLine(strs):
    dic = {}
    strlist = strs.split(')  (')
    for sp in strlist:
        sp = sp.strip('(')
        sp = sp.strip(')')
        strlist2 = sp.split(' : ')
        dic[int(strlist2[0])] = int(strlist2[1])
    return dic


def avgerage(f, dicList):
    dicAll = {}
    dicAvg = {}
    for dic in dicList:
        for key in dic.keys():
            if key not in dicAll.keys():
                dicAll[key] = []
            dicAll[key].append(dic[key])

    for key in dicAll.keys():
        dicAvg[key] = round(float(sum(dicAll[key]))/float(len(dicList)), 3)

    printDicAvg(dicAvg, f)

def printDicAvg(dic,f):
    f.write('way\n')
    for key in dic.keys():
        f.write('(')
        f.write(str(key) + ' : ')
        f.write(str(dic[key])+ ') ')
    f.write('\n')
   
                
if __name__ == "__main__":

    subject = [' for Tomcat',' for HSQLDB', ' for Gcc', ' for JFlex', ' for Tcas' ]

    approach2 = ['fd', 'ICT_FB_MUOFOT', 'sct']
    way = ['2-way', '3-way','4-way']

    txt = '.txt'

    folder = ['five', 'mfs', 'op']

    for app in approach2:
        for sub in subject:
            filename = 'five\/' + app + 'statistic' + sub + txt
            f = open(filename, 'w')
            f.write('')


            for wa in way:
                frname = app + wa + sub+txt
                result = getOneFile(frname)
                avgerage(f, result)

            f.close()

    print('over')
