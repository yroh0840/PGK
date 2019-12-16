import widget as wt
import requests
import googlemaps

#Geocoding APIのURL
Url = "https://maps.googleapis.com/maps/api/geocode/json"

#パラメータの設定
params={}
params["key"] = "AIzaSyBgOUJo1ZUpZLy-9JnGx4hLGcw8cO71yEw" #取得したAPIキーをセット
params["address"] = "株式会社Yasui"
params["language"] = "ja"

#リクエスト結果
print(requests.get(Url, params).json())



'''
class map():
    def __init__(self, master=None):
        super().__init__(master)

    def 
'''
