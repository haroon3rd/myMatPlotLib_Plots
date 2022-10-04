# import libraries
import numpy as np
import matplotlib.pyplot as plt

# Creating dataset
#x = np.arange(1.0, 100.0, 0.191)
x = np.arange(0.0, 7.0, 1.0)

#dataset_1 = np.exp(x**0.25) - np.exp(x**0.5)
#dataset_2 = np.sin(0.4 * np.pi * x**0.5) + np.cos(0.8 * np.pi * x**0.25)

dataset_1 = np.array([0.45, 0.55, 0.45, 0.35, 0.35, 0.20, 0.25])
dataset_2 = np.array([0.50, 0.50, 0.40, 0.40, 0.35, 0.25, 0.20])
dataset_3 = np.array([0.48, 0.53, 0.43, 0.38, 0.38, 0.29, 0.15])
#error3 = (0.45, 0.45, 0.40, 0.35, 0.30, 0.20, 0.15)
#error4 = (0.40, 0.40, 0.40, 0.30, 0.25, 0.15, 0.15)
#error5 = (0.40, 0.40, 0.35, 0.30, 0.20, 0.10, 0.10)

# Creating plot with dataset_1 and dataset_2
fig, ax1 = plt.subplots(figsize=(8, 4), dpi=300)

color1 = 'tab:red'

ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y1-axis', color = color1)
ax1.plot(x, dataset_1, color = color1)
#ax1.tick_params(axis ='y', labelcolor = color1)
# Add second series
color2 = 'tab:blue'
ax1.plot(x, dataset_2, color = color2)
#ax1.tick_params(axis ='y', labelcolor = color2)

# Adding Twin Axes to plot using dataset_3
ax2 = ax1.twinx()

color3 = 'tab:green'
ax2.set_ylabel('Y2-axis', color = color3)
ax2.plot(x, dataset_3, color = color3)
#ax2.tick_params(axis ='y', labelcolor = color3)


# Adding title
plt.title('Use different y-axes on the left and right of a Matplotlib plot', fontweight ="bold")

# Save Plot
plt.savefig("example2save.png")

# Show plot
#plt.show()


