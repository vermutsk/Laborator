import json
print("Главное меню:")
choice=int(input("1) Зашифровать\n2) Расшифровать\n3) Сгенерировать ключ\nВыбор: ")) 
if choice==1:
    choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\nВыбор: "))
    if choice1==1:
        crypt='шифр замены'
    elif choice1==2:
        crypt='шифр перестановки'
    elif choice1==3:
        crypt='шифр гамирования'
    else:
        print("Ошибка")
    way=input("Введите путь к файлу текста: ")
    if way.endswith(".txt"):
        text_filename=way
    else:
        print("Неправильный формат файла")
    key=input("Введите путь к файлу ключа: ")
    if key.endswith(".key"):
        key_filename=key
    else:
        print("Неправильный формат файла")
    with open(key_filename, "r") as key_file:
        data = json.load(key_file)
        if data['alg_type']==crypt:
            print(crypt)
        else:
            print("Неправильный файл ключа")
elif choice==2:
    choice2=int(input("Выберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\nВыбор: "))
    if choice2==1:
        crypt='шифр замены'
    elif choice2==2:
        crypt='шифр перестановки'
    elif choice2==3:
        crypt='шифр гамирования'
    else:
        print("Ошибка")
    way1=input("Введите путь к файлу шифротекста: ")
    if way1.endswith(".encode"):
        crypt_text_filename=way1
    else:
        print("Неправильный формат файла")
    key=input("Введите путь к файлу ключа: ")
    if key.endswith(".key"):
        key_filename=key
    else:
        print("Неправильный формат файла")
    with open(key_filename, "r") as key_file:
        data = json.load(key_file)
        if data['alg_type']==crypt:
            print(crypt)
        else:
            print("Неправильный файл ключа")

elif choice==3:
    choice3=int(input("Сгенерировать ключ для следующего алгоритма: \n1) Шифр замены\n2) Шифр перестановки\n3) Шифр гамирования\nВыбор: "))
    if choice3==1:
        way2=input("Введите путь к файлу алфавита: ")
        if way1.endswith(".alph"):
            alph_filename=way2
    else:
        print("Неправильный формат файла")   
else:
    print('no')

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def encrypt(
            self,
            text_filename: str,
            key_filename: str,
            **args) -> bool:
        
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    @abstractmethod
    def decrypt(
            self,
            encrypted_filename: str,
            key_filename: str,
            **args) -> bool:
        
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    @abstractmethod
    def gen_key(self, **args) -> bool:
        raise Exception("Данный метод переопределяется в дочернем классе.\
             Его логика уникальная для каждого отдельного класса.")

    def _read_text(self, text_filename: str) -> bool:
        raise Exception("Данный метод реализуется в этом классе.\
                         Его логика не меняется для всех классов.")
