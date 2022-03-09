from operator import imod
import pandas as pd

import plotly.express as ps

df = pd.read_csv("C103/csv files/data.csv")
graph = ps.bar(df , x = 'Country' , y = 'Population')
graph.show()

