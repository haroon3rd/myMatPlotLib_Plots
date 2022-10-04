import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']

N = 7
one_replica =     (16.75, 16.85, 17.15, 17.35, 17.60, 17.90, 17.95)
three_replicas =  (23.15, 23.70, 23.35, 25.55, 25.75, 25.30, 26.95)
five_replicas =   (23.10, 23.10, 23.55, 25.80, 25.60, 25.85, 26.20)
seven_replicas =  (23.10, 23.20, 24.10, 26.10, 25.90, 26.15, 27.50)
nine_replicas =   (23.15, 23.35, 24.15, 26.30, 27.00, 26.25, 27.90)

#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.15

error1 = (0.20, 0.25, 0.35, 0.40, 0.45, 0.50, 0.50)
error2 = (0.20, 0.25, 0.35, 0.40, 0.40, 0.50, 0.50)
error3 = (0.20, 0.20, 0.30, 0.35, 0.40, 0.45, 0.45)
error4 = (0.20, 0.15, 0.25, 0.30, 0.40, 0.40, 0.40)
error5 = (0.20, 0.10, 0.20, 0.30, 0.35, 0.40, 0.40)



plt.bar(ind, 						one_replica, 	width, label='1',  linewidth = 2.0, hatch= "/", 	color= "lightcoral", edgecolor='black',)
plt.bar(0.02 + ind + width, 				three_replicas, width, label='3', linewidth = 2.0, hatch = '\\', 	color = "palegreen", edgecolor='black', )
plt.bar(0.04 + ind + width + width, 			five_replicas, 	width, label='5', linewidth = 2.0, hatch = "|", 	color = "skyblue", edgecolor='black',)
plt.bar(0.06 + ind + width + width + width, 		seven_replicas, width, label='7', linewidth = 2.0, hatch = "X", 	color = "lightpink", edgecolor='black',)
plt.bar(0.08 + ind + width + width + width + width, 	nine_replicas, 	width, label='9', linewidth = 2.0, hatch = "-", 	color = "lightyellow", edgecolor='black',)

fontLabel = {'family': 'Tahoma', 'color':  'black', 'size': 65}
plt.ylabel('Ave. Write Latency (ms)', fontdict=fontLabel)
plt.xlabel('Metadata Size', fontdict=fontLabel)

plt.xticks(fontsize=55)
plt.yticks(fontsize=60)

plt.xticks(ind + (3.5*width) / 2, ('1KB', '2KB', '4KB', '8KB', '10KB', '12KB', '15KB'))
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5, fancybox=True, shadow=True, prop={'size': 40}, title = "Number of Servers", title_fontsize = 35)
plt.legend(loc='upper center', ncol=5, fancybox=True, shadow=True, prop={'size': 46.5}, title = "Number of Servers", title_fontsize = 45)

ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


plt.ylim(16, 31)
plt.show()



#plt.savefig("succ.pdf", bbox_inches='tight')met	
