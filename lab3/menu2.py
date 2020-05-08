from abc import ABC, abstractmethod

class MyAbstractClass(ABC):

    @abstractmethod
    def encrypt(self, text_filename: str, key_filename: str, **args):
        print('yes')
        raise Exception

    @abstractmethod
    def decrypt(self,encrypted_filename: str,key_filename: str,**args):
        print('yes')
        raise Exception

    @abstractmethod
    def gen_key(self, **args):
        print('yes')
        raise Exception
    
    def _read_text(self, text_filename: str):
        with open(text_filename, "r", encoding="utf-8") as text_file:
            text_filename=[]
            for line in text_file:
                str0=list(line)
                text_filename.extend(str0)
            if len(text_filename)!=0:
                print(text_filename)
        raise Exception


class ChangeEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self, text_filename: str,key_filename: str,**args):
        print("yes")

    def decrypt(self, encrypted_filename: str, key_filename: str,**args):
        pass

    def gen_key(self, **args):
        pass

    def _read_encrypt(self, encrypted_filename: str):
        pass

    def _read_key(self, key_filename: str):
        pass


def test():
    if fileway.endswith(f".{file}"):
        pass
    else:
        raise Exception
    return fileway

def key_open(crypt):
    with open(fileway, "r", encoding="utf-8") as key_file:
        key_list=[]
        for line in key_file:
            key_str=line.rstrip('\n')
            key_list.append(key_str)
            if key_list[0]==crypt:
                pass
            else:
                raise Exception
    return key_list

def choiced():
    if choice1==1:
        crypt='шифр замены'
        key_open(crypt)
    elif choice1==2:
        crypt='шифр перестановки'
        key_open(crypt)
    elif choice1==3:
        crypt='шифр гамирования'
        key_open(crypt)
    return crypt

def alp_test():
    with open(fileway, "r", encoding="utf-8") as alph_file:
        alph_list=[]
        alph_list1=[]
        for line in alph_file:
            alph_str=line.rstrip('\n')
            if len(alph_str)!=1:
                pass
            else:
                alph_list.append(alph_str)
        def no_repeat(alph_list):
            for z in alph_list:
                if z not in alph_list1:
                    alph_list1.append(z)
            return alph_list1
        no_repeat(alph_list)
    return alph_list1

flag=True
while flag:
    print("Главное меню:")
    choice=int(input("1) Зашифровать\n2) Расшифровать\n3) Сгенерировать ключ\nВыбор: ")) 
    
    '''Зашифровать'''
    if choice==1: 
        choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\nВыбор: "))
        if choice1==1 or choice1==2 or choice1==3:
            file="txt"
            fileway=input("Введите путь к файлу текста: ")
            test()
            text_filename=fileway
            file="key"
            fileway=input("Введите путь к файлу ключа: ")
            test()
            key_filename=fileway
            choiced()
        else:
            raise Exception
        if choice1==1:
            change=ChangeEncrypt()
            change._read_text(text_filename)
            change.encrypt(text_filename,key_filename)
    
        '''Расшифровать'''        
    elif choice==2:
        choice1=int(input("Выберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\nВыбор: "))
        if choice1==1 or choice1==2 or choice1==3:
            file="encode"
            fileway=input("Введите путь к файлу шифротекста: ")
            test()
            encrypted_filename=fileway
            file="key"
            fileway=input("Введите путь к файлу ключа: ")
            test()
            key_filename=fileway
            choiced()
        else:
            raise Exception
    
        '''Сгенерировать ключ'''
    elif choice==3:
        choice3=int(input("Сгенерировать ключ для следующего алгоритма: \n1) Шифр замены\n2) Шифр перестановки\n3) Шифр гамирования\n4) Вернуться в главное меню\nВыбор: "))
        file="key"
        fileway=input("Введите путь для создания файла ключа: ")
        test()
        key_fileway=fileway
        if choice3==1:
            file="alph"
            fileway=input("Введите путь к файлу алфавита: ")
            test()
            alph_list1=alp_test()
            alph_dict={}
            alph_dict['alp']=alph_list1

        elif choice3==2:
            len_crypt=int(input("Введите длину блока: "))

        elif choice3==3:
            file="alph"
            fileway=input("Введите путь к файлу алфавита: ")
            test()
            alph_list1=alp_test()
            len_alph=len(alph_list1)
            len_crypt1=int(input("Введите длину блока: "))
        else:
            raise Exception         
        with open(key_fileway, "x", encoding="utf-8") as key_file:
            key_file.write("Test string")
            key_file.close()
    else:
        raise Exception
