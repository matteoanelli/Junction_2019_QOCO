import base64
import datetime
import io
import plotly.graph_objs as go
import cufflinks as cf
import json
import requests
import pdb

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from pandas.io.json import json_normalize
import pandas as pd

api_key = 'jmdSHjy6WPaXwoR75E6mJ1ImhxKPRJb51v6DBS0A'
api_url = 'https://junction.dev.qoco.fi/api/'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
missingBags = []
damagedBags = []
airports = {}
airportMissing = {}
airportDamage = {}
df_airports = pd.read_csv('airport.csv')

bag_events = []

r = requests.get(api_url + 'baggage', headers={'x-api-key': api_key})
# data = r.json()

for bag in r.json()['baggage']:
    events = []
    for bagevent in requests.get(api_url + 'events/' + bag['baggageId'], headers={'x-api-key': api_key}).json()[
        'events']:
        events.append(bagevent)
        airports[bagevent['airport']] = bagevent['airport']
        if bagevent['type'] == 'MISSING':
            missingBags.append(bagevent)
            if bagevent['airport'] in airportMissing.keys():
                airportMissing[bagevent['airport']] = airportMissing[bagevent['airport']] + 1
            else:
                airportMissing[bagevent['airport']] = 1
        if bagevent['type'] == 'DAMAGED':
            damagedBags.append(bagevent)
            if bagevent['airport'] in airportDamage.keys():
                airportDamage[bagevent['airport']] = airportDamage[bagevent['airport']] + 1
            else:
                airportDamage[bagevent['airport']] = 1
    bag_events.append(events)

fig = go.Figure()
fig.add_trace(go.Scattergeo(
    locationmode = 'ISO-3',
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(
        size = 15,
        color = 'rgb(0, 255, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))
lat = []
long = []
for i in range(0,35):
    for paths in bag_events[i]:
        ap = df_airports.loc[df_airports['airport'] == paths['airport']]
        lat.append(float(ap['lat']))
        long.append(float(ap['long']))
        if paths['type'] == 'DAMAGED':
            fig.add_trace(go.Scattergeo(
                locationmode='ISO-3',
                lon=list(ap['long']),
                lat=list(ap['lat']),
                hoverinfo='text',
                text=paths['airport'],
                mode='markers',
                marker=dict(
                    size=15,
                    color='rgb(255, 255, 0)',
                    line=dict(
                        width=3,
                        color='rgba(68, 68, 68, 0)'
                    )
                )))
        if paths['type'] == 'MISSING':
            fig.add_trace(go.Scattergeo(
                locationmode='ISO-3',
                lon=list(ap['long']),
                lat=list(ap['lat']),
                hoverinfo='text',
                text=paths['airport'],
                mode='markers',
                marker=dict(
                    size=20,
                    color='rgb(255, 0, 0)',
                    line=dict(
                        width=3,
                        color='rgba(68, 68, 68, 0)'
                    )
                )))
fig.add_trace(
    go.Scattergeo(
        locationmode = 'ISO-3',
        lon = long,
        lat = lat,
        mode = 'lines',
        line = dict(width = 1,color = 'black'),
        #opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
    )
)

fig.update_layout(
    title_text = 'Recorded flights',
    showlegend = False,
    autosize=False,
    width=1800,
    height=1000,
    geo = go.layout.Geo(
        scope = 'world',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)
colors = {
    "graphBackground": "#F5F5F5",
    "background": "#ffffff",
    "text": "#000000"
}

app.layout = html.Div([
    #dcc.Graph(figure=go.Figure([go.Bar(x=['PVG', 'DXB', 'LAX', 'ATL'], y=[3, 1, 2, 1])]),id='damagedGraph'),
    dcc.Graph(figure=fig),
    # dcc.Graph(figure=go.Figure([go.Bar(x=['CDG', 'ORD', 'LHR', 'ATL', 'PEK', 'LAX', 'PVG', 'HND'], y=[1, 2, 2, 2, 1, 1, 1, 1])]),id='missingGraph'),
    html.Div(id='output-data-upload')
])




if __name__ == '__main__':
    # print(list(airportDamage.keys()))
    # print(list(airportMissing.values()))
    # print(list(airportMissing.keys()))
    app.run_server(debug=True)
