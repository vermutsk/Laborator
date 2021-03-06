from abc import ABC, abstractmethod
import random

class AbstractClass(ABC):

    @abstractmethod
    def encrypt(self, **args):
        pass

    @abstractmethod
    def decrypt(self, **args):
        pass

    @abstractmethod
    def gen_key(self, **args):
        pass

    ###################################################################################
    def _test_way(self, file):
        flag = True
        while flag:
            way=input(f"Введите путь к {file} файлу: ")
            try:
                if way.endswith(f".{file}"):
                    flag = False
                    break
                else:
                    print("Неправильный тип файла")
            except Exception:
                print("Ошибка в пути файла")
        return way         

    def _create_file(self, file):
        flag = True
        while flag:
            try:
                way = input(f"Введите путь для создания файла {file}: ")
                if way.endswith(f".{file}"):
                    flag=False
                    break
                else:
                    print("Неправильный тип файла")
            except Exception:
                print("Ошибка в пути файла")
        return way           

    def _text_open(self):
        flag = True
        while flag:
            try:
                way = self._test_way('txt')
                with open(way, "r", encoding="utf-8") as text_file:
                    text_list = []
                    for line in text_file:
                        text_list.extend(list(line))
                    if len(text_list)!=0:
                        flag = False
                        break
                    else:
                        print("Пустой файл")
            except Exception:
                print("Возникла ошибка")
        return text_list

    def _encrypt_open(self, crypt):
        flag = True
        while flag:
            try:
                way = self._test_way('encrypt')
                with open(way, "r", encoding="utf-8") as encrypt_file:
                    encrypt_list = []
                    for line in encrypt_file:
                        key_str = line.rstrip('\n')
                        encrypt_list.append(key_str)
                    if encrypt_list[0] == crypt:
                        encrypt_list.clear()
                        str0 = list(line)
                        encrypt_list.extend(str0)
                        if len(encrypt_list) != 0:
                            flag = False
                            break
                        else:
                            print("Пустой файл")
                    else:
                        print("Файл шифротекста для другого метода")        
            except Exception:
                print("Возникла ошибка")
        return way

    def _key_open(self, crypt):
        flag = True
        while flag:
            try:
                way = self._test_way('key')
                with open(way, "r", encoding="utf-8") as key_file:
                    key_list = []
                    for line in key_file:
                        key_str = line.rstrip('\n')
                        key_list.append(key_str)
                    if key_list[0] == crypt:
                        if len(key_list) != 0:
                            flag = False
                            break
                        else:
                            print("Пустой файл")
                    else:
                        print("Файл ключа для другого метода")    
                    
            except Exception:
                print("Возникла ошибка")
        return way

    def _alp_open(self):
        flag = True
        while flag:
            try:
                alph_list1 = []
                way = self._test_way('alph')
                with open(way, "r", encoding="utf-8") as alph_file:
                    alph_list = []
                    for line in alph_file:
                        alph_str = line.rstrip('\n')
                        if len(alph_str) == 1 and line[0] != '\n':
                            alph_list.append(alph_str)
                        elif len(alph_str) != 1:
                            str0 = alph_str.split()
                            alph_str = ''.join(str0)
                            if len(alph_str) == 1:
                                alph_list.append(alph_str)
                    for z in alph_list:
                        if z not in alph_list1:
                            alph_list1.append(z)
                    if len(alph_list1) == 0:
                        print("В файле алфавита нет подходящих значений/Пустой файл")            
                flag = False
                break
            except Exception:
                print("Возникла ошибка")
        return alph_list1
            
#######################################################################################
class ChangeEncrypt(AbstractClass):

    def encrypt(self, **args):
        key_dict = self.__read_key()
        text_list = self._text_open()
        flag = True
        while flag:
            try:
                encrypt_way = self._create_file('encrypt')
                with open(encrypt_way,'x', encoding='utf-8') as encrypt_file:
                    encrypt_file.write('шифр замены\n')
                    str0=''
                    for k in range(len(text_list)):
                        i=0 
                        for key, value in key_dict.items():
                            i+=1   
                            if text_list[k] == key: 
                                str0 = str0 + f'{value}'
                                break
                            elif i == len(key_dict):
                                str0 = str0 + f'{text_list[k]}'
                                break                      
                    encrypt_file.write(str0)
                    print("\nУспешно")        
                flag = False
                break
            except Exception:
                print("Возникла ошибка")      

    def decrypt(self, **args):
        key_dict = self.__read_key()
        encrypt_list = self.__read_encrypt()
        flag = True
        while flag:
            try:
                text_way = self._create_file('txt')
                with open(text_way,'x', encoding='utf-8') as text_file:
                    str0=''
                    for k in range(len(encrypt_list)): 
                        i=0
                        for key, value in key_dict.items():
                            i+=1   
                            if encrypt_list[k] == value:
                                str0 = str0 + f'{key}'
                                break
                            elif i == len(key_dict):
                                str0 = str0 + f'{encrypt_list[k]}'
                                break          
                    text_file.write(str0)
                    print("\nУспешно")        
                flag=False
                break
            except Exception:
                print("Возникла ошибка")

    def gen_key(self, **args):
        flag1 = True
        while flag1:
            key_fileway = self._create_file('key')    
            alph_list = self._alp_open()
            key_list = random.sample(alph_list, len(alph_list))
            try:
                with open(key_fileway, "x", encoding="utf-8") as key_file:
                    key_file.write('шифр замены')
                    i=0
                    while i < len(alph_list):
                        str0 = '\n' + alph_list[i] + ':' + key_list[i]
                        key_file.write(str0)
                        i+=1
                    flag1 =False
                    print("\nУспешно")
                    break 
            except Exception:
                print("Возникла ошибка")

    def __read_encrypt(self):
        encrypt_file = open(self._encrypt_open('шифр замены'),'r', encoding='utf-8' )
        encrypt_list = []
        i=0
        for line in encrypt_file:
            if i<1:
                i+=1
            else:
                encrypt_list.extend(list(line))
        return encrypt_list   

    def __read_key(self):
        key_filename = self._key_open('шифр замены')
        key_dict = {}
        with open(key_filename,'r', encoding='utf-8') as key_file:
            for line in key_file:
                if line[0] != '\n':
                    key_list = line.split(':',1)
                    if len(key_list) == 1:
                        pass
                    elif len(key_list) == 2:
                        key_dict[line[0]] = line[2]
        return key_dict

#######################################################################################
class ReplaceEncrypt(AbstractClass):

    def encrypt(self, **args):
        text_list = self._text_open()
        key_list = self.__read_key()
        len_key = len(key_list)
        while len(text_list)%len_key != 0:
            text_list.append(random.choice(text_list))
        len_text = len(text_list)
        
        flag = True
        while flag:
            try:
                encrypt_way = self._create_file('encrypt')
                with open(encrypt_way,'x', encoding='utf-8') as encrypt_file:
                    encrypt_file.write('шифр перестановки\n')
                    str0=''
                    k=0
                    p=0
                    block_lict=[None]*len_key
                    for i in range(len_text):
                        x=0
                        flag1 = True
                        while flag1:
                            if int(key_list[x]) == k%len_key + 1:
                                block_lict.pop(x)
                                block_lict.insert(x, text_list[i])
                                k+=1
                                flag1 = False
                                break
                            else:
                                x+=1
                        p+=1
                        if p == len_key:
                            for z in range(len_key):
                                str0 = str0 + f'{block_lict[z]}'
                            block_lict = [None]*len_key
                            p=0
                    encrypt_file.write(str0)
                    print("\nУспешно")
                    flag = False
                    break
            except Exception:
                print("Возникла ошибка")  

    def decrypt(self, **args):
        key_list = self.__read_key()
        len_key = len(key_list)
        encrypt_list = self.__read_encrypt(len_key)
        len_encrypt = len(encrypt_list)
        flag1 = True
        while flag1:
            try:
                decrypt_way = self._create_file('txt')
                with open(decrypt_way,'x', encoding='utf-8') as decrypt_file:
                    str0=''
                    k=0
                    p=0
                    block_lict = [None]*len_key
                    for i in range(len_encrypt):
                        x=0
                        flag = True
                        while flag:
                            for x in range(len_key):
                                if (x+1) == int(key_list[k]):
                                    block_lict.pop(x)
                                    block_lict.insert(x, encrypt_list[i])
                                    k = (k + 1)%len_key
                                    flag = False
                                    break
                                else:
                                    x+=1
                        p+=1
                        if p == len_key:
                            for z in range(len_key):
                                str0 = str0 + f'{block_lict[z]}'
                            block_lict = [None]*len_key
                            p=0
                    decrypt_file.write(str0)
                    print("\nУспешно")
                    flag1 = False
                    break
            except Exception:
                print("Возникла ошибка") 

    def gen_key(self, **args):
        flag = True
        er=0
        while flag:
            try:
                len_key = 0
                while len_key < 2:
                    len_key = int(input("Введите длину ключа: "))
                    if len_key < 2:
                        print("Слишком короткий ключ")    
                key_list = [x for x in range(1, len_key+1)]
                random.shuffle(key_list)
                key_fileway = self._create_file('key')
                with open(key_fileway,'x',encoding='utf-8') as key_file:
                    key_file.write('шифр перестановки\n')
                    i=0
                    str0=''
                    while i < len(key_list):                   
                        str0 = str0 + str(key_list[i]) + ' '
                        i+=1 
                    key_file.write(str0)
                    flag == False
                    print("\nУспешно")
                    break
            except ValueError:
                print("Недопустимый символ")
                er+=1
                if er > 2:
                    print("Слишком много ошибок")
                    flag = False
                    break
            except Exception:
                print("Возникла ошибка")                

    def __read_encrypt(self, len_key):
        encrypt_file = open(self._encrypt_open('шифр перестановки'),'r', encoding='utf-8' )
        encrypt_list = []
        i=0
        for line in encrypt_file:
            if i < 1:
                i+=1
            else:
                encrypt_list.extend(list(line))
        return encrypt_list

    def __read_key(self):
        key_filename = self._key_open('шифр перестановки')
        with open(key_filename,'r', encoding='utf-8') as key_file:
            i=0
            for line in key_file:
                if i < 1:
                    i+=1
                    pass
                elif i==1:
                    line=line.rstrip(' ')
                    key_list = line.split(' ')    
        return key_list

#######################################################################################
class GammEncrypt(AbstractClass):

    def encrypt(self, **args):
        text_list = self._text_open()
        key_list, gamma = self.__read_key()
        alph_list=self._alp_open()
        while len(text_list)%gamma != 0:
            text_list.append(random.choice(text_list))
        len_text = len(text_list)
        len_alph = len(alph_list)
        flag1 = True
        while flag1:
            try:
                with open(self._create_file('encrypt'),'x', encoding='utf-8') as encrypt_file:
                    encrypt_file.write('шифр гаммирования\n')
                    i=0
                    k=0
                    str0=''
                    while len(str0) != len_text:
                        if k<len_alph:
                            if  text_list[i] == alph_list[k]:
                                key_val = int(key_list[i%gamma])
                                encrypt_val = (k+key_val)%len_alph
                                str0 = str0 + f'{alph_list[encrypt_val]}'
                                i+=1
                                k=0
                            else:
                                k+=1
                        else:
                            str0 = str0 + text_list[i]
                            i+=1
                            k=0
                    encrypt_file.write(str0)
                    print("\nУспешно")
                    flag1 = False
                    break
            except Exception:
                print("Возникла ошибка")       

    def decrypt(self, **args):
        encrypt_list = self.__read_encrypt()
        key_list, gamma = self.__read_key()
        alph_list = self._alp_open()
        len_encrypt = len(encrypt_list)
        len_alph = len(alph_list)
        flag1 = True
        while flag1:
            try:
                with open(self._create_file('txt'),'x', encoding='utf-8') as decrypt_file:
                    i=0
                    k=0
                    str0=''
                    while len(str0) != len_encrypt:
                        if k<len_alph:
                            if  encrypt_list[i] == alph_list[k]:
                                key_val = int(key_list[i%gamma])
                                encrypt_val = (k - key_val + len_alph)%len_alph
                                str0 = str0 + f'{alph_list[encrypt_val]}'
                                i+=1
                                k=0
                            else:
                                k+=1
                        else:
                            str0 = str0 + encrypt_list[i]
                            i+=1
                            k=0
                    decrypt_file.write(str0)
                    print("\nУспешно")
                    flag1=False
                    break
            except Exception:
                print("Возникла ошибка")

    def gen_key(self, **args):
        flag = True
        er=0
        while flag:
            try:
                gamma=0
                while gamma < 2:
                    gamma=int(input("Введите гамму: "))
                    if gamma < 2:
                        print("Слишком маленькое значение гаммы")
                key_list = [i + 1 for i in range(gamma)]
                random.shuffle(key_list)
                key_file = open(self._create_file('key'),'x',encoding='utf-8')
                key_file.write('шифр гамирования\n')
                i=0
                str0=''
                while i < len(key_list):                   
                    str0 = str0 + str(key_list[i]) + ' '
                    i+=1
                str0 = str0.rstrip(' ')
                key_file.write(str0)
                flag == False
                print("\nУспешно")
                break
            except ValueError:
                print("Недопустимый символ")
                er+=1
                if er > 2:
                    print("Слишком много ошибок")
                    flag = False
                    break
            except Exception:
                print("Возникла ошибка")                     
       
    def __read_encrypt(self):
        encrypt_file = open(self._encrypt_open('шифр гаммирования'),'r', encoding='utf-8' )
        encrypt_list = []
        i=0
        for line in encrypt_file:
            if i < 1:
                i+=1
            else:
                encrypt_list.extend(list(line))
        return encrypt_list

    def __read_key(self):
        key_file = open(self._key_open('шифр гамирования'),'r', encoding='utf-8')
        key_list = []
        i=0
        for line in key_file:
            if i < 1:
                i+=1
            else:
                key_list = line.split(' ')
        return key_list, len(key_list)

change=ChangeEncrypt()
replace=ReplaceEncrypt()
gamm=GammEncrypt()
#######################################################################################
er=0
flag = True
while flag:
    flag2 = True
    try:
        print("\nГлавное меню:")
        choice = int(input("\n1) Зашифровать\n2) Расшифровать\
            \n3) Сгенерировать ключ\n4) Выйти из программы\nВыбор: "))
        
        if choice==1: 
            er=0     
            while flag2:
                choice1 = int(input("\nВыберите метод шифровки:\n \n1) Метод замены\
                    \n2) Метод перестановки\n3) Метод гамирования\n4)Вернуться в главное меню\nВыбор: "))
                if choice1 != 1 and choice1 != 2 and choice1 != 3 and choice1 != 4:
                    print("Ошибка ввода")
                    er+=1
                    if er > 2:
                        print("Слишком много ошибок")
                        flag = False
                        break
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
            er=0    
            while flag2:
                choice1 = int(input("\nВыберите метод расшифровки:\n \n1) Метод замены\
                    \n2) Метод перестановки\n3) Метод гамирования\n4)Вернуться в главное меню\nВыбор: "))
                if choice1 != 1 and choice1 != 2 and choice1 != 3 and choice1 != 4:
                    print("Ошибка ввода")
                    er+=1
                    if er > 2:
                        print("Слишком много ошибок")
                        flag = False
                        break
                elif choice1==4:
                    flag2=False
                    break
                if choice1==1:
                    change.decrypt()
                elif choice1==2:
                    replace.decrypt()
                elif choice1==3:
                    gamm.decrypt()                  
                
        elif choice==3: 
            er=0    
            while flag2:
                choice1 = int(input("\nСгенерировать ключ для следующего алгоритма: \n \n1) Шифр замены\
                    \n2) Шифр перестановки\n3) Шифр гамирования\n4) Вернуться в главное меню\nВыбор: "))
                if choice1 != 1 and choice1 != 2 and choice1 != 3 and choice1 != 4:
                    print("Ошибка ввода")
                    er+=1
                    if er > 2:
                        print("Слишком много ошибок")
                        flag = False
                        break
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
            er+=1
            if er > 2:
                print("Слишком много ошибок")
                flag = False
                break
    
    except SyntaxError:
        print("SyntaxError")
    except KeyboardInterrupt:
        pass
    except TypeError:
        print("TypeError")
    except UnboundLocalError:
        print("Возникла ошибка")
    except IndexError:
        print("IndexError")
    except ValueError:
        print("ValueError") 
    