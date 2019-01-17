import dash  
import dash_table 
import pandas as pd  

df =  pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv', index_col=0)

app = dash.Dash(__name__) 
app.layout = dash_table.DataTable(
    id = 'table',
    columns = [{"name": i, "id": i} for i in df.columns],
    data = df.to_dict("rows"),
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')