def test():
    if fileway.endswith(f".{file}"):
        pass
    else:
        raise Exception
    return fileway

def key_open(crypt):
    with open(fileway, "r", encoding="utf-8") as key_file:
        key_list=[]
        s=0
        for line in key_file:
            key_str=line.rstrip('\n')
            key_list.append(key_str)
            if key_list[0]==crypt:
                pass
            else:
                if s==0:
                    print("Неправильный файл ключа")
                    s=+1
        raise Exception
    return key_list

def choice():
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
        def no_repeat(alph_list):
            alph_list1=[]
            for z in alph_list:
                if z not in alph_list1:
                    alph_list1.append(z)
            return alph_list1
        alph_list2=no_repeat(alph_list)
    return alph_list2

flag=True
while flag:
    print("Главное меню:")
    choice=int(input("1) Зашифровать\n2) Расшифровать\n\3) Сгенерировать ключ\nВыбор: ")) 
    
    if choice==1:
        choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
        if choice1==1 or choice1==2 or choice1==3:
            file="txt"
            fileway=input(f"Fileway for {file}:")
            test()
            print(fileway)
            file="key"
            fileway=input(f"Fileway for {file}:")
            test()
            choice()
        else:
            raise Exception

    elif choice==2:
        choice1=int(input("Выберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
        if choice1==1 or choice1==2 or choice1==3:
            file="encode"
            fileway=input(f"Fileway for {file}:")
            test()
            file="key"
            fileway=input(f"Fileway for {file}:")
            test()
            choice()
        else:
            raise Exception


    elif choice==3:
        choice3=int(input("Сгенерировать ключ для следующего алгоритма: \n1) Шифр замены\n2) Шифр перестановки\n3) Шифр гамирования\n4) Вернуться в главное меню\nВыбор: "))
        file="key"
        fileway=input(f"Fileway for {file}:")
        test()
        if choice3==1:
            file="alph"
            fileway=input(f"Fileway for {file}:")
            test()
            alph_list2=alp_test()
            alph_dict={}
            alph_dict['alp']=alph_list2  
            print(alph_dict)

        elif choice3==2:
            len_crypt=int(input("Введите длину блока: "))

        elif choice3==3:
            file="alph"
            fileway=input(f"Fileway for {file}:")
            test()
            alph_list2=alp_test()
            len_alph=len(alph_list2)  
            print(len_alph)
            len_crypt1=int(input("Введите длину блока: "))
        else:
            raise Exception         
        with open(fileway, "x", encoding="utf-8") as key_file:
            key_file.write("Test string")
            key_file.close()
    else:
        raise Exception