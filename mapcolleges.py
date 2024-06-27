from pathlib import Path
import json

import plotly.express as px

#Load the JSON data
Big12_Unis = []
with open('univ.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for university in data:
        naia_info = university['NCAA']
        if naia_info["NAIA conference number football (IC2020)"] == 108:
            Big12_Unis.append(university)

geojson_file = Path('schools.geojson') 
contents = Path.read_text(encoding='utf-8')
data = json.loads(contents)

# Examine in the dataset.
all_eq_dicts = data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict['properties']['NAME'] in Big12_Unis:
        eq_title = eq_dict['properties']['NAME']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
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