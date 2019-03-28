import json, csv
import pandas as pd

schools = []
with open('schools.json') as json_data:
    d = json.load(json_data)
    for i, s in enumerate(d['schools']):
    	s['lon'] = s['location'][0]
    	s['lat'] = s['location'][1]
    	s['fragment_ids'] = ''
        schools.append(s)

pd.DataFrame(schools).to_csv('schools.csv', index=False)
