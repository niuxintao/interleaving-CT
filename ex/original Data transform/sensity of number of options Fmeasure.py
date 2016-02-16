import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data

out_metric = [[11.0,10.6,12.8,12.4,13.6,15.4,16.2,17.6,18.8,19.6,20.4,21.0,21.2,21.6,],
[15.4,17.0,18.0,21.0,26.0,30.4,42.0,53.0,63.8,74.0,84.8,95.8,106.2,116.0,],
[32.4,39.0,43.4,51.8,56.8,101.8,148.6,227.8,322.6,325.2,419.2,510.8,662.0,735.2,],]

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
axmetric.set_xlabel(r"$(f)\ The\ number\ of\ options\ in\ the\ SUT$")


#set X labels
axmetric.set_ylabel(r"$value\ of \ f-meaure$")


#adjust plot spacing
plt.subplots_adjust(left=0.09, bottom=0.14, right=0.97, top=0.90, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
