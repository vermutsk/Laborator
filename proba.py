<<<<<<< HEAD
flag=True
while flag:

    index=input("Введите индекс: ")
    with open("conf", 'r') as file:
        for line in file:
            if line[0] !='#' and line[0] !=';' and line[0] !='\n':
                str0=line 
                if str0.startswith(index):
                    if str0.find(' '):    
                        list0=str0.split()
                        dict0={}
                        dict0[list0[0]]=list0[1]            
                        for key, value in dict0.items():
                            print(key,':',value)
                    else:
                        print(str0)


    for i in range(3):
        command=input("Прододжить? Y/N :")
        if command=='Y':
            break
        elif command=='N':
            flag=False
            break
        else:
            print("Ошибка")
        if i==2:
         print ("Слишком много ошибок")
         flag=False
=======
flag=True
while flag:

    index=input("Введите индекс: ")
    with open("conf", 'r') as file:
        for line in file:
            if line[0] !='#' and line[0] !=';' and line[0] !='\n':
                str0=line 
                if str0.startswith(index):
                    if str0.find(' '):    
                        list0=str0.split()
                        dict0={}
                        dict0[list0[0]]=list0[1]            
                        for key, value in dict0.items():
                            print(key,':',value)
                    else:
                        print(str0)


    for i in range(3):
        command=input("Прододжить? Y/N :")
        if command=='Y':
            break
        elif command=='N':
            flag=False
            break
        else:
            print("Ошибка")
        if i==2:
         print ("Слишком много ошибок")
         flag=False
>>>>>>> 7c646f9bf51ba615865624c646537fa23e118a3f
         break