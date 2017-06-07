import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

strs = [r"$number\ of \ Test\ Cases$", r"$value\ of \ f-meaure$", r"$value\ of \ covered-t-num$" ]

tests = 0
f_measure = 1
covered_t = 2

xtips = ['8', '10', '16', '20', '30', '40',  '50', '60', '70', '80', '90']

DATA = [
[
[47.3,53.9,72.1,77.7,96.3,129.9,143.8,161.1,181.8,200.4,227.3,],
[89.2,134.5,183.2,228.2,326.7,434.3,519.0,608.2,693.9,836.9,935.7,],
[81.7,101.6,154.1,200.9,296.7,376.6,504.7,612.2,671.0,907.0,1041.9,],
],
[
[0.13,0.11,0.07,0.08,0.06,0.04,0.03,0.02,0.02,0.02,0.02,],
[0.48,0.55,0.66,0.66,0.66,0.65,0.67,0.67,0.67,0.65,0.67,],
[0.46,0.46,0.48,0.42,0.41,0.47,0.46,0.42,0.42,0.44,0.46,],
],
[
[0.99,0.99,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,],
[0.94,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,],
[0.98,0.99,0.99,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,],
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
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ parameters\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(strs[metric])


plt.xticks(x, xtips)

#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
