from requests import get
from pandas import json_normalize
import json


def load_json(geoJsonPath):
    with open(geoJsonPath) as f:
        data = json.load(f)

    #print(data['features'][0]['geometry']['type'])
    count = 0;
    for feature in data["features"]:
        if feature['geometry']['type'] == "LineString":
            count+=1
            #print(feature["geometry"]["coordinates"])
        #print(data["type"])
    print(count)




def get_elevation(lat = None, long = None):
    '''
        script for returning elevation in m from lat, long
    '''

    # using
    if lat is None or long is None: return None

    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')


    # Request with a timeout for slow responses
    r = get(query, timeout = 20)

    results = json_normalize(r.json(), 'results')
    print(results)

    tableOfResults = json_normalize(r.json(), 'results')
    # Only get the json response in case of 200 or 201
    if r.status_code == 200 or r.status_code == 201:
        elevation = json_normalize(r.json(), 'results')  # ['elevation'].values[0] displays jsut elevation
    else:
        elevation = None
    return elevation


def get_elevation_OpenTopo(lat=None, long=None):
        '''
            script for returning elevation in m from lat, long
        '''

        # using
        if lat is None or long is None: return None

        query = ('https://api.opentopodata.org/v1/ned10m'
                         f'?locations={lat},{long}')
        # Request with a timeout for slow responses
        r = get(query, timeout=20)

        results = json_normalize(r.json(), 'results')
        print(results)

        tableOfResults = json_normalize(r.json(), 'results')
        # Only get the json response in case of 200 or 201
        if r.status_code == 200 or r.status_code == 201:
            elevation = json_normalize(r.json(), 'results')['elevation'].values[0]
        else:
            elevation = None
        return elevation


def get_elevations(elevationData):
    url = ('https://api.opentopodata.org/v1/ned10m')
    locations = {
        "locations":
            [
                {
                    "latitude": 10,
                    "longitude": 10
                },
                {
                    "latitude": 20,
                    "longitude": 20
                },
                {
                    "latitude": 41.161758,
                    "longitude": -8.583933
                }
            ]
    }




    #query = ('https://api.open-elevation.com/api/v1/lookup'\
             #'Accept: application/json'\


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # meters = get_elevation(42.36, -71.0589)['elevation'].values[0]
    # feet = meters * 3.28084
    # #print(meters)
    # #print("Shown in feet", feet)
    # print("\n")


    #load_json("boston_massachusetts.geojson")
    # meters = get_elevation_OpenTopo(42.36, -71.0589)
    # print("\n")
    # meters = get_elevation(40.7128, -74.0060)

    pt1 = get_elevation_OpenTopo(42.3575544, -71.0622114)
    pt2 = get_elevation_OpenTopo(42.3575291, -71.0622167)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
