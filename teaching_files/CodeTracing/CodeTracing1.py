import matplotlib.pyplot as plot

p =[[1,2,3,4,6],[22,0,-2,6,18]]
f,a = plot.subplots()
a.plot(p[0],p[1], color = "pink", linestyle = ":")
a.minorticks_on()
a.set_title("Practice Plot")
a.set_ylabel("y axis")
a.grid(True)
plot.show()
a.set_xlabel("x axis")

