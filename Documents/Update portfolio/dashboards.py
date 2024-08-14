import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

options_x = ["FoodCourt", "Spa", "RoomService", "ShoppingMall", "VRDeck", "Age", "CabinNumber", "IDCode#1", "IDCode#2", "Spent"]
markers = ["HomePlanet", "Destination", "CryoSleep", "VIP", "Deck", "Side", "Transported"]

app.layout = html.Div([
    html.Div([
        html.H2('Space Titanic Investigation Crossexamination'),
        dcc.Graph(id="scatter-plot")],
        style={"width": "70%", 'padding': 10, 'flex': 1}),

    html.Div([
        html.H1(),
        html.P("Choose X axis:"),
        dcc.Dropdown(id="x_axis",
                     options=[{'label': opt, 'value': opt} for opt in options_x],
                     multi=False,
                     value="FoodCourt",
                     style={"width": "100%"}),
        html.Br(),
                       
        html.P("Choose Y axis:"),
        dcc.Dropdown(id="y_axis",
                     options=[{'label': opt, 'value': opt} for opt in options_x],
                     multi=False,
                     value="Spa",
                     style={"width": "100%"}),
        html.Br(),
                       
        html.P("Choose color:"),
        dcc.Dropdown(id="marker",
                     options=[{'label': marker, 'value': marker} for marker in markers],
                     multi=False,
                     value="Transported",
                     style={"width": "100%"}),
        html.Br()],
        style={"width": "30%", 'padding': 10, 'flex': 0.5, 'marginTop': 45})
], style={'backgroundColor': 'white', 'display': 'flex', 'flex-direction': 'row'})

@app.callback(
    Output("scatter-plot", "figure"),
    [Input(component_id='x_axis', component_property='value'), 
     Input(component_id='y_axis', component_property='value'),
     Input(component_id='marker', component_property='value')])

def update_graph(x_option, y_option, marker):
    df = pd.read_csv("https://raw.githubusercontent.com/Herrikez/Dashboards/main/spacetitanic.csv")
    df = df.dropna()
    
    fig = px.scatter(
        df, x=x_option, y=y_option, 
        color=marker,
        hover_data=["1stName", "Surname"])
    fig.update_traces(marker_size=10)
    fig.update_layout(legend_title_text= marker + "?")
    
    return fig

app.run_server(host="localhost", port=8888)