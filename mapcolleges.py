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

# Read data as a string and convert to a Python object.
path = Path('schools.geojson')
contents = path.read_text(encoding='utf-8')
data = json.loads(contents)

# Examine in the dataset.
all_eq_dicts = data['features']
enrollments, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    for university in Big12_Unis:
        if eq_dict['properties']['NAME'] == university["instnm"]:
            eq_title = eq_dict['properties']['NAME']
            enrollment = float(university["Total  enrollment (DRVEF2020)"])
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]

            eq_titles.append(eq_title)
            enrollments.append(enrollment)
            lons.append(lon)
            lats.append(lat)

title = 'Big 12 Schools Graph'
fig = px.scatter_geo(lat=lats, lon=lons, size=enrollments, title=title,
        color=enrollments,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()