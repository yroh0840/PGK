import requests
import json

#小業態マスタ取得API
url = 'https://api.gnavi.co.jp/master/CategorySmallSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'

#パラメータの設定
params={}
params['keyid'] = keyid


#params["sort"] = "1" # 並び替え
#params["hit_per_page"] = "3" # response max value
#params["lunch"] = "1" # ランチ営業


#リクエスト結果
result_api = requests.get(url, params)
result_api = result_api.json()

print(result_api)


