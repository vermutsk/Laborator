import os
import re
import json
import requests
import webbrowser


BASE_URL = 'https://api.vk.com/method/'
REDIRECT_URI = 'https://oauth.vk.com/blank.html'

#Добавить проверку на существование файла

class Config():

    def __init__(self):
        self.data = ''
        self.APP_ID = open('app_id.txt', 'r').read()
        #self.SECRET = ''
        #self.ACS_TO = ''
        #with open('app_id.txt', 'r') as app:
        #    list0 = []
        #    for line in app:
        #        str0 = line.rstrip('\n')
        #        list0.append(str0)
        #    self.APP_ID = list0[0]
        #    self.SECRET = list0[1]
        #    self.ACS_TOK = list0[2]

    def is_loaded(self):
    
        if os.path.isfile('id_token.txt') is True:
            self.data = open('id_token.txt', 'r').read()
        else:
            self.data= self.new_token()
            with open('id_token.txt', 'a') as doc:
                doc.write(self.data)
        #check = BASE_URL + f'secure.checkToken?access_token={self.ACS_TOK}&client_secret={self.SECRET}&v=5.21&client_id={self.APP_ID}&token={self.data}'
        #load = requests.get(check).json()
        #print(load)
        #if load['response']['success'] != 1:
        #    return False
        #else:
        #    return True
    
    def new_token(self):
        template = re.compile(r'^https://oauth.vk.com/blank.html#access_token=(\w+)&expires_in=(\d+)&user_id=(\d+)$')
        flag = True
        while flag:
            webbrowser.open(IMPLICIT_URL)
            token_url = input('Вставьте URL открывшейся страницы\n')
            if template.match(token_url):
                access_token, expires_in, user_id = re.findall(r'=\w+', token_url)
                access_token  = access_token[1:]
                return access_token
            else:
                print('неверный формат URL')
            

config = Config()
IMPLICIT_URL = f'https://oauth.vk.com/authorize?client_id={config.APP_ID}&display=page&redirect_uri={REDIRECT_URI}&scope=friends&response_type=token&v=5.124'
