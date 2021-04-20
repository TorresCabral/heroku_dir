# -*- coding: utf-8 -*-

"""
Created on Fri Sep 11 20:35:16 2020
@author: Prof. Dr. Wellington M. S. Bernardes
"""
from numpy import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Define variables
myheading = 'Circuitos Trifásicos Desequilibrados (Configuração Estrela)'
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

#---------------------------------------------------------------
#Taken from https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
df = pd.read_csv("COVID-19-geographic-disbtribution-worldwide-2020-03-29.csv")

dff = df.groupby('countriesAndTerritories', as_index=False)[['deaths','cases']].sum()
print (dff[:5])
# Set up the layout
app.layout = html.Div(children=[

    html.H1(myheading),
    #html.H2('Configuração Estrela')
    html.P('Disciplina: Exp. Circ. Elétricos II'),
    html.P('Docente: Prof. Dr. Wellington Maycon Santos Bernardes'),
    html.P('Discentes: Iohana A. Torres Cabral e Wallison Junio'),

    html.Div([
        dash_table.DataTable(
            id='data_table',
            columns=[{
                'name': 'Column {}'.format(i),
                'id': 'column-{}'.format(i),
            } for i in range(1, 5)],
            data=[
            {'column-{}'.format(i): (j + (i-1)*5) for i in range(1, 5)}
            for j in range(5)
            ]
        ),
        html.Div(id='output_div')
    ])className='row'),
])
@app.callback(
    Output('output_div', 'children'),
    Input('data_table', 'active_cell'),
    State('data_table', 'data')
)
def getActiveCell(active_cell, data):
    if active_cell:
        col = active_cell['column_id']
        row = active_cell['row']
        cellData = data[row][col]
return html.P(f'row: {row}, col: {col}, value: {cellData}')
return html.P('no cell selected')

dcc.Interval(             
    id='interval-component',             
    interval=1*1000, # in milliseconds             
    n_intervals=0         
)
@app.callback(
    Output('component-to-update', 'property'),                      
    Input('interval-component', 'n_intervals')
)
def update(n_intervals):
    if n_intervals > 0:
        # update table data

@app.callback(
    Output('data_table', 'data'),
    Input('interval-component', 'n_intervals'),
    [State('data_table', 'data'), State('data_table', 'columns')]
)
def updateData(n, data, columns):
    if n > 0:
        data.append({c['id']: n for c in columns})
    return data
    


#------------------------------------------------------------------



if __name__ == '__main__':
 app.run_server(debug=True)