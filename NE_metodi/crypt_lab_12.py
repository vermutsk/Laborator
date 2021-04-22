import pyAesCrypt
import os
import random
import time


def remove_file(file: str):
    os.remove(file)


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


def step_1(User_A):
    with open("File_A.txt","w") as file:
        file.write(str(User_A))


def step_2(User_B,User_B_id):
    with open("File_A.txt","r") as file:
        rA=file.readline()
    os.remove("File_A.txt")
    # b -> a 
    with open("File_B.txt","w") as file:
        strin=rA+"\n"+str(User_B)+"\n"+User_B_id
        file.write(strin)
    aes_file=AES_encrypt("File_B.txt",key)
    os.remove("File_B.txt")
    return aes_file


def step_3(User_A,User_B_id,aes_file):
    AES_decrypt(aes_file,"File_A_From_B.txt",key)
    strin=list()
    with open("File_A_From_B.txt","r") as file:
        strin=file.read()
    strin=strin.split("\n")
    os.remove(aes_file)
    os.remove("File_A_From_B.txt")
    
    if User_A==int(strin[0]) and User_B_id==strin[2]:
        print("User A: the user B identity is verified\n")
    with open("File_B_From_A.txt","w") as file:
        file.write(strin[1]+"\n"+strin[0]+"\n"+User_A_id)
    aes_file=AES_encrypt("File_B_From_A.txt",key)
    os.remove("File_B_From_A.txt")
    return aes_file


def step_4 (User_B,User_A_id,aes_file):
    #step 4 for B
    AES_decrypt(aes_file,"File_B_From_A_From_B.txt",key)
    os.remove(aes_file)
    with open("File_B_From_A_From_B.txt","r") as file:
        strin=file.read()
    strin=strin.split("\n")
    if User_B==int(strin[0]) and User_A_id==strin[2]:
        print("User B: the user B identity is verified\n")
    os.remove("File_B_From_A_From_B.txt")


key = gen_key(256)
User_A=random.randint(5,pow(2,32))
User_B=random.randint(5,pow(2,32))
User_A_id="id_001"
User_B_id="id_002"

step_1(User_A)
aes_file=step_2(User_B,User_B_id)
aes_file=step_3(User_A,User_B_id,aes_file)
step_4(User_B,User_A_id,aes_file)