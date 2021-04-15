import os
from Crypto.Util import number
import SHA
import random
import Stribog as STR
from datetime import date

def NOD(a, b):
    #генерация образующего элемента
    if a < b:
        return NOD(b, a)
    elif a % b == 0:
        return b;
    else:
        return NOD(b, a % b)

def gen_alpha(p):
    gen_fielde = []
    for i in range(2, p):
        rang = [x for x in range(1, p)]
        for j in range(p):
            elem = i**j%p
            if elem in rang:
                rang.remove(elem)
        if len(rang)==0:
            gen_fielde.append(i)
    return gen_fielde[random.randrange(0,len(gen_fielde),1)]


def gen_keys():
    p = number.getPrime(10, None)
    alpha = gen_alpha(p)
    #alpha = random.randint(2, p)
    #while NOD(p, alpha) != 1:
    #    alpha = random.randint(pow(2, p))
    a = random.randint(1, p-2)
    beta = pow(alpha, a, p)
    
    with open("privat.txt","w",encoding="UTF-8") as prifile:
        prifile.write(str(a))
    with open("publick.txt","w",encoding="UTF-8") as pubfile:
        pubfile.write(str(alpha)+'\n'+str(beta)+'\n'+str(p))

def gamal(hesh, a, alpha, beta, p):
    hesh, a, alpha, beta, p = int(hesh, base=16), int(a), int(alpha), int(beta), int(p)
    r = random.randint(1, p-2)
    while NOD(r, p-1)!=1:
        r = random.randint(1, p-2)
    gamma = pow(alpha, r, p)
    r2 = pow(r, -1, p-1)
    delta = ((hesh-a*gamma)*r2)%(p-1)
    with open("ЦП.txt","w") as cpp:
        cpp.write(str(gamma) + ' ' + str(delta))
    return str(gamma) + ' ' + str(delta)

def FBI_OPEN_UP():
    cp_list = []
    with open("ЦП.txt","r") as prifile:
        gamma, delta = (prifile.read().split())
    with open("Cp_Document.txt","r") as pubfile:
        cp_list = pubfile.read().split('\n')
    hm = cp_list[1]
    alpha, beta, p = cp_list[3].split()
    mes = cp_list[13]
    alpha, beta, p, gamma, delta = int(alpha), int(beta), int(p), int(gamma), int(delta)
    if PKCS_7[1] == hm:
        hesh = int(SHA.sha256(mes), base=16)
    elif PKCS_7[1] == hm:
        hesh = int(SHA.sha512(mes), base=16)
    elif PKCS_7[1] == hm:
        hesh = int(STR.Stribog(mes, 256), base=16)
    elif PKCS_7[1] == hm:
        hesh = int(STR.Stribog(mes, 512), base=16)
    print(pow(beta, gamma, p)*pow(gamma, delta, p)%p, '==', pow(alpha, hesh, p))
    if pow(beta, gamma, p)*pow(gamma, delta, p)%p==pow(alpha, hesh, p):
        print("true")
    else:
        print("false")
    

flag = True
mes = ""
H = ""
PKCS_7 = [1, "DigAlId", "Document", "Open_Key", "None", 1, "FIO", "Dig_AlId2", "None", "RSAdsi", "SignatureValue",
          "TimeStamp", "SetOfAtributeValue"]
while flag:
    point = str(input(
        "Step 1\n>> Give message - 1\n>> Create keys - 2\n>> Generate ЦП and Подписать указанный ранее документ - 3\n>> Check CP - 4\n>> Exit - 5\n>>> "))
    if point == "1":
        flag_1 = True
        while flag_1:
            choose = str(input(">> Only from file - 1\n>> Exit - 2\n"))
            if choose == "1":
                while True:
                    way = input("Enter file path\n(end on .txt)\n")
                    if os.path.isfile(way) and way[-4:] == ".txt":
                        with open(way, 'r') as file:
                            mes = file.read()
                        flag_1 = False
                        break
                    else:
                        print("Error - incorrect path\n")
            elif choose == "2":
                flag_1 = False
                break
    elif point == "2":
        gen_keys()
    elif point == "3" and mes != "":
        flag_3 = True
        while flag_3:
            type = str(input(
                "Выберите тип хеширования, для уменьшения размера ЦП\n>> SHA 256 - 1\n>> SHA 512 - 2\n>> STR 256 - 3\n>> STR 512 - 4\n>>> "))
            if type == "1":
                H = SHA.sha256(mes)
                PKCS_7[1] = "SHA256"
                PKCS_7[7] = "SHA256"
                flag_3 = False
            elif type == "2":
                H = SHA.sha512(mes)
                PKCS_7[1] = "SHA512"
                PKCS_7[7] = "SHA512"
                flag_3 = False
            elif type == "3":
                H = STR.Stribog(mes, 256)
                PKCS_7[1] = "STR256"
                PKCS_7[7] = "STR256"
                flag_3 = False
            elif type == "4":
                H = STR.Stribog(mes, 512)
                PKCS_7[1] = "STR512"
                PKCS_7[7] = "STR512"
                flag_3 = False
            else:
                print("\nError. Bad input. Try more\n")
        try:
            print("\nstart read pub\priv")
            with open("privat.txt","r") as prifile:
                a = int(prifile.read())
            with open("publick.txt","r") as pubfile:
                alpha, beta, p = pubfile.read().split('\n')
            PKCS_7[3] = alpha + " " + beta + " " + p
            
        except FileNotFoundError:
            print("Need generate keys. Please, do it and try latter\n")
            break
        print("\nstart cp\priv")
        cp = gamal(H, a, alpha, beta, p)
        PKCS_7[6] = input("Enter you Name and Fname pleas ( Name Fname)\n>> ")
        cp=cp.split()
        SignVal = hex(int(cp[0]))
        SignVal=SignVal+" "+hex(int(cp[1]))
        cp=SignVal
        PKCS_7[10] = SignVal[2:]
        PKCS_7[11] = date.today()
        if PKCS_7[1] == "SHA256":
            PKCS_7[12] = SHA.sha256(mes + cp)
        elif PKCS_7[1] == "SHA512":
            PKCS_7[12] = SHA.sha512(mes + cp)
        elif PKCS_7[1] == "STR256":
            PKCS_7[12] = STR.Stribog(mes + cp, 256)
        elif PKCS_7[1] == "STR512":
            PKCS_7[12] = STR.Stribog(mes + cp, 512)
        with open("Cp_Document.txt", "w") as doc:
            for i in PKCS_7:
                stri = ""
                stri = stri + str(i) + "\n"
                doc.write(stri)
            doc.write(mes)
    elif point == "4":
        FBI_OPEN_UP()
    elif point == "5":
        flag = False
        break
    else:
        print("\nError. Bad input. Try more\n")