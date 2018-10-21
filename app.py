import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
import os
import flask


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Satify'
server = app.server
df = pd.read_csv('data.csv')

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://image.ibb.co/hDy7Y0/Screenshot-from-2018-10-20-18-55-47.png', height='100', width='120')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


app.layout = html.Div([

    # Header
    get_logo(),
    html.Br([]),
    html.H5('Select range for pixels'),
    dcc.RangeSlider(
        id='pixel-slider',
        min=min(df['Pixel_size']),
        max=max(df['Pixel_size']),
        step=0.5,
        value=[min(df['Pixel_size']),max(df['Pixel_size'])]
    ),
html.Div(id='pixel-val'),
    html.H5('Select range for frequency'),
    dcc.RangeSlider(
        id='freq-slider',
        min=min(df['Frequency']),
        max=max(df['Frequency']),
        step=0.5,
        value=[min(df['Frequency']), max(df['Frequency'])]

    ),
html.Div(id='freq-val'),
    html.H5('Select range for time'),
    dcc.RangeSlider(
        id='time-slider',
        min=min(df['Imaging_time']),
        max=max(df['Imaging_time']),
        step=0.5,
        value=[min(df['Imaging_time']), max(df['Imaging_time'])]

    ),
html.Div(id='time-val'),
    html.H5('Select range for length'),
    dcc.RangeSlider(
        id='length-slider',
        min=min(df['Length_of_image']),
        max=max(df['Length_of_image']),
        step=0.5,
        value=[min(df['Length_of_image']), max(df['Length_of_image'])]

    ),
html.Div(id='length-val'),
    dcc.Graph(id='output-table-main')
])



@app.callback(
    Output('pixel-val', 'children'),
    [Input('pixel-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)
@app.callback(
    Output('time-val', 'children'),
    [Input('time-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)
@app.callback(
    Output('freq-val', 'children'),
    [Input('freq-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)
@app.callback(
    Output('length-val', 'children'),
    [Input('length-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


@app.callback(Output('output-table-main', 'figure'),[Input('pixel-slider', 'value'),Input('freq-slider', 'value'),Input('time-slider', 'value'),Input('length-slider', 'value')])
def display_table(pixel, freq, time, length):
    df = pd.read_csv('data.csv')
    print(pixel[0])
    df_data = df[(df.Pixel_size >= pixel[0]) & (df.Pixel_size <= pixel[1]) & (df.Frequency >= freq[0]) & (df.Frequency <= freq[1]) & (df.Length_of_image >= length[0]) & (df.Length_of_image <= length[1]) & (df.Imaging_time >= time[0]) & (df.Imaging_time <= time[1])]
    print(df_data)
    table = ff.create_table(df_data)
    return table



if __name__ == '__main__':
    app.run_server(debug=True)
