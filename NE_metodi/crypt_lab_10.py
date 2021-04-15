import random
import math
import SHA
import Stribog
import function as fun
import json
from Crypto.Util import number

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
                349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
                569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
                619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757,
                761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                991, 997, 1009, 1013, 1019, 1021, 1031,
                1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
                1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259,
                1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399,
                1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487,
                1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607,
                1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733,
                1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873,
                1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999]

def M_R(n):
    for s in range(0, n):
        if ((n - 1) % (2 ** s)) == 0 and (((n - 1) / (2 ** s)) % 2) != 0:
            r = int((n - 1) / (2 ** s))
            print(r)


def Ferma(num, t=5):
    for i in range(t):
        a = random.randint(2, num - 2)
        r = pow(a, num - 1, num)
        if r != 1:
            return False
    return True


def simple_q(p, cup):
    for q in range(547, cup, 2):
        for i in range(len(prime_list)):
            if q % prime_list[i] == 0:
                continue
        check = Ferma(q)
        if check:
            if (p - 1) % q == 0:
                return q
        else:
            continue


def pre_simple_chek(p):
    with open('simple.txt', 'r', encoding='utf-8') as file:
        list_prime = file.read().split(',')
    for i in range(len(list_prime)):
        if (p - 1) % int(list_prime[i]) == 0:
            return int(list_prime[i])
        else:
            return -1


def ORD(q, p):
    for a in range(2, p):
        if pow(a, q, p) == 1:
            return a


def Gen_PQA():
    p = number.getPrime(32, None)
    print('p', p)
    hight_cup = (p - 1) / 2
    hight_cup = int(hight_cup)
    q = simple_q(p, hight_cup)
    print('q', q)
    a = ORD(q, p)
    print('a', a)
    return p, q, a


def Eler(n):
    print('Идет вычисления функции эйлера')
    i = 2
    result = n
    while i * i <= n:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
            result -= result / i
    if n > 1:
        result -= result / n
    print('Функция эйлера вычеслина')
    return int(result)


def test():
    return 2150047507, 1489, 753709


def Open_Secret_key(p, a, count):
    z = random.randint(100, p - 2)
    l = pow(a, z, p)
    secret_key = {'LEAD': z}
    open_key = {'LEAD': l}
    for j in range(1, int(count) + 1):
        name = input('Введите имя пользователя'
                    '>>')
        k = random.randint(100, p - 2)
        p = pow(a, k, p)
        secret_key.update({name: k})
        open_key.update({name: p})
    return secret_key, open_key  # Возвращает список всех открытых ключей и закрытых ключей


def LEAD_secret_end(p):
    p1 = number.getPrime(32, None)
    p2 = number.getPrime(32, None)
    d = random.randint(100, p - 2)
    n = p1 * p2
    # wi = Eler(n)
    wi = (p1 - 1) * (p2 - 1)
    e = (1 / d) % wi
    return e, n, d


def hesh_choose(message, type):
    if type == '1':
        H = SHA.sha256(message)
        return H
    elif type == '2':
        H = SHA.sha512(message)
        return H
    elif type == '3':
        H = Stibog.Main(message, 256)
        return H
    elif type == '4':
        H = Stibog.Main(message, 512)
        return H
    else:
        print('Error')
        return 0


def genCP():
    print('Генерация общих параметров: ')
    #p, q, a = Gen_PQA()
    p, q, a = test()
    count = input('Количество пользователей помимо лидера.\n'
                '>>')
    SeK, OpK = Open_Secret_key(p, a, count)
    e, n, d = LEAD_secret_end(p)
    while True:
        type_hesh = input('Выбирете тип хэш функции:\n'
                        '1. sha256\n'
                        '2. sha512\n'
                        '3. stribog256\n'
                        '4. stribog512\n'
                        '>>')
        message = input('Сообщения для групповой подписи.\n'
                        '>>')
        H = hesh_choose(message, type_hesh)
        if H == 0:
            continue
        else:
            break
    U, lmd_l = LEAD_1(H, OpK, n, d, p)
    R_l, t_l = USERS_2(p, q, a, int(count))
    E, T = LEAD_3(p, q, a, R_l, message, U, type_hesh)
    E = int(E, 16)
    S_l = USERS_4(q, SeK, t_l, lmd_l, E)
    S = LEAD_5(R_l, OpK, lmd_l, E, a, S_l, p, T, SeK, q, int(count))
    if S == -1:
        print('Не ну это домой.')
    else:
        get_sign(U, E, S)
        saveCP(type_hesh, U, OpK['LEAD'], a, p, message, E, S)


def LEAD_1(H, OpenKey: dict, n, d, p):
    lmd_l = []
    p_list = []
    for k, j in OpenKey.items():
        if k == 'LEAD':
            continue
        t = (int(H, 16) + j)
        # t = int(t, 16)
        lmd = pow(t, d, n)
        lmd_l.append(lmd)
        p_list.append(j)
    U = 1
    for i in range(len(p_list)):
        a = p_list[i]
        b = lmd_l[i]
        U = U * pow(a, b, p)
    return U, lmd_l  # Лидер возврaщает каждому пользователю лямбда


def USERS_2(p, q, a, count: int):
    R_l = []
    t_l = []
    for i in range(count):
        t = random.randint(2, q - 1)
        R = pow(a, t, p)
        R_l.append(R)
        t_l.append(t)
    return R_l, t_l  # Каждый пользователь возврaщает лидеру R, t пользователь не возврaщает, но в данной лабе возврaщает


def LEAD_3(p, q, a, R_l: list, M, U, type):
    T = random.randint(2, q - 1)
    R_lead = pow(a, T, p)
    R = 1
    for i in range(len(R_l)):
        R = R * R_l[i]
    R = R_lead * (R % p)
    E = M + str(R) + str(U)
    if type == '1':
        E = SHA.sha256(E)
        return E, T  # Лидер отправляет каждому пользователю E, лидер T не передаёт, но тут передаёт
    elif type == '2':
        E = SHA.sha512(E)
        return E, T 
    elif type == '3':
        E = Stibog.Main(E, 256)
        return E, T 
    elif type == '4':
        E = Stibog.Main(E, 512)
        return E, T 


def USERS_4(q, SecretKey: dict, t_l, lmd_l, E):
    S_l = []
    secret_key_l = []
    for k, j in SecretKey.items():
        if k == 'LEAD':
            continue
        secret_key_l.append(j)
    for i in range(len(secret_key_l)):
        S = (t_l[i] + secret_key_l[i] * lmd_l[i] * E) % q
        S_l.append(S)
    return S_l  # Каждый пользователь возврощает S


def LEAD_5(R_l, OpenKey: dict, lmd_l, E, a, S_l, p, T, SecretKey: dict, q, count):
    open_key_list = []
    list_True = []
    flag = True
    for k, j in OpenKey.items():
        if k == 'LEAD':
            continue
        open_key_list.append(j)

    for i in range(count):
        # lop = -1 * lmd_l[i] * E
        # print(open_key_list[i], lop, p)
        # g = pow(open_key_list[i], lop) * pow(a, S_l[i])
        # g = (open_key_list[i] ** lop) * (a ** S_l[i])
        '''semi_1 = quick_pow_mod(open_key_list[i], lop, p)
        semi_2 = quick_pow_mod(a, S_l[i], p)
        semi = semi_1 * semi_2'''
        if R_l[i] == (
                int(fun.obrat(pow(open_key_list[i], lmd_l[i] * E, p), p)) * pow(a, S_l[i], p)) % p:
            print(f"{i} is not okey")

    if flag:
        S_h = (T + SecretKey['LEAD'] * E) % q
        S_sum = 0
        for i in range(count):
            S_sum += S_l[i]
        S = (S_h + S_sum) % q
        return S
    else:
        return -1


def get_sign(U, E, S):
    print('Цифровая подписиь:\nU - {}\nE - {}\nS - {}'.format(U, E, S))


def saveCP(hesh, U, L, a, p, message, E, S):
    dataCP = {'hesh': hesh, 'U': U, 'L': L, 'a': a, 'p': p, 'message': message, 'E': E, 'S': S}
    with open('CP.txt', 'w') as file:
        json.dump(dataCP, file)


def loadCP():
    with open('CP.txt', 'r') as file:
        dataCP = json.load(file)
    return dataCP


def check_CP():
    data = loadCP()
    if data['hesh'] == '1':
        H = SHA.sha256(data['message'])
    elif data['hesh'] == '2':
        H = SHA.sha512(data['message'])
    elif data['hesh'] == '3':
        H = stibog.Main(data['message'], 256)
    elif data['hesh'] == '4':
        H = stibog.Main(data['message'], 512)
    R_test = (int(fun.obrat(pow(data['U'] * data['L'], data['L'], data['p']), data['p'])) * pow(
        data['a'], data['S'], data['p'])) % data['p']
    kon = data['message'] + str(R_test) + str(data['U'])
    if data['hesh'] == '1':
        E_test = SHA.sha256(kon)
    elif data['hesh'] == '2':
        E_test = SHA.sha512(kon)
    elif data['hesh'] == '3':
        E_test = Stibog.Main(kon, 256)
    elif data['hesh'] == '4':
        E_test = Stibog.Main(kon, 512)

    if data['E'] == E_test:
        print(True)
    else:
        print(False)


flag = True
while flag:
    menu = input('Главное меню.\n1. Генерация подписи\n2. Проверка подписи\n3. Выход\n>>')
    if menu == '1':
        genCP()
    elif menu == '2':
        check_CP()
    elif menu == '3':
        flag = False
        break
    else:
        print('Ошибка ввода')

