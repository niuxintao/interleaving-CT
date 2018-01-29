import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$value\ of \ f-meaure$", r"$value\ of \ f-meaure for test cases containing multiple MFS$" ]

tests = 0
f_measure = 1
covered_t = 2

xtips = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30','40', '50', '60', '70', '80', '90']

DATA = [
[
[
[1.0,0.39,0.19,0.14,0.12,0.11,0.11,0.11,0.02,0.03,0.06,0.03,0.03,0.02,0.01,0.02,0.02,0.01,],
[1.0,1.0,0.78,0.58,0.52,0.29,0.29,0.23,0.2,0.22,0.25,0.27,0.21,0.25,0.08,0.04,0.03,0.04,],
[1.0,0.8,0.54,0.57,0.35,0.4,0.21,0.15,0.07,0.1,0.15,0.15,0.07,0.09,0.11,0.07,0.04,0.02,],
],
[
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,],
[-1,0.67,0.5,0.46,0.4,0.32,0.2,0.2,0.19,0.16,0.23,0.2,0.2,0.15,0.04,0.07,0.05,0.04,],
[-1,0.07,0.08,0.05,0.06,0.04,0.01,0.02,0.01,0.02,0.02,0.01,0.02,0.03,0.01,0.01,0.01,0.01,],
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
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ MFS\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
