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
                
if __name__ == "__main__":

    approach = ['fdstatistic', 'ICT_FB_MUOFOTstatistic', 'sctstatistic']
    subject = [' for Tomcat',' for HSQLDB', ' for Gcc', ' for JFlex', ' for Tcas' ]


    syn = ' for Syn'
    senMFS = ['1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90']
    senOptions = ['8','9','10','12','16','20','30','40','50','60','70','80','90','100']

    txt = '.txt'

    folder = ['five', 'mfs', 'op']

    print('test Cases')
    for sub in subject:
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            for i in range(0, 3):
                print(str(round(result[i].num_r,2)) +'\t'+ str(round(result[i].num_i,2)) + '\t' +str(round(result[i].numAll,2)) +'\t', end= '')
            print('')

    print('')
    print('identification quality')
    for sub in subject:
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            for i in range(0, 3):
                print(str(round(result[i].precise,2)) +'\t'+ str(round(result[i].recall,2)) + '\t' +str(round(result[i].f_measure,2)) +'\t', end= '')
            print('')

    print('')
    print('multi')
    for sub in subject:
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            for i in range(0, 3):
                print(str(round(result[i].multi,2)) +'\t', end= '')
            print('')
            
    print('')
    print('tested-t-way')
    for sub in subject:
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            for i in range(0, 3):
                print(str(round(result[i].t_cover,2)) + '(' + str(result[i].t_cover/result[i].all_cover) +')'+'\t', end= '')
            print('')
