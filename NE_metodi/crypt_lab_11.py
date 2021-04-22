
import pyAesCrypt
import os
import random
from datetime import datetime


def AES_encrypt(file_txt: str, key: str, buffsize=512 * 1024):
    file_aes = file_txt + '.aes'  # Зашифрованный файл
    pyAesCrypt.encryptFile(file_txt, file_aes, key, buffsize)
    return file_aes


def AES_decrypt(file_aes: str, file_txt: str, key: str, buffsize=512 * 1024):
    pyAesCrypt.decryptFile(file_aes, file_txt, key, buffsize)


def gen_key(size):
    key = random.getrandbits(size)
    key = bin(key)[2:]
    return key


def step_1(marker, User_A):
    with open("File_A.txt","x") as file:
        strin=marker + "\n" + str(User_A)
        file.write(strin)
    aes_file=AES_encrypt("File_A.txt",key)
    os.remove("File_A.txt")
    return aes_file


def step_2(User_A,marker,aes_file):
    AES_decrypt(aes_file,"File_B_From_A.txt",key)
    strin=list()
    with open("File_B_From_A.txt","r") as file:
        strin=file.read()
    strin=strin.split("\n")
    os.remove(aes_file)
    os.remove("File_B_From_A.txt")
    if User_A==strin[1] and marker==strin[0]:
        print("User B: the user A identity is verified\n")
    with open("File_A_From_B.txt","w") as file:
        file.write(strin[0]+"\n"+User_B)
    aes_file=AES_encrypt("File_A_From_B.txt",key)
    os.remove("File_A_From_B.txt")
    return aes_file


def step_3 (User_B,marker,aes_file):
    #step 4 for B
    AES_decrypt(aes_file,"File_A_From_B_From_A.txt",key)
    os.remove(aes_file)
    with open("File_A_From_B_From_A.txt","r") as file:
        strin=file.read()
    strin=strin.split("\n")
    if User_B==strin[1] and marker==strin[0]:
        print("User A: the user B identity is verified\n")
    os.remove("File_A_From_B_From_A.txt")


key = gen_key(256)

User_A="id_001"
User_B="id_002"


while True:
    print('>>Выберите идентификатор<<: \n1. Метка врeмени \n2. Случайное число \n3. Выход')
    choose = input('>>')
    if choose == '1':
        marker = datetime.now()
        marker = str(marker)
        marker = marker.replace(':', '').replace('-', '').replace(' ', '')[2:].split('.')[0]
        print("Метка создана")
    elif choose == "2":
        marker=str(random.randint(5,pow(2,32)))
        print("Число создано")
    elif choose == '3':
        break
    else:
        print("Неправильно введена команда\n")
        continue
    aes_file=step_1(marker, User_A)
    aes_file=step_2(User_A,marker,aes_file)
    step_3(User_B,marker,aes_file)
