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
[58.5,67.0,73.3,82.0,95.9,92.5,103.3,96.4,75.4,76.6,142.6,221.6,284.4,362.4,400.3,406.9,421.0,398.2,],
[61.8,73.7,82.8,82.6,88.2,73.5,78.7,73.3,72.6,76.6,105.7,140.1,141.0,216.1,240.4,152.4,157.5,171.6,],
[66.9,80.3,83.5,88.1,90.0,93.4,86.8,84.7,79.8,81.8,118.5,161.2,170.1,193.7,346.4,427.1,489.3,514.0,],
],
[
[1.0,0.39,0.19,0.14,0.12,0.11,0.11,0.11,0.02,0.03,0.06,0.03,0.03,0.02,0.01,0.02,0.02,0.01,],
[1.0,1.0,0.78,0.58,0.52,0.29,0.29,0.23,0.2,0.22,0.25,0.27,0.21,0.25,0.08,0.04,0.03,0.04,],
[1.0,0.8,0.54,0.57,0.35,0.4,0.21,0.15,0.07,0.1,0.15,0.15,0.07,0.09,0.11,0.07,0.04,0.02,],
],
[
[1.0,1.0,1.0,1.0,0.99,0.99,0.99,0.98,0.97,0.97,0.95,0.93,0.9,0.86,0.78,0.75,0.71,0.63,],
[1.0,1.0,0.99,0.98,0.98,0.97,0.97,0.97,0.97,0.97,0.95,0.91,0.87,0.81,0.7,0.62,0.59,0.52,],
[1.0,0.99,0.99,0.99,0.98,0.98,0.98,0.98,0.97,0.97,0.94,0.9,0.85,0.8,0.76,0.69,0.57,0.52,],
],
]

out_metric = DATA[covered_t]
metric = covered_t



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
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ MFS\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
