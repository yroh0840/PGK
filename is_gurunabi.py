###############################    ぐるなびAPIから店データを取得するモジュール    ######################################

import requests
import json
import geocoder # 現在地を取得するモジュール

# グルナビからデータを取得するクラス
class GurunabiResponder:
    def __init__(self):
        self.params_range = dict([['300m', '1'],['500m', '2'],['1000m', '3'],['2000m', '4'],['3000m', '5']])
        self.params_yen = dict([['500円', 500],['1000円', 1000],['1500円', 1500],['2000円', 2000], ['3000円', 3000]])
        self.params_genre = dict([['ラーメン', 'RSFST08008'], ['カレーライス', 'RSFST16005'], ['その他の料理', 'RSFST90001']])
    # tkinterのwidgetからキーを取得
    def is_gurunabi(self, pr_key, py_key, pg_key):
        if pr_key in self.params_range and py_key in self.params_yen and pg_key in self.params_genre:
            prv = self.params_range[pr_key]
            pyv = self.params_yen[py_key]
            pgv = self.params_genre[pg_key]
        return self.get_gurunabi(prv, pyv, pgv)
        
    # KEYをもとにデータを取得
    def get_gurunabi(self, range_value, yen_value, genre_value):
        url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
        keyid = 'f8538f6f177eaaa41226f9fc9a805897'
        hit_per_page = '20'
        geo = geocoder.ip('me')
        lat, lon = str(geo.latlng[0]), str(geo.latlng[1])

        payload = { 'keyid': keyid,
                    'hit_per_page': hit_per_page,
                    'latitude':  lat,
                    'longitude': lon,
                    'range': range_value,
                    'category_s': genre_value }
                    #'category_l': genre_value 
        try:
            shop_data = requests.get(url, params = payload).json()
            shop_data_hit = shop_data['hit_per_page']
            shop_dict = {i+1 : (shop_data['rest'][i]['name'], shop_data['rest'][i]['budget'], shop_data['rest'][i]['url']) for i in range(shop_data_hit) if isinstance(shop_data['rest'][i]['budget'], int)}
            result_list = [shop_dict[shop_num] for shop_num in shop_dict if shop_dict[shop_num][1] <= yen_value]
            return result_list
        except:
            return
        '''

        for rl in result_list[0]:
            result_massage += (
                '\n'
                + '店の名前は'
                + rl[0]
                + 'の平均予算は'
                + rl[1]
                + 'URLは'
                + rl[2]
            )
        print((result_massage))
        '''