import requests
import json

#レストラン検索APIのURL
url = 'https://api.gnavi.co.jp/PhotoSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'

#パラメータの設定
params={}
params['keyid'] = keyid
#params["latitude"] = "35.695861" # 緯度
#params["longitude"] = "139.775018" # 経度
params['shop_name'] = '吉野家'
#params["range"] = "1" # 範囲
#params["pref"] = "1" # 都道府県コード
#params["sort"] = "1" # 並び替え
#params["hit_per_page"] = "3" # response max value
#params["freeword"] = "" # フリーワード検索
#params["lunch"] = "1" # ランチ営業
#params["category_s"] = "RSFST08011"

#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json()
print(result_api['response']['0']['photo']['shop_name'])
print(result_api['response']['0']['photo']['image_url']['url_1024'])
print(result_api['response']['0']['photo']['image_url']['url_320'])
print(result_api['response']['0']['photo']['image_url']['url_250'])
print(result_api['response']['0']['photo']['image_url']['url_200'])


'''print(result_api['rest'][0]['name'])
print(result_api['rest'][0]['code']['category_name_l'])
print(result_api['rest'][0]['code']['category_name_s'])
'''

