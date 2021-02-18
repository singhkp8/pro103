import pandas as pa
import plotly.express as px

df = pa.read_csv("pro.csv")

fig = px.scatter(df,x = "cases", y="country")

fig.show()
# date,cases,country