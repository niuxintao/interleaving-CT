import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co
import mpl_toolkits.axisartist.floating_axes as floating_axes
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.angle_helper as angle_helper
from mpl_toolkits.axisartist.grid_finder import FixedLocator, MaxNLocator, DictFormatter

#data

strs = [r"$value\ of \ f-meaure$", r"$value\ of \ f-meaure\ (multiple\ MFS)$" ]

f_measure_normal = 0
f_measure_multi = 1

xtips = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30','40', '50', '60', '70', '80', '90']

DATA = [
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

out_metric = DATA[f_measure_multi]
metric = f_measure_multi



num = len(out_metric[0])
x = range(0,num)

fm1 = DATA[0]
fm2 = DATA[1]
decrease = []
dec1 = []
dec2 = []
decrease.append(dec1)
decrease.append(dec2)

for i in range(0, len(fm1[1])):
    de1 = fm1[1][i] - fm2[1][i]
    de2 = fm1[2][i] - fm2[2][i]
    dec1.append(de1)
    dec2.append(de2)
    


#define figure and figure size figsize=(width, height)


#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18





fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))
#bar_width,

ax0.set_ylim(ymin=-0.1, ymax= 1)
ax1.set_ylim(ymin=-0.1, ymax= 1)

for i in dec1[1:]:
    print(i, end="\t")
print()
for i in dec2[1:]:
    print(i, end="\t")
print()
ax0.bar(x[1:], dec1[1:],  alpha=1, color='k', label='ICT')
ax0.set_title('ICT')

ax0.set_xlabel('number of MFS')
ax0.set_ylabel('The decrease of f-measure')

# Create a histogram by providing the bin edges (unequally spaced).

ax1.bar(x[1:], dec2[1:],  alpha=1, color='w', label='SCT')
ax1.set_title('SCT')

ax1.set_xlabel('number of MFS')
ax1.set_ylabel('The decrease of f-measure')

plt.setp([ax0, ax1], xticks=x, xticklabels=xtips)



fig.tight_layout()
plt.show()
