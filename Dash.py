import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import requests
import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------


df = pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deceased'] - df['Other']
df['Date'] = pd.to_datetime(df['Date'])

r = requests.get(url='https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson')
geojson = r.json()
st = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')

st_map = st.copy()

st_map['State'] = st_map['State'].apply(lambda x: x.replace('Odisha', 'Orissa') if 'Odisha' in str(x) else x)
st_map['State'] = st_map['State'].apply(
    lambda x: x.replace('Uttarakhand', 'Uttaranchal') if 'Uttarakhand' in str(x) else x)
st_map['State'] = st_map['State'].apply(
    lambda x: x.replace('Andaman and Nicobar Islands', 'Andaman and Nicobar') if 'Andaman and Nicobar Islands' in str(
        x) else x)

st_map = st_map.iloc[:, :5]

st_map.drop([0, 31], inplace=True)

st_map.reset_index(drop=True, inplace=True)

States = []
for i in np.sort(df['State'].unique()):
    States.append({'label': i, 'value': i})

color = {'Confirmed': px.colors.sequential.Reds,
         'Active': px.colors.sequential.Blues,
         'Recovered': px.colors.sequential.Greens,
         'Deaths': px.colors.sequential.Greys}

# ------------------------------------------------------------------------------


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1(children='COVID-19 India Dashboard',
            style={'textAlign': 'center', 'color': '#0062ff'}),

    html.Div([

        dcc.Graph(id='indicator'),

        html.Label(['States & Union Territories:'], style={ "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown', options=States, optionHeight=35, value='India',
                     disabled=False, multi=False, searchable=True, search_value='India',
                     placeholder='Select a State or Union Territory', clearable=False, style={'width': "50%"}),

        dcc.Graph(id='donut'),

        dcc.Graph(id='our_graph'),

        dcc.Graph(id='our_graph2')
    ]),

    html.Div([
        html.Label(['Status:'], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.RadioItems(
            id='candidate',
            options=[{'value': x, 'label': x} for x in st_map.columns[1:]],
            value='Confirmed',
            labelStyle={'display': 'inline-block'}),

        dcc.Graph(id='choro'),

    ]),

])


# ------------------------------------------------------------------------------


@app.callback(
    Output(component_id='indicator', component_property='figure'),
    Output(component_id='donut', component_property='figure'),
    Output(component_id='our_graph', component_property='figure'),
    Output(component_id='our_graph2', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def build_graph(column_chosen):
    df1 = df[df['State'] == column_chosen]
    df1['Daily Confirmed'] = df1['Confirmed'].diff()
    df1['Daily Active'] = df1['Active'].diff()
    df1['Daily Recovered'] = df1['Recovered'].diff()
    df1['Daily Deceased'] = df1['Deceased'].diff()
    df1['Daily Tested'] = df1['Tested'].diff()
    df1['Positivity'] = (df1['Daily Confirmed'] / df1['Daily Tested']) * 100

    dfm = df[df['State'] == column_chosen]

    data1 = [go.Indicator(mode="number+delta", value=dfm.iloc[-1, 2],
                          delta={'position': "bottom", 'reference': (dfm.iloc[-2, 2])},
                          title={"text": 'Confirmed'},
                          domain={'x': [0, 0.25], 'y': [0, 1]}),

             go.Indicator(mode="number+delta", value=dfm.iloc[-1, 3],
                          delta={'position': "bottom", 'reference': (dfm.iloc[-2, 3])},
                          title={"text": 'Recovered'},
                          domain={'x': [0.25, 0.5], 'y': [0, 1]}),

             go.Indicator(mode="number+delta", value=dfm.iloc[-1, 4],
                          delta={'position': "bottom", 'reference': (dfm.iloc[-2, 4])},
                          title={"text": 'Deceased'},
                          domain={'x': [0.5, 0.75], 'y': [0, 1]}),

             go.Indicator(mode="number+delta", value=dfm.iloc[-1, 7],
                          delta={'position': "bottom", 'reference': (dfm.iloc[-2, 7])},
                          title={"text": 'Active'},
                          domain={'x': [0.75, 1], 'y': [0, 1]})]

    fig1 = go.Figure(data=data1)
    fig1.update_layout(paper_bgcolor="lightgray", height=250, width=1320)

    labels = ['Active', 'Recovered', 'Deceased']

    recovered = dfm.iloc[-1, 3]
    deceased = dfm.iloc[-1, 4]
    active = dfm.iloc[-1, 7]

    values = [active, recovered, deceased]

    colors = ['#66b3ff', '#02bf47', '#db1200']

    fig_d = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {"type": "xy"}]],
                          subplot_titles=("Current Status", "Test Positivity Ratio"))

    fig_d.add_trace(go.Pie(labels=labels, values=values, name="GHG Emissions", hole=.4, hoverinfo="label+percent",
                           marker=dict(colors=colors, line=dict(color='#ffffff', width=2))), row=1, col=1)

    fig_d.add_trace(
        go.Scatter(name="Postivity Ratio", x=df1['Date'], y=df1['Positivity'], mode='lines', marker_color='#ff4714', ),
        row=1, col=2)

    fig_d.update_layout(showlegend=False,
                        title="Current Status in {}".format(column_chosen),
                        title_x=0.2,
                        annotations=[dict(text=column_chosen, x=0.225, y=0.46, font_size=16, showarrow=False),
                                     dict(text='Test Positivity Ratio of {}'.format(column_chosen), x=0.75, y=1,
                                          font_size=17, showarrow=False)])

    data2 = [go.Scatter(name="Confirmed", x=df1['Date'], y=df1['Confirmed'], marker_color='Red'),
             go.Scatter(name="Active", x=df1['Date'], y=df1['Active'], marker_color='Blue'),
             go.Scatter(name='Recovered', x=df1['Date'], y=df1['Recovered'], marker_color='Green'),
             go.Scatter(name='Deceased', x=df1['Date'], y=df1['Deceased'], marker_color='Grey')]

    layout2 = go.Layout(
        title='Cumulative Graph of {}'.format(column_chosen),
        title_x=0.5,
        yaxis={'title': 'No of cases'},
        xaxis={'title': 'Date'},
        font=dict(size=14))
    fig2 = go.Figure(data=data2, layout=layout2)

    data3 = [go.Bar(name="Confirmed", x=df1['Date'], y=df1['Daily Confirmed'], marker_color='Red'),
             go.Bar(name="Active", x=df1['Date'], y=df1['Daily Active'], marker_color='Blue'),
             go.Bar(name="Recovered", x=df1['Date'], y=df1['Daily Recovered'], marker_color='Green'),
             go.Bar(name="Deceased", x=df1['Date'], y=df1['Daily Deceased'], marker_color='Grey')]

    layout3 = go.Layout(
        plot_bgcolor='#000000',
        template='plotly',
        title='Daily Graph of {}'.format(column_chosen),
        title_x=0.5,
        yaxis={'title': 'No of cases'},
        xaxis={'title': 'Date'},
        font=dict(size=14))
    fig3 = go.Figure(data=data3, layout=layout3)

    return fig1, fig_d, fig2, fig3


# ------------------------------------------------------------------------------


@app.callback(
    Output('choro', "figure"),
    [Input('candidate', "value")])
def display_choropleth(status):
    fig1 = px.choropleth(st_map, geojson=geojson, color=status,
                         locations="State", featureidkey="properties.NAME_1",
                         hover_name='State',
                         hover_data=['Confirmed', 'Recovered', 'Deaths', 'Active'],
                         color_continuous_scale=color[status],
                         title='India: Total {} cases per state'.format(status)
                         )
    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_geos(projection_type="orthographic")
    fig1.update_layout(height=600, margin={"r": 0, "t": 30, "l": 0, "b": 30})

    return fig1


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
