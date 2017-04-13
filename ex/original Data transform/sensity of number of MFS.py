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
[58.2,67.0,80.8,85.5,91.9,99.8,100.9,94.3,91.1,87.5,148.2,240.5,278.2,365.6,389.1,408.7,411.1,441.4,],
[61.6,70.8,78.7,77.5,79.9,71.3,73.8,71.1,75.4,70.6,96.1,134.4,193.2,241.6,582.9,462.6,463.9,470.8,],
[136.6,165.4,178.5,181.6,203.4,190.8,200.1,223.5,225.1,215.0,320.6,409.3,467.2,500.6,524.6,531.4,550.7,553.4,],
],
[
[0.97,0.35,0.14,0.15,0.12,0.1,0.13,0.1,0.08,0.06,0.05,0.03,0.03,0.02,0.01,0.02,0.02,0.01,],
[1.0,1.0,0.82,0.53,0.51,0.27,0.28,0.22,0.24,0.17,0.18,0.22,0.19,0.33,0.17,0.0,0.0,0.0,],
[1.0,0.8,0.7,0.68,0.67,0.58,0.5,0.53,0.5,0.46,0.44,0.43,0.44,0.41,0.31,0.16,0.12,0.07,],
],
[
[1.0,1.0,1.0,1.0,0.99,0.99,0.99,0.98,0.98,0.98,0.95,0.93,0.89,0.86,0.79,0.76,0.69,0.69,],
[1.0,1.0,0.99,0.98,0.98,0.97,0.97,0.97,0.97,0.97,0.94,0.9,0.86,0.85,0.76,0.0,0.0,0.0,],
[1.0,1.0,1.0,1.0,1.0,0.99,0.99,0.99,0.99,0.99,0.96,0.92,0.9,0.85,0.75,0.61,0.5,0.43,],
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
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ MFS\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
