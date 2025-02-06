import matplotlib.pyplot as plot

mockGraphResults = {
    "yes":2398,
    "no":3731,
    "maybe":1281
}

key = [k for k in mockGraphResults]
value = [k for v,k in mockGraphResults]

print(key)
print(value)

fig, ax = plot.subplots()
ax.bar(key ,value)