import random
import os
import BASE
import math
import json

globkey = b'V%\xb84\x95\x88m\xa2\x9a\x1e\xb7F|\xd6\x990'


# def filer(way):
#     with open(way, "r") as f:
#         varbls = {line[0]: line[3:] for line in f}
#     return varbls


def LogIn():
    way = 'logpas.txt'
    if os.path.isfile(way):
        with open(way, 'r') as file:
            UsersInformation = json.load(file)
            # UserInformation = file.read()
    else:
        UsersInformation = {}
    f = True
    while f == True:
        print('Login:')
        login = input('>>')
        if login in UsersInformation.keys():
            print('Тhis login is busy')
            return 0
        f = False
    print('Password:')
    password = input('>>')
    password_base, rav = BASE.Text_to_ASCII_64(password)
    H = BASE.encrypted_BASE64(password_base, rav)
    UsersInformation.update({login: H})
    with open(way, 'w') as file:
        json.dump(UsersInformation, file)


def SignIn():
    way = 'logpas.txt'
    if os.path.isfile(way):
        with open(way, 'r') as file:
            UsersInformation = json.load(file)
    else:
        UsersInformation = {}
        print('No accounts')
        return 0
    while True:
        print('Login:')
        login = input('>>')
        if login in UsersInformation.keys():
            print('Password:')
            password = input('>>')
            password_base, rav = BASE.Text_to_ASCII_64(password)
            H = BASE.encrypted_BASE64(password_base, rav)
            if H != UsersInformation[login]:
                print('Logins do not match')
                return 0, 0
            else:
                print('Logged in')
                return login, H
        else:
            print('Аccount does not exist')
            return 0, 0


def check_password(login, password_b):
    way = 'logpas.txt'
    if os.path.isfile(way):
        with open(way, 'r') as file:
            UsersInformation = json.load(file)
    else:
        print('No accounts')
        return False
    if login in UsersInformation.keys() and UsersInformation[login] == password_b:
        return True
    else:
        return False


def choose():
    while True:
        print('\nВыберите действие:')
        print('1.Log In\n2.Sign In\n3.Exit')
        ch = input('Select action number: ')
        if ch == '1.' or ch == '1':
            if LogIn() == 0:
                print("Try again")
        elif ch == '2.' or ch == '2':
            login, paswword_b = SignIn()
            return login, paswword_b
        elif ch == '3.' or ch == '3':
            print('...EXIT...')
            exit()
        else:
            print('There is no such option')


def A_to_B():
    login, paswword_b = choose()


if __name__ == '__main__':
    flag = False
    while True:
        print("Вход пользователя А:")
        login_A, password_A = choose()
        ###
        print("Пользователь В индентифицирует пользователя А")
        if check_password(login_A, password_A):
            print("Пользователь А индетифицирован")
            ###
            while True:
                print("Вход полльзователя В")
                login_B, password_B = choose()
                ###
                print("Пользователь A индентифицирует пользователя B")
                if check_password(login_B, password_B):
                    print("Пользователь B индетифицирован")
                    print("Соединение устоновленно!")
                    flag = True
                    break
                else:
                    print("Пользователь B клоун")
                    print("Try again")
                    continue
            if flag:
                break
        else:
            print("Пользователь А клоун")
            print("Try again")
            continue
