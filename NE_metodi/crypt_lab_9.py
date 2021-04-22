import Keys
import random
import SHA
import Stribog as STR
import os
from datetime import date

def convert_base(num, to_base, from_base):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def Pim(ai,si,n):
    pim=1
    for i in range (0,len(ai)):
        aisi=pow(int(ai[i]),int(si[i]),int(n))
        pim=pim*aisi
    return pim


def FBI_OPEN_UP(m=512):
    PKS=list()
    with open("publick.txt","r") as priv:
        Bi=priv.read().split("\n")
        n=Bi[1]
        Bi=Bi[0].split()
    with open("Cp.txt","r") as priv:
        s=priv.read().split()
        t=s[1]
        s=s[0]
    with open("Cp_Document.txt","r") as Cp_D:
        for i in Cp_D:
            PKS.append(i)
    M=PKS[13]
    w=int(t)*int(t)
    j=1
    i=0
    k=0
    z=Pim(Bi,s,n)
    w=int((w*z)%int(n))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(w)
    H=SHA.sha512(str(M)+str(w))
    H = str(convert_base(H, 2, 16))
    while len(H)!=512:
        H="0"+H
    print(len(s))
    print(len(H))
    print("s = "+str(s))
    print("s'= "+str(H))
    if s==H:
        print(True)
    else:
        print(False)

def Cp(Bi,n,Ai,M):
    n=int(n)
    r=random.randint(1,n)
    u=pow(r,2,n)
    H=SHA.sha512(str(M)+str(u))
    s=convert_base(H, 2, 16)
    while len(s)!=512:
        s="0"+s
    z=1
    print("s  = " + str(len(s)))
    print(u)
    z=Pim(Ai,s,n)
    t=int((r*z))
    with open("Cp.txt","w") as cp:
        strin=str(s)+" "+str(t)
        cp.write(strin)
    return s

flag = True
mes = ""
H = ""
type=0

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
        type=Keys.gen_keys()
    elif point == "3" and mes != "" and type!=0:
        flag_3 = True
        while flag_3:
            type_hesh = input("Выберите тип хеширования, для уменьшения размера ЦП\n>> SHA - 1\n>> STR - 2\n>>> ")
            if type == 256 and type_hesh=="1":
                H = "1"
                flag_3 = False
            elif type == 512 and type_hesh=="1":
                H = "2"
                flag_3 = False
            elif type == 256 and type_hesh=="2":
                H = "3"
                flag_3 = False
            elif type == 512 and type_hesh=="2":
                H = "4"
                flag_3 = False
            else:
                print("\nError. Bad input. Try more\n")
        try:
            print("\nstart read pub\priv")
            with open("privat.txt", "r") as pub_k:
                Ai=pub_k.read().split("\n")
                Ai=Ai[0].split()
            with open("publick.txt", "r") as pub_k:
                Bi = pub_k.read().split("\n")
                n = Bi[1]
                Bi = Bi[0].split()
                PKCS_7[3] = str(n)
        except FileNotFoundError:
            print("Need generate keys. Please, do it and try later\n")
            break
        print("\nstart cp\priv")
        cp = Cp(Bi,n,Ai,mes)
        PKCS_7[6] = input("Enter you Name and Fname pleas ( Name Fname)\n>> ")
        SignVal = hex(int(cp))
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
        print("\nE1rror. Bad input. Try more\n")

