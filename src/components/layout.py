from dash import Dash, html, dcc
import pandas as pd
import dash_bootstrap_components as dbc


from . import chart, chartmap, nation_dropdown, tech_dropdown, first_sdrop, second_sdrop, third_sdrop

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:

    # sidebar with filters
    nsidebar = html.Div([
        dbc.Row(dbc.Col([html.Img(src='../../assets/cu_logo.png', width='20%', style={'display':'inline-block'}), html.H3("Analysis", className="hr-5", style={'margin-left':'15px', 'display':'inline-block'})])),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col([first_sdrop.render(app, data)], width=1),
            dbc.Col([second_sdrop.render(app, data)], width=1),
            dbc.Col([third_sdrop.render(app, data)], width=1)], 
            className="dropdown-container", align='center'),
        html.Br(),
        dbc.Row([
            dbc.Col(nation_dropdown.render(app, data)),
            dbc.Col(tech_dropdown.render(app, data))
        ], className="dropdown-container")
    ], style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "20rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
        "overflow":"scroll"
    }
    )

    # setup card for graph one
    graphoneCard = dbc.Card(dbc.CardBody([
        chart.render(app, data)
    ]), style={"margin-right":"50px","margin-top":"20px"})

    # setup card for graph two
    graphtwoCard = dbc.Card(dbc.CardBody([
        chartmap.render(app, data)
    ]), style={"margin-right":"50px","margin-top":"20px"})


    # bulk function to be sent as html.Div() with everything layed out
    bulk = html.Div([
        html.H1(app.title, className="hr", style={'text-align':'center','margin-top':'20px'}),
        html.H6("Developed by Luca Barcelo", style={'text-align':'center','font-size':'16px','margin-top':'7px'}),
        html.H6("Columbia Engineering - Earth & Environmental Engineering", style={'text-align':'center','font-size':'14px','margin-top':'3px'}),
        html.Hr(style={'width':'75%', 'margin-left':'350px'}),
        html.Br(),
        dbc.Row(children=[
            dbc.Col([nsidebar], width=3),
            dbc.Col([graphoneCard, graphtwoCard], width=9)
        ], align='center')
    ])

    return bulk



















# --------------------------------------------------------------------------
# dbc.Card(
#             dbc.CardBody([
#                 dbc.Row([
#                     dbc.Col([nsidebar], width=3),
#                     dbc.Col([chart.render(app, data)], width=9)
#                 ], align='center')
#             ])
#         )






    # bulk = html.Div(className="app-div", children=
    #     [
    #     html.H1(app.title, style={'text-align':'center','margin-top':'5px'}),
    #     # sidebar,
    #     html.Hr(style={'border-width':'thick'}),
    #     dropdowns,
    #     html.Hr(),
    #     graphone
    #     ]
    # )

    # bulk = html.Div(children = [
    #     dbc.Row(dbc.Col([html.H1(app.title, className="display-3", style={'text-align':'center','margin-top':'5px'}), html.Hr(), chart.render(app, data)])),
    #     dbc.Row(dbc.Col(nsidebar)),
    # ]
    # )

    # bulk = html.Div([
    #     html.Div([
    #         html.H1(app.title, className="display-3", style={'text-align':'center','margin-top':'5px'}),
    #         html.Hr(),
    #         chart.render(app, data)
    #     ], className="six columns"),
    #     nsidebar
    # ], className="row")




