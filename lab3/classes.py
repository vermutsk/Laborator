from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def encrypt(self,text_filename: str,key_filename: str, **args) -> bool:
        '''
        шифрование файла по ключу
        text_filename -- имя файла для зашифрования
        key_filename -- имя файла ключа
        '''
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    @abstractmethod
    def decrypt(self,encrypted_filename: str,key_filename: str,**args) -> bool:
        '''
        расшифрование файла по ключу
        encrypted_filename -- имя файла для расшифрования
        key_filename -- имя файла ключа
        '''
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






class Ways():
    def __init__(self, way):
        self.way=way
    def file_way(self, *args):
        if self.way.endswith(".txt"):
            text_filename=self.way
            print(text_filename)
        else:
            print("Неправильный формат файла")

class Ways1():
    def __init__(self, key):
        self.key=key
    def file_way1(self, *args):
        if self.key.endswith(".key"):
            key_filename=self.key
            print(key_filename)
        else:
            print("Неправильный формат файла")

class Open_files(Ways1):
    key_list=[]
    def __init__(self, crypt, key_filename):
        self.key_filename=key_filename
        self.crypt=crypt
    def open_file(self, *args):
        with open(self.key_filename, "r", encoding="utf-8") as key_file:
            for line in key_file:
                key_str=line.rstrip('\n')
                self.key_list.append(key_str)
                if self.key_list[0]==self.crypt:
                    print(self.crypt)
                else:
                    print("Неправильный файл ключа")
