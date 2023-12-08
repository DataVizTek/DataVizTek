import csv
import pandas as pd

def main():
    fiber_data = []
    commune_data = []

    with open('fiber.csv', 'r') as fiber_file:
        reader = csv.reader(fiber_file)
        for row in reader:
            fiber_data.append(row)

    with open('commune.csv', 'r') as commune_file:
        reader = csv.reader(commune_file)
        for row in reader:
            commune_data.append(row)

    fiber_data.pop(0)
    commune_data.pop(0)

    fiber_and_commune_data = pd.join(fiber_data, commune_data, on_left='code_insee', on_right='COM')

    with open('fiber_and_commune.csv', 'w') as fiber_and_commune_file:
        writer = csv.writer(fiber_and_commune_file)
        writer.writerows(fiber_and_commune_data)

if __name__ == '__main__':
    main()
