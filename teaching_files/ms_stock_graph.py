import matplotlib.pyplot as plt
import numpy as np
import csv

#stock price data: https://www.kaggle.com/datasets/umerhaddii/microsoft-stock-data-2025/data

#Load the data from the file
result = {
    "Date" and 0:[],
    "Open" and 1:[],
    "High" and 2:[],
    "Low" and 3:[],
    "Close" and 4:[],
    "Adj Close" and 5:[],
    "Volume" and 6:[]
  }
def loadData():


  with open("teaching_files/microsoft_stock_price.csv", newline="") as csvfile:
      read = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for n,row in enumerate(read):
          if n == 0: continue
          else:
              resultArray = row[0].split(",")
              for i,v in enumerate(resultArray):
                  #print(i,v)
                  result[i].append(v)
loadData()


#Setup the graph
fig, ax = plt.subplots()
def graphSetup():
  ax.set(xlabel='Date (year)', ylabel='Stock Price (USD)',
        title='Microsoft Stock Price Over Time')
  ax.grid()
  ax.set_yscale('linear')
graphSetup()



#Load the data into arrays
a = []
b = []
def intoArrays():
  for count,v in enumerate(result[1]):
      b.append(float(v))

intoArrays()
a = np.linspace(1986,2025,len(b))


#Show and save the graph
def displayGraph():
  ax.plot(a,b)
  fig.savefig("teaching_files/stock_price.png")
  plt.show()
displayGraph()