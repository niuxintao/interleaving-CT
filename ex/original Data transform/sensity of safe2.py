import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$number\ of \ Test\ Cases$", r"$value\ of \ f-meaure$", r"$value\ of \ covered-t-num$" ]

tests = 0
f_measure = 1
covered_t = 2

xtips = ['1', '2', '3', '4', '5', '6',  '7', '8', '9', '10']

DATA = [
[
[82.1,151.3,124.3,94.7,338.6,374.3,321.3,345.4,398.7,422.6,],
[87.8,231.8,222.2,217.6,430.7,506.2,611.4,587.5,689.9,871.6,],
[96.2,222.1,200.1,218.6,547.1,725.9,884.6,828.2,835.2,1056.7,],
],
[
[0.08,0.05,0.05,0.03,0.01,0.01,0.01,0.01,0.0,0.0,],
[0.61,0.67,0.59,0.55,0.58,0.61,0.58,0.52,0.57,0.55,],
[0.54,0.64,0.49,0.42,0.52,0.52,0.51,0.52,0.53,0.52,],
],
[
[0.97,0.96,0.99,1.0,0.98,0.99,1.0,1.0,1.0,1.0,],
[0.93,0.94,0.94,0.99,0.95,0.96,0.97,0.98,0.99,0.99,],
[0.94,0.91,0.95,0.98,0.92,0.94,0.96,0.98,0.99,0.99,],
],
]

out_metric = DATA[tests]
metric = tests



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
line_1, = axmetric.plot(x, out_metric[0],  marker="s",  color="k")
line_2, = axmetricn.plot(x, out_metric[1], ls="--", marker="d",   color="k")
line_3, = axmetricn1.plot(x, out_metric[2], ls=":", marker="o", mfc="None",   color="k")

#configure legend
fig.legend([line_1, line_2, line_3], ['fda-cit', 'ict', 'sct'],'upper left',
           ncol=3,prop={'size':10})


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
