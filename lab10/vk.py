import time
import json
import requests
import webbrowser
import config
from pymongo import MongoClient

#323367571   261645081
client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db['vk_riend_list']


def get_user_info(user_id):
    res = requests.get(config.BASE_URL + f'users.get?user_ids={user_id}&fields=city,universities&v=5.52&access_token={config.config.data}')
    if res.status_code == 200:
        try:
            resp = res.json()
            if 'response' in resp:
                for i in range(len(resp['response'])):
                    people = []
                    dict0 = {}
                    res = resp['response'][i]
                    dict0.update(
                        {'user_id': res['id'],
                        'first_name':res['first_name'],
                        'last_name':res['last_name']}
                    )
                    if 'city' in res:
                        if res['city'] == 0:
                            dict0.update({'city':'-'})
                        else:
                            dict0.update({'city':res['city']['title']})
                    else:
                        dict0.update({'city':'-'})

                    if 'universities' in res:
                        if len(res['universities']) > 0:
                            dict0.update({'universities':res['universities'][0]['name']})
                        else:
                            dict0.update({'universities':'-'})
                    else:
                        dict0.update({'universities':'-'})

                    friends_id, friend_count = get_friends(f"{res['id']}")
                    dict0.update({'friends' : friends_id})
                    people.append(dict0)
                    new_collection.insert_many(people)
                return friends_id, friend_count
            else:
                print('\n', resp['error']['error_msg'])
        except Exception as e:
            print(e, '\n')

def get_friends(user_id):
    friends_id = []
    friend_count = 0
    res = requests.get(config.BASE_URL + f'friends.get?user_id={user_id}&v=5.52&access_token={config.config.data}')
    if res.status_code == 200:
        try:
            if 'response' in res.json():
                res = res.json()['response']
                friend_count = res['count']
                for friend in res['items']:
                    friends_id.append(friend)
            return friends_id, friend_count
        except Exception as e:
            print(e, '\n')

if config.config.is_loaded() is False:
    print('Произошла ошибка при авторизации')
else:
    try:
        user_id = str(input('Введите идентификатор анализируемого пользователя\n'))
        friends, friend_count = get_user_info(user_id)
        friends_id = ''
        for i in range(friend_count):
            friends_id += str(friends[i]) + ','
        if friend_count > 1000:
            n = friend_count // 1000
            ost = friend_count % 1000
            for i in range(1, n):
                miin = i*1000
                maax = miin + 999
                get_user_info(friends_id[miin:maax])
                time.sleep(2)
        else:
            get_user_info(friends_id)
    except Exception:
        pass
