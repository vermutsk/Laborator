import random
def evkl_x_y():
    flagxy = True
    while flagxy:
        try:
            flagx = True
            flagy = True
            while flagx:
                x = int(input('\n Введите x:'))
                if x > 0:
                    flagx = False
                else:
                    print('x не может быть отрицательным')
            while flagy:
                y = int(input('\n Введите y:'))
                if y > 0:
                    flagy = False
                else:
                    print('y не может быть отрицательным')
            if x >= y:
                flagxy = False
                m, a, b = evklid(x, y)
                return m, a, b
            else:
                print('Ошибка: y > x')
        except Exception:
            print('Ошибка')

def evklid(x, y):
    a1, a2, b1, b2 = 0, 1, 0, 1
    while y != 0:
        q = x // y
        r = x - (q*y)
        a = a2 - (q*a1)
        b = b2 - (q*b1)
        x = y
        y = r
        a2 = a1
        a1 = a
        b2 = b1
        b1 = b
    m = x
    a = a2
    b = b2
    l = [m, a, b]
    return l

def to_bin(n):
    n = bin(n)
    n = str(n)
    b = []
    for i in range(len(n)):
        b.append(n[i])
    b.reverse()
    b.pop()
    b.pop()
    return b

def exponentiating():
    flag = True
    while flag:
        try:
            a = int(input('\n Введите основание: '))
            n = int(input('Введите степень: '))
            flag = False
        except Exception:
            print('Ошибка')
    x = 1
    b = to_bin(n)
    for i in range(len(b)):
        x = x * (a**(int(b[i])*(2**(i))))
        print(x, b[i], i)

def mod_exponentiating():
    flag = True
    while flag:
        try:
            a = int(input('\n Введите основание: '))
            s = int(input('Введите степень: '))
            n = int(input('Введите mod: '))
            flag = False
        except Exception:
            print('Ошибка')
    b = to_bin(s)
    g = a
    x = a**int(b[0])
    for i in range(0, len(b)):
        g = g**2
        y = pow(g, 2, n)
        if b[i] == '1':
            x = pow(x*y, 1, n)
    print(x)

def yakobi(n, a):
    m = evklid(n, a)
    if m[0] != 1:
        return 0
    g = 1
    if a < 0:
        a = -a
        if n%4==3:
            g = -g
    while a != 0:
        t = 0
        while a%2 == 0:
            t+=1
            a = a/2
        if t%2!=0:
            if n%8 == 3 or n%8 == 5:
                g = -g
        if a%4 == n and n%4==3:
            g = -g
        c=a
        a=n%c
        n=c
    return g

def simple():
    flag = True
    while flag:
        try:
            n = int(input('Введите нечетное число для проверки: '))
            if n % 2 == 0:
                print('Число четное')
            elif n < 5:
                print('Число не должно быть меньше 5')
            else:
                flag = False
                a = random.randint(2, n-2)
                return n, a
        except Exception:
            print('Ошибка')

def ferma(n, a):
    r = pow(a, n-1, n)
    if r == 1:
        print('Число, вероятно, простое')
    else:
        print('Число составное')

def shtrassen(n, a):
    k = (n-1)//2
    print(a, n, k)
    r = pow(a, k, n)
    if r != 1 and r != n - 1:
        ans = 'Число составное'
        return ans
    s = yakobi(n, a)
    if s%n == r:
        ans = 'Число, вероятно, простое'
    else:
        ans = 'Число составное'
    return ans

def miller(n, a):
    r = n-1
    s = 0
    while r%2 == 0:
        s+=1
        r = r/2
    r = int(r)
    y = pow(a, r, n)
    while y != 1 and y != n-1:
        j = 1
        while j <= s-1 and y != n-1:
            y = pow(y, 2, n)
            if y==1:
                
                return False
            j += 1
        if y!= n-1:
            return False
    return True

def gen_simple():
    ready = True
    while ready:
        flag = True
        while flag:
            k = int(input('Введите разрядность: '))
            t = int(input('Введите параметр: '))
            if k > 0 and t >= 1:
                flag = False
        p = '1'
        for i in range(1,k-1):
            n = random.randint(0, 1)
            p += f'{n}'
        p += '1'
        p0 = 0
        for i in range(k-1, -1, -1):
            if p[i] == '1':
                p0 += 2**(k-i-1)
        p0 = int(p0)
        flag = True
        for i in range(1, t+1):
            a = random.randint(2, p0-2)
            if miller(p0, a) == False:
                flag = False
                break
        if flag == True:
            print(p0)
            return 0

def compair_1():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    m = int(input('Введите m: '))
    d = evklid(a, m) 
    if b%d[0] != 0:
        print('Решений нет')
        return False
    if d[0] != 1:
        a1 = a/d[0]
        b1 = b/d[0]
        m1 = m/d[0]
        a01= evklid(a1, m1)
        x0 = a01[2]*b1%m1
        print('x0 =', x0)
    else:
        x = d[2]*b%m
        print('x =', x)
        return True
    for i in range(1, d-1):
        t = int(x0 + (i*m1))
        print(f', x{i} =', t) 

def compair_2():
    flag = True
    while flag:
        p = int(input('Введите p: '))
        if p > 2:
            a = random.randint(1, p-2)
            if miller(p, a)==True:
                a = int(input('Введите a: '))
                N = int(input('Введите N: '))
                if yakobi(p, a)==1 and yakobi(p, N)==-1:
                    flag = False
    h=p-1
    k=0
    while h%2 == 0:
        k+=1
        h = int(h/2)
    a1 = pow(a, int((h+1)/2), p)
    a2 = evklid(a, p) 
    N1 = pow(N, h, p)
    N2 = 1
    j = 0
    for i in range(k-1):
        b = a1*N2%p
        c = a2[2]*(b**2)%p
        d = pow(c, k-2-i, p)
        if d == 1:
            j = 0
        elif d == -1:
            j = 1
        N2 *= pow(N1, (2**i)*j, p)
    x = a1*N2%p
    print(x, x*(-1))

def compair_system():
    flag = True
    while flag:
        n = int(input('Введите количество уравнений в системе: '))
        b = []
        m = []
        for i in range(n):
            b_i = int(input(f'Введите b{i}: '))
            m_i = int(input(f'Введите m{i}: '))
            b.append(b_i)
            m.append(m_i)
        for i in range(0, n-1):
            d = evklid(m[i], m[i+1])
            if d[0] == 1:
                flag = False
            else:
                flag = True
                break
    M = m[0]
    for i in range(1, n):
        M *= m[i]
    x=0
    for j in range(n):
        M_j = M/m[j]
        N = evklid(M_j, m[j]) 
        x += b[j]*N[2]*M_j
    x = int(x%M)
    print(x)


#././././././././././././././././././././././././.Меню./././././././././././././././././././././././././././././.
er=0
flag = True
while flag:
    flag2 = True
    try:
        print("\nГлавное меню:")
        choice = int(input("\n1) Обобщенный (расширенный) алгоритм Евклида\n2) Алгоритм быстрого возведения в степень по модулю\
            \n3) Вычисление символа Якоби\n4) Алгоритмы проверки чисел на простоту \n5) Генерация простого числа заданной размерности\
            \n6) Решение сравнения первой степени\n7) Решение сравнения второй степени\n8) Решение системы уравнений\n9) Выйти из программы\nВыбор: "))
        
        if choice==1: 
            er=0
            m, a, b = evkl_x_y()
            print(m, a, b)

        elif choice==2:
            er=0 
            choice1 = int(input("\n1) Возведение в степень\n2) Возведение в степень по модулю\
            \n3) Вернуться\nВыбор: "))
            if choice1 == 1:
                exponentiating()
            elif choice1 == 2:
                mod_exponentiating()
            elif choice1 == 3:
                break
            else:
                print("Ошибка ввода\n")
                er+=1
                if er > 2:
                    print("Слишком много попыток")
                    flag = False
                    break

        elif choice==3: 
            er=0
            flagxy = True
            while flagxy:
                try:
                    flagx = True
                    flagy = True
                    while flagx:
                        n = int(input('\n Введите n:'))
                        if n < 3:
                            print('n не может быть меньше 3')
                        elif n % 2 == 0:
                            print('n четное')
                        else:
                            flagx = False
                    while flagy:
                        a = int(input('\n Введите a:'))
                        if a < 0:
                            print('a не может быть отрицательным')
                        else:
                            flagy = False
                    if n > a:
                        flagxy = False
                    else:
                        print('Ошибка: a >= n')
                except Exception:
                    print('Ошибка')
            ans = yakobi(n, a) 
            print(ans)

        elif choice==4: 
            er=0
            choice1 = int(input("\n1) Тест Ферма\n2) Тест Соловэя-Штрассена\
            \n3) Тест Миллера-Рабина \n4) Вернуться\nВыбор: "))
            if choice1 == 1:
                n, a = simple()
                ferma(n, a)
            elif choice1 == 2:
                n, a = simple()
                ans = shtrassen(n, a)
                print(ans)
            elif choice1 == 3:
                n, a = simple()
                if miller(n, a) == True:
                    print('Число, вероятно, простое')
                else:
                    print('Число составное')
            elif choice1 == 4:
                break
            else:
                print("Ошибка ввода\n")
                er+=1
                if er > 2:
                    print("Слишком много попыток")
                    flag = False
                    break

        elif choice==5:
            gen_simple()
        
        elif choice==6:
            compair_1()

        elif choice==7:
            compair_2()

        elif choice==8:
            compair_system()
        elif choice == 9:
            flag = False
            break

        else:
            print("Ошибка ввода\n")
            er+=1
            if er > 2:
                print("Слишком много попыток")
                flag = False
                break
    
    except SyntaxError:
        print("SyntaxError")
    except KeyboardInterrupt:
        pass
    except TypeError:
        print("TypeError")
    except UnboundLocalError:
        print("Возникла ошибка")
    except IndexError:
        print("IndexError")
    except ValueError:
        print("ValueError") 