# -*- coding: utf-8 -*-

"""
Created on Fri Sep 11 20:35:16 2020
@author: Prof. Dr. Wellington M. S. Bernardes
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Define variables
myheading = 'Testando Python no Heroku'
apptitle = "UFU!"
milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']
moodle_address = 'http://www.ufu.br/tags/moodle'
fig = go.Figure(data=go.Scatter(y = time_series, mode = 'lines')) # or any Plotly Express function e.g. px.bar(...)

# Initiate app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title=apptitle
server = app.server

# Set up the layout
app.layout = html.Div(children=[
 html.H1(myheading),
 html.P('Disciplina: Exp. Circ. Elétricos II'),
 html.P('Prof. Dr. Wellington Maycon Santos Bernardes'),
 html.I('Caros alunos, aqui segue um exemplo de uma página feita no Python e que está disponibilizada na Internet.'),
 dcc.Graph(
 id='figura',
 figure=fig),
 html.A('Acesse UFU',href='http://www.ufu.br'),
 html.Br(),
 html.A('Acesse Moodle', href=moodle_address)])
if __name__ == '__main__':
 app.run_server(debug=True)