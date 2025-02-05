import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(0,10,100)

fig, ax = plot.subplots()
ax.grid(visible=True)
ax.plot(x,x**2)
plot.show()