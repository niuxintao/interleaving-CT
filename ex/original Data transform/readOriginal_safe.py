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
        self.encSafe =0
        self.triSafe = 0
        self.idenTimes = 0

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
        elif strs.find('encounter unsafe values  ')>=0:
            result.encSafe = float(strlist[1])
        elif strs.find('trigger unsafe values  ')>=0:
            result.triSafe = float(strlist[1])
        elif strs.find('identification times  ')>=0:
            result.idenTimes = float(strlist[1])
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

    senSafe = ['8-0', '10-1', '12-2', '16-2', '20-3', '25-4', '30-5', '35-7', '40-5', '50-6']
    senUnden = ['0.01', '0.05', '0.1', '0.15', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '0.98']

    txt = '.txt'

    folder = ['five', 'mfs', 'op', 'und4', 'safe2']

    print('test Cases')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
            
        for j in range(1,3):
            result = results[j-1]
            result_2 = [ -1, -1, -1]
            if j == 1:
                result_2 = [results[j][0].num_i,results[j][1].num_i,results[j][2].num_i,]
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].num_r,2)) +'\t&'+ getStrong(result[i].num_i,result_2[i],0)+ '\t&' +str(round(result[i].numAll,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].num_r,2)) +'\t&'+ getStrong(result[i].num_i,result_2[i],0) + '\t&' +str(round(result[i].numAll,2)) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')

    print('')
    print('identification quality')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)
            
        for j in range(1,3):
            result = results[j-1]
            result_2 = [ -1, -1, -1]
            if j == 1:
                result_2 = [results[j][0].f_measure,results[j][1].f_measure,results[j][2].f_measure,]
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].precise,2)) +'\t&'+ str(round(result[i].recall,2)) + '\t&' +getStrong(result[i].f_measure,result_2[i],1) +'\t&', end= '')
                else:
                    print(str(round(result[i].precise,2)) +'\t&'+ str(round(result[i].recall,2)) + '\t&' +getStrong(result[i].f_measure,result_2[i],1) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')

    print('')
    print('multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].multi,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].multi,2)) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')




# all the masking effects are obtained by the generated test cases which contain multiple MFS, hence we just let the generated test cases to minus multiple, use num_r - multi or numAll - multi
    print('')
    print('non-maksing tests :  gen - multi')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
           # result = getOneFile(filename)
            result_temp = getOneFile(filename)
            results.append(result_temp)

        for j in range(1,3):
            result = results[j-1]
            result_2 = [ -1, -1, -1]
            if j == 1:
                result_2 = [results[j][0].num_r - results[j][0].multi,results[j][1].num_r - results[j][1].multi,results[j][2].num_r - results[j][2].multi,]
                
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(getStrong(result[i].num_r - result[i].multi,result_2[i],1) +'\t&', end= '')
                else:
                    print(getStrong(result[i].num_r - result[i].multi,result_2[i],1) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')

    print('')
    print('time')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result = getOneFile(filename)
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    print(str(round(result[i].time,2)) +'\t&', end= '')
                else:
                    print(str(round(result[i].time,2)) +'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
                print('')
            
    print('')
    print('tested-t-way')
    for k in range(5):
        sub = subject[k]
        ssub = [showresultSub[k], '', '']
        results = []
        for j in range(1,3):
            app = approach[j]
            filename = folder[0] +'\/'+app+sub+txt
            result_temp = getOneFile(filename)
            results.append(result_temp)

        for j in range(1,3):
            result = results[j-1]
            result_2 = [ -1, -1, -1]
            if j == 1:
                result_2 = [results[j][0].t_cover,results[j][1].t_cover,results[j][2].t_cover,]
                
            print(ssub[j-1] + '\t&' + showresultApp[j]+'\t&', end = '')
            for i in range(0, 3):
                if i < 2:
                    if(getStrong(result[i].t_cover,result_2[i],1).find("textbf") != -1):
                        print(getStrong(result[i].t_cover,result_2[i],1) + "\\textbf{" +  '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')' +"}"+'\t&', end= '')
                    else:
                        print(getStrong(result[i].t_cover,result_2[i],1) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t&', end= '')
                else:
                    if(getStrong(result[i].t_cover,result_2[i],1).find("textbf") != -1):
                        print(getStrong(result[i].t_cover,result_2[i],1) + "\\textbf{" +  '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')' +"}"+'\t\\\\', end= '')
                    else:
                        print(getStrong(result[i].t_cover,result_2[i],1) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t\\\\', end= '')
                #    print(getStrong(result[i].t_cover,result_2[i],1) + '(' + str("{:.2%}".format(result[i].t_cover/result[i].all_cover)).replace('%','\%') +')'+'\t\\\\', end= '')
            if(j == 2):
                print('\\hline')
            else:
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

#    print('')
#    print('fd multi')
#    for k in range(5):
#        sub = subject[k]
#        ssub = [showresultSub[k], '', '']
#        result = []
#        for j in range(0,3):
#            app = approach[j]
#            filename = folder[0] +'\/'+app+sub+txt
#            result_temp = getOneFile(filename)
#            result.append(result_temp)
#        print(showresultSub[k] + '\t&', end = '')
#        for i in range(0, 3):
#            if i < 2:
#               print(str(round(result[0][i].multi,2)) + '(' + getStrongPerCent(result[0][i].multi - result[1][i].multi,0,1) + ',' + getStrongPerCent(result[0][i].multi - result[2][i].multi,0,1)+  ')' +'\t&', end= '')
#           else:
#               print(str(round(result[0][i].multi,2)) + '(' + getStrongPerCent(result[0][i].multi - result[1][i].multi,0,1) + ',' + getStrongPerCent(result[0][i].multi - result[2][i].multi,0,1)+  ')' +'\t\\\\', end= '')
#        #print('')
#        if(k == 4):
#            print('\\hline')
#       else:
#           print('')

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


    

    print('')
    print('sensity of number of MFS --- test cases')
    print('sensity of number of MFS --- f-measure')
    print('sensity of number of MFS --- t-cover')

    print('[')

    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senMFS:
            app = approach[j]
            filename = folder[1] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].numAll,2)) +',', end= '')
        print('],')

    print('],')

    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senMFS:
            app = approach[j]
            filename = folder[1] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].f_measure,2)) +',', end= '')
        print('],')
        
    print('],')

    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senMFS:
            app = approach[j]
            filename = folder[1] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].t_cover/result[0].all_cover,2)) +',', end= '')
        print('],')
    print('],')

    print(']') 


    print('')
    print('sensity of number of options --- test cases')
    print('sensity of number of options --- f-measure')
    print('sensity of number of options --- t-cover')


    print('[')


    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senOptions:
            app = approach[j]
            filename = folder[2] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].numAll,2)) +',', end= '')
        print('],')

    print('],')

    print('[')
  
    for j in range(0,3):
        print('[', end = '')
        for sub in senOptions:
            app = approach[j]
            filename = folder[2] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].f_measure,2)) +',', end= '')
        print('],')
        
        
    print('],')

    print('[')

    for j in range(0,3):
        print('[', end = '')
        for sub in senOptions:
            app = approach[j]
            filename = folder[2] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].t_cover/result[0].all_cover,2)) +',', end= '')
        print('],')

    print('],')

    print(']')

    print('')
    print('sensity of undetermine --- test cases')
    print('sensity of undetermine --- f-measure')
    print('sensity of undetermine --- t-cover')





    print('[')


    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senUnden:
            app = approach[j]
            filename = folder[3] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].numAll,2)) +',', end= '')
        print('],')

    print('],')

    print('[')
  
    for j in range(0,3):
        print('[', end = '')
        for sub in senUnden:
            app = approach[j]
            filename = folder[3] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].f_measure,2)) +',', end= '')
        print('],')
        
        
    print('],')

    print('[')

    for j in range(0,3):
        print('[', end = '')
        for sub in senUnden:
            app = approach[j]
            filename = folder[3] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].t_cover/result[0].all_cover,2)) +',', end= '')
        print('],')

    print('],')

    print(']') 



    print('sensity of undetermine --- w iden')

    print('[', end = '')
    for sub in senUnden:
        app = approach[1]
        filename = folder[3] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        print(str(round(result[0].widen,2)) +',', end= '')
    print('],')


    print('sensity of undetermine --- w check')

    print('[', end = '')
    for sub in senUnden:
        app = approach[1]
        filename = folder[3] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        print(str(round(result[0].wcheck,2)) +',', end= '')
    print('],')



    print('')
    print('show wcheck and widen')

    print('fixed'+'\t&', end = '')
    for sub in senUnden:
        app = approach[1]
        filename = folder[3] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        if sub == senUnden[len(senUnden) - 1]:
            print(str(round(result[0].wcheck,2)) +'\t\\\\', end= '')    
        else:
            print(str(round(result[0].wcheck,2)) +'\t&', end= '')
    print('\\hline')

    print('unfixed'+'\t&', end = '')
    for sub in senUnden:
        app = approach[1]
        filename = folder[3] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        if sub == senUnden[len(senUnden) - 1]:
            print(str(round(result[0].widen,2)) +'\t\\\\', end= '')    
        else:
            print(str(round(result[0].widen,2)) +'\t&', end= '')
            
    print('\\hline')
            
    


    print('')
    print('sensity of safe --- test cases')
    print('sensity of safe --- f-measure')
    print('sensity of safe --- t-cover')


    print('[')


    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].numAll,2)) +',', end= '')
        print('],')

    print('],')

    print('[')
  
    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].f_measure,2)) +',', end= '')
        print('],')
        
        
    print('],')

    print('[')

    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].t_cover/result[0].all_cover,2)) +',', end= '')
        print('],')

    print('],')

    print(']')


    print('')
    print('sensity of safe --- enSafe')
    print('sensity of safe --- triSafe')
    print('sensity of safe --- idenTimes')



    print('[')


    print('[')
    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].encSafe,2)) +',', end= '')
        print('],')

    print('],')

    print('[')
  
    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].triSafe,2)) +',', end= '')
        print('],')
        
        
    print('],')

    print('[')

    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            print(str(round(result[0].idenTimes,2)) +',', end= '')
        print('],')

    print('],')

    print('[')

    for j in range(0,3):
        print('[', end = '')
        for sub in senSafe:
            app = approach[j]
            filename = folder[4] +'\/'+app+syn+sub+txt
            result = getOneFile(filename)
            if result[0].idenTimes > 0:
                print(str(round(result[0].triSafe/result[0].idenTimes,2)) +',', end= '')
        print('],')

    print('],')

    print(']')


    print('sensity of safe --- w iden')

    print('[', end = '')
    for sub in senSafe:
        app = approach[1]
        filename = folder[4] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        print(str(round(result[0].widen,2)) +',', end= '')
    print('],')


    print('sensity of safe --- w check')

    print('[', end = '')
    for sub in senSafe:
        app = approach[1]
        filename = folder[4] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        print(str(round(result[0].wcheck,2)) +',', end= '')
    print('],')

    print('')
    print('show wcheck and widen')

    print('fixed'+'\t&', end = '')
    for sub in senSafe:
        app = approach[1]
        filename = folder[4] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        if sub == senSafe[len(senSafe) - 1]:
            print(str(round(result[0].wcheck,2)) +'\t\\\\', end= '')    
        else:
            print(str(round(result[0].wcheck,2)) +'\t&', end= '')
    print('\\hline')

    print('unfixed'+'\t&', end = '')
    for sub in senSafe:
        app = approach[1]
        filename = folder[4] +'\/'+app+syn+sub+txt
        result = getOneFile(filename)
        if sub == senSafe[len(senSafe) - 1]:
            print(str(round(result[0].widen,2)) +'\t\\\\', end= '')    
        else:
            print(str(round(result[0].widen,2)) +'\t&', end= '')
            
    print('\\hline')

