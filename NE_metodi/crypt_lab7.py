import Stribog as STR
import SHA
import RSA
import os
from random import randint
from bitstring import BitArray
from datetime import date


def Key():
    notsecret = os.urandom(randint(5, 6415))
    # notsecret = BitArray(hex=notsecret)
    # notsecret=notsecret.bin[2:]
    with open("NotKey.jspy", "w") as notkeyfile:
        notkeyfile.write(str(notsecret))
    return notsecret


def FBI_OPEN_UP():
    flag = True
    PKCS_7 = ""
    sor=""
    while flag:
        task = input("Pleas enter file with cp with .txt\n>> ")
        try:
            with open(task, "r") as cp_file:
                PKCS_7 = cp_file.read().split("\n")
            with open("ЦП.txt", "r") as cp_file:
                sor = cp_file.read()
                flag = False
                break
        except FileNotFoundError:
            print("cant find file, please try new name write\n")
    mes = PKCS_7[13]
    s = int(PKCS_7[10], 16)
    e = PKCS_7[3].split()
    n = e[1]
    e = e[0]
    if PKCS_7[1] == "SHA256":
        hm = SHA.sha256(mes)
    elif PKCS_7[1] == "SHA512":
        hm = SHA.sha512(mes)
    elif PKCS_7[1] == "STR256":
        hm = STR.Stribog(mes, 256)
    elif PKCS_7[1] == "STR512":
        hm = STR.Stribog(mes, 512)
    hmshtrix = pow(s, int(e), int(n))
    print("\nResult - " + "None\n" + "Algorithm hash - " + PKCS_7[2] + "\nAlgoritm CP - " + PKCS_7[9] + "\nAuthor - " +
          PKCS_7[6] + "\nTime create CP - " + PKCS_7[11] + "\n")
    print("ЦП = " + str(sor))
    print("Cp_s = " + str(s))
    # print("NC = "+str(hex(int(hmshtrix))))
    print("NC = " + str(int(hmshtrix)))



def mes_b(mes, b):
    M = []
    for x in range(b):
        m0 = []
        for y in range(16):
            j = res[:64]
            res = res[64:]
            m0.append(j)
        M.append(m0)


def fast_fast_pow(a, s, n):  # x ^^ mod
    y = 1
    x = 1
    j = n
    if s % 2 != 0:
        y = a
        s = s - 1
    while (s != 1):
        a = a * a
        s = int(s / 2)
    a = a * y
    x = a % n
    print(x)


def mes_ord(mes):
    m = [0] * len(mes)
    for i in range(0, len(mes)):
        m[i] = ord(mes[i])
    return m


def Cp(hm_0: str, d, e, n):
    hm = int(hm_0, base = 16)
    print("\nstart s\priv")
    s = pow(hm, int(d),n)
    #s = powe % n  # n - ?
    print("\nstart write cp\priv")
    with open("ЦП.txt", "w") as cp:
        cp.write(str(s))
    return str(s)


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
        RSA.generate_keys()
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
            with open("private.txt", "r") as pub_k:
                d = float(pub_k.readline())
            with open("publick.txt", "r") as pub_k:
                e = int(pub_k.readline())
                n = int(pub_k.readline())
                PKCS_7[3] = str(e) + " " + str(n)
        except FileNotFoundError:
            print("Need generate keys. Please, do it and try latter\n")
            break
        print("\nstart cp\priv")
        cp = Cp(H, d, e, n)
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
        print("\nError. Bad input. Try more\n")