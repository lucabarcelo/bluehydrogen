import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..datap.loader import DataSchema
from . import ids
from .sankey_generator import genSankey


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.CHARTONE, "children"),
        [Input(ids.NATION_DROPDOWN, "value"), Input(ids.TECH_DROPDOWN, "value"),
        Input(ids.FIRST_SDROP, "value"), Input(ids.SECOND_SDROP, "value"), Input(ids.THIRD_SDROP, "value")]
    )
    def update_sankey_chart(nations: list[str], techs: list[str], first: str, second: str, third: str) -> html.Div:
        filtered_data = data.query("Country in @nations and Technology in @techs")
        if filtered_data.shape[0] == 0:
            return html.Div("No data has been selected.")
        
        fig = genSankey(
            filtered_data,
            cat_cols=[first, second, third],
            value_cols=DataSchema.IEA,
            title='Production Technology Employed Correlated to Product & End Use'
            )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.CHARTONE)
    
    return html.Div(id=ids.CHARTONE)



    # fig = genSankey(
    #         filtered_data,
    #         cat_cols=[DataSchema.TECH, DataSchema.PRODS, DataSchema.ENDU],
    #         value_cols=DataSchema.IEA,
    #         title='Production Technology Employed Correlated to Product & End Use'
    #         )