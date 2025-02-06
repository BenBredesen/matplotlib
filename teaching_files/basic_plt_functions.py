import matplotlib.pyplot as plt
import numpy as np


#Setup the chart
fig, ax = plt.subplots()
ax.set(xlabel='X-axis Label', ylabel='Y-axis Label',title='Graph Title')
ax.grid()


#Create the data
xMin, xMax, steps = 0,2,10
yMin,yMax = 0,10
x2 = np.linspace(xMin,xMax,steps)
y2=[]

#Random value generation
y2 = np.random.rand(steps)*yMax

#Using predefined values
x = np.linspace(0,2,7)
y=[0,1,3,9,2,6,8]


#Put the data on the graph
ax.plot(x,y,label='Predefined Data')
ax.plot(x2,y2,label='Random Data')
ax.legend(loc='best', fontsize='small')

plt.show()