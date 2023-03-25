from bokeh.plotting import figure, show
from bokeh.models import WMTSTileSource
from bokeh.models import HoverTool
import pandas as pd
import numpy as np

def web_mercator(df, lon="lon", lat="lat"):
    #convert decimal lon&lat mercator format
    
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90+ df[lat]) * np.pi/360)) *k
    return df

#data
data = dict(
    name = ["sanpada", "mumbai", "herndon", "nainital", "kanpur"],
    lat = [19.0608, 19.0760, 38.9696, 29.3919, 26.4499],
    lon = [73.0261, 72.8777, 38.9696,79.4542, 80.3319]
)

df = pd.DataFrame(data)
map_df = web_mercator(df)
print(map_df.head())


#USA = x_range, y_range = ((-13884029, -7453304), (2698291, 6455972 ))
p = figure(tools="wheel_zoom, pan ", x_range=(-2000000,12000000), y_range=(-1000000,7000000), 
           x_axis_type="mercator", y_axis_type="mercator")

url = "http://a.basemaps.cartocdn.com/rastertiles/voyager/{Z}/{X}/{Y}.png"

p.add_tile(WMTSTileSource(url=url, ))
p.circle(x=df['x'], y=df['y'], 
         fill_color="grey",size=15)

show(p)