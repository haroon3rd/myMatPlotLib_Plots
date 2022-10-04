import matplotlib.pyplot as plt

labels = ['Cookies', 'Jellybean', 'Milkshake']
sizes = [38.4, 40.6, 20.7]
colors = ['yellowgreen', 'gold', 'lightskyblue']
patches, texts = plt.pie(sizes, colors=colors, shadow=False, startangle=90)
plt.legend(patches, labels, loc="best", fancybox=True, shadow=True, prop={'size':35.5}, title = "Code Rate", title_fontsize = 45, edgecolor = 'k')
plt.axis('equal')
plt.tight_layout()
plt.show()
