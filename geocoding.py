import json
import time

import googlemaps

gmaps = googlemaps.Client(key='Your API Key')

with open('./area.json') as f:
    areaData = json.load(f)

positionData = []

for city in areaData:
    for area in city['areaList']:
        address = city['cityName'] + area['areaName']
        geocode_result = gmaps.geocode(f'{address}, TW')
        positionObj = {
            'areaName': address, 
            'position': geocode_result[0]['geometry']['location']
        }
        positionData.append(positionObj)
        time.sleep(0.1)

with open("position.json", "a+") as f:  
    json.dump(positionData, f, ensure_ascii=False)
