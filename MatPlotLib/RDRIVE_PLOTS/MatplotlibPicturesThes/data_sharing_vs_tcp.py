import matplotlib.pyplot as plt
import numpy as np

N = 5
rsock =  (1200/60, 785/60, 510/60, 355/60, 315/60)
tcp =    (515/60,  325/60, 205/60, 140/60, 120/60)


rsock_errUp =   [3.5,     2.5,     1.5,     1.3,     0.5]
rsock_errDown = [0.5,     0.5,     0.5,     0.0,     0.0]

tcp_errUp =   [1.6,   1.3,   0.7,   0.3,   0.3]
tcp_errDown = [0.2,   0.1,   0.0,   0.0,   0.0]

rsock_err = [rsock_errDown, rsock_errUp]
tcp_err = [tcp_errDown, tcp_errUp]

#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.35



plt.bar(ind, 						rsock, 	width, label='RSock',  linewidth = 1.3, hatch= "/", 	color= "lightcoral", edgecolor='black', yerr = rsock_err, ecolor='black', capsize=10 )
plt.bar(0.02 + ind + width, 				tcp, width, label='TCP', linewidth = 1.3, hatch = '\\', 	color = "palegreen", edgecolor='black', yerr = tcp_err, ecolor='black', capsize=10)

fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 65}
plt.ylabel('Ave. Sharing Delay (Min)', fontdict=fontLabel)
plt.xlabel('Prob. of Link Availability', fontdict=fontLabel, labelpad = -5)

plt.xticks(fontsize=55)
plt.yticks(fontsize=60)

plt.xticks(ind + (1.05*width) / 2, ('0.2', '0.4', '0.6', '0.8', '1.0'))

plt.legend(loc='best', bbox_to_anchor=(0.5, 1.0), ncol=1, fancybox=True, shadow=True, prop={'size':46.5}, title_fontsize = 45)

ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


plt.ylim(1, 26.5, 1)
plt.show()




#plt.savefig("succ.pdf", bbox_inches='tight')met	
