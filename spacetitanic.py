# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:25:06 2022

@author: Utente
"""

import pandas as pd
import plotly.express as px
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

options_x = ["FoodCourt", "Spa", "RoomService", "ShoppingMall", "VRDeck", "Age", "CabinNumber", "IDCode#1", "IDCode#2", "Spent"]
markers = ["HomePlanet", "Destination", "CryoSleep", "VIP", "Deck", "Side"]


app.layout = html.Div([
    html.H1('Space Titanic investigation crossexamination'),
    
    dcc.Graph(id="scatter-plot"),

    
    html.P("Choose X axis:"),
    dcc.Dropdown(id="x_axis",
                 options=options_x,
                 multi=False,
                 value="FoodCourt",
                 style = {"width": "40 %"}),
    html.Br(),
    
    html.P("Choose y axis:"),
    dcc.Dropdown(id="y_axis",
                 options=options_x,
                 multi=False,
                 value="Spa",
                 style = {"width": "40 %"}),
    html.Br(),
    
    html.P("Choose marker:"),
    dcc.Dropdown(id="marker",
                 options=markers,
                 multi=False,
                 value="VIP",
                 style = {"width": "40 %"}),
    html.Br(),
    
])


@app.callback(
     Output("scatter-plot", "figure"),
    [Input(component_id='x_axis', component_property='value'), 
     Input(component_id='y_axis', component_property='value'),
     Input(component_id='marker', component_property='value')])

def update_graph(x_option, y_option, marker):
        
    df = pd.read_csv("spacetitanic.csv")
    df = df.dropna()
        
    fig = px.scatter(
        df, x=x_option, y=y_option, 
        color="Transported",
        symbol=marker,
        hover_data=["1stName", "Surname"])
    fig.update_traces(marker_size=10)
    fig.update_layout(
    title={
        'text': 'Transported?, '+ marker+"?",
        'y':0.9,
        'x':1,
        'xanchor': 'right',
        'yanchor': 'top'})

    return fig

app.run_server(debug=True)
