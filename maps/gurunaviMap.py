import requests
import json
#import geocoder
#g = geocoder.ip('me')
#lat, lon = str(g.latlng[0]), str(g.latlng[1])
pgk = ['34.7639591', '135.4932691']
range_param = [str(5)]
#レストラン検索APIのURL
url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'
hit_per_page = '100'
#パラメータの設定
params={}
params['keyid'] = keyid
params['hit_per_page'] = hit_per_page
#params["latitude"] = pgk[0] # 緯度
#params["longitude"] = pgk[1] # 経度
#params['range'] = range

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
for i in range(result_api['hit_per_page']):
    print(result_api['rest'][i]['budget'])
'''
ral = []
for i in range(int(hit_per_page) - 1):
    r = result_api['rest'][i]['name']
    ral.append(r)
dl = dict([key, value] for key, value in enumerate(ral) )
print(dl)
print('succes >> ',dl[8])
'''
'''
if result_api['rest'][0]['budget'] >= 1000:
    print(result_api['rest'][0]['name'] + '　とかいう店は、予算オーバーやわ！')
elif result_api['rest'][0]['budget'] <= 1000:
    print(result_api['rest'][0]['name'] + '　とかいう店は、お金足りましたよ！')
else:
    print(result_api['rest'][0]['name'] + '店決まらんて！')
'''
'''
print(result_api['rest'][0]['image_url']['shop_image1'])
print(result_api['rest'][0]['image_url']['shop_image2'])

print(result_api['rest'][0]['name'])
print(result_api['rest'][0]['code']['category_name_l'])
print(result_api['rest'][0]['code']['category_name_s'])
'''
