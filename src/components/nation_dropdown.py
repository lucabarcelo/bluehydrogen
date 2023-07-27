from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from src.datap.loader import DataSchema

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    # example of subsequent retireval
    cleaned = data[data[DataSchema.COUNTRY].notna()]    
    gall_nations: list[str] = cleaned[DataSchema.COUNTRY].tolist()
     
    # gtop_nations: list[str] = list(cleaned.groupby([DataSchema.COUNTRY])['IEA zero-carbon estimated normalized capacity [nm3 H2/h]'].sum().nlargest(20).keys())

    all_nations = sorted(set(gall_nations), key=str)
    # top_nations = sorted(set(gtop_nations), key=str)

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks")
    )
    def select_all_nations_button(_:int) -> list[str]:
        return all_nations


    return html.Div(
        children=[
            html.H6("Producing Nations"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                options=[{"label":country, "value":country} for country in all_nations],
                value=all_nations,
                multi=True,
            ),
            html.Button(
                className="dropdown-all-button",
                children=["Select All"],
                id=ids.SELECT_ALL_NATIONS_BUTTON,
                n_clicks=0
            )
        ], style={
            "width": "auto",
            "height": "auto",
            "margin-left": "5px",
            "margin-right": "5px",
            "verticalAlign":"center",
            "align-items":"center", 
            "justify-content":"center"
        }
    )