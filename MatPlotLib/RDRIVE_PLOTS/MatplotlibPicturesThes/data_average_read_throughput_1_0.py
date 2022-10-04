import matplotlib.pyplot as plt
import numpy as np

N = 8
one_replica=      (11.56, 11.23, 11.43, 12.21, 12.84, 13.91, 15.70, 16.67)
three_replicas =  (10.75, 10.60, 11.24, 11.70, 13.67, 12.83, 15.59, 17.54)
five_replicas =   (10.32, 10.71, 11.24, 11.58, 12.47, 12.13, 14.60, 15.52)
seven_replicas =  (10.00, 10.31, 10.50, 11.58, 12.27, 12.22, 14.35, 14.84)
nine_replicas =   (09.81, 10.92, 10.16, 10.99, 12.60, 11.96, 14.52, 15.19)

#plt.rcParams["font.weight"0 = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.16

error1 = (0.51, 0.49, 0.35, 0.71, 0.33, 0.25, 0.18, 0.12)
error2 = (0.21, 0.78, 0.33, 0.41, 0.62, 0.24, 0.18, 0.67)
error3 = (0.28, 0.38, 0.63, 0.36, 0.31, 0.19, 0.16, 0.11)
error4 = (0.25, 0.45, 0.41, 0.62, 0.25, 0.54, 0.44, 0.09)
error5 = (0.35, 0.35, 0.41, 0.32, 0.25, 0.14, 0.14, 0.56)


plt.bar(ind, 						one_replica, 	width, label='1/1',  linewidth = 1.3, hatch= "/", 	color= "lightcoral", edgecolor='black',  yerr = error1, ecolor='black', capsize=10)
plt.bar(0.02 + ind + width, 				three_replicas, width, label='2/3', linewidth = 1.3, hatch = '\\', 	color = "palegreen", edgecolor='black', yerr = error2, ecolor='black', capsize=10 )
plt.bar(0.04 + ind + width + width, 			five_replicas, 	width, label='3/5', linewidth = 1.3, hatch = "|", 	color = "skyblue", edgecolor='black',  yerr = error3, ecolor='black', capsize=10 )
plt.bar(0.06 + ind + width + width + width, 		seven_replicas, width, label='4/7', linewidth = 1.3, hatch = "X", 	color = "lightpink", edgecolor='black',  yerr = error4, ecolor='black', capsize=10 )
plt.bar(0.08 + ind + width + width + width + width, 	nine_replicas, 	width, label='5/9', linewidth = 1.3, hatch = "-", 	color = "lightyellow", edgecolor='black', yerr = error5, ecolor='black', capsize=10 )

fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 65}
plt.ylabel('Ave. Read Tput. (MB/sec)', fontdict=fontLabel)
plt.xlabel('Block Size', fontdict=fontLabel)

plt.xticks(fontsize=55)
plt.yticks(fontsize=60)

plt.xticks(ind + (4*width) / 2, ('1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '80MB'))
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5, fancybox=True, shadow=True, prop={'size': 40}, title = "K/N ratios", title_fontsize = 35)
plt.legend(loc='upper left', ncol=3, fancybox=True, shadow=True, prop={'size': 46.5}, title = "K/N ratios", title_fontsize = 45)

ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


plt.ylim(9, 19)
plt.show()



#plt.savefig("succ.pdf", bbox_inches='tight')met	
