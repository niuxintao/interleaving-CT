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
        self.wcheck = 0
        self.widen = 0

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
        elif strs.find('multi ')>=0:
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
        elif strs.find('w check')>=0:
            result.wcheck = float(strlist[1])
        elif strs.find('w iden')>=0:
            result.widen = float(strlist[1])
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


    showresultApp = ['ict','sct', 'fd']
    showresultSub =['hsqldb 2.0rc', 'hsqldb 2.25', 'hsqldb 2.29', 'Jflex 1.4.1', 'Jflex 1.4.2']

    approach = ['ICT_FB_MUOFOTstatistic', 'sctstatistic', 'fdstatistic']
    subject = [' for hsqldb 2.0rc',' for hsqldb 2.25', ' for hsqldb 2.29', ' for jflex 1.4.1', ' for jflex 1.4.2' ]

    txt = '.txt'

    folder = ['multipleDefects']

    print('test Cases')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
            
        for j in range(0, 3):
            result = results[j]
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].numAll,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].numAll,2)) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')


    print('test Cases reduction')
    decreasek = []
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        decreasek.append([])
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
        #methods
        u = -1
        for j in range(0, 3):
            result = results[j]
            for h in range(0, 3):
                if h > j:
                    decreasek[k].append([])
                    u = u+1
                    #print('compare' + ssub[j] + '' + ssub[h])
                    result2 = results[h]
                    #degree
                    for i in range(0, 3):
                        #print(str(i+2)+'way')
                        decreasek[k][u].append(result[i].numAll - result2[i].numAll)
    decreseAvg = []
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                u = u+1
                decreseAvg.append([])
                for i in range (0, 3):
                    avg = 0
                    for k in range(5):
                        avg += decreasek[k][u][i]
                    avg /= 5
                    decreseAvg[u].append(avg)
            
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                 print('compare' + showresultApp[j] + '' + showresultApp[h])
                 u = u+1
                 for i in range (0, 3):
                     print(str(round(decreseAvg[u][i], 2)) + '\t', end= '' )
                 print('')

    print('')
    print('identification quality')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
            
        for j in range(0,3):
            result = results[j]
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].f_measure, 2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].f_measure, 2)) +'\t\\\\', end= '')
            if(j == 3):
                print('\\hline')
            else:
                print('')


    print('MFS identification increasing')
    decreasek = []
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        decreasek.append([])
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
        #methods
        u = -1
        for j in range(0, 3):
            result = results[j]
            for h in range(0, 3):
                if h > j:
                    decreasek[k].append([])
                    u = u+1
                    #print('compare' + ssub[j] + '' + ssub[h])
                    result2 = results[h]
                    #degree
                    for i in range(0, 3):
                        #print(str(i+2)+'way')
                        decreasek[k][u].append(result[i].f_measure - result2[i].f_measure)
    decreseAvg = []
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                u = u+1
                decreseAvg.append([])
                for i in range (0, 3):
                    avg = 0
                    for k in range(5):
                        avg += decreasek[k][u][i]
                    avg /= 5
                    decreseAvg[u].append(avg)
            
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                 print('compare' + showresultApp[j] + ' ' + showresultApp[h])
                 u = u+1
                 for i in range (0, 3):
                     print(str(round(decreseAvg[u][i], 2)) + '\t', end= '' )
                 print('')

    print('')
    print('multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].multi,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].multi,2)) +'\t\\\\', end= '')
            if(j == 3):
                print('\\hline')
            else:
                print('')

    print('multi increasing')
    decreasek = []
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        decreasek.append([])
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
        #methods
        u = -1
        for j in range(0, 3):
            result = results[j]
            for h in range(0, 3):
                if h > j:
                    decreasek[k].append([])
                    u = u+1
                    #print('compare' + ssub[j] + '' + ssub[h])
                    result2 = results[h]
                    #degree
                    for i in range(0, 3):
                        #print(str(i+2)+'way')
                        decreasek[k][u].append(result[i].multi - result2[i].multi)
    decreseAvg = []
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                u = u+1
                decreseAvg.append([])
                for i in range (0, 3):
                    avg = 0
                    for k in range(5):
                        avg += decreasek[k][u][i]
                    avg /= 5
                    decreseAvg[u].append(avg)
            
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                 print('compare' + showresultApp[j] + ' ' + showresultApp[h])
                 u = u+1
                 for i in range (0, 3):
                     print(str(round(decreseAvg[u][i], 2)) + '\t', end= '' )
                 print('')



# all the masking effects are obtained by the generated test cases which contain multiple MFS, hence we just let the generated test cases to minus multiple, use num_r - multi or numAll - multi
    print('')
    print('non-maksing tests :  gen - multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
           # result = getOneFile(filename)
            result_temp = getOneFile(filename)
            results.append(result_temp)

        for j in range(0,3):
            result = results[j-1]
            result_2 = [ -1, -1, -1]
            if j == 1:
                result_2 = [results[j][0].num_r - results[j][0].multi,results[j][1].num_r - results[j][1].multi,results[j][2].num_r - results[j][2].multi,]
                
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(getStrong(result[i].num_r - result[i].multi,result_2[i],1) +'\t&', end= '')
                else:
                    print(getStrong(result[i].num_r - result[i].multi,result_2[i],1) +'\t\\\\', end= '')
            if(j == 3):
                print('\\hline')
            else:
                print('')




    print('')
    print('time')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].time,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].time,2)) +'\t\\\\', end= '')
            if(j == 3):
                print('\\hline')
            else:
                print('')
            
    print('')
    print('tested-t-way')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)

        for j in range(0,3):
            result = results[j]
            print(ssub[j] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                        print(str(round(result[i].t_cover, 2)) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t&', end= '')
                else:
                        print(str(round(result[i].t_cover, 2)) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t\\\\', end= '')
                #    print(getStrong(result[i].t_cover,result_2[i],1) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t\\\\', end= '')
            if(j == 3):
                print('\\hline')
            else:
                print('')

    print('t-cover increasing')
    decreasek = []
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        decreasek.append([])
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
        #methods
        u = -1
        for j in range(0, 3):
            result = results[j]
            for h in range(0, 3):
                if h > j:
                    decreasek[k].append([])
                    u = u+1
                    #print('compare' + ssub[j] + '' + ssub[h])
                    result2 = results[h]
                    #degree
                    for i in range(0, 3):
                        #print(str(i+2)+'way')
                        decreasek[k][u].append((result[i].t_cover - result2[i].t_cover)/max(result[i].t_cover,  result2[i].t_cover))
    decreseAvg = []
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                u = u+1
                decreseAvg.append([])
                for i in range (0, 3):
                    avg = 0
                    for k in range(5):
                        avg += decreasek[k][u][i]
                    avg /= 5
                    decreseAvg[u].append(avg)
            
    u = -1
    for j in range(0, 3):
        for h in range(0, 3):
            if h > j:
                 print('compare' + showresultApp[j] + ' ' + showresultApp[h])
                 u = u+1
                 for i in range (0, 3):
                     print(str(round(decreseAvg[u][i], 2)) + '\t', end= '' )
                 print('')



    print('')
    print('fd test cases')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        result = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            result.append(result_temp)
        print(showresultSub[k] + '\t&', end = '')
        for i in range(0, 3):
            if i < 2:
                print(str(round(result[0][i].numAll,2)) + '(' + getStrong(result[0][i].numAll - result[1][i].numAll,0,1) + ',' + getStrong(result[0][i].numAll - result[2][i].numAll,0,1)+  ')' +'\t&', end= '')
            else:
                print(str(round(result[0][i].numAll,2)) + '(' + getStrong(result[0][i].numAll - result[1][i].numAll,0,1) + ',' + getStrong(result[0][i].numAll - result[2][i].numAll,0,1)+  ')' +'\t\\\\', end= '')
        if(k == 4):
            print('\\hline')
        else:
            print('')

    print('')
    print('fd identification')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        result = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            result.append(result_temp)
        print(showresultSub[k] + '\t&', end = '')
        for i in range(0, 3):
            if i < 2:
                print(str(round(result[0][i].f_measure,2)) + '(' + getStrongPerCent(result[0][i].f_measure - result[1][i].f_measure,0,1) + ',' + getStrongPerCent(result[0][i].f_measure - result[2][i].f_measure,0,1)+  ')' +'\t&', end= '')
            else:
                print(str(round(result[0][i].f_measure,2)) + '(' + getStrongPerCent(result[0][i].f_measure - result[1][i].f_measure,0,1) + ',' + getStrongPerCent(result[0][i].f_measure - result[2][i].f_measure,0,1)+  ')' +'\t\\\\', end= '')
        #print('')
        if(k == 4):
            print('\\hline')
        else:
            print('')

    print('')
    print('fd multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        result = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            result.append(result_temp)
        print(showresultSub[k] + '\t&', end = '')
        for i in range(0, 3):
            if i < 2:
                print(str(round(result[0][i].multi,2)) + '(' + getStrong(result[0][i].multi - result[1][i].multi,0,1) + ',' + getStrong(result[0][i].multi - result[2][i].multi,0,1)+  ')' +'\t&', end= '')
            else:
                print(str(round(result[0][i].multi,2)) + '(' + getStrong(result[0][i].multi - result[1][i].multi,0,1) + ',' + getStrong(result[0][i].multi - result[2][i].multi,0,1)+  ')' +'\t\\\\', end= '')
        if(k == 4):
            print('\\hline')
        else:
            print('')

    print('')
    print('fd tested-t-way')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        result = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            result.append(result_temp)
        print(showresultSub[k] + '\t&', end = '')
        for i in range(0, 3):
            if i < 2:
                print(str(round(result[0][i].t_cover,2)) + '(' + getStrongPerCent(((result[0][i].t_cover - result[1][i].t_cover)/max(result[0][i].t_cover , result[1][i].t_cover)),0,1) + ',' + getStrongPerCent(((result[0][i].t_cover - result[2][i].t_cover)/max(result[0][i].t_cover , result[2][i].t_cover)),0,1)+  ')' +'\t&', end= '')
            else:
                print(str(round(result[0][i].t_cover,2)) + '(' + getStrongPerCent(((result[0][i].t_cover - result[1][i].t_cover)/max(result[0][i].t_cover , result[1][i].t_cover)),0,1) + ',' + getStrongPerCent(((result[0][i].t_cover - result[2][i].t_cover)/max(result[0][i].t_cover , result[2][i].t_cover)),0,1)+  ')' +'\t\\\\', end= '')
       # print('')
        if(k == 4):
            print('\\hline')
        else:
            print('')


    print('')
    print('fd non-maksing tests :  gen - multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        result = []
        for j in range(0,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            result.append(result_temp)
        print(showresultSub[k] + '\t&', end = '')
         #  print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
        for i in range(0, 3):
                if i < 2:
                    print(str(round(result[0][i].num_r - result[0][i].multi,2)) + '(' + getStrong((result[0][i].num_r - result[0][i].multi - (result[1][i].num_r - result[1][i].multi)),0, 0)+ ',' + getStrong((result[0][i].num_r - result[0][i].multi - (result[2][i].num_r - result[2][i].multi)),0, 0)+  ')' +'\t&',  end= '')
                else:
                    print(str(round(result[0][i].num_r - result[0][i].multi,2)) + '(' + getStrong((result[0][i].num_r - result[0][i].multi - (result[1][i].num_r - result[1][i].multi)),0, 0)+ ',' + getStrong((result[0][i].num_r - result[0][i].multi - (result[2][i].num_r - result[2][i].multi)),0, 0)+  ')' +'\t\\\\', end= '')
    #    print('')   
        if(k == 4):
            print('\\hline')
        else:
            print('')


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


