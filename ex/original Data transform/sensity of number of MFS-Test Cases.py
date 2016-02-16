import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

out_metric = [[23.6,27.2,38.2,30.6,27.6,29.4,26.8,26.4,27.0,31.4,46.8,60.6,81.8,82.8,77.6,83.2,82.6,129.8,],
[28.4,39.0,49.0,63.6,78.0,68.2,68.6,62.2,47.4,74.0,128.4,246.6,322.4,81.0,81.0,81.0,81.0,81.0,],
[59.2,76.6,80.8,94.4,101.2,89.8,105.2,99.6,104.8,129.0,160.4,180.8,178.6,196.4,192.6,203.0,201.2,208.4,]]

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
axmetric.set_ylabel(r"$number\ of \ Test\ Cases$")


#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
