#Flight Paths in different colours

import pandas as pd
import geopandas as gpd
import folium as folium
from geopandas import GeoDataFrame
from shapely.geometry import Point, LineString

def style_red(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'red',
        'weight': 1.5,
        'dashArray': '5, 5'
    }
def style_blue(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'blue',
        'weight': 1.5,
        'dashArray': '5, 5'
    }

def highlight_function(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'green',
        'weight': 3,
        'dashArray': '5, 5'
    }

flights_df = pd.read_csv(r"C:\Users\Gareth.Ahern\Desktop\13.csv")
flights_df['Position_DateTime']= pd.to_datetime(flights_df['Position_DateTime'])
flights13 = gpd.GeoDataFrame(flights_df, geometry=gpd.points_from_xy(flights_df.Longitude, flights_df.Latitude))

#df = flights13.groupby(['Flight_ID'])['geometry'].apply(lambda x: LineString(x.tolist()))
df = flights13.groupby(['Flight_ID'])['geometry'].apply(lambda x: LineString(x.tolist()) if x.size > 1 else x.tolist())
df = df.to_frame()


m = folium.Map(
    location=[40, 10],
    zoom_start=4,
    control_scale=True,
    prefer_canvas=True
)

for Flight_ID, row in df.iterrows():
    c = folium.GeoJson(
        row['geometry'],
        overlay=True,
        style_function=style_red,
        highlight_function=highlight_function
    )
    folium.Popup('Flight ID : ' + str(Flight_ID)).add_to(c)
    c.add_to(m)

flights_df = pd.read_csv(r"C:\Users\Gareth.Ahern\Desktop\14.csv")
flights_df['Position_DateTime']= pd.to_datetime(flights_df['Position_DateTime'])
flights14 = gpd.GeoDataFrame(flights_df, geometry=gpd.points_from_xy(flights_df.Longitude, flights_df.Latitude))

#df = flights13.groupby(['Flight_ID'])['geometry'].apply(lambda x: LineString(x.tolist()))
df = flights14.groupby(['Flight_ID'])['geometry'].apply(lambda x: LineString(x.tolist()) if x.size > 1 else x.tolist())
df = df.to_frame()

c = folium.GeoJson(df)
c.add_to(m)
 
for Flight_ID,row in df.iterrows():
    c = folium.GeoJson(
        row['geometry'],
        overlay=True,
        style_function=style_blue,
        highlight_function=highlight_function
    )
    folium.Popup('Flight ID : ' + str(Flight_ID)).add_to(c)
    c.add_to(m)

m.save('/Users/Gareth.Ahern/Desktop/flights2.html')