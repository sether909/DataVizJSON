from pathlib import Path
import json

import plotly.express as px

geojson_file = Path('schools.geojson') 
json_file = Path('univ.json')
title_to_find = "Central High School"
contents = Path.read_text(encoding='utf-8')
data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['NAME']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['NAME']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Big 12 Schools Graph'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()