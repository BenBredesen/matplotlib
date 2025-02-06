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
b = []
for count,v in enumerate(result[1]):
    b.append(float(v))
a = np.linspace(1986,2025,len(b))
ax.plot(a,b)
print(a[-1],b[-1])
plot.show()