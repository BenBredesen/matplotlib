import matplotlib.pyplot as plt
import numpy as np


#this code generates a basic, random scatter plot. Can you make a visible trend in the data? For example, you could make different colors have higher or lower values on average.

np.random.seed(19680801)
fig, ax = plt.subplots()


for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750 #Number of data points
    x, y = np.random.rand(2, n) #Generates a list of length n of random numbers from 0-1
    scale = 200.0 * np.random.rand(n) #Generates a random scale for each point
    ax.scatter(x, y, c=color, s=scale, label=color,alpha=0.3, edgecolors='none') #Adds the scatter plot to the graph

ax.legend()
ax.grid()
plt.savefig('practice_problems/scatter_plot/scatter_plot.png')
plt.show()