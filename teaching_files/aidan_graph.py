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
a = [dt.datetime.strptime(d, "%Y-%m-%d").date() for d in result[0]] # thanks to https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis for helping with datetime stuff
b = [float(v) for v in result[2]]
c = [float(v) for v in result[3]]
d = [float(v) for v in result[5]]
avg = [(float(result[2][i]) + float(result[3][i]))/2 for i in range(0, len(result[2]))]

ax.plot(a,avg, label = "Average Price", color = "green", linewidth = 1)
ax.plot(a,d, label = "Trade Volume", color = "blue", linestyle = "--", linewidth = 1)
plot.title("Microsoft Stock Price Over Time")
plot.xlabel("Date")
plot.ylabel("Price (USD)")
plot.legend()
plot.show()
