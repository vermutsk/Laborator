import time
import json
import requests
import webbrowser
import config
from pymongo import MongoClient

#323367571
client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db['hata_list']
new_collection.create_index('_id')


def get_user_info(user_id):
    people = []
    dict0 = {}
    res = requests.get(config.BASE_URL + f'users.get?user_ids={user_id}&fields=city,universities&v=5.52&accesss_token={config.config.data}')
    if res.status_code == 200:
        try:
            res = res.json()
            print(res)
            dict0.update(
                {'user_id': res['response']['id'],
                'first_name':res['response']['first_name'],
                'last_name':res['response']['last_name'],
                'city':res['response']['city']['title'],
                'universities': res['response']['universities']['name']}
            )
            friends_id = get_friends(f"{res['response']['id']}", 1)
            dict0.update({'friends' : friends_id})
            people.append(dict0)
            new_collection.insert_many(people)
        except Exception as e:
            print('лох', 'ex is ', e)

def get_friends(user_id, max_depth, depth = 0):
    friends_id = []
    res = requests.get(config.BASE_URL + f'friends.get?user_id={user_id}&v=5.52&accesss_token={config.config.data}')
    if res.status_code == 200:
        try:
            friend_count = res.json()['response']['count']
            for friend in res.json()['response']['items']:
                friends_id.append(friend['id'])
            return friends_id
        except Exception as e:
            print(e)

if config.config.is_loaded() is False:
    print('Произошла ошибка при авторизации')
else:
    user_id = str(input('Введите идентификатор анализируемого пользователя\n'))
    get_user_info(user_id)