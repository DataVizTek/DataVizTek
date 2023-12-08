import csv
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pyproj import Transformer


def main():
    iris_file = gpd.read_file('assets/iris.geojson')

    fiber_and_commune_data = []

    with open('fiber_and_commune.csv', 'r') as fiber_and_commune_file:
        reader = csv.reader(fiber_and_commune_file)
        for row in reader:
            fiber_and_commune_data.append(row)


    fiber_and_commune_data.pop(0)
    i = 0
    fiber_and_commune_length = len(fiber_and_commune_data)

    transformer = Transformer.from_crs("epsg:4326", "epsg:2975")

    fiber_and_commune_and_iris = []

    for row in fiber_and_commune_data:
        print(f'{i}/{fiber_and_commune_length}')
        i += 1

        try:
            point_to_check = Point(transformer.transform(row[2], row[1]))

            fiber_and_commune_and_iris.append(row + [iris_file[iris_file.contains(point_to_check)].iloc[0]['CODE_IRIS']])
        except:
            continue

    with open('fiber_and_commune_and_iris.csv', 'w') as fiber_and_commune_and_iris_file:
        writer = csv.writer(fiber_and_commune_and_iris_file)
        writer.writerows(fiber_and_commune_and_iris)

if __name__ == '__main__':
    main()