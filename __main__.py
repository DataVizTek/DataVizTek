import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html, Output, Input
from dash_extensions.javascript import arrow_function
import csv

fiber_and_commune_data = []

with open('fiber_and_commune.csv', 'r') as fiber_and_commune_file:
    reader = csv.reader(fiber_and_commune_file)
    for row in reader:
        fiber_and_commune_data.append(row)

fiber_and_commune_data.pop(0)

fiber_and_commune = []

for row in fiber_and_commune_data:
    fiber_and_commune.append(dict(lat=row[2], lon=row[1]))


app = Dash()
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),
        dl.GeoJSON(data=dlx.dicts_to_geojson(fiber_and_commune), cluster=True)

    ], center=(-21.120096, 55.525324), zoom=10.25, style={
        'height': '100vh',
        'margin': "auto",
        }),
])

if __name__ == '__main__':
    app.run_server()