import gen_simple as gs
import random


# Перемножение матриц Квадратная на столбец
def MXM(A, B) -> list:
    def splitmatrix(M: list):
        c = []
        for i in range(len(M)):
            for j in range(len(M[i])):
                c.append(M[i][j])
        return c

    c_a = splitmatrix(A)
    c_b = splitmatrix(B)
    k = 1
    while len(c_a) != len(c_b):
        k += 1
        if len(c_b) < len(c_a):
            c = splitmatrix(B)
            c_b = c_b + c
        elif len(c_a) < len(c_b):
            c = splitmatrix(A)
            c_a = c_a + c
    # print(c_a)
    # print(c_b)
    c_f = []
    for i in range(len(c_a)):
        c_f.append(c_a[i] * c_b[i])
    # print(c_f)
    finaly_vector = []
    for i in range(0, len(c_f), k):
        c = 0
        for j in range(k):
            c += c_f[i + j]
        finaly_vector.append(c)
    # print(finaly_vector)
    return finaly_vector


# Доверительный центр - генерирует размер конечного поля и секретную матрицу над этим полем
# Так же он отправляет пользователям их Закрытые ключи и идентификаторы
def Center(num_acc=2):
    p = gs.gen_simple(8)
    n = 5
    # n = num_acc
    r_list = []
    while len(r_list) != n:
        r_i = random.randint(1, p)
        if r_i in r_list:
            continue
        else:
            r_list.append(r_i)
    m = random.randint(1, n)
    D = []  # Секретная матрица
    for i in range(m):
        i_string = []
        for j in range(m):
            a_i_j = random.randint(1, p)
            i_string.append(a_i_j)
        D.append(i_string)

    for i in range(m):
        for j in range(m):
            D[j][i] = D[i][j]

    # print(D)

    list_Identification = []  # Индификаторы пользователей
    for i in range(num_acc):
        key_i = []
        for i in range(m):
            d = []
            k = random.randint(1, p)
            d.append(k)
            key_i.append(d)
        list_Identification.append(key_i)

    # print(list_Identification)

    list_secret_key = []  # Все секретныйе ключи пользователей, каждый список в нем есть ключ одного пользователя
    for i in range(num_acc):
        key = MXM(D, list_Identification[i])
        for i in range(len(key)):
            key[i] = key[i] % p
        list_secret_key.append(key)

    # print(list_secret_key)

    list_Iden = []
    for i in range(len(list_Identification)):
        user_Iden = []
        for j in range(len(list_Identification[i])):
            for k in range(len(list_Identification[i][j])):
                user_Iden.append(list_Identification[i][j][k])
        list_Iden.append(user_Iden)
    print(list_Iden)
    return list_secret_key, list_Iden, p


# Пользователю передают идентификатор другоо пользователя которого он иденттфицирует
def cheack_key(SeK, Ind_not_Own):
    print(SeK, Ind_not_Own)
    if len(SeK) != len(Ind_not_Own):
        print('Error')
        exit()
    else:
        k = 0
        for i in range(len(SeK)):
            a = SeK[i] * Ind_not_Own[i]
            k = k + a
        return k


def main():
    SeK_list, Iden_list, p = Center()  # В списках: 0 индекс - 1вый пользователь, 1 индекс - 2рой пользователь и тд
    A = cheack_key(SeK_list[0],
                   Iden_list[1])  # Передаем полльзователю А индификатор полльзавателя В и секретный ключ пользователя А
    B = cheack_key(SeK_list[1],
                   Iden_list[0])  # Передаем полльзователю В индификатор полльзавателя А и секретный ключ пользователя А
    A = A % p
    B = B % p
    print('Cеансовые ключи А и В соответсвенно')
    print(A, B)
    if A == B:
        print('Ключи совпадают')


test_A = [[1, 6, 2],
          [6, 3, 8],
          [2, 8, 2]]
test_B = [[3], [10], [11]]

if __name__ == '__main__':
    main()
