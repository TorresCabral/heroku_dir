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
    html.H2('Configuração Estrela')
    html.P('Disciplina: Exp. Circ. Elétricos II'),
    html.P('Docente: Prof. Dr. Wellington Maycon Santos Bernardes'),
    html.P('Discentes: Iohana A. Torres Cabral e Wallison Junio'),

    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 6,
            # page_action='none',
            # style_cell={
            # 'whiteSpace': 'normal'
            # },
            # fixed_rows={ 'headers': True, 'data': 0 },
            # virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'countriesAndTerritories'},
                    'width': '40%', 'textAlign': 'left'},
                {'if': {'column_id': 'deaths'},
                    'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'cases'},
                    'width': '30%', 'textAlign': 'left'},
            ],
        ),
    ],className='row'),

    html.Div([
        html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'deaths'},
                         {'label': 'Cases', 'value': 'cases'}
                ],
                value='deaths',
                multi=False,
                clearable=False
            ),
        ],className='six columns'),

        html.Div([
        dcc.Dropdown(id='piedropdown',
            options=[
                     {'label': 'Deaths', 'value': 'deaths'},
                     {'label': 'Cases', 'value': 'cases'}
            ],
            value='cases',
            multi=False,
            clearable=False
        ),
        ],className='six columns'),

    ],className='row'),

    html.Div([
        html.Div([
            dcc.Graph(id='linechart'),
        ],className='six columns'),

        html.Div([
            dcc.Graph(id='piechart'),
        ],className='six columns'),

    ],className='row'),




 html.A('Acesse UFU',href='http://www.ufu.br'),
 html.Br(),
 html.A('Acesse Moodle', href=moodle_address)])

#------------------------------------------------------------------
@app.callback(
    [Output('piechart', 'figure'),
     Output('linechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value')]
)
def update_data(chosen_rows,piedropval,linedropval):
    if len(chosen_rows)==0:
        df_filterd = dff[dff['countriesAndTerritories'].isin(['China','Iran','Spain','Italy'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='countriesAndTerritories',
            values=piedropval,
            hole=.3,
            labels={'countriesAndTerritories':'Countries'}
            )


    #extract list of chosen countries
    list_chosen_countries=df_filterd['countriesAndTerritories'].tolist()
    #filter original df according to chosen countries
    #because original df has all the complete dates
    df_line = df[df['countriesAndTerritories'].isin(list_chosen_countries)]

    line_chart = px.line(
            data_frame=df_line,
            x='dateRep',
            y=linedropval,
            color='countriesAndTerritories',
            labels={'countriesAndTerritories':'Countries', 'dateRep':'date'},
            )
    line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)

#------------------------------------------------------------------



if __name__ == '__main__':
 app.run_server(debug=True)