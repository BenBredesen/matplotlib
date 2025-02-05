import matplotlib.pyplot as plt
import numpy as np
import csv

#stock price data: https://www.kaggle.com/datasets/umerhaddii/microsoft-stock-data-2025/data

csvFile = []
with open('microsoft_stock_price.csv', mode ='r')as file:
  csvFile = csv.reader(file)


fig, ax = plt.subplots()


# for line in csvFile:
#     n = 750
#     x, y = np.random.rand(2, n)
#     scale = 200.0 * np.random.rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Date (year)', ylabel='Stock Price (USD)',
       title='Microsoft Stock Price Over Time')
ax.grid()

fig.savefig("stock_price.png")
plt.show()