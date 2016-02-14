"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def show(ax, x, y_1, y_2):
    n_groups = 5
    

    bar_width = 0.25

    opacity = 0.4

    rects1 = ax.bar(x, y_1, bar_width,
                     color='#000000')

    rects2 = ax.bar(x + bar_width, y_2, bar_width,
                     color='#ffffff')

    height = rects1[0].get_height()
    label = round(y_1,2)
    if y_1 != 0 and label == 0 :
        label = round(y_1, 3)
        print(label)
    ax.text(rects1[0].get_x() + rects1[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects2[0].get_height()
    label = round(y_2,2)
    ax.text(rects2[0].get_x() + rects2[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')
    return rects1, rects2

def show2(ax, x, y_1, y_2, y_3):
    n_groups = 5
    
    bar_width = 0.3

    opacity = 0.4

    rects1 = ax.bar(x, y_1, bar_width,
                     color='#000000')

    rects2 = ax.bar(x + bar_width, y_2, bar_width,
                     color='#ffffff')

    rects3 = ax.bar(x + bar_width + bar_width, y_3, bar_width,
                     alpha=opacity,
                     color='#969696')

    height = rects1[0].get_height()
    label = round(y_1,2)
    ax.text(rects1[0].get_x() + rects1[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects2[0].get_height()
    label = round(y_2,2)
    ax.text(rects2[0].get_x() + rects2[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    height = rects3[0].get_height()
    label = round(y_3,2)
    ax.text(rects3[0].get_x() + rects3[0].get_width()/2, height , label, rotation='vertical', ha='center', va='bottom')

    return rects1, rects2, rects3

   
    
if __name__ == "__main__":
    avg1 = [[0.4666391838814202,0.8490583664021164,0.47873638917951333],
[0.6305555555555555,2.522222222222222,0.6444444444444445],
[8.133333333333333,0.7472222222222222,9.975],
[0.0,0.33055555555555555,0.0],
[0.2833333333333333,0.11944444444444444,0.1111111111111111],
[1.6388888888888888,0.08888888888888889,1.913888888888889],
[113.98055555555555,98.69722222222222,98.69722222222222]]
    
    avg2 =[[0.48810500427366854,0.8460268775720164,0.47655305364791184],
[0.5694444444444444,2.911111111111111,0.6166666666666667],
[14.722222222222221,0.7583333333333333,15.28888888888889],
[0.0,0.45,0.0],
[0.0027777777777777783,0.03333333333333333,0.0],
[0.8722222222222222,0.16111111111111112,1.5388888888888892],
[219.5611111111111,181.88611111111112,181.88611111111112]]


    avg3 = [[0.4861558887782635,0.8487597001763668,0.481585077038233],
[0.575,2.927777777777778,0.6055555555555555],
[20.211111111111112,0.8166666666666667,19.6],
[0.0,0.46944444444444444,0.0],
[0.0,0.008333333333333333,0.0],
[0.14444444444444446,0.15,0.8555555555555555],
[458.1138888888889,355.5027777777778,355.5027777777778]]


    #to change this factor 
    avg = avg3

    
    fig = plt.figure(figsize=(7.5, 3))

    ax1= fig.add_subplot(1,7,6)
    x = np.array([0])
    rects1, rects2 = show(ax1, x, avg[0][0], avg[0][1])
    ax1.set_xlabel('Aggregative')

    ax2= fig.add_subplot(1,7,1)
    x = np.array([0])
    show(ax2, x, avg[1][0], avg[1][1])
    ax2.set_xlabel('Accuate')

    ax3= fig.add_subplot(1,7,2)
    x = np.array([0])
    show(ax3, x, avg[2][0], avg[2][1])
    ax3.set_xlabel('Super')

    ax4= fig.add_subplot(1,7,3)
    x = np.array([0])
    show(ax4, x, avg[3][0], avg[3][1])
    ax4.set_xlabel('Sub')

    ax5= fig.add_subplot(1,7,4)
    x = np.array([0])
    show(ax5, x, avg[4][0], avg[4][1])
    ax5.set_xlabel('Ignore')

    ax6= fig.add_subplot(1,7,5)
    x = np.array([0])
    show(ax6, x, avg[5][0], avg[5][1])
    ax6.set_xlabel('Irrelevant')


    ax7= fig.add_subplot(1,7,7)
    x = np.array([0])
    show(ax7, x, avg[6][0], avg[6][1])
    ax7.set_xlabel('TestCase')

    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    ax3.set_xticklabels([])
    ax4.set_xticklabels([])
    ax5.set_xticklabels([])
    ax6.set_xticklabels([])
    ax7.set_xticklabels([])


    #disable labels for some plots
    ax1.set_yticklabels([])
    ax2.set_yticklabels([])
    ax3.set_yticklabels([])
    ax4.set_yticklabels([])
    ax5.set_yticklabels([])
    ax6.set_yticklabels([])
    ax7.set_yticklabels([])
    ##

    #axmetric.set_ylim(0, 1.05)
    #axaccuate.set_ylim(0, 1.05)
    #axtestnum.set_ylim(0, 1.05)

    high = max(avg[0])
    high = high * 1.28
    ax1.set_ylim(0, high)
    high = max(avg[1])
    high = high * 1.28
    ax2.set_ylim(0, high)
    high = max(avg[2])
    high = high * 1.31
    ax3.set_ylim(0, high)
    high = max(avg[3])
    high = high * 1.28
    ax4.set_ylim(0, high)
    high = max(avg[4])
    high = high * 1.28
    ax5.set_ylim(0, high)
    high = max(avg[5])
    high = high * 1.28
    ax6.set_ylim(0, high)
    high = max(avg[6])
    high = high * 1.38
    ax7.set_ylim(0, high)
    
    
    ax1.set_xlim(-0.04, 0.54)
    ax2.set_xlim(-0.04, 0.54)
    ax3.set_xlim(-0.04, 0.54)
    ax4.set_xlim(-0.04, 0.54)
    ax5.set_xlim(-0.04, 0.54)
    ax6.set_xlim(-0.04, 0.54)
    ax7.set_xlim(-0.04, 0.54)

   # ax1.set_ylabel('number of schemas')
   # plt.title('(a)Result for the 2-way covering array')
   # ax1.set_xticks(x + bar_width, x)
    fig.legend([rects1, rects2], ['FDA-CIT', 'ILP'],'upper left',
           ncol=2,prop={'size':10})

    #plt.tight_layout()
    plt.subplots_adjust(left=0.01, bottom=0.09, right=0.97, top=0.88, wspace=0, hspace=0.25)

    plt.show()
