from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from ..datap.loader import DataSchema
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    columns_sankey = list(data.columns)

    return html.Div(className='six columns', children=[
            # html.H6("Technologies"),
            dcc.Dropdown(
                id=ids.FIRST_SDROP,
                options=[{"label": column, "value": column} for column in columns_sankey],
                value=columns_sankey,
                multi=False)], style={'width':'33%'})
            # "width": "auto",
            # "height": "auto",
            # "margin-left": "1px",
            # "margin-right": "1px",
            # "verticalAlign":"top",
            # "align-items":"center",
            # "justify-content":"center"
            # "display":"inline-block"
        #     }
        # )


# html.Div(className='six columns', children=[
#                 dcc.Dropdown(
#                     id='dropdown_dataset',
#                     options=[
#                         {'label': 'diabetes', 'value': 'diabetes'},
#                         {'label': 'Custom Data', 'value': 'custom'},
#                         {'label': 'Linear Curve', 'value': 'linear'},
#                     ],
#                     value='diabetes',
#                     clearable=False,
#                     searchable=False,
#                 )], style=dict(width='50%'))