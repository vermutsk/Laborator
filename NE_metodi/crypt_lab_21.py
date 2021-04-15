import random
import gen_simple as gs


# Нахождения всех примитиво поля от простого числа (неоптимизированный) до 16 битов
def primitive(p: int) -> list:
    gen_field = []
    for i in range(2, p):
        rangee = [x for x in range(1, p)]
        for j in range(p):
            elem = i ** j % p
            if elem in rangee:
                rangee.remove(elem)
        if len(rangee) == 0:
            gen_field.append(i)
    return gen_field


# p - simple, alph - primitive GF(p)
def User_open_param(p, alph):
    r = random.randint(1, p - 2)
    z = gs.quick_pow_mod(int(alph), r, p)
    return r, z  # r - случайное число(другими пользователями не используеться z - открытая экспанента


def open_param_all_Users(p, alph, num_users=3):
    r_l = []
    z_l = []
    for i in range(num_users):
        r, z = User_open_param(p, alph)
        r_l.append(r)
        z_l.append(z)
    return r_l, z_l  # Рассывале всем пользователям открытую экспаненту, и случаынйе числа (в настоящам протоколе они хроняться у каждого пользователя отдельно)


def User_X(z_next_user, z_last_user, r_user):
    X = (z_next_user * (z_last_user ** (-1))) ** r_user
    X = int(X)
    return X


def Users_all_X(r_l, z_l, num_users=3):
    X_l = []
    for i in range(num_users):
        next_i = (i + 1) % num_users
        last_i = (i - 1) % num_users
        X = User_X(z_l[next_i], z_l[last_i], r_l[i])
        X_l.append(X)
    return X_l


def User_key(X_l, z, r, p, num_users=3):
    pre = z ** (num_users * r)
    k = 1
    for i in range(0, num_users):
        for j in range(num_users, -1, -1):
            k = k * (X_l[int((j - i) % num_users)] ** i)
            break
    k = pre * k
    k = k % p
    return k


def Users_all_key(X_l, z_l, r_l, p, num_users=3):
    k_l = []
    for i in range(num_users):
        k = User_key(X_l, z_l[i], r_l[i], p, num_users)
        #print('user ', i, ': Key = ', k)
        k_l.append(k)
    return k_l


def main():
    p = gs.gen_simple(8)
    a = primitive(p)
    ind = random.randint(0, len(a) - 1)
    a = a[ind]
    r_l, z_l = open_param_all_Users(p, a)
    X_l = Users_all_X(r_l, z_l)
    k_l = Users_all_key(X_l, z_l, r_l, p)
    flag = True
    for i in range(len(k_l)):
        if k_l[i % len(k_l) - 1] == k_l[i + 1 % len(k_l) - 1]:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('Ключи всех пользователей совпадает. Протокол выполнен успешно.')
    else:
        print("Ключи не совпадают. Пересапустите протокол")


if __name__ == '__main__':
    main()
