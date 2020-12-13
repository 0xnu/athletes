import dash
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv(r"data/athletes.csv", dtype={"fips": str})

# Remove space from row column
df['Range'] = df['Range'].str.strip()

# Selects
df1 = df[(df.Range=='1')&(df.Sex=='M')][['Year','Performances','Names']]
df2 = df[(df.Range=='1')&(df.Sex=='W')][['Year','Performances','Names']]

fig = go.Figure(data=[go.Scatter(x=df1['Year'], y=df1['Performances'])])
fig2 = go.Figure(data=[go.Scatter(x=df2['Year'], y=df1['Performances'])])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Mens Triple Jump from 1891 to 2020'),
    dcc.Graph(
        id='Perf',
        figure=fig
    ),
    html.Div(children=[
        html.H1(children='Females Triple Jump from 1891 to 2020'),
        dcc.Graph(
            id='Perf2',
            figure=fig2
        )
    ])
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
