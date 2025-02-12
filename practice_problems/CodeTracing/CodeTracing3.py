import matplotlib.pyplot as plot

SurveyResults = [
    ["Yes", "No", "Maybe", "invisible"],
    [100,22, 68, -18],
    ["red", "orange", "yellow", "white"]]

fig, ax = plot.subplots(figsize=(5,2.7), layout='constrained')
ax.bar(SurveyResults[0],SurveyResults[1],color = SurveyResults[2])
fig.savefig("practice_problems/CodeTracing/ct3.png")
plot.show()