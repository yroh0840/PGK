import requests
import googlemaps
import json

#レストラン検索APIのURL
Url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"
 
#パラメータの設定
params={}
params["keyid"] = "f8538f6f177eaaa41226f9fc9a805897" #取得したアクセスキー
params["latitude"] = "35.695861"
params["longitude"] = "139.775018"
params["range"] = "1"

#リクエスト結果
print(requests.get(Url, params).json())


'''
class map():
    def __init__(self, master=None):
        super().__init__(master)

    def 
'''
