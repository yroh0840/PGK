import requests
import json
#大業態マスタ取得API
#l_url = 'https://api.gnavi.co.jp/master/CategoryLargeSearchAPI/v3/'
#小業態マスタ取得API
s_url = 'https://api.gnavi.co.jp/master/CategorySmallSearchAPI/v3/'
keyid = 'f8538f6f177eaaa41226f9fc9a805897'


params={}
params['keyid'] = keyid
params['lang'] = 'ja'

#params["sort"] = "1" # 並び替え
#params["hit_per_page"] = "3" # response max value
#params["lunch"] = "1" # ランチ営業


#リクエスト結果
#result_api_l = requests.get(l_url, params) #大業態
result_api_s = requests.get(s_url, params) #小業態

#result_api_l = result_api_l.json() # 大業態
result_api_s = result_api_s.json() # 小業態

#category_l_max_num = len(result_api_l['category_l'][0:])
category_s_max_num = len(result_api_s['category_s'][0:])

for i in range(category_s_max_num):
    r = result_api_s['category_s'][i]['category_s_name']
    c = result_api_s['category_s'][i]['category_s_code']
    d = {r:c}
    if 'ラーメン' in d or 'カレーライス' in d or 'その他の料理' in d:
        print(d)

'''
l = []
for i in range(category_l_max_num):
    result = result_api_l['category_l'][i]['category_l_name']
    l.append(result)
'''
'''
cl = ['ラーメン', '中華', '洋食', '和食', 'カレーライス', 'その他の料理']
for i in cl:
    print(i in l)
'''

'''
for i in range(category_max_num):
    print({keys_values: keys_values for keys_values in [result_api['category_s'][i]['category_s_name']]})
'''