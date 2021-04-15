import AES
import json
from datetime import datetime
import random


def AccountCreation():
    def creat_acc(name_acc: str, file: str):
        print('>>>Регистрация пользователя {}'.format(name_acc))
        while True:
            loginA = input('Введите логин: ')
            passwordA = input('Введите пароль: ')
            passwordA_chek = input('повторите пароль: ')
            if passwordA_chek == passwordA:
                with open(file, 'w') as f:
                    UsersInformation = {loginA: passwordA}
                    json.dump(UsersInformation, f)
                AES.AES_encrypt(file, generalkey)
                print('Аккаунт {} создан'.format(name_acc))
                break

    A_file = open('User_A.txt', 'w')
    A_file.close()
    B_file = open('User_B.txt', 'w')
    B_file.close()

    with open('aes_key.txt', "w", encoding="UTF-8") as keyfile:
        generalkey = AES.gen_key(16)
        keyfile.write(str(generalkey))

    creat_acc('A', 'User_A.txt')
    creat_acc('B', 'User_B.txt')


def AccountLogIn(userletter):
    print('>>>Вход пользователя', userletter)
    with open('aes_key.txt', "r", encoding="UTF-8") as keyfile:
        generalkey = keyfile.read()
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    UsersInformation_check = {login: password}
    way = 'User_' + userletter + '.txt.aes'
    new_file_name = AES.AES_decrypt(way, way.rstrip('.aes'), generalkey)
    with open(new_file_name, 'r') as file:
        UsersInformation = json.load(file)
    if UsersInformation_check == UsersInformation:
        print('Вход выполнен')
    else:
        print('Неверный логин или пароль')
        return 0


def Sending(sender, marker):
    with open('aes_key.txt', "r", encoding="UTF-8") as keyfile:
        generalkey = keyfile.read()
    # получение расшифрованного логина/пароля
    # way = 'User_' + sender + '.aes'
    # new_file_name = 'Message_From_' + AES.AES_decrypt(way, generalkey)
    # with open(new_file_name, 'r') as file:
    # UsersInformation = json.load(file)
    # шифрование маркера
    mark_way = 'Marker_' + sender + '.txt'
    with open(mark_way, 'w') as file:
        json.dump(marker, file)
    AES.AES_encrypt(mark_way, generalkey)


def Receive(sender, recipient):
    with open('aes_key.txt', "r", encoding="UTF-8") as keyfile:
        generalkey = keyfile.read()
    # расшифровывание маркера
    mark_way = 'Marker_' + sender + '.txt.aes'
    new_markfile_name = AES.AES_decrypt(mark_way, mark_way.rstrip('.aes'), generalkey)
    with open(new_markfile_name, 'r') as file:
        marker = json.load(file)
    # подтверждение отправителя
    way = 'User_' + sender + '.txt.aes'
    new_file_name = 'Message_From_' + way.rstrip('.aes')
    AES.AES_decrypt(way, new_file_name, generalkey)
    with open(new_file_name, 'r') as file:
        In_message = json.load(file)
    correct_way = 'User_' + sender + '.txt'
    with open(correct_way, 'r') as file:
        Correct = json.load(file)
    if In_message == Correct:
        print(f'Пользователь {recipient} подтвердил личность пользователя {sender}')
    else:
        print('Ошибка аутентификации')
        return 0
    return marker


def MainMemu():
    while True:
        print('>>Главное меню<<\n1.Регистрация \n2.Вход \n3.Обмен сообщениями \n4.Выход')
        choose = input('>>')
        if choose == '1':
            AccountCreation()
        elif choose == '2':
            AccountLogIn('A')
            AccountLogIn('B')
        elif choose == '3':
            while True:
                print('>>Выберите идентификатор<<: \n1. Метка врмени \n2. Случайное число')
                mark_ch = input('>>')
                if mark_ch == '1':
                    marker = datetime.now()
                    marker = str(marker)
                    marker = marker.replace(':', '').replace('-', '').replace(' ', '')[2:].split('.')[0]
                    print("Метка создана")
                elif mark_ch == "2":
                    marker = random.randint(1, 9876543210)
                    print("Число создано")
                else:
                    print("Неправильно введена команда\n")
                    continue
                Sending('A', marker)
                marker = Receive('A', 'B')
                Sending('B', marker)
                marker = Receive('B', 'A')
                Sending('A', marker)
                marker = Receive('A', 'B')
                break
        elif choose == '4':
            break
        else:
            print("Неправильно введена команда\n")


if __name__ == '__main__':
    MainMemu()
