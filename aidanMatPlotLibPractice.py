import matplotlib.pyplot as plot
import numpy as np
import csv

result = {
    "Date" and 0:[],
    "Open" and 1:[],
    "High" and 2:[],
    "Low" and 3:[],
    "Close" and 4:[],
    "Adj Close" and 5:[],
    "Volume" and 6:[]
}


with open("microsoft_stock_price.csv", newline="") as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for n,row in enumerate(read):
        if n == 0: continue
        else:
            resultArray = row[0].split(",")
            for i,v in enumerate(resultArray):
                #print(i,v)
                result[i].append(v)
a = []
b = []
for count,v in enumerate(result[1]):
    a.append(count)
    b.append(float(v))
fig, ax = plot.subplots()
ax.plot(a,b)
plot.show()