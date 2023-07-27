from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

from src.datap.loader import DataSchema
from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_techs: list[str] = data[DataSchema.TECH].dropna().tolist()
    uniq_techs = sorted(set(all_techs), key=str)

    @app.callback(
        Output(ids.TECH_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_TECHS_BUTTON, "n_clicks")
    )

    def select_all_techs(_:int) -> list[str]:
        return uniq_techs

    return html.Div(
        children=[
            html.H6("Technologies"),
            dcc.Dropdown(
                id=ids.TECH_DROPDOWN,
                options=[{"label": tech, "value": tech} for tech in uniq_techs],
                value=uniq_techs,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_TECHS_BUTTON,
                n_clicks=0,
            )
        ], style={
            "width": "auto",
            "height": "auto",
            "margin-left": "5px",
            "margin-right": "5px",
            "verticalAlign":"top",
            "align-items":"center", 
            "justify-content":"center"
        }
    )


