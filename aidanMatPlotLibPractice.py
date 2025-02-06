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



with open("microsoft_stock_price.csv", newline="") as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for n,row in enumerate(read):
        if n == 0: continue
        else:
            resultArray = row[0].split(",")
            for i,v in enumerate(resultArray):
                #print(i,v)
                result[i].append(v)
a = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in result[0]] #datetime math added in with the help of https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis
b = [float(v) for v in result[1]] #opening price
c = [float(v) for v in result[4]] #closing price
fig, ax = plot.subplots()
ax.plot(a,b)
ax.plot(a,c)
plot.show()
