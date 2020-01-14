import requests
import json
#import geocoder


class GurunabiResponder:
    def __init__(self):
        self.params_range = dict([['300m', '1'],['500m', '2'],['1000m', '3'],['2000m', '4'],['3000m', '5']])
        self.params_yen = dict([['500円', 500],['1000円', 1000],['1500円', 1500],['2000円', 2000], ['3000円', 3000]])
        self.params_genre = dict([['中華', '中華'],['和食', '和食'],['洋食', '洋食'],['ラーメン', 'ラーメン'], ['カレーライス', 'カレーライス'], ['その他の料理', 'その他の料理']])

    def is_gurunabi(self, pr_key, py_key, pg_key):
        if pr_key in self.params_range and py_key in self.params_yen and pg_key in self.params_genre:
            return self.get_gurunabi(self.params_range[pr_key], self.params_yen[py_key], self.params_genre[pg_key])
        
        else:
            print('error')

    def get_gurunabi(self, range_value, yen_value, genre_value):
        url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
        keyid = 'f8538f6f177eaaa41226f9fc9a805897'
        hit_per_page = '10'
        pgk = ['34.7639591', '135.4932691']
        #geo = geocoder.ip('me')
        #lat, lon = str(geo.latlng[0]), str(geo.latlng[1])

        payload = { 'keyid': keyid,
                    'hit_per_page': hit_per_page,
                    'latitude':  pgk[0],
                    'longitude': pgk[1],
                    'range': range_value,
                    'category_l': genre_value }
                    #'category_s': genre_value 

        shop_data = requests.get(url, params = payload).json()
        shop_budget_dict = {}
        shop_data_hit = shop_data['hit_per_page']
        for i in range(shop_data_hit - 1):
            shop_url = shop_data['rest'][i]['url']
            shop_name = shop_data['rest'][i]['name']
            shop_data_budget = shop_data['rest'][i]['budget']
            shop_budget_dict[shop_name] = shop_data_budget, shop_url
            if len(shop_budget_dict) >= shop_data_hit:
                for sbl in shop_budget_dict:
                    if shop_budget_dict[sbl][0] >= self.params_yen[yen_value]:
                        del shop_budget_dict[sbl]
        return shop_budget_dict.keys()
guru = GurunabiResponder()
print(guru.is_gurunabi('3000m', '3000円', '和食'))

'''
        forecast = '天気予報だよ～\n'
        for weather in weather_data['forecasts']:
            # 応答文字列を作成
            forecast += (
                '\n'                    # 改行
                + weather['dateLabel']  # 予報日を取得
                + 'の天気は'            # つなぎの文字列
                + weather['telop']      # 天気情報を取得
            )
        return forecast
'''