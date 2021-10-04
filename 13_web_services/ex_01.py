"""Change either geojson.py or geoxml.py to print out the two-character country code
from the retrieved data. Add error checking so your program does not traceback if the
country code is not there. Once you have it working, search for “Atlantic Ocean” and
make sure it can handle locations that are not in any country."""
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API Key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/,aps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retreive ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    location = js['results'][0]['formatted_address']
    print(location)

    results = js['results'][0]
    address_components = results['address_components']
    country = 0
    for each_dict in address_components:
        types = each_dict['types']
        if types == ['country', 'political']:
            country = 1
            print('The two character country code is: ',
                  each_dict['short_name'])

    if country == 0:
        print('Location isn\'t in any country')