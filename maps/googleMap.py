import requests
import googlemaps
import geocoder
import folium

key = "AIzaSyBgOUJo1ZUpZLy-9JnGx4hLGcw8cO71yEw" #取得したAPIキーをセット
gmaps = googlemaps.Client(key=key)
 
#住所をジオコーディングする
results = gmaps.geocode((36.5748441, 139.2394179))
 
#リクエスト結果
print(results)

