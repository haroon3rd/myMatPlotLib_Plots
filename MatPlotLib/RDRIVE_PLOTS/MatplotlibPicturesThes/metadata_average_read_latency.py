import matplotlib.pyplot as plt
import numpy as np

N = 7
one_replica =     (14.50, 14.50, 14.60, 14.70, 15.00, 15.10, 15.10)
three_replicas =  (12.15, 12.25, 12.25, 12.30, 12.35, 12.70, 12.80)
five_replicas =   (11.95, 12.25, 12.15, 12.25, 12.35, 12.60, 12.50)
seven_replicas =  (11.95, 12.20, 12.15, 12.20, 12.25, 12.50, 12.45)
nine_replicas =   (11.90, 11.90, 11.85, 12.15, 12.20, 12.45, 12.05)

#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.15

error1 = (0.50, 0.50, 0.45, 0.40, 0.35, 0.25, 0.20)
error2 = (0.50, 0.50, 0.40, 0.40, 0.35, 0.25, 0.20)
error3 = (0.45, 0.45, 0.40, 0.35, 0.30, 0.20, 0.15)
error4 = (0.40, 0.40, 0.40, 0.30, 0.25, 0.15, 0.15)
error5 = (0.40, 0.40, 0.35, 0.30, 0.20, 0.10, 0.10)



plt.bar(ind, 						one_replica, 	width, label='1',  linewidth = 1.3, hatch= "/", 	color= "lightcoral", edgecolor='black', )
plt.bar(0.02 + ind + width, 				three_replicas, width, label='3', linewidth = 1.3, hatch = '\\', 	color = "palegreen", edgecolor='black', )
plt.bar(0.04 + ind + width + width, 			five_replicas, 	width, label='5', linewidth = 1.3, hatch = "|", 	color = "skyblue", edgecolor='black', )
plt.bar(0.06 + ind + width + width + width, 		seven_replicas, width, label='7', linewidth = 1.3, hatch = "X", 	color = "lightpink", edgecolor='black', )
plt.bar(0.08 + ind + width + width + width + width, 	nine_replicas, 	width, label='9', linewidth = 1.3, hatch = "-", 	color = "lightyellow", edgecolor='black',)

fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 65}
plt.ylabel('Ave. Read Latency (ms)', fontdict=fontLabel)
plt.xlabel('Metadata Size', fontdict=fontLabel)

plt.xticks(fontsize=55)
plt.yticks(fontsize=60)

plt.xticks(ind + (3.5*width) / 2, ('1KB', '2KB', '4KB', '8KB', '10KB', '12KB', '15KB'))
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5, fancybox=True, shadow=True, prop={'size':46.5}, title = "Number of Servers", title_fontsize = 45)

ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


plt.ylim(11, 17)
plt.show()



#plt.savefig("succ.pdf", bbox_inches='tight')met	
