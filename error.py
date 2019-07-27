import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("E:\\Brajendra\\Big Data\\DataSets\\iClose_Error.csv",delimiter = ',')
#print(df[8050:8067])
data = df
data = data.fillna(0)
data['Year'] = pd.DatetimeIndex(data.TimeUtc).year

df_2015 = data[data.Year == 2015]
df_2016 = data[data.Year == 2016]
df_2017 = data[data.Year == 2017]
df_2018 = data[data.Year == 2018]
#print(len(df_2015))

col_names =  ['Id', 'Year', 'ErrorCount']
my_df  = pd.DataFrame(columns = col_names)


my_dic = {'Id':1, 'Year':2015, 'ErrorCount':len(df_2015)}
my_df.loc[len(my_df)] = my_dic 

my_dic = {'Id':2, 'Year':2016, 'ErrorCount':len(df_2016)}
my_df.loc[len(my_df)] = my_dic 

my_dic = {'Id':3, 'Year':2017, 'ErrorCount':len(df_2017)}
my_df.loc[len(my_df)] = my_dic 

my_dic = {'Id':4, 'Year':2018, 'ErrorCount':len(df_2018)}
my_df.loc[len(my_df)] = my_dic 



app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=my_df[my_df['Id'] == i]['Year'],
                    y=my_df[my_df['Id'] == i]['ErrorCount'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in my_df.Id.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)