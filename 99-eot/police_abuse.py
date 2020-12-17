from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
JupyterDash.infer_jupyter_proxy_config()

df = pd.read_csv('/Users/teacher/Desktop/NYPD_police_complaints.csv')

df_abuse = pd.read_csv('https://raw.githubusercontent.com/hunter-teacher-cert/fall-2020-ethics-work-acomeaux93/master/99-eot/Abuse_Of_Authority.csv')
df_discourtesy = pd.read_csv('https://raw.githubusercontent.com/hunter-teacher-cert/fall-2020-ethics-work-acomeaux93/master/99-eot/Discourtesy.csv')
df_force = pd.read_csv('https://raw.githubusercontent.com/hunter-teacher-cert/fall-2020-ethics-work-acomeaux93/master/99-eot/Force.csv')
df_language = pd.read_csv('https://raw.githubusercontent.com/hunter-teacher-cert/fall-2020-ethics-work-acomeaux93/master/99-eot/Offensive_Language.csv')

df_abuse.info()
print(df_abuse.head(10))

allegations = df['Allegation FADO Type'].unique()
years = df['Close Year'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

# Create server variable with Flask server object for use with gunicorn
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id='offense_category',
        options=[
            {'label': 'Force', 'value': 'F'},
            {'label': 'Discourtesy', 'value': 'D'},
            {'label': 'Abuse of Authority', 'value': 'A'},
            {'label': 'Offensive Language', 'value': 'O'}

        ],
        value='F'

#         options=[{'label': i, 'value': i} for i in allegations],
#         value='FADO allegation type'
    ),

html.Div([
    dcc.Graph(
        id='police_graph'
    )
])
])

 # Callback for Updating the figure
@app.callback(
    dash.dependencies.Output('police_graph', 'figure'),
    [dash.dependencies.Input('offense_category', 'value')])

def update_graph(value):

    category = df

    if(value == 'F'):
        category = df_force
    elif(value == 'D'):
        category = df_discourtesy
    elif(value == 'A'):
        category = df_abuse
    else:
        category = df_language

    return {
        'data': [
                {'x': category['Year'], 'y': category['Total'], 'type': 'bar', 'name': 'Total Complaints'},
                {'x': category['Year'], 'y': category['True Video'], 'type': 'bar', 'name': 'Complaints With Video'},
            ],
            'layout': {
                'barmode': 'overlay',
                'title': 'NYPD Yearly Complaint Totals by Offense Category'
            }
    }

  app.run_server()

  app.run_server(mode="inline")
