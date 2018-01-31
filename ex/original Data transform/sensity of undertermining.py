import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$number\ of \ Test\ Cases$", r"$value\ of \ f-meaure$", r"$value\ of \ covered-t-num$" ]

tests = 0
f_measure = 1
covered_t = 2

xtips = ['0.01', '0.05', '0.1', '0.15', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.80', '0.9', '0.98']

DATA = [
[
[33.1,32.6,34.4,33.4,35.1,34.5,38.6,41.5,47.4,46.2,51.3,47.7,41.5,],
[33.9,36.0,43.5,47.1,55.5,59.0,70.8,74.0,84.1,75.8,77.7,58.4,45.5,],
[33.1,35.4,38.2,47.0,45.5,65.1,61.0,66.3,68.9,79.7,70.3,62.0,49.8,],
],
[
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.05,0.11,0.11,0.43,0.88,],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.22,0.71,0.9,],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.07,0.0,0.22,0.55,1.0,],
],
[
[1.0,1.0,0.99,0.99,0.97,0.98,0.98,0.96,0.97,0.97,0.97,0.98,0.99,],
[1.0,1.0,1.0,0.99,0.98,0.97,0.97,0.97,0.97,0.97,0.96,0.98,1.0,],
[0.99,0.99,0.99,0.99,0.98,0.99,0.98,0.98,0.98,0.98,0.98,0.99,0.99,],
],
]

out_metric = DATA[f_measure]
metric = f_measure



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
axmetric.set_xlabel(r"$(f)\ The\ probality\ that\ the\ undetermined\ failure\ is\ triggered$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
