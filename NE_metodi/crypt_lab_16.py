import RSA
import random
import lab7  # CS_RSA
import time


def cp_k_t(k, t, keys: list):
    k_t = k + t
    print('Подписываем временную метку и сеансовый ключ')
    sign, hf = lab7.Formirovanie(k_t, keys)
    # print(type(sign), type(hf))
    return sign, hf


def Encrypted(k, t, CP_1, CP_2, keys: list):
    print('Зашифровываем сеансовый ключ, временную метку и цифровую подпись')
    c_k = RSA.Encription(keys, int(k))
    c_t = RSA.Encription(keys, int(t))
    c_CP_1 = RSA.Encription(keys, int(CP_1))
    c_CP_2 = RSA.Encription(keys, int(CP_2))
    return c_k, c_t, c_CP_1, c_CP_2


def A_to_B(k, t, keys: list):
    CP_1, CP_2 = cp_k_t(k, t, keys)  # подписанный сеансовый ключ и временная метка
    c_k, c_t, c_CP_1, c_CP_2 = Encrypted(k, t, CP_1, CP_2, keys)  # Зашифрование данных
    return c_k, c_t, c_CP_1, c_CP_2  # Передача данных пользователю В


# Пользователь В принимает зашифрованные данные
def check_B(c_k, c_t, c_CP_1, c_CP_2, keys: list):
    print('Пользователь В расшифровывает данные')
    k = RSA.Decription(keys, c_k)
    t = RSA.Decription(keys, c_t)
    CP_1 = RSA.Decription(keys, c_CP_1)
    CP_2 = RSA.Decription(keys, c_CP_2)
    print('Пользователь В проверяет ЦП пользователя А')
    check = lab7.Proverka(CP_1, keys, CP_2)
    if check:
        print('Проверка ЦП прошла успешна.Ключ передан')
        print('Сеансовый ключ - ', k)
        print('Временная метка - ', t)
        return 0
    else:
        print('Проверка ЦП прровалилась. прекрощение протокола.')
        return -1


def main():
    k = str(random.getrandbits(32))  # Сеансовый ключ
    keys = RSA.GenKeys()  # Открытый и закрытый ключи
    t = ''.join(str(time.time()).split('.'))  # Временная метка
    print(type(t))
    print(type(k))
    c_k, c_t, c_CP_1, c_CP_2 = A_to_B(k, t, keys)
    print('Передаем данные пользователю В')
    kkk = check_B(c_k, c_t, c_CP_1, c_CP_2, keys)
    if kkk == -1:
        return -1


if __name__ == '__main__':
    main()
