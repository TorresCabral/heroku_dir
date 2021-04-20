# -*- coding: utf-8 -*-

"""
Created on Fri Sep 11 20:35:16 2020
@author: Prof. Dr. Wellington M. S. Bernardes
"""
import calculoce2
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
moodle_address = 'http://www.ufu.br/tags/moodle'


# Initiate app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title=apptitle
server = app.server

#---------------------------------------------------------------

# Set up the layout
app.layout = html.Div(children=[

    html.H1(myheading),
    #html.H2('Configuração Estrela')
    html.P('Disciplina: Exp. Circ. Elétricos II'),
    html.P('Docente: Prof. Dr. Wellington Maycon Santos Bernardes'),
    html.P('Discentes: Iohana A. Torres Cabral e Wallison Junio'),

    html.Div([
        dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
        )
    ])
])

#------------------------------------------------------------------



if __name__ == '__main__':
 app.run_server(debug=True)