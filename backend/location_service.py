import pandas as pd
from .config import DEMO_LOCATIONS_PATH

def get_demo_locations(city=None):
    df=pd.read_csv(DEMO_LOCATIONS_PATH)
    if city and city!="All":
        df=df[df["city"].str.casefold()==city.casefold()]
    return df.to_dict("records")

def cities():
    return ["All"] + sorted(pd.read_csv(DEMO_LOCATIONS_PATH)["city"].dropna().unique().tolist())
