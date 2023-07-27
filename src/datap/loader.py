import pandas as pd

class DataSchema:
    COUNTRY = "Country"
    TECH = "Technology"
    PRODS = "Product"
    SIZE = "NormCap (MWel)"
    IEA = "IEA zero-carbon estimated normalized capacity [nm3 H2/h]"
    NH3 = "Normalized Capacity (nm³ H₂/h)"
    H2 = "Normalized Capacity (kt H2/y)"
    CO2 = "Normalized Capacity (t CO2 captured/y)"
    ENDU = "End Use"


def load_data(path: str) -> pd.DataFrame:
    # load the data from an excel file
    data = pd.read_excel(
        path,
    )
    
    # process data underneath here
    Country_Industries = data[['Country','Refining','Ammonia','Methanol','Iron&Steel','Other Ind',
                                'Mobility','Power','Grid inj','CHP','Domestic heat','Biofuels',
                                'Synfuels','CH4 grid inj','CH4 mobility']].groupby('Country').count().idxmax(axis='columns')
    
    data['End Use'] = data['Country'].map(Country_Industries.to_dict())

    return data

# load_data("data/WWHydrogenPlants.xlsx")
