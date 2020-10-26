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
        a = a2 = (q*a1)
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
    return m, a, b

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
    m, l, b = evklid(n, a)
    if m != 1:
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

def ferma():
    n, a = simple()
    r = pow(a, n-1, n)
    if r == 1:
        print('Число, вероятно, простое')
    else:
        print('Число составное')

def shtrassen():
    n, a = simple()
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

def miller():
    n, a = simple()
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
                print('Число составное')
                return 0
            j += 1
        if y!= n-1:
            print('Число составное')
            return 0
    print('Число, вероятно, простое')

def gen_simple():
    pass


#././././././././././././././././././././././././.Меню./././././././././././././././././././././././././././././.
er=0
flag = True
while flag:
    flag2 = True
    try:
        print("\nГлавное меню:")
        choice = int(input("\n1) Обобщенный (расширенный) алгоритм Евклида\n2) Алгоритм быстрого возведения в степень по модулю\
            \n3) Вычисление символа Якоби\n4) Алгоритмы проверки чисел на простоту \n5) Генерация простого числа заданной размерности\
            \n6) Выйти из программы\nВыбор: "))
        
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
                ferma()
            elif choice1 == 2:
                ans = shtrassen()
                print(ans)
            elif choice1 == 3:
                miller()
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
            pass
        
        elif choice==6:
            flag==False
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
    #except TypeError:
    #    print("TypeError")
    #except UnboundLocalError:
    #    print("Возникла ошибка")
    #except IndexError:
    #    print("IndexError")
    #except ValueError:
    #    print("ValueError") 