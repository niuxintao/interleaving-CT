import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data
x= [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

array = [[[0.49999999999998884, 0.7708333333333334, 0.5833333333333324, 0.41666666666685614, 0.5220959595960968, 0.39137806637806677, 0.5093537414965966, 0.45348837209302234, 0.9106918238993715, 0.3561688311688371, 0.5239935587761715, 0.30713429256594826, ],[0.8402777777777525, 0.9166666666666666, 0.8657407407407239, 0.875, 0.9166666666666666, 0.7803030303030286, 0.8571428571428589, 0.7271317829457389, 0.9905660377358491, 0.755844155844156, 0.7789855072463736, 0.7624700239808144, ],[0.9583333333333334, 0.9166666666666666, 0.8888888888888383, 1.0, 0.9166666666666666, 0.858585858585858, 0.9682539682539687, 0.6957364341085306, 0.9952830188679245, 0.8252525252525257, 0.8115942028985508, 0.8153477218225419, ],[0.668995346257691, 0.9166666666666666, 0.8888888888888383, 1.0, 0.9166666666666666, 0.82662037037037, 0.9087797619047624, 0.7307251291989709, 0.9952830188679245, 0.8252525252525257, 0.6782340311325818, 0.8153477218225419, ]],
[[0.25, 0.8333333333333334, 0.7222222222222222, 1.0, 0.8333333333333334, 0.5909090909090909, 0.7023809523809523, 0.3953488372093023, 0.8867924528301887, 0.5584415584415584, 0.5434782608695652, 0.2814748201438849, ],[0.6666666666666666, 0.8333333333333334, 0.7222222222222222, 0.75, 0.8333333333333334, 0.6212121212121212, 0.7023809523809523, 0.5581395348837209, 0.9622641509433962, 0.7619047619047619, 0.717391304347826, 0.6510791366906474, ],[0.8333333333333334, 0.8333333333333334, 0.6666666666666666, 1.0, 0.8333333333333334, 0.7878787878787878, 0.9285714285714286, 0.4883720930232558, 0.9811320754716981, 0.935064935064935, 0.7898550724637681, 0.762589928057554, ],[0.542722800925926, 0.8333333333333334, 0.6666666666666666, 1.0, 0.8333333333333334, 0.7603535353535353, 0.856845238095238, 0.5583494832041344, 0.9811320754716981, 0.935064935064935, 0.6409151905528717, 0.762589928057554, ]],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],[0.08333333333333333, 0.16666666666666666, 0.16666666666666666, 0.25, 0.16666666666666666, 0.19696969696969696, 0.20238095238095238, 0.32558139534883723, 0.03773584905660377, 0.23809523809523808, 0.08695652173913043, 0.1906474820143885, ],[0.16666666666666666, 0.16666666666666666, 0.1111111111111111, 0.0, 0.16666666666666666, 0.06060606060606061, 0.023809523809523808, 0.32558139534883723, 0.018867924528301886, 0.06493506493506493, 0.0, 0.07913669064748201, ],[0.021173321759259258, 0.16666666666666666, 0.1111111111111111, 0.0, 0.16666666666666666, 0.0404040404040404, 0.023809523809523808, 0.32558139534883723, 0.018867924528301886, 0.06493506493506493, 0.0, 0.07913669064748201, ]],
[[0.5833333333333334, 0.16666666666666666, 0.2777777777777778, 0.0, 0.16666666666666666, 0.45454545454545453, 0.32142857142857145, 0.4186046511627907, 0.03773584905660377, 0.6190476190476191, 0.4492753623188406, 0.9181654676258992, ],[0.16666666666666666, 0.0, 0.05555555555555555, 0.0, 0.0, 0.06060606060606061, 0.047619047619047616, 0.11627906976744186, 0.0, 0.025974025974025976, 0.13768115942028986, 0.12589928057553956, ],[0.0, 0.0, 0.2222222222222222, 0.0, 0.0, 0.06060606060606061, 0.047619047619047616, 0.18604651162790697, 0.0, 0.06926406926406926, 0.21014492753623187, 0.15827338129496402, ],[0.1655888310185185, 0.0, 0.2222222222222222, 0.0, 0.0, 0.07866161616161617, 0.07212301587301588, 0.11606912144702843, 0.0, 0.06926406926406926, 0.22885802469135802, 0.15827338129496402, ]],
[[0.16666666666666666, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2558139534883721, 0.07547169811320754, 0.021645021645021644, 0.057971014492753624, 0.08363309352517985, ],[0.08333333333333333, 0.0, 0.05555555555555555, 0.0, 0.0, 0.12121212121212122, 0.047619047619047616, 0.06976744186046512, 0.0, 0.07792207792207792, 0.13768115942028986, 0.1906474820143885, ],[0.0, 0.0, 0.0, 0.0, 0.0, 0.09090909090909091, 0.0, 0.06976744186046512, 0.0, 0.03463203463203463, 0.07971014492753623, 0.15827338129496402, ],[0.2705150462962963, 0.0, 0.0, 0.0, 0.0, 0.12058080808080808, 0.04722222222222222, 0.06976744186046512, 0.0, 0.03463203463203463, 0.2099369296833065, 0.15827338129496402, ]],
[[0.16666666666666666, 0.6666666666666666, 0.6666666666666666, 5.75, 3.8333333333333335, 1.8484848484848484, 1.4285714285714286, 0.5813953488372093, 0.07547169811320754, 2.225108225108225, 0.9565217391304348, 2.2068345323741005, ],[0.08333333333333333, 0.0, 0.05555555555555555, 0.0, 0.0, 0.12121212121212122, 0.047619047619047616, 0.27906976744186046, 0.0, 0.2943722943722944, 0.12318840579710146, 0.03237410071942446, ],[0.0, 0.0, 0.0, 0.0, 0.0, 0.09090909090909091, 0.0, 0.27906976744186046, 0.0, 0.2943722943722944, 0.08695652173913043, 0.0, ],[0.2705150462962963, 0.0, 0.0, 0.0, 0.0, 0.12058080808080808, 0.04722222222222222, 0.27906976744186046, 0.0, 0.2943722943722944, 0.20473698336017176, 0.0, ]],
[[8.125, 8.666666666666666, 9.166666666666666, 23.5, 20.5, 10.242424242424242, 9.5, 9.906976744186046, 13.037735849056604, 14.519480519480519, 10.405797101449275, 12.755395683453237, ],[11.916666666666666, 7.666666666666667, 8.61111111111111, 6.5, 9.0, 7.090909090909091, 6.476190476190476, 13.023255813953488, 13.69811320754717, 9.969696969696969, 8.492753623188406, 8.33453237410072, ],[17.0, 10.166666666666666, 12.0, 8.0, 11.666666666666666, 11.136363636363637, 12.047619047619047, 18.03488372093023, 14.69811320754717, 17.181818181818183, 11.391304347826088, 21.105215827338128, ],[17.720789930555554, 11.29561149691358, 13.130410879629629, 9.6790283203125, 13.118190285011574, 13.568813131313131, 14.266765873015872, 18.45032299741602, 14.837997903563942, 17.660732323232324, 12.496128556092325, 20.476768585131893, ]],
[[4.331163194444445, 2.435763888888889, 3.8831380208333335, 1.976655505952381, 2.11865234375, 8.030645161290323, 11.45890410958904, 7.120898100172711, 3.2685185185185186, 10.133916884816754, 4.72704475308642, 19.255992329817833, ],[0.01272363410366012, 0.006145162248014376, 0.008523015044621683, 0.0033490215761749686, 0.004921260005963646, 0.015300201101078006, 0.01576048947531405, 0.015018813086033684, 0.006949632144878326, 0.011798075896293822, 0.0131411174634825, 0.027845385989771584, ],[1.2352683832825473E-105, 2.967330386821144E-94, 4.721008633825423E-112, 2.695813079955322E-116, 1.8161720662182217E-120, 1.0008102419858093E-82, 1.4442645969255912E-87, 1.1830286015267275E-91, 2.0588934294297445E-62, 9.193508543210208E-107, 1.31896808515691E-90, 4.68227586194568E-103, ]],
[[1.0, 1.0, 1.7777777777777777, 1.75, 1.6666666666666667, 2.3484848484848486, 1.7380952380952381, 2.244186046511628, 0.16981132075471697, 3.3073593073593073, 1.0434782608695652, 2.8138489208633093, ],[2.1107638888888887, 1.6673514660493827, 2.2214216820987653, 2.5012247721354166, 2.6656584563078702, 3.375126262626263, 2.6499007936507937, 2.2910206718346253, 0.24465408805031447, 3.381664862914863, 1.5421363392377885, 2.8544664268585134, ],[1.6281627763270404E-60, 1.121493132615122E-51, 1.2650354166588515E-51, 2.495450439373704E-67, 3.905770127609793E-70, 8.019865191866931E-37, 1.535285828461501E-42, 2.4970108163579735E-28, 2.126451319141871E-28, 1.129426684469806E-28, 4.2981326208801734E-45, 3.157285023523077E-16, ]],
[[4.333333333333333, 2.1666666666666665, 2.5, 1.7142857142857142, 1.8, 2.412903225806452, 3.76027397260274, 2.922279792746114, 1.0, 2.884816753926702, 1.75, 5.268136784915308, ],[2.8668400616773324, 1.9765677770705985, 2.5096012908540817, 1.570842464974814, 1.5449068159002624, 2.2217649794141034, 3.0310543631483258, 2.9114056096014624, 1.2655712533601555, 2.9016106267266277, 2.2155683441432523, 4.917640742669347, ],[1.7403372249936588E-63, 3.270105837605587E-44, 2.797818188083444E-9, 1.1126117093661497E-58, 1.9916273215267565E-68, 1.2962796525278577E-23, 8.715308834032628E-41, 5.698436680878932E-15, 8.051870223935173E-21, 1.5577251731919414E-17, 5.283841617632623E-39, 1.0464382710412911E-39, ]],
]

out_metric = array[0]

out_accuate =array[1]

out_parent = array[2]

out_child =  array[3]

out_ignore = array[4]

out_irrelevant = array[5]


out_testNum = array[6]


#define figure and figure size figsize=(width, height)
fig = plt.figure(figsize=(11, 22))

#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18


axmetric = fig.add_subplot(4,2,6) #gas1
axmetricn = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn1 = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud
axmetricn2 = fig.add_subplot(4,2,6, sharex=axmetric, sharey=axmetric, frameon=False) #gas1 nomeeritud


axaccuate = fig.add_subplot(4,2,1) #out9
axaccuaten = fig.add_subplot(4,2,1, sharex=axaccuate,sharey=axaccuate, frameon=False) #out9
axaccuaten1 = fig.add_subplot(4,2,1, sharex=axaccuate, sharey=axaccuate, frameon=False) #gas1 nomeeritud
axaccuaten2 = fig.add_subplot(4,2,1, sharex=axaccuate, sharey=axaccuate, frameon=False) #gas1 nomeeritud


axtestnum = fig.add_subplot(4,2,7) #out8
axtestnumn = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #out8
axtestnumn1 = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #gas1 nomeeritud
axtestnumn2 = fig.add_subplot(4,2,7, sharex=axtestnum, sharey=axtestnum, frameon=False) #gas1 nomeeritud



axparent = fig.add_subplot(4,2,3) #out8
axparentn = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #out8
axparentn1 = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #gas1 nomeeritud
axparentn2 = fig.add_subplot(4,2,3, sharex=axparent, sharey=axparent, frameon=False) #gas1 nomeeritud


axchild = fig.add_subplot(4,2,2) #out8
axchildn = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #out8
axchildn1 = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #gas1 nomeeritud
axchildn2 = fig.add_subplot(4,2,2, sharex=axchild, sharey=axchild, frameon=False) #gas1 nomeeritud

axignore = fig.add_subplot(4,2,4) #out8
axignoren = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #out8
axignoren1 = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #gas1 nomeeritud
axignoren2 = fig.add_subplot(4,2,4, sharex=axignore, sharey=axignore, frameon=False) #gas1 nomeeritud

axirrelevant = fig.add_subplot(4,2,5) #out8
axirrelevantn = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #out8
axirrelevantn1 = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #gas1 nomeeritud
axirrelevantn2 = fig.add_subplot(4,2,5, sharex=axirrelevant, sharey=axirrelevant, frameon=False) #gas1 nomeeritud


#plot data and normalized data 
line_1, = axmetric.plot(x, out_metric[0],  marker="s",  color="k")
line_2, = axmetricn.plot(x, out_metric[1], ls="--", marker="d",   color="k")
line_3, = axmetricn1.plot(x, out_metric[2], ls=":", marker="o", mfc="None",   color="k")
line_4, = axmetricn2.plot(x, out_metric[3], ls="-.", marker="*", mfc="None",   color="k")

axaccuate.plot(x, out_accuate[0],  marker="s", color="k")
axaccuaten.plot(x, out_accuate[1], ls="--", marker="d",   color="k")
axaccuaten1.plot(x, out_accuate[2], ls=":", marker="o", mfc="None",   color="k")
axaccuaten2.plot(x, out_accuate[3], ls="-.", marker="*", mfc="None",   color="k")

axtestnum.plot(x, out_testNum[0],  marker="s", color="k")
axtestnumn.plot(x, out_testNum[1], ls="--",marker="d",  color="k")
axtestnumn1.plot(x, out_testNum[2], ls=":", marker="o", mfc="None",   color="k")
axtestnumn2.plot(x, out_testNum[3], ls="-.", marker="*", mfc="None",   color="k")


axparent.plot(x, out_parent[0],  marker="s", color="k")
axparentn.plot(x, out_parent[1], ls="--",marker="d",  color="k")
axparentn1.plot(x, out_parent[2], ls=":", marker="o", mfc="None",   color="k")
axparentn2.plot(x, out_parent[3], ls="-.", marker="*", mfc="None",   color="k")


axchild.plot(x, out_child[0],  marker="s", color="k")
axchildn.plot(x, out_child[1], ls="--",marker="d", color="k")
axchildn1.plot(x, out_child[2], ls=":", marker="o", mfc="None",   color="k")
axchildn2.plot(x, out_child[3], ls="-.", marker="*", mfc="None",   color="k")


axignore.plot(x, out_ignore[0],  marker="s", color="k")
axignoren.plot(x, out_ignore[1], ls="--",marker="d",color="k")
axignoren1.plot(x, out_ignore[2], ls=":", marker="o", mfc="None",   color="k")
axignoren2.plot(x, out_ignore[3], ls="-.", marker="*", mfc="None",   color="k")


axirrelevant.plot(x, out_irrelevant[0],  marker="s", color="k")
axirrelevantn.plot(x, out_irrelevant[1], ls="--",marker="d", color="k")
axirrelevantn1.plot(x, out_irrelevant[2], ls=":", marker="o", mfc="None",   color="k")
axirrelevantn2.plot(x, out_irrelevant[3], ls="-.", marker="*", mfc="None",   color="k")


#configure legend
fig.legend([line_1, line_2, line_3, line_4], ['regard one', 'distin', 'ILP', 'random'],'upper left',
           ncol=4,prop={'size':10})


#configure axis

#1233
#axmetric.set_ylim(0, 1.05)
#axaccuate.set_ylim(0, 1.05)
#axtestnum.set_ylim(0, 1.05)

#axmetric.set_yticks(np.arange(0.7, 1.05, 0.1))
#axaccuate.set_yticks(np.arange(0.8, 1.05, 0.1))
#axtestnum.set_yticks(np.arange(0.8, 1.05, 0.1))

#hide Y tick labels for some plots(only plots on the left and right have labels and ticklabels
##axaccuate.set_yticklabels([]) 
##axtestnum.set_yticklabels([])

#axmetric.set_xlim(1, 12)
#axaccuate.set_xlim(1, 12)
#axtestnum.set_xlim(1, 12)

#axmetric.set_xticks(np.arange(2, 4, 1))
#axaccuate.set_xticks(np.arange(2, 5, 1))
#axtestnum.set_xticks(np.arange(2, 6, 1))


#axmetric.set_xticklabels(['2','3'])
#axaccuate.set_xticklabels(['2','3','4'])
#axtestnum.set_xticklabels(['2','3','4','5'])



#axmetric.set_xticklabels(['2','3'])
#axaccuate.set_xticklabels(['2','3','4'])
#axtestnum.set_xticklabels(['2','3','4','5'])



#disable labels for some plots
##axmetricn.set_yticklabels([])
##axaccuaten.set_yticklabels([])
##axtestnumn.set_yticklabels([])
##
##ax4n.set_yticklabels([])
##ax5n.set_yticklabels([])
##ax6n.set_yticklabels([])


axmetric.yaxis.tick_left()
axaccuate.yaxis.tick_left()
axtestnum.yaxis.tick_left()


#set Y labels
axaccuate.set_xlabel(r"$(a)\ Result\ of\ the\ number\ of\ accurately\ identified\ MFS$")
axmetric.set_xlabel(r"$(f)\ The\ aggregative\ result\ for\ the\ five\ metrics$")
axtestnum.set_xlabel(r"$(g)\ Needed\ test\ cases$")
axparent.set_xlabel(r"$(c)\ Result\ of\ the\ number\ of\ identified\ super-schemas\ of\ the\ MFS$")
axchild.set_xlabel(r"$(b)\ Result\ of\ the\ number\ of\ identified\ sub-schemas\ of\ the\ MFS$")
axignore.set_xlabel(r"$(d)\ Result\ of\ the\ number\ of\ ignored\ MFS$")
axirrelevant.set_xlabel(r"$(e)\ Result\ of\ the\ number\ of\ identified\ irrelevant\ schemas\ of\ the\ MFS$")


#set X labels
axmetric.set_ylabel(r"$AGGREGATIVE\ VALUE$")
axaccuate.set_ylabel(r"$ACCURATE\ NUMBER$")
axtestnum.set_ylabel(r"$NUMBER\ OF\ TEST\ CASES$")
axparent.set_ylabel(r"$SUPER\ NUMBER$")
axchild.set_ylabel(r"$SUB\ NUMBER$")
axignore.set_ylabel(r"$IGNORE\ NUMBER$")
axirrelevant.set_ylabel(r"$IRRELEVANT\ NUMBER$")

#adjust plot spacing
plt.subplots_adjust(left=0.07, bottom=0.08, right=0.97, top=0.96, wspace=0.20, hspace=0.25)

#finally draw the plot
plt.show()
