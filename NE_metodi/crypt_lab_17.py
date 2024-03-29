import gen_simple as gs
import random

# Функция Эйлера
def fi(n: int):
    f = n;
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i;
            f = f // i;
            f = f * (i - 1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n - 1);
    return f;


# Нахождения всех взаимно простых с num
def all_num_in_fi(num: int):
    simple_list = []
    for i in range(2, num):
        if num % i != 0:
            simple_list.append(i)
        else:
            continue
    return simple_list


# Нахождения всех примитивоb поля от простого числа (неоптимизированный) до 16 битов
def primetive(p: int):
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



# p и g известные данные обоим сторонам
def A_to_B_1(p: int, g: int):
    x = random.randint(2, p - 2)
    a = pow(g, x, p)
    print('Параметры пользователя А сформированы')
    return a, x


# p и g известные данные обоим сторонам
def B_to_A_2(p: int, g: int):
    y = random.randint(2, p - 2)
    b = pow(g, y, p)
    print('Параметры пользователя В сформированы')
    return b, y


# p - общиизвестный параметр, x - вычислялся А на шаге 1, b - передавался в шаге 2
def A_3(p: int, x: int, b: int):
    k = pow(b, x, p)
    return k


# p - общиизвестный параметр, y - вычислялся B на шаге 2, a - передавался в шаге 1
def B_3(p: int, y: int, a: int):
    k = pow(a, y, p)
    return k


def modul_main(p,g):
    a, x = A_to_B_1(p, g)
    b, y = B_to_A_2(p, g)
    k_A = A_3(p, x, b)
    k_B = B_3(p, y, a)
    print(k_A, k_B)
    if k_A == k_B:
        print('Распределенные ключи совпадают')
        return True
    else:
        print('Распределенные ключи не совпадают')
        return False


def main():
    p = gs.gen_simple(8)
    g_list = primetive(p)
    g_i = random.randint(0, len(g_list))
    g = g_list[g_i]
    a, x = A_to_B_1(p, g)
    b, y = B_to_A_2(p, g)
    k_A = A_3(p, x, b)
    k_B = B_3(p, y, a)
    print(k_A, k_B)
    if k_A == k_B:
        print('Распределенные ключи совпадают')
    else:
        print('Распределенные ключи не совпадают')


if __name__ == '__main__':
    main()