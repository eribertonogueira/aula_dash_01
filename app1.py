import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = px.data.gapminder()

fig = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp', 
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    animation_frame='year',
    animation_group='country',
    size_max=120
)

fig1 = px.line(
    df[df['country'].isin(['Brazil', 'China', 'Argentina', 'Colombia'])],
    x='year',
    y='lifeExp',
    color='country'
)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Dashboard 1', style={'textAlign' : 'center'}),
            dcc.Graph(figure=fig),
        ], className=['container-chart']),
        html.Div([
            html.H1('Dashboard 2', style={'textAlign' : 'center'}),
            dcc.Graph(figure=fig1),
        ], className=['container-chart'])
    ], className=['container'])
])

if __name__ == '__main__':
    app.run(port=8050, debug=True)