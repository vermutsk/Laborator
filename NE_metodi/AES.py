import pyAesCrypt
import os
import random
import time


def remove_file(file: str):
    os.remove(file)


def AES_encrypt(file_txt: str, key: str, buffsize=512 * 1024):
    # 1. Файл который шифруется,
    # 2. Ключ по которому шифруют,
    # 3. (Стандартное значение 512 * 1024) Буфер
    file_aes = file_txt + '.aes'  # Зашифрованный файл
    pyAesCrypt.encryptFile(file_txt, file_aes, key, buffsize)
    return file_aes


def AES_decrypt(file_aes: str, file_txt: str, key: str, buffsize=512 * 1024):
    # 1. Файл который рашифровываеться,
    # 2. Файл куда записываеться расшифрованный текст
    # 3. Ключ по которому расшифровывают,
    # 4. (Стандартное значение 512 * 1024) Буффер
    # file_txt = file_aes.rstrip('.aes')
    pyAesCrypt.decryptFile(file_aes, file_txt, key, buffsize)
    return file_txt


def gen_key(size):
    # 1. Размер ключа в битах
    key = random.getrandbits(size)
    key = bin(key)[2:]
    return key


def timestamp():
    stamp = str(time.time())
    stamp = stamp.split('.')
    stamp = ''.join(x for x in stamp)
    return stamp


if __name__ == '__main__':
    print('This is module for crypt by AES')
