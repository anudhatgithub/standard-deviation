import csv
import math
with open("classa.csv","r") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

count = 0
sum = 0
for i in data:
    sum = sum + int(i[1])
    count = count + 1

print(count)
print(sum)

average = sum/count
print(average)

sdsum = 0
#calculating Standard Deviation
for i in data:
    diff = int(i[1]) - average
    diff = diff * diff
    sdsum = sdsum + diff

sd =math.sqrt( sdsum/count)


import pandas as pd
import plotly_express as px

df = pd.read_csv("stand.csv")
fig = px.scatter(df, x="Student Number",y = "Marks")

fig.update_layout(shapes=[dict(type='line', x0 = 0,y0=average,x1=count,y1=average)])
fig.update_yaxes(rangemode="tozero")
fig.show()

print (sd)