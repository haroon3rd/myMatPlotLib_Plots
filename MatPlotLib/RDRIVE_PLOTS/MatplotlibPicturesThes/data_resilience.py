import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

device_avail_rate = ['0.2', '0.4', '0.6', '0.8', '1.0']
success_rate = [15, 35, 55, 90, 100]
error = [0.5, 2, 2.5, 5, 0]

hatches = [ '/' , '\\' , '|' , 'X' , '-']


#fints
fontLabel = {'family': 'Helvetica', 'color':  'black', 'size': 65}
plt.ylabel('File Retrieval Success Rate', fontdict=fontLabel)
plt.xlabel('Device Availability', fontdict=fontLabel, labelpad = 5)

#x and y ticks
plt.xticks(fontsize=55)
plt.yticks(fontsize=60)

#outside borders
ax = plt.axes()    
ax.set_axisbelow(True)    
ax.yaxis.grid(color='black', linestyle='dashed')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)


#legends
p1 = mpatches.Patch(color='lightcoral', label='0.2', linewidth = 10,)
p2 = mpatches.Patch(color='palegreen', label='0.4', edgecolor ='black', linewidth = 10, hatch = 'X')
p3 = mpatches.Patch(color='skyblue', label='0.6', edgecolor ='black', linewidth = 10)
p4 = mpatches.Patch(color='lightpink', label='0.8', edgecolor ='black', linewidth = 10)
p5 = mpatches.Patch(color='lightyellow', label='1.0', edgecolor ='black', linewidth = 10)

# plot the bar
barr = plt.bar(device_avail_rate, success_rate, color=['lightcoral', 'palegreen', 'skyblue', 'lightpink', 'lightyellow'], linewidth = 1.3,  edgecolor='k', yerr = error, ecolor='black', capsize=10)

#legends
plt.legend(handles=[p1, p2, p3, p4, p5], ncol=1, fancybox=True, shadow=True, prop={'size':46.5}, title = "Code Rate", title_fontsize = 45, edgecolor = 'k')


#add hatched to each bar
for i,thisbar in enumerate(barr.patches):
    # Set a different hatch for each bar
    thisbar.set_hatch(hatches[i])

#legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large', prop={'size':40.5}, edgecolor = 'k')

plt.ylim(0, 105)
plt.show()



