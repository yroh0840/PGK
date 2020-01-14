import requests
import json
#import geocoder


class GurunabiResponder:
    def __init__(self):
        self.params_range = dict([['300m', '1'],['500m', '2'],['1000m', '3'],['2000m', '4'],['3000m', '5']])
        self.params_yen = dict([['500円', 500],['1000円', 1000],['1500円', 1500],['2000円', 2000], ['3000円', 3000]])
        self.params_genre = dict([['中華', '中華'],['和食', '和食'],['洋食', '洋食'],['ラーメン', 'ラーメン'], ['カレーライス', 'カレーライス'], ['その他の料理', 'その他の料理']])

    def is_gurunabi(self, py_key):
        try:
            if py_key in self.params_yen:
                return self.get_gurunabi(self.params_yen[py_key])
        except KeyError:
            print('そのような選択肢は、ありません！')

    def get_gurunabi(self, yen_value):
        url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
        keyid = 'f8538f6f177eaaa41226f9fc9a805897'
        hit_per_page = '10'
        pgk = ['34.7639591', '135.4932691']
        #geo = geocoder.ip('me')
        #lat, lon = str(geo.latlng[0]), str(geo.latlng[1])

        payload = { 'keyid': keyid,
                    'hit_per_page': hit_per_page,
                   }
                    #'category_s': genre_value 

        shop_data = requests.get(url, params = payload).json()
        shop_budget_dict = {}
        shop_data_hit = shop_data['hit_per_page']
        for i in range(shop_data_hit):
            shop_url = shop_data['rest'][i]['url']
            shop_name = shop_data['rest'][i]['name']
            shop_data_budget = shop_data['rest'][i]['budget']
            shop_budget_dict[str(i+1)] = (shop_name, shop_data_budget, shop_url)
            if len(shop_budget_dict) == shop_data_hit:
                result_list = []
                for shop_num in shop_budget_dict:
                    if shop_budget_dict[shop_num] <= yen_value:
                        result_list.append(shop_budget_dict[shop_num])
        return result_list

guru = GurunabiResponder()
print(guru.is_gurunabi('3000円'))