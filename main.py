from dash import Dash
from dash_bootstrap_components.themes import *
import dash_bootstrap_components as dbc

from src.components.layout import create_layout
from src.datap.loader import load_data

DATA_PATH = "data/WWHydrogenPlants.xlsx"

def main() -> None:
    data = load_data(DATA_PATH)
    app = Dash(external_stylesheets=[MORPH])
    app.title = "Blue Hydrogen Quantifier"
    app.layout = create_layout(app, data)
    app.run(debug=True)

if __name__ == "__main__":
    main()