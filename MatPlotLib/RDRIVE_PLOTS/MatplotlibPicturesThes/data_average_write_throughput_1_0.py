import matplotlib.pyplot as plt
import numpy as np

N = 8

one_replica =     (06.92, 07.19, 07.69, 08.37, 09.48, 11.58, 14.50, 14.99)
three_replicas =  (06.45, 07.50, 07.41, 07.69, 08.83, 09.45, 14.39, 14.76)
five_replicas =   (06.00, 06.84, 08.36, 08.12, 08.49, 10.97, 13.30, 14.16)
seven_replicas =  (05.86, 06.56, 07.12, 07.38, 07.96, 09.24, 14.20, 13.76)
nine_replicas =   (04.21, 05.12, 05.84, 06.76, 08.91, 10.04, 13.12, 13.66)

#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"

ind = np.arange(N) 
width = 0.15

error1 = (0.32, 0.30, 0.26, 0.22, 0.24, 0.46, 0.39, 0.33)
error2 = (0.32, 0.79, 0.34, 0.22, 0.23, 0.65, 0.39, 0.33)
error3 = (0.29, 0.29, 0.64, 0.67, 0.22, 0.65, 0.37, 0.32)
error4 = (0.36, 0.36, 0.42, 0.23, 0.26, 0.32, 0.65, 0.30)
error5 = (0.36, 0.26, 0.22, 0.22, 0.44, 0.72, 0.35, 0.28)

plt.bar(ind, 						one_replica, 	width, label='1/1',  linewidth = 1.3, hatch= "/", 	color= "lightcoral", edgecolor='black', yerr = error1, ecolor='black', capsize=10)
plt.bar(0.02 + ind + width, 				three_replicas, width, label='2/3', linewidth = 1.3, hatch = '\\', 	color = "palegreen", edgecolor='black', yerr = error2, ecolor='black', capsize=10)
plt.bar(0.04 + ind + width + width, 			five_replicas, 	width, label='3/5', linewidth = 1.3, hatch = "|", 	color = "skyblue", edgecolor='black', yerr = error3, ecolor='black', capsize=10)
plt.bar(0.06 + ind + width + width + width, 		seven_replicas, width, label='4/7', linewidth = 1.3, hatch = "X", 	color = "lightpink", edgecolor='black', yerr = error4, ecolor='black', capsize=10)
plt.bar(0.08 + ind + width + width + width + width, 	nine_replicas, 	width, label='5/9', linewidth = 1.3, hatch = "-", 	color = "lightyellow", edgecolor='black', yerr = error5, ecolor='black', capsize=10)

fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 65}
plt.ylabel('Ave. Write Tput. (MB/sec)', fontdict=fontLabel)
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

ax.set_yticks(range(4, 18, 1))

plt.ylim(4, 16)
plt.show()



#plt.savefig("succ.pdf", bbox_inches='tight')met	
