import matplotlib.pyplot as plt
import numpy as np


#Setup the chart
fig, ax = plt.subplots()
ax.set(xlabel='X-axis Label', ylabel='Y-axis Label',title='Graph Title')
ax.grid()


#Create the data
xMin, xMax, steps = 0,10,10
yMin,yMax = 0,100
x = np.linspace(xMin,xMax,steps)
y=[]

#Random value generation
y = np.random.rand(steps)

#Using predefined values
x = np.linspace(0,2,7)
y=[0,1,3,9,2,6,8]


#Put the data on the graph
ax.plot(x,y)

plt.show()