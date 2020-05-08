from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def encrypt(self,text_filename: str,key_filename: str, **args) -> bool:
        
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    @abstractmethod
    def decrypt(self,encrypted_filename: str,key_filename: str,**args) -> bool:
        
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    @abstractmethod
    def gen_key(self, **args) -> bool:
        """генерация ключа"""
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    def _read_text(self, text_filename: str) -> bool:
        """общий метод для чтения текстового файла"""
        raise Exception("Данный метод реализуется в этом классе.\
                         Его логика не меняется для всех классов.")





class ChangeEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self, text_filename: str,key_filename: str,**args) -> bool:
        pass

    def decrypt(self, encrypted_filename: str, key_filename: str,**args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self, encrypted_filename: str) -> bool:
        """прочитать защифрованный файл
        encrypted_filename -- имя файла для чтения
        """
        pass

    def _read_key(self, key_filename: str) -> bool:
        """метод для чтения ключа
        key_filename -- имя файла для чтения
        """
        pass

class ReplaceEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self, text_filename: str,key_filename: str,**args) -> bool:
        pass

    def decrypt(self, encrypted_filename: str, key_filename: str,**args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self, encrypted_filename: str) -> bool:
        """прочитать защифрованный файл
        encrypted_filename -- имя файла для чтения
        """
        pass

    def _read_key(self, key_filename: str) -> bool:
        """метод для чтения ключа
        key_filename -- имя файла для чтения
        """
        pass

class GammEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self,text_filename: str,key_filename: str,**args) -> bool:
        pass

    def decrypt(self,encrypted_filename: str,key_filename: str,**args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self, encrypted_filename: str) -> bool:
        """прочитать защифрованный файл
        encrypted_filename -- имя файла для чтения
        """
        pass

    def _read_key(self, key_filename: str) -> bool:
        """метод для чтения ключа
        key_filename -- имя файла для чтения
        """
        pass


'''Шифр Виженера = гамирования'''


def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict() 

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 

def full_encode(value, key):
    dic = comparator(value, key)
    print('Compare full encode', dic)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code

def full_decode(value, key):
    dic = comparator(value, key)
    print('Deshifre=', dic)
    d = form_dict() 
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis  


