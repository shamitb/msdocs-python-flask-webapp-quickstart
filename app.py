from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from flask import Flask, request

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)
user_principal = request.headers.get('X-Ms-Client-Principal-Name')

app.layout = html.Div([
    html.H1(children=user_principal, style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run_server(debug=True)
