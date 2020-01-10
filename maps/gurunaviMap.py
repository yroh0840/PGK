import requests
import json
import geocoder
g = geocoder.ip('me')
lat, lon = str(g.latlng[0]), str(g.latlng[1])
pgk = ['34.7639591', '135.4932691']
range = [str(5)]
#レストラン検索APIのURL
url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'

#パラメータの設定
params={}
params['keyid'] = keyid
params['hit_per_page'] = '10'
params["latitude"] = pgk[0] # 緯度
params["longitude"] = pgk[1] # 経度
params['range'] = range

#params["range"] = "1" # 範囲
#params["pref"] = "1" # 都道府県コード
#params["sort"] = "1" # 並び替え
#params["hit_per_page"] = "3" # response max value
#params["freeword"] = "" # フリーワード検索
#params["lunch"] = "1" # ランチ営業
#params["category_s"] = "RSFST08011"
#params['name'] = '吉野家なんばCITY南館店'

#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json()
print(result_api['rest'][0]['name'])
'''
print(result_api['rest'][0]['image_url']['shop_image1'])
print(result_api['rest'][0]['image_url']['shop_image2'])
'''
'''print(result_api['rest'][0]['name'])
print(result_api['rest'][0]['code']['category_name_l'])
print(result_api['rest'][0]['code']['category_name_s'])
'''

