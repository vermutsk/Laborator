import random
from math import log
flag = True
def miller(n):
    a = random.randint(2, n-2)
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

while flag:
    p = int(input('Введите p: '))
    if miller(p) == True:
        flag = False
    else:
        print('p не является простым')
flag = True
while flag:
    a = int(input('Введите a: '))
    b = int(input('Введите p: '))
    if b > 1 and b < p:
        flag = False
    else:
        print('b не лежит в интервале 1<b<p')
flag = True
while flag:
        function = input('Введите f(x): ')
        if function.find('x')!=-1:
            function = function.replace('x', '{}')
            flag = False
        else:
            print('Некорректная функция')
u = 2
v = 2
c = (a**u)*(b**v)%p
d = c
c = eval(function.format(c))%p
d = eval(function.format(function.format(d)))%p


