import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..datap.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    px.set_mapbox_access_token('pk.eyJ1IjoiY3VscDNyIiwiYSI6ImNsaDZrbmg5YzAzMnMzbWxwZm9mc2RreG4ifQ.D4kikmeAEAQJ6s0URBfLQQ')
    cleaned = data[data[DataSchema.IEA].notna()]

    fig = px.scatter_mapbox(cleaned, lat=cleaned['Lat'], lon=cleaned['Long'],
                    hover_name=DataSchema.COUNTRY, # column added to hover information
                    color=DataSchema.ENDU,
                    size=DataSchema.IEA, 
                    color_continuous_scale=px.colors.cyclical.IceFire,
                    zoom=1
    )
    
    return html.Div(dcc.Graph(figure=fig), id=ids.CHARTTWO)
