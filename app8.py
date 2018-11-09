import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import pandas as pd 

df = pd.read_csv('iris.csv')
df = df.iloc[:, 1:].copy()

available_ind = df.columns[:-1]

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id = 'y_axis_plot',
        options = [{'label': i, 'value':i} for i in available_ind],
        value='sepal length (cm)',
        style= {'width': '50%', 'display': 'inline-block'}
        ),
    dcc.Dropdown(
        id = 'x_axis_plot',
        options = [{'label': i, 'value':i} for i in available_ind],
        value='sepal width (cm)',
        style= {'width': '50%', 'display': 'inline-block'}
        ),
    dcc.Graph(
        id='iris_chart',
        hoverData = {})

    ])

@app.callback(
    Output('iris_chart', 'figure'),
        [Input('y_axis_plot', 'value'),
        Input('x_axis_plot', 'value')])

def update_graph(y_column_name, x_column_name):
    traces = []

    for i in df['speces'].unique():
        df_by_speces = df[df['speces'] == i]
        traces.append(go.Scatter(
            x = df_by_speces[x_column_name],
            y = df_by_speces[y_column_name],
            text = df_by_speces['speces'],
            mode = 'markers',
            opacity = 0.7,
            marker={
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}},
                name = i)
            )
    return {
    'data': traces,
    'layout': [go.Layout(
        autosize= False,
        width= 50,
        height= 1500,
        xaxis={'title': '{}'.format(x_column_name)},
        yaxis={'title': '{}'.format(y_column_name)},
        )]}

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
