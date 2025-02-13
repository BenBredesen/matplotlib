import pandas as pd 
import matplotlib.pyplot as plot 
import datetime as dt

data = pd.read_csv("teaching_files/microsoft_stock_price.csv")
data.iloc[:,0] = pd.to_datetime(data.iloc[:,0], format="%Y-%m-%d")
x = data.iloc[:,0]
#x = [dt.datetime.strptime(d, "%Y-%m-%d").date() for d in data['Date']]
y = data['High']

fig, ax = plot.subplots()
ax.plot(x,y)
plot.show()