# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
	html.H1(children='Hello Dash'),

	html.Div(children='''
		Dash: A web application framework for Python.
		'''),

	dcc.Graph(
		id='example-graph',
		figure={
		'data':[
		{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'TOKYO'},
				{'x' : [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'KYOTO'},
				],
				'layout': {
				'title': 'Dash Data Visualization',
				'fontsize': '43px'
				}
		})])

if __name__ == '__main__':
	app.run_server(debug=True, host='0.0.0.0')
