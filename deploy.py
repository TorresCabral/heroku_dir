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

# Calculo
angA = 0
angB = 120
angC = -120
Van = carga*exp(1j*deg2rad(angA))
Za = 15 + 0j
iA = Van/Za
Vbn = carga*exp(1j*deg2rad(angB))
Zb = 10 + 5j
iB = Vbn/Zb
Vcn = carga*exp(1j*deg2rad(angC))
Zc = 6 - 8j
iC = Vbn/Zb
iN = iA + iB + iC

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
            placeholder='Carga',
            type='text',
            id='carga'
        ),
        dcc.Textarea(
            placeholder='Ia = ' + iA,
            value='Ia = ' + iA,
            style={'width': '100%'}
        ), 
        dcc.Textarea(
            placeholder='Ib = ' + iB,
            value='Ib = ' + iB,
            style={'width': '100%'}
        ), 
        dcc.Textarea(
            placeholder='Ic = ' + iC,
            value='Ic = ' + iC,
            style={'width': '100%'}
        ),
        dcc.Textarea(
            placeholder='In = ' + iN,
            value='In = ' + iN,
            style={'width': '100%'}
        )  
    ])
])


@app.callback(
    Output("number-out", "children"),
    Input("carga", "value"),
)
def number_render(iA, iB, iC):
    return "Ia: {}, Ib: {}, Ic: {}, In: {}".format(iA, iB, iC, iN)

#------------------------------------------------------------------



if __name__ == '__main__':
 app.run_server(debug=True)