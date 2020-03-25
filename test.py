flag=True
while flag:
    val_1=int(input("Введите первое число: "))
    val_2=int(input("Введите второе число: "))
    comm=input("Выберите операцию: '+', '-', '*', '/':   ")
    if comm=='+':
        print(val_1+val_2)
    elif comm=='-':
        print(val_1-val_2)
    elif comm=='*':
        print(val_1*val_2)
    elif comm=='/':
        print(val_1/val_2)
    else:
        print("Ошибка") 


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
         break