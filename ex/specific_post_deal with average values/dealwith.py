from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


class item:
    def __init__(self):
        self.numAll = 0
        self.num_r = 0
        self.num_i = 0
        self.recall = 0
        self.precise = 0
        self.f_measure = 0
        self.multi = 0
        self.time = 0
        self.time_r = 0
        self.time_i = 0
        self.t_cover = 0
        self.all_cover = 0
        self.CoverNUM = ''

def getOneFile(inputFile):
    result_2way = item()
    result_3way = item()
    result_4way = item()
    result = []
    result.append(result_2way)
    result.append(result_3way)
    result.append(result_4way)
    inf = open(inputFile)
    line = inf.readline()
    i = - 1
    while line:
        line = line.strip()
        if line.find('way')  >= 0:
            i = i + 1
        if i >= 0 and i <= 2:
            dealLine(result[i], line)
        line = inf.readline()
    inf.close()
    return result

def dealLine(result, strs):
    if strs.find('average') >= 0:
        strlist = strs.split(':')
        if strs.find('num_r') >= 0:
            result.num_r = float(strlist[1])
        elif strs.find('num_i')>= 0:
            result.num_i = float(strlist[1])
        elif strs.find('num ')>=0:
            result.numAll = float(strlist[1])
        elif strs.find('recall')>=0:
            result.recall = float(strlist[1])
        elif strs.find('precise')>=0:
            result.precise  = float(strlist[1])
        elif strs.find('f-measure')>=0:
            result.f_measure = float(strlist[1])
        elif strs.find('multi')>=0:
            result.multi = float(strlist[1])
        elif strs.find('time ')>=0:
            result.time = float(strlist[1])
        elif strs.find('time_r')>=0:
            result.time_r = float(strlist[1])
        elif strs.find('time_i')>=0:
            result.time_i = float(strlist[1])
        elif strs.find('t_cover')>=0:
            result.t_cover = float(strlist[1])
        elif strs.find('all_cover')>=0:
            result.all_cover = float(strlist[1])
    elif strs.find('(') >= 0 and strs.find('[') < 0:
        result.CoverNUM = strs
    return result


def showResult(result):
    for i in range(0,3):
        print(str(i+2) + ' way :')
        print(result[i].numAll)
        print(result[i].CoverNUM)


def getStrong(num, numTobeCompared, biggerOrSmall):
    if numTobeCompared == -1:
        return str(round(num,2)) 
    if num > numTobeCompared:
        if biggerOrSmall == 0:  #smaller
            return str(round(num,2))
        else:   #stress strong one
            return "\\textbf{" + str(round(num,2)) +"}"
    elif num < numTobeCompared:
        if biggerOrSmall == 0:  #smaller
            return "\\textbf{" + str(round(num,2)) +"}"
        else:   #stress strong one
            return str(round(num,2))
    else:
        return str(round(num,2))


def getStrongPerCent(num, numTobeCompared, biggerOrSmall):
    if numTobeCompared == -1:
        return str("{:.2%}".format(num).replace('%','\%')) 
    if num > numTobeCompared:
        if biggerOrSmall == 0:  #smaller
            return str(round(num,2))
        else:   #stress strong one
            return "\\textbf{" + str("{:.2%}".format(num).replace('%','\%')) +"}"
    elif num < numTobeCompared:
        if biggerOrSmall == 0:  #smaller
            return "\\textbf{" + str("{:.2%}".format(num).replace('%','\%'))   +"}"
        else:   #stress strong one
            return str("{:.2%}".format(num).replace('%','\%'))  
    else:
        return str("{:.2%}".format(num).replace('%','\%')) 

    
                
if __name__ == "__main__":


    showresultApp = ['fd','ict','sct']
    showresultSub =['Tomcat', 'Hsqldb', 'Gcc', 'Jflex', 'Tcas']

    approach = ['fdstatistic', 'ICT_FB_MUOFOTstatistic', 'sctstatistic']
    subject = [' for Tomcat',' for HSQLDB', ' for Gcc', ' for JFlex', ' for Tcas' ]


    syn = ' for Syn'
    senMFS = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90']
    senOptions = ['8','9','10','12','16','20','30','40','50','60','70','80','90','100']

    txt = '.txt'

    folder = ['five', 'mfs', 'op']

    print('')
    print('covered num')
    for sub in subject:
        filesNames = ['cover_num\/2-way' + sub + txt,'cover_num\/3-way' + sub + txt,'cover_num\/4-way' + sub + txt]
        files = []
        for k in range(0,3):
            f = open(filesNames[k], 'w')
            f.write('')
            files.append(f)
        for j in [1,2,0]:
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            for i in range(0, 3):
                files[i].write(result[i].CoverNUM + '\n')
                files[i].write('\n')

        for k in range(0,3):
            files[k].close()
    print('write to files in cover_num')
