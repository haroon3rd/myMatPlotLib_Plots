import matplotlib.pyplot as plt
import numpy as np

N = 5
time = 	 (22.40, 18.90, 00.625, 43.60, 53.00)
error1 = (06.50, 04.50, 00.100, 03.25, 08.35)

#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.50
plt.bar(ind, time, width, label='1',  linewidth = 2.0, hatch= "", 	color= "lightblue", edgecolor='black',  yerr = error1, ecolor='black', capsize=10)



fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 50}
plt.ylabel('Edge Formation Delay (sec) \n', fontdict=fontLabel)
plt.xlabel('\n Replica Setting', fontdict=fontLabel)

plt.xticks(fontsize=45)
plt.yticks(fontsize=45)

plt.xticks(ind, ('0R/0T + 2C\n = 2R', '2R/2T + 1C\n = 3R', '3R/3T + 2C\n = 3R + 2C', '3R/5T - 1R\n = 3R + 1C', '3R/5T - 2R\n = 3R'))

ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


plt.ylim(0, 62)
plt.show()



#plt.savefig("succ.pdf", bbox_inches='tight')met	
