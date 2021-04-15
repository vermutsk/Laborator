import SHA_V  # 5 lab
import stibog  # 4 
import random
import json
import os


def Enter_message(text: str):
    print(text)
    mes = input('>>')
    return mes


def Register(h_t: int, n=10):
    login = Enter_message('Введите логин')
    file_name = login + '.acc'
    list_acc = os.listdir()
    if file_name in list_acc:
        print('Никнейм занят')
        return 0
    password_1 = Enter_message('Введите пароль')
    h_password_1 = SHA_V.sha_alg_512(password_1)
    password_2 = Enter_message('Повторите пароль')
    h_password_2 = SHA_V.sha_alg_512(password_2)
    if h_password_1 == h_password_2:
        print('Пользователь зарегистрирован:')
        wi_max = hesh_n(h_t, password_1, n)
        data_user = {login: [password_1, 0, n, wi_max], 'B': [wi_max, 0]}
        with open(file_name, 'w') as file:
            json.dump(data_user, file)
        return 1
    else:
        print('Обосрамс')
        return -1


def Enterens():
    login = Enter_message('Введите логин')
    file_name = login + '.acc'
    list_acc = os.listdir()
    if file_name not in list_acc:
        print('Пользователя не существует')
        return 0
    password_e = Enter_message('Введите пароль')
    password_h = SHA_V.sha_alg_512(password_e)
    with open(file_name, 'r') as file:
        data_users = json.load(file)
    password = data_users[login][0]
    if password_e == password:
        print('Вход произведен')
        return data_users, login
    else:
        print('Обосрамс')
        return -1


def Acc_logic(h_t: int):
    while True:
        ch = Enter_message('Вход/Регистрация.\n1. Регистрация\n2. Вход\n3. Exit')
        if ch == '1':
            R = Register(h_t)
            if R == 0:
                continue
            elif R == 1:
                continue
            elif R == -1:
                continue
        elif ch == '2':
            E = Enterens()
            if E == 0:
                continue
            elif E == -1:
                continue
            else:
                return E
        elif ch == '3':
            return 0
        else:
            print('Соре, на та кнопка.')
            continue


def choose_type_hesh_fun():
    while True:
        c_type = Enter_message('Выберите функцию хеширования:\n1. SHA-256\n2. SHA-512\n3. STRIBOG-256\n4. STRIBOG_512')
        if c_type == '1':
            return 1
        elif c_type == '2':
            return 2
        elif c_type == '3':
            return 3
        elif c_type == '4':
            return 4
        else:
            print('Соре, на та кнопка.')
            continue


def HESH(type_h: int, message: str):
    if type_h == 0:
        return '0'
    elif type_h == 1:
        H = SHA_V.sha_alg_256(message)
        return H
    elif type_h == 2:
        H = SHA_V.sha_alg_512(message)
        return H
    elif type_h == 3:
        H = stibog.Main(message, 256)
        return H
    elif type_h == 4:
        H = stibog.Main(message, 512)
        return H


def gen_password(size: int):
    psw = random.getrandbits(size)
    psw = str(psw)
    return psw


def hesh_n(type_h: int, message: str, n):
    M = message
    for i in range(n):
        H = HESH(type_h, M)
        M = H
    return M


def main():
    h_t = choose_type_hesh_fun()
    acc = Acc_logic(h_t)
    if acc == 0:
        exit()
    else:
        print('Пользователь А в системе')
        login = acc[1]
        data = acc[0]
        w = data[login][0]
        i = data[login][1]
        n = data[login][2]
        wi_max = data[login][3]
        A = login
        print('Пользователь А передаёт: ', A, i, wi_max)
        if i > n:
            print('i > n Количиство индетификаций превышенно')
            exit()
        if i == data['B'][1]:
            hesh_A = hesh_n(h_t, w, n - i)
            if hesh_A == data['B'][0]:
                i += 1
                wi = hesh_A
                hesh_A = hesh_n(h_t, w, n - i)
                data_user = {login: [w, i, n, wi], 'B': [hesh_A, i]}
                file_name = login + '.acc'
                os.remove(file_name)
                with open(file_name, 'w') as file:
                    json.dump(data_user, file)

        """print('Пользователь А в системе')
        w = gen_password(32)
        A = acc
        n = 5
        hesh_type = choose_type_hesh_fun()
        w_list = hesh_list(hesh_type, w, n)
        print(w_list)
        i = random.randint(1, n)
        wi = w_list[n - i]
        print('Пользователь А отпровляет: ', A, i, wi)"""


if __name__ == '__main__':
    main()
