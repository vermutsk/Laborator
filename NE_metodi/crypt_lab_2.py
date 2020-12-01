import math
import random
def evklid(x, y):
    while y != 0:
        r = x%y
        x = y
        y = r
    return x

def miller(n):
    r = n-1
    s = 0
    a = random.randint(2,n-2)
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

def base():
    b = [2, 3, 5, 7, 11, 13]
    i = 17
    while len(b)<1000:
        if miller(i)==True:
            b.append(i)
    return b

def first():
    n = int(input('Введите n: '))
    c = random.randint(3, 1000)
    flag = True
    while flag:
        function = input('Введите f(x): ')
        if function.find('x')!=-1:
            function = function.replace('x', '{}')
            if function.find('n')!=-1:
                function = function.replace('n', f'{n}')
                flag = False
        else:
            print('Некорректная функция')
    a = c
    b = c
    flag2 = True
    while flag2:
        a = eval(function.format(a))
        b = eval(function.format(function.format(b)))
        d = evklid(a-b, n)
        if d > 1 and d < n:
            print(d)
            return 0
        elif d == n:
            print('Делитель не найден')
            return 0

def second():
    n = int(input('Введите n: '))
    a = random.randint(2, n-2)
    b = base()
    for i in range(1000):
        l = int(math.log(i+1)//math.log(b[i]))
        a = pow(a, b[i]**l, n)
    d = evklid(a-1, n)
    if d == 1 or d == n:
        print('Делитель не найден')
        return 0
    else:
        print(d)

er=0
flag = True
while flag:
    flag2 = True
    try:
        print("\nГлавное меню:")
        choice = int(input("\n1) ρ-метод Полларда\n2) ρ-1 -метод Полларда\
            \n3) Выйти из программы\nВыбор: "))
        if choice==1: 
            first()
        elif choice==2:
            second()
        elif choice == 3:
            flag = False
            break
        else:
            print("Ошибка ввода\n")
            er+=1
            if er > 2:
                print("Слишком много попыток")
                flag = False
                break  
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
    except SyntaxError:
        print("SyntaxError")