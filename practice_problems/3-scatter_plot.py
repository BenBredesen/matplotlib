import matplotlib.pyplot as plt
import numpy as np


#This code generates a basic, random scatter plot. Can you make a visible trend in the data? For example, you could make different colors have higher or lower values on average.

np.random.seed(19680801)
fig, ax = plt.subplots()


for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750 #Number of data points
    x, y = np.random.rand(2, n) #Generates two lists of length n of random numbers from 0-1
    scale = 200.0 * np.random.rand(n) #Generates a random scale for each point
    ax.scatter(x, y, c=color, label=color,s=scale,alpha=0.3) #Adds the scatter plot to the graph and the legend

ax.legend()
ax.grid()
plt.savefig('practice_problems/3-scatter_plot.png')
plt.show()