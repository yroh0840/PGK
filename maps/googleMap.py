import requests
import googlemaps
import geocoder
import folium
import gps

key = "AIzaSyBgOUJo1ZUpZLy-9JnGx4hLGcw8cO71yEw" #取得したAPIキーをセット
gmaps = googlemaps.Client(key=key)
 
#住所をジオコーディングする
results = gmaps.reverse_geocode((34.7614, 135.5157))
 
#リクエスト結果
print(results)

