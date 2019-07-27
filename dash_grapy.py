
import os
import copy
import time


import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379')
}

df = pd.read_csv("E:\\Brajendra\\Big Data\\DataSets\\weather_report.csv",sep="\t",delimiter=";")

newdf = df[df.columns[0:8]]

df_2019 = newdf[(newdf['Year'] > '2018') & (newdf['Year'] <= '2019')]
df_2018 = newdf[(newdf['Year'] > '2017') & (newdf['Year'] <= '2018')]
'''df_2017 = newdf[(newdf['date'] > '2017-01-01') & (newdf['date'] < '2018-01-01')]
df_2016 = newdf[(newdf['date'] > '2016-01-01') & (newdf['date'] < '2017-01-01')]
df_2015 = newdf[(newdf['date'] > '2015-01-01') & (newdf['date'] < '2016-01-01')]
'''
  

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
         options=[
            {'label': '2019', 'value': '2019'},
            {'label': '2018', 'value': '2018'},
            {'label': '2017', 'value': '2017'},
			{'label': '2016', 'value': '2016'},
			{'label': '2015', 'value': '2015'}
        ],
        value='2019'
    ),
    html.Div([
        html.Div(dcc.Graph(id='graph-1')),
    ], className="row"),
    
    
    # hidden signal value
    html.Div(id='signal', style={'display': 'none'})
])


# perform expensive computations in this "global store"
# these computations are cached in a globally available
# redis memory store which is available across processes
# and for all time.

def global_store(value):
    # simulate expensive query
    print('Computing value with {}'.format(value))
#    time.sleep(5)
    df = df_2019
    if value=="2018":
        df = df_2018
    if value == "2019":
        df = df_2019
    '''if value == "2017":
        df = df_2017
    if value == "2016":
        df = df_2016
    if value == "2015":
        df = df_2015'''
    return df


def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_dataframe = global_store(value)
    #print(value)
    #print(filtered_dataframe)
    fig['data'][0]['x'] = filtered_dataframe['date']
    fig['data'][0]['y'] = filtered_dataframe['temperaturemax']
    fig['layout'] = {'title':'Basic non interactive','xaxis':{'title':'Date'},'yaxis':{'title':'Tempreture'}}
    return fig


@app.callback(Output('signal', 'children'), [Input('dropdown', 'value')])
def compute_value(value):
    # compute value and send a signal when done
    global_store(value)
    return value


@app.callback(Output('graph-1', 'figure'), [Input('signal', 'children')])
def update_graph_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return generate_figure(value, {
        'data': [{
            'type': 'bar'
            
        }]
    })



if __name__ == '__main__':
    app.run_server(debug=True)
