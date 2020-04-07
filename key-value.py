flag=True
while flag:
    index=input("Введите параметр: ")
    with open('conf1', 'r') as file:
        for line in file:
            if line[0] !='#' and line[0] !=';' and line[0] !='\n':
                if "#" in line:
                    line = line[0:line.index("#")]
                str0=line 
                if str0.startswith(index):   
                    list0=str0.split(' ', 1)
                    if len(list0)==1:        
                        print('True')
                    else:
                        dict0={}
                        dict0[list0[0]]=list0[1]            
                        for key, value in dict0.items():
                            print(key,':',value)

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