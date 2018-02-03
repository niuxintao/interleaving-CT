import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$Times\ of \ non-safe\ values\ triggered$", r"$Times\ of \ non-safe\ values\ triggered\ average$" ]

enTr = 0
enTrAvg = 1

xtips = ['1', '2', '3', '4', '5', '6',  '7', '8', '9', '10']

DATA = [
[
[0,0,0,0,0,0,0,0,0,0,],
[19.0,100.2,92.2,73.6,171.8,196.5,266.6,245.4,257.4,385.8,],
[21.5,103.2,83.8,97.6,308.9,444.3,440.1,467.7,446.2,572.8,],
],
[
[0,0,0,0,0,0,0,0,0,0,],
[4.32,11.39,12.63,13.89,18.28,20.9,27.77,31.46,33.0,47.05,],
[1.76,5.49,4.93,6.14,10.62,13.88,12.19,12.78,11.56,12.79,],
],
]

out_metric = DATA[enTrAvg]
metric = enTrAvg



num = len(out_metric[0])
x = range(0,num)



#define figure and figure size figsize=(width, height)
fig = plt.figure(figsize=(8, 4))

#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18


axmetric = fig.add_subplot(1,1,1) #gas1
axmetricn = fig.add_subplot(1,1,1, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn1 = fig.add_subplot(1,1,1, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn2 = fig.add_subplot(1,1,1, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud


#plot data and normalized data 
#line_1, = axmetric.plot(x, out_metric[0],  marker="s",  color="k")
line_2, = axmetricn.plot(x, out_metric[1], ls="--", marker="d",   color="k")
line_3, = axmetricn1.plot(x, out_metric[2], ls=":", marker="o", mfc="None",   color="k")

#configure legend
fig.legend([line_2, line_3], [ 'ict', 'sct'],'upper left',
           ncol=2,prop={'size':10})


axmetric.yaxis.tick_left()

#set Y labels
axmetric.set_xlabel(r"$The\ ID\ of\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
