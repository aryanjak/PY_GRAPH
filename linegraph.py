from turtle import color
import pandas as ps

import plotly.express as pe

df = ps.read_csv("C103/csv files/line_chart.csv")
gr = pe.line(df , x = 'Year' , y = 'Per capita income' , color = 'Country')
gr.show()
