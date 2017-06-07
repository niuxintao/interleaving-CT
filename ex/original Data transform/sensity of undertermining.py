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
[38.3,38.5,40.7,38.4,42.1,42.6,48.4,47.0,54.2,61.7,53.3,54.6,52.3,],
[44.7,48.7,54.7,56.3,69.7,68.4,85.0,80.6,95.4,88.4,108.0,102.6,71.9,],
[48.9,52.8,57.6,60.6,57.1,80.9,86.3,88.8,99.3,91.8,89.2,70.1,64.6,],
],
[
[0.62,0.55,0.41,0.44,0.3,0.17,0.12,0.11,0.06,0.04,0.14,0.16,0.15,],
[0.67,0.62,0.57,0.56,0.47,0.5,0.41,0.43,0.34,0.39,0.35,0.63,0.92,],
[0.65,0.61,0.55,0.47,0.53,0.33,0.28,0.18,0.21,0.37,0.47,0.74,0.69,],
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
