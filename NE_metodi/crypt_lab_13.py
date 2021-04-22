import SHA
import Stribog
import RSA1 as RSA
import random


def hesh_message(message: str, type_hesh: int):
    if type_hesh == 1:
        H = SHA.sha256(message)
    elif type_hesh == 2:
        H = SHA.sha512(message)
    elif type_hesh == 3:
        H = Stribog.Stribog(message, 256)
    elif type_hesh == 4:
        H = Stribog.Stribog(message, 512)
    else:
        H = '0'
    return H


# Принимает А- идентификатор пользователя А, z - случайное число, type_hesh - ип хеширования(обычно задан сам протоколом)
# KEYS - ключчи для шифрования и дешифрования(в настоящем протоколе пользователю А извесен только открытый,пользователю В открытый и закрытый через который он и расшифровывает
def A_to_B(z: int, type_hesh: int, KEYS: list):
    print('Приступаем к процедуре идентификации пользователя A')
    A = random.getrandbits(8)
    h_z = hesh_message(str(z), type_hesh)
    E_z = RSA.Encription(KEYS, z)
    E_A = RSA.Encription(KEYS, A)
    return h_z, A, E_z, E_A  # Передает пользователю В хэшировано z, идентификатор А, Зашифрованное z,зашифрованное А


# Принимает хэшировано z, идентификатор А, Зашифрованное z,зашифрованное А
def B_to_A(h_z, A, E_z, E_A, KEYS, type_hesh):
    D_A = RSA.Decription(KEYS, E_A)
    if A == D_A:
        print('Пользователь В идентифицировал пользователя А')
        D_z = RSA.Decription(KEYS, E_z)
        h_z_ag = hesh_message(str(D_z), type_hesh)
        if h_z == h_z_ag:
            print('Хэши случайного числа совпали\n')
            print('Приступаем к процедуре идентификации пользователя B')
            return D_z  # Передает пользователю А расшифрованное z
        else:
            print('Хэши случайного числа не совпали, завершение протокола')
            return -1
    else:
        print('Пользователь A не идентифицирован, завершение протокола')
        return -1


# z_A - передаеться пользователю А в шаге 1, z_B - передаеться пользователем В
def check_A(z_A, z_B):
    if z_A == z_B:
        print('Пользователь А идентифицировал пользователя В')
        return True
    else:
        print('Пользователь В не идентифицирован, завершение протокола')
        return False
    pass


flag = True
while flag:
    z = random.getrandbits(8)
    hesh_type = 0
    flag2 = True
    while flag2:
        mes = input('Выберите функцию хеширования:\n1. SHA_256\n2. SHA_512\n3. STRIBOG_256\n4. STRIBOG_512 \n >>')
        if mes == '1':
            hesh_type = 1
        elif mes == '2':
            hesh_type = 2
        elif mes == '3':
            hesh_type = 3
        elif mes == '4':
            hesh_type = 4
        else:
            print('Error')
        if hesh_type != 0:
            flag2 = False
    key_list = RSA.GenKeys()
    h_z, A, E_z, E_A = A_to_B(z, hesh_type, key_list)
    z_B = B_to_A(h_z, A, E_z, E_A, key_list, hesh_type)
    if z_B == -1:
        print('Повторите протокол с начала')
    else:
        b = check_A(z, z_B)
        if b:
            print('Протокол завершeн успешно')
            flag = False
        else:
            print('Возникла ошибка')