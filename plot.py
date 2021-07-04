import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots


def initial(data):
    no, yes = list(data['Churn'].value_counts())
    labels = ['No', 'Yes']
    values = [no, yes]

    fig1 = go.Figure(
        data=[go.Pie(labels=labels, values=values, pull=[0, 0.2])])
    fig1.write_html("one.html", include_plotlyjs="cdn")


def figures_to_html(figs, filename="telecom_eda.html"):
    dashboard_cube = open(filename, 'w')
    dashboard_cube.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard_cube.write(inner_html)
    dashboard_cube.write("</body></html>" + "\n")


data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(data.head())

initial(data)

# figures_to_html([fig1, fig1])
