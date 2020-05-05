try:
    choice2=int(input("Выберите метод расшифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
    if choice2==1:
        crypt='шифр замены'
    elif choice2==2:
        crypt='шифр перестановки'
    elif choice2==3:
        crypt='шифр гамирования'    
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
    with open(key_filename, "x", encoding="utf-8") as key_file:
        key_list=[]
        for line in key_file:
            key_str=line.rstrip('\n')
            key_list.append(key_str)
            if key_list[0]==crypt:
                print(crypt)
            else:
                print("Неправильный файл ключа")
except Exception:
    print("Выберите метод")