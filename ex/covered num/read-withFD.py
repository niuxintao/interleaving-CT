import numpy as np
import matplotlib.pyplot as plt
import show

def readFile(inputFile):
    fig, ax = plt.subplots()
    inf = open(inputFile)
    line = inf.readline()
    bar_inc = [0, 0.35, 0.7];
    a = ['ICT','SCT','FD']
    color = ['b','r','y']
    dot = ['--', '-.']
    mark = ['o','d']
    i = 0
    while line:
        line = line.strip()
        if len(line) != 0 and line[0] == '(' :
            [x, y] = dealLine(line)
            if i >= 2:
                show.show1(x, y, a[i], color[i])
            elif i < 2:
                show.show2(x, y, a[i], color[i], mark[i], dot[i])
            i = i + 1
        line = inf.readline()   
    inf.close()
    
    plt.xlabel('covered times')
    plt.ylabel('number of schemas')
    plt.title('Scores by group and gender')
    bar_width = 0.35
    plt.xticks(x + bar_width + bar_width/2, x)
    plt.legend()

    plt.tight_layout()
    plt.show()

def dealLine(str):
    strlist = str.split(')  (')
    x = np.array([])
    y = np.array([])
    for s in strlist:
        s = s.strip('()')
        slist = s.split(':')
        a = []
        for c in slist:
            c = c.strip()
            a.append(c)
        x = np.append(x, int(a[0]))
        y = np.append(y,float(a[1]))
    print(x)
    print(y)
    return [x, y]

if __name__ == "__main__":
    readFile("2-way gcc.txt")
   
