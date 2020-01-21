import requests
import json
import geocoder

url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'
hit_per_page = '100'
pgk = ['34.7639591', '135.4932691']
geo = geocoder.ip('me')
lat, lon = str(geo.latlng[0]), str(geo.latlng[1])
payload = { 'keyid': keyid,
            'hit_per_page': hit_per_page,
            'category_s': 'RSFST08008',
            'latitude':  lat,
            'longitude': lon,
            'range': '5'                 }
            #'category_l': genre_value '


shop_data = requests.get(url, params = payload).json()
for i in range(30):
    print(type(shop_data['rest'][i]['budget']))