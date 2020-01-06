import requests
import json

#レストラン検索APIのURL
Url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'

#パラメータの設定
params={}
params['keyid'] = keyid
params["latitude"] = "35.695861" # 緯度
params["longitude"] = "139.775018" # 経度

params["range"] = "1" # 範囲
params["pref"] = "1" # 都道府県コード
params["sort"] = "1" # 並び替え
params["hit_per_page"] = "３" # response max value
params["freeword"] =  # フリーワード検索
praams["lunch"] = "1" # ランチ営業


#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json()

print(result_api)
