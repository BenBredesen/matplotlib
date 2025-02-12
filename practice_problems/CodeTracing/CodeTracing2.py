import matplotlib.pyplot as plot
import numpy as np

fig, ax = plot.subplots()

result = [[],[]]
for n in range(-700,700,10):
    result[0].append(np.sin(n/100)*0.5)
    result[1].append(n/100)

ax.plot(result[0],result[1], lw = 0.5)
fig.savefig("practice_problems/CodeTracing/ct2.png")
plot.show()
