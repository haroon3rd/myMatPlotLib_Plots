# import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Linux Libertine'
#rcParams['font.sans-serif'] = ['Linux Libertine']

# Changes overall font size
plt.rc('font', size=18)

# Set title font to size 50
#plt.rc('axes', titlesize=50) 

# Set axes labels font to size 16
plt.rc('axes', labelsize=21) 

# Font settings
#fontLabel = {'family': 'Linux Libertine', 'color':  'black', 'size': 18}
csfont = {'fontname':'Linux Libertine'}
#hfont = {'fontname':'Helvetica'}




# Set tick labels font to size 15
#plt.rc('xtick', labelsize=16) 
#plt.rc('ytick', labelsize=16)

# Creating dataset
#x = np.arange(1.0, 100.0, 0.191)
x = np.arange(0.0, 102.5, 2.5)

#dataset_1 = np.exp(x**0.25) - np.exp(x**0.5)
#dataset_2 = np.sin(0.4 * np.pi * x**0.5) + np.cos(0.8 * np.pi * x**0.25)

throughput = np.array([0.0,None,None,None,11.517,None,None,None,22.75,None,None,None,38.383,None,None,None,57.267,None,None,None,72.2,None,None,None,80.483,None,None,None,81.95,None,None,None,82.223,None,None,None,81.633,None,None,None,82.0]).astype(np.double)
pfr_lte = np.array([0.0,0.23,0.380,0.52,0.6,None,0.7,None,0.72,None,None,None,0.63,None,None,None,0.47,None,None,None,0.38,None,None,None,0.325,None,None,None,0.30952380952381,None,None,None,0.3,None,None,None,0.304,None,None,None,0.298]).astype(np.double)
pfr_lte2 = np.array([None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0.30952380952381,None,0.24625,None,0.2014,None,0.136,None,0.0605,None,0.0097,None,0.0]).astype(np.double)
#error3 = (0.45, 0.45, 0.40, 0.35, 0.30, 0.20, 0.15)
#error4 = (0.40, 0.40, 0.40, 0.30, 0.25, 0.15, 0.15)
#error5 = (0.40, 0.40, 0.35, 0.30, 0.20, 0.10, 0.10)

# Creating plot with dataset_1
fig, ax1 = plt.subplots(figsize=(8, 4), dpi=150)

color1 = 'tab:red'

ax1.set_xlim([0, 100])
ax1.set_xlabel('LTE CPU Share [% of a core]')
#ax1.set_xlabel('LTE CPU Share [% of a core]', fontdict=fontLabel)

ax1.set_ylim([0, 100])
#ax1.set_ylabel('LTE Throughput [mbps]', color = color1)
ax1.set_ylabel('LTE Throughput [mbps]')
#ax1.set_ylabel('LTE Throughput [mbps]', fontdict=fontLabel)

legend1 = ax1.plot(x, throughput, marker = 's', linestyle='None', label="Throughput", color = color1, ms=6)
#ax1.tick_params(axis ='y', labelcolor = color1)


# Adding Twin Axes to plot using dataset_3
ax2 = ax1.twinx()
#ax2.set_ylabel('MStorm PFR [fps]', color = color3)
ax2.set_ylabel('Processing Frame Rate [fps]')
#ax2.set_ylabel('Processing Frame Rate [fps]', fontdict=fontLabel)
#ax2.plot(x, dataset_3, color = color3)
#ax2.tick_params(axis ='y', labelcolor = color3)

# Add second series
color2 = 'tab:blue'

ax2.set_ylim([0.0, 1.0])
legend2 = ax2.plot(x, pfr_lte, marker = 'o', linestyle='None', label="PFR-LTE", color = color2, ms=6)
#ax2.legend(loc =9)
#ax1.tick_params(axis ='y', labelcolor = color2)

# Add third series
color3 = 'tab:green'
legend3 = ax2.plot(x, pfr_lte2, marker = '*', linestyle='None', label="PFR-LTE+", color = color3, ms = 8)
#ax2.legend(loc =9)


# Make lines continuous if missing data



#Legend Location
#Location String	Location Code
#'best'			0
#'upper right'			1
#'upper left'			2
#'lower left'			3
#'lower right'			4
#'right'			5
#'center left'			6
#'center right'		7
#'lower center'		8
#'upper center'		9
#'center'			10


# Combine all legends and put them together in one location
legends = legend1 + legend2 + legend3
labels = [l.get_label() for l in legends]

# With legend frame
#ax1.legend(legends, labels, ncol=3, bbox_to_anchor=(0.5, 1.035), loc=9) 

# With no legend frame
ax1.legend(legends, labels, frameon=False, ncol=3, bbox_to_anchor=(0.5, 1.03), loc=9) 


# adding grid
#ax1.grid()

# Adding labels
#ax.set_xlabel("X-axis")
#ax.set_ylabel(r"Y1-axis")
#ax2.set_ylabel(r"Y2-axis")

# Setting Y limits
#ax2.set_ylim(0, 35)
#ax.set_ylim(-20, 100)

# Adding title
#plt.title('Use different y-axes on the left and right of a Matplotlib plot', fontweight ="bold")

# Save Plot
#plt.savefig("example2save.png")

# Show plot
plt.show()


