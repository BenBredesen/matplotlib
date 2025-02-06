import matplotlib.pyplot as plot
import numpy as np
import csv
import datetime as dt

result = {
    "Date" and 0:[],
    "Open" and 1:[],
    "High" and 2:[],
    "Low" and 3:[],
    "Close" and 4:[],
    "Adj Close" and 5:[],
    "Volume" and 6:[]
}


with open("teaching_files/microsoft_stock_price.csv", newline="") as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for n,row in enumerate(read):
        if n == 0: continue
        else:
            resultArray = row[0].split(",")
            for i,v in enumerate(resultArray):
                #print(i,v)
                result[i].append(v)
fig, ax = plot.subplots()
a = [dt.datetime.strptime(d, "%Y-%m-%d").date() for d in result[0]]
b = [float(v) for v in result[1]]
ax.plot(a,b)
plot.show()