import geopandas
import datawrappergraphics as dw

raw = geopandas.read_file('https://geo.weather.gc.ca/geomet?service=wfs&version=2.0.0&request=GetFeature&typeNames=ALERTS&outputFormat=GeoJSON', driver='geojson')

data = raw[raw['alert_type']=='warning']



data["fill-opacity"] = 0.5
data["stroke"] = "#c42127"
data["outline-opacity"] = 0.5

(dw.Map("dt6ev")
 .data(data, append="./assets/shapes/shapes-heatwarnings.json")
 .footer(source="Environment Canada", timestamp=True, byline=False)
 .publish()
 )
