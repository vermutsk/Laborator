flag=True
while flag:
    print("Главное меню:")
    choice=int(input("1) Зашифровать\n2) Расшифровать\n3) Сгенерировать ключ\nВыбор: ")) 
    if choice==1:
        choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
        if choice1==1 or choice1==2 or choice1==3:
            if choice1==1:
                crypt='шифр замены'
            elif choice1==2:
                crypt='шифр перестановки'
            elif choice1==3:
                crypt='шифр гамирования'
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
            with open(key_filename, "r", encoding="utf-8") as key_file:
                key_list=[]
                for line in key_file:
                    key_str=line.rstrip('\n')
                    key_list.append(key_str)
                    if key_list[0]==crypt:
                        print(crypt)
                    else:
                        print("Неправильный файл ключа")
        elif choice1==4:
            break
        else:
            print("Ошибка")


    elif choice==2:
        choice2=int(input("Выберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
        if choice2==1:
            crypt='шифр замены'
        elif choice2==2:
            crypt='шифр перестановки'
        elif choice2==3:
            crypt='шифр гамирования'
        elif choice2==4:
            break    
        else:
            print("Ошибка")
        way1=input("Введите путь к файлу шифротекста: ")
        if way1.endswith(".encrypt"):
            crypt_text_filename=way1
        else:
            print("Неправильный формат файла")
        key=input("Введите путь к файлу ключа: ")
        if key.endswith(".key"):
            key_filename=key
        else:
            print("Неправильный формат файла")
        with open(key_filename, "r", encoding="utf-8") as key_file:
            key_list=[]
            for line in key_file:
                key_str=line.rstrip('\n')
                key_list.append(key_str)
                if key_list[0]==crypt:
                    print(crypt)
                else:
                    print("Неправильный файл ключа")


    elif choice==3:
        choice3=int(input("Сгенерировать ключ для следующего алгоритма: \n1) Шифр замены\n2) Шифр перестановки\n3) Шифр гамирования\n4) Вернуться в главное меню\nВыбор: "))
        if choice3==1:
            way2=input("Введите путь к файлу алфавита: ")
            if way2.endswith(".alph"):
                alph_filename=way2
            else:
                print("Неправильный формат файла")
            with open(alph_filename, "r", encoding="utf-8") as alph_file:
                alph_dict={}
                alph_list=[]
                i=0
                for line in alph_file:
                    alph_str=line.rstrip('\n')
                    if len(alph_str)!=1:
                        while i==0:
                            print("Неподходящие значения алфавита: ")
                            i=+1
                        print(alph_str)
                    else:
                        alph_list.append(alph_str)
                def f(alph_list):
                    alph_list1=[]
                    for z in alph_list:
                        if z not in alph_list1:
                            alph_list1.append(z)
                    return alph_list1
                alph_list2=f(alph_list)
                alph_dict['alp']=alph_list2  
                print(alph_dict)

        elif choice3==2:
            len_crypt=int(input("Введите длину блока: "))

        elif choice3==3:
            way3=input("Введите путь к файлу алфавита: ")
            if way3.endswith(".alph"):
                alph_filename=way3
            else:
                print("Неправильный формат файла")
            with open(alph_filename, "r", encoding="utf-8") as alph_file:
                alph_list=[]
                i=0
                for line in alph_file:
                    alph_str=line.rstrip('\n')
                    if len(alph_str)!=1:
                        while i==0:
                            print("Неподходящие значения алфавита: ")
                            i=+1
                        print(alph_str)
                    else:
                        alph_list.append(alph_str)
                def f(alph_list):
                    alph_list1=[]
                    for z in alph_list:
                        if z not in alph_list1:
                            alph_list1.append(z)
                    return alph_list1
                alph_list2=f(alph_list)
                len_alph=len(alph_list2)  
                print(len_alph)
            len_crypt1=int(input("Введите длину блока: "))
        elif choice3==4:
            break
        else:
            print("Ошибка")         


    else:
        print('Ошибка')


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
