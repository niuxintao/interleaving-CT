"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt

def show1(ax, x, y_1, labelS, c):
    bar_width = 0.35

    opacity = 1

    rects1 = ax.bar(x, y_1, bar_width,
                     alpha=opacity,
                     color=c,
                     label=labelS)
    return rects1
    
def show1_special(ax, x, y_1, minimal, labelS, c):
    x_new = x[0:minimal]
    y_new = y_1[0:minimal]
    x_new_right = x[minimal:]
    y_new_right = y_1[minimal:]
    allRight = 0
    
    for i in y_new_right:
        allRight += i


    if len(x) < minimal:
        x_final = x
        y_final = y_1
    else:
        x_final = x_new
        y_final = y_new

##    if len(x_new_right) > 0:
##        x_final = np.append(x_new, x_new_right[0])
##        y_final = np.append(y_new, allRight)
##    else :
##        x_final = x_new
##        y_final = y_new
        
    bar_width = 0.35
    
    opacity = 1

    rects1 = ax.bar(x_final, y_final, bar_width,
                     alpha=opacity,
                     color=c,
                     label=labelS)
    return rects1
    #ax.annotate('pixels', xy=(20, 20),  xycoords='figure pixels')

def show2(ax, x, y_1, labelS, c, mark, dot):
   line_2, = ax.plot(x, y_1, ls=dot, marker=mark, mfc="None", label=labelS,  color=c)
   return line_2
   
def show2_special(ax, x, y_1, minimal, labelS, c, mark, dot):
    x_new = x[0:minimal]
    y_new = y_1[0:minimal]
    x_new_right = x[minimal:]
    y_new_right = y_1[minimal:]
    allRight = 0
    
    for i in y_new_right:
        allRight += i


    if len(x) < minimal:
        x_final = x
        y_final = y_1
    else:
        x_final = x_new
        y_final = y_new

    line_2, = ax.plot(x_final, y_final, ls=dot, marker=mark, mfc="None", label=labelS,  color=c)
    return line_2

def show(x, y_1, y_2):
    n_groups = 5
    
    fig, ax = plt.subplots()

    bar_width = 0.35

    opacity = 0.4

    rects1 = plt.bar(x, y_1, bar_width,
                     alpha=opacity,
                     color='b',
                     label='ICT')

    rects2 = plt.bar(x + bar_width, y_2, bar_width,
                     alpha=opacity,
                     color='r',
                     label='SCT')

    plt.xlabel('covered times')
    plt.ylabel('number of schemas')
    plt.title('Scores by group and gender')
    plt.xticks(x + bar_width, x)
    plt.legend()

    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    x = np.array([0, 1, 2, 3, 4])
    y_1 = (20, 35, 30, 35, 27)
    y_2 = (25, 32, 34, 20, 25)
    show(x, y_1, y_2)
