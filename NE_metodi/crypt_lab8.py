from Crypto.Util import number
import SHA
import random

def NOD(a, b):
    #генерация образующего элемента
    if a < b:
        return NOD(b, a)
    elif a % b == 0:
        return b;
    else:
        return NOD(b, a % b)

def gen_keys():
    p = number.getPrime(256, None)
    alpha = random.randint(2, p)
    while NOD(p, alpha) != 1:
        alpha = random.randint(pow(2, p))
    a = random.randint(1, p-2)
    beta = pow(alpha, a, p)
    
    with open("privat.txt","w",encoding="UTF-8") as prifile:
        prifile.write(str(a))
    with open("publick.txt","w",encoding="UTF-8") as pubfile:
        pubfile.write(str(alpha)+'\n'+str(beta)+'\n'+str(p))

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
    return x % c

def gamal():
    mes = 'hello'
    hesh = int(SHA.sha256(mes), base=16)
    with open("privat.txt","r") as prifile:
        a = int(prifile.read())
    with open("publick.txt","r") as pubfile:
        alpha, beta, p = pubfile.read().split('\n')
    alpha, beta, p = int(alpha), int(beta), int(p)
    r = random.randint(1, p-2)
    while NOD(r, p-1)!=1:
        r = random.randint(1, p-2)
    gamma = power(alpha, r, p)
    r2 = pow(r, -1, p-1)
    delta = ((hesh-alpha*gamma)*r2)%(p-1)

    print('beta*gamma=', power(beta, gamma, p);'gamma*delta=', power(gamma, delta, p))
    print(power(beta, gamma, p)*power(gamma, delta, p)%p, '==', power(alpha, hesh, p))
    
    if power(beta, gamma, p)*power(gamma, delta, p)%p==power(alpha, hesh, p):
        print("true")
    else:
        print("lol")

gen_keys()
gamal()