from turtle import color
import pandas as ps

import plotly.express as pe

df = ps.read_csv("C103/csv files/Copy+of+data+-+data.csv")
gr = pe.scatter(df , x = 'date' , y = 'cases' , color = 'country')
gr.show()
