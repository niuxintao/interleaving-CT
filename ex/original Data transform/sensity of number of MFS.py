import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$number\ of \ Test\ Cases$", r"$value\ of \ f-meaure$", r"$value\ of \ covered-t-num$" ]

tests = 0
f_measure = 1
covered_t = 2

xtips = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30','40', '50', '60', '70', '80', '90']

DATA = [
[
[23.2,28.8,30.4,37.6,35.8,33.4,31.4,27.2,26.2,32.6,49.2,63.2,89.6,82.4,77.6,83.2,82.6,129.8,],
[28.5,37.8,47.2,51.8,47.1,37.5,37.6,37.4,37.0,42.7,70.0,77.5,125.3,311.0,248.0,251.3,246.6,248.4,],
[57.2,75.4,78.8,102.4,101.0,87.0,91.4,100.6,99.6,134.4,158.4,162.4,185.4,198.4,192.6,203.0,201.2,208.4,],
],
[
[1.0,0.55,0.34,0.25,0.18,0.14,0.06,0.0,0.0,0.0,0.0,0.01,0.01,0.0,0.01,0.0,0.01,0.0,],
[1.0,1.0,0.86,0.69,0.49,0.25,0.24,0.2,0.18,0.2,0.24,0.13,0.22,0.1,0.0,0.0,0.0,0.0,],
[1.0,0.68,0.57,0.49,0.41,0.29,0.09,0.15,0.04,0.21,0.13,0.05,0.06,0.01,0.01,0.02,0.01,0.01,],
],
[
[1.0,1.0,0.98,0.98,0.96,0.95,0.94,0.93,0.93,0.93,0.8,0.72,0.57,0.46,0.42,0.3,0.17,0.15,],
[1.0,1.0,0.99,0.98,0.97,0.96,0.96,0.96,0.96,0.95,0.87,0.8,0.73,0.45,0.0,0.0,0.0,0.0,],
[1.0,1.0,0.99,0.98,0.98,0.97,0.95,0.95,0.94,0.93,0.81,0.66,0.46,0.27,0.17,0.16,0.14,0.14,],
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
fig.legend([line_1, line_2, line_3], ['fic-fda', 'ict', 'sct'],'upper left',
           ncol=3,prop={'size':10})


axmetric.yaxis.tick_left()

#set Y labels
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ MFS\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
