import time
import json
import requests
import webbrowser
import config
from pymongo import MongoClient

#323367571
client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db['vk_riend_list']


def get_user_info(user_id):
    people = []
    dict0 = {}
    res = requests.get(config.BASE_URL + f'users.get?user_ids={user_id}&fields=city,universities&v=5.52&access_token={config.config.data}')
    if res.status_code == 200:
        try:
            res = res.json()
            if res['error'] is False:
                ['response'][0]
                print(res['id'])
                dict0.update(
                    {'user_id': res['id'],
                    'first_name':res['first_name'],
                    'last_name':res['last_name']}
                )
                if res['city'] is True:
                    dict0.update({'city':res['city']['title']})
                else:
                    dict0.update({'city':'-'})

                if res['universities'] is True and len(res['universities']) > 0:
                    dict0.update({'universities':res['universities'][0]['name']})
                else:
                    dict0.update({'universities':'-'})

                friends_id = get_friends(f"{res['id']}")
                dict0.update({'friends' : friends_id})
                people.append(dict0)
                new_collection.insert_many(people)
                return friends_id
            else:
                print('Ошибка доступа токена')
        except Exception as e:
            print(e, '\n')

def get_friends(user_id):
    friends_id = []
    res = requests.get(config.BASE_URL + f'friends.get?user_id={user_id}&v=5.52&access_token={config.config.data}')
    if res.status_code == 200:
        try:
            res = res.json()['response']
            friend_count = res['count']
            for friend in res['items']:
                friends_id.append(friend)
            return friends_id
        except Exception as e:
            print(e, '\n')

if config.config.is_loaded() is False:
    print('Произошла ошибка при авторизации')
else:
    user_id = str(input('Введите идентификатор анализируемого пользователя\n'))
    friends_id = get_user_info(user_id)
    print(friends_id)
    for i in range(len(friends_id)):
        get_user_info(friends_id[i])
        time.sleep(2)