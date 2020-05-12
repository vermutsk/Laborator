from abc import ABC, abstractmethod
import random

class AbstractClass(ABC):

    @abstractmethod
    def encrypt(self, text_filename: str, key_filename: str, **args):
        print('yes')
        raise Exception

    @abstractmethod
    def decrypt(self, **args):
        encrypt_filename=self.encrypt_open
        print(encrypt_filename)
        key_filename=self.key_open
        print(key_filename)
        '''raise Exception'''

    @abstractmethod
    def gen_key(self, **args):
        flag1=True
        while flag1:
            way=input("Введите путь для создания файла ключа: ")
            try:
                if way.endswith(".key"):
                    key_fileway=way
                else:
                    print("Неправильный тип файла")
                with open(key_fileway, "x", encoding="utf-8") as key_file:
                    key_file.write("Test string") 
            except Exception:
                print("Ошибка в пути файла")
            
        raise Exception
    

    ###########################################################


    def _test_way(self, file):
        flag1=True
        while flag1:
            way=input(f"Введите путь к {file} файлу: ")
            try:
                if way.endswith(f".{file}"):
                    pass
                else:
                    print("Неправильный тип файла")
                return way 
            except Exception:
                print("Ошибка в пути файла")

    def _read_text(self):
        way=self._test_way('txt')
        with open(way, "r", encoding="utf-8") as text_file:
            text_filename=[]
            for line in text_file:
                str0=list(line)
                text_filename.extend(str0)
            if len(text_filename)!=0:
                return text_filename
            else:
                print("Пустой файл")

    def encrypt_open(self):
        way=self._test_way('encrypt')
        with open(way, "r", encoding="utf-8") as text_file:
            text_filename=[]
            for line in text_file:
                str0=list(line)
                text_filename.extend(str0)
            if len(text_filename)!=0:
                return text_filename
            else:
                print("Пустой файл")


    def key_open(self, crypt):
        way=self._test_way('key')
        with open(way, "r", encoding="utf-8") as key_file:
            key_list=[]
            for line in key_file:
                key_str=line.rstrip('\n')
                key_list.append(key_str)
            if key_list[0]==crypt:
                pass
            else:
                print("Файл ключа для другого метода")    
        return key_list


    def alp_open(self):
        way=self._test_way('alph')
        try:
            with open(way, "r", encoding="utf-8") as alph_file:
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
                if len(alph_list1)==0:
                    print("В файле алфавита нет подходящих значений")
        except FileNotFoundError:
            print("Файл алфавита не найден")            
        return alph_list1
#########################################


class ChangeEncrypt(AbstractClass):
    
    def __init__(self):
        self.crypt='шифр замены'

    def encrypt(self, **args):
        pass

    def decrypt(self, **args):
        pass

    def gen_key(self, **args):
        alph_list=self.alp_open()
        alph_dict={}
        alph_dict['alp']=alph_list
        print(alph_dict)

    def _read_encrypt(self):
        pass

    def _read_key(self):
        pass

class ReplaceEncrypt(AbstractClass):
    def __init__(self):
        self.crypt='шифр перестановки'

    def encrypt(self, **args):
        pass

    def decrypt(self, **args):
        pass

    def gen_key(self, **args):
        len_crypt=int(input("Введите длину блока: "))
        return len_crypt

    def _read_encrypt(self):
        pass

    def _read_key(self):
        """метод для чтения ключа
        key_filename -- имя файла для чтения
        """
        pass

class GammEncrypt(AbstractClass):
    def __init__(self):
        self.crypt='шифр гамирования'

    def encrypt(self, **args):
        pass

    def decrypt(self, **args):
        pass

    def gen_key(self, **args):
        alph_list=self.alp_open()
        len_alph=len(alph_list)
        len_crypt=int(input("Введите длину блока: "))

    def _read_encrypt(self):
        way=self._test_way('encrypt')
        return way

    def _read_key(self):
        """метод для чтения ключа
        key_filename -- имя файла для чтения
        """
        pass
change=ChangeEncrypt()
replace=ReplaceEncrypt()
gamm=GammEncrypt()
########

flag=True
while flag:
    flag2=True
    try:
        print("\nГлавное меню:")
        choice=int(input("\n1) Зашифровать\n2) Расшифровать\n3) Сгенерировать ключ\n4) Выйти из программы\nВыбор: "))
        if choice==1:       
            while flag2:
                choice1=int(input("\nВыберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4)Вернуться в главное меню\nВыбор: "))
                if choice1!=1 and choice1!=2 and choice1!=3:
                    print("Ошибка ввода")
                elif choice1==4:
                    flag2==False
                    break
                if choice1==1:
                    change.encrypt()
                elif choice1==2:
                    replace.encrypt()
                elif choice1==3:
                    gamm.encrypt()       

        elif choice==2:     
            while flag2:
                choice1=int(input("\nВыберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4)Вернуться в главное меню\nВыбор: "))
                if choice1!=1 and choice1!=2 and choice1!=3:
                    print("Ошибка ввода")
                elif choice1==4:
                    flag2==False
                    break
                if choice1==1:
                    change.decrypt()
                elif choice1==2:
                    replace.decrypt()
                elif choice1==3:
                    gamm.decrypt()                  
                
        elif choice==3:     
            while flag2:
                choice1=int(input("\nСгенерировать ключ для следующего алгоритма: \n1) Шифр замены\n2) Шифр перестановки\n3) Шифр гамирования\n4) Вернуться в главное меню\nВыбор: "))
                if choice1!=1 and choice1!=2 and choice1!=3:
                    print("Ошибка ввода")
                elif choice1==4:
                    flag2==False
                    break     
                if choice1==1:
                    change.gen_key()    
                elif choice1==2:
                    replace.gen_key()    
                elif choice1==3:
                    gamm.gen_key()

        elif choice==4:
            flag==False
            break
        else:
            print("Ошибка ввода\n")
    except ValueError:
        pass
    except SyntaxError:
        print("Wrong command")
    except UnboundLocalError:
        print("UnboundLocalError")
    except FileNotFoundError:
        print("File not found")                     
    except FileExistsError:
        print("Файл с таким именем уже существует")