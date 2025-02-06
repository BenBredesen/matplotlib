import matplotlib.pyplot as plt
import numpy as np

#Setup the chart
fig, (ax1,ax2) = plt.subplots(2)
ax1.set(ylabel='Y-axis Label',title='Graph Title')
ax2.set(ylabel='Y-axis Label',title='Graph Title')
ax1.grid()
ax2.grid()

#Generate 2 sets of x and y values, one for each graph

x1 = [0,1,2,3]
y1 = [3,5,1,8]
x2 = [4,5,6,7]
y2 = [1,9,4,8]


ax1.plot(x1,y1)
ax2.plot(x1,y1,label='Data 1')
ax2.plot(x1,y2,label='Data 2')
ax2.legend(loc='best', fontsize='small')
plt.savefig('practice_problems/basic_practice/setup_practice.png')
plt.show()