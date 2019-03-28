import json, csv
import pandas as pd

properties = []
with open('listings.json') as json_data:
    d = json.load(json_data)
    for i, p in enumerate(d['map']['properties']):
        properties.append(p[8][11])

pd.DataFrame(properties).to_csv('properties.csv', index=False)
