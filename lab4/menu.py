import db
import security as sec
import notes
er=0
access = ''
flag=True
while flag:
    flag2=True
    try:
        print("\nГлавное меню:")
        choice=int(input("\n1) Управление аккаунтом\n2) Работа с заметками\
            \n3) Выйти из программы\nВыбор: "))
        
        if choice==1: 
            er=0     
            while flag2:
                choice1=int(input("\nУправление аккаунтом\n \n1) Создать аккаунт\
                    \n2) Аутентифицироваться\n3) Удалить аккаунт\
                    \n4) Изменить ключ шифрования\n5) Вернуться в главное меню\nВыбор: "))
                if choice1<1 or choice1>5:
                    print("Ошибка ввода")
                    er+=1
                    if er>2:
                        print("Слишком много ошибок")
                        flag=False
                        break
                elif choice1==5:
                    flag2==False
                    break
                if choice1==1:
                    print("Создание аккаунта")
                    db.create_akk()

                elif choice1==2:
                    print("Аутентификация")
                    flag3 = True
                    while flag3:
                        if access != '':
                            agree = input("Вы точно хотите выйти из аккаунта?(Y/N)\n")
                            if agree == 'Y':
                                access = ''
                                access = db.authentication()
                                flag3 = False
                                break
                            elif agree == 'N':
                                flag3 = False
                                break
                            else:
                                print("Ошибка")
                        else:
                            access = db.authentication()
                            flag3 = False
                            break
                        
                elif choice1==3:
                    if access == '':
                        print("Ошибка доступа\nНеобходима аутентификация")
                    elif access != '':
                        db.delete_akk(access)
                        access = ''

                elif choice1==4:
                    if access == '':
                        print("Ошибка доступа\nНеобходима аутентификация")
                    elif access != '':
                        db.change_keys(access)                       

        elif choice==2:
            if access == '':
                print("Ошибка доступа\nНеобходима аутентификация")
            else:
                er=0    
                while flag2:
                    choice1=int(input("\nРабота с заметками:\n \n1) Создать заметку\
                        \n2) Изменить заметку\n3) Удалить заметку\
                        \n4) Удалить все заметки\n5) Получить список заметок\
                        \n6) Вернуться в главное меню\nВыбор: "))
                    if choice1<1 or choice1>6:
                        print("Ошибка ввода")
                        er+=1
                        if er>2:
                            print("Слишком много ошибок")
                            flag=False
                            break
                    elif choice1==6:
                        flag2==False
                        break
                    if choice1==1:
                        notes.create_note(access)    
                    elif choice1==2:
                        notes.change_note(access)
                    elif choice1==3:
                        notes.delete_note(access)
                    elif choice1==4:
                        notes.delete_all_notes(access) 
                    elif choice1==5:
                        notes.list_notes(access)
                                 

        elif choice==3:
            flag==False
            break
        
        else:
            print("Ошибка ввода\n")
            er+=1
            if er>2:
                print("Слишком много ошибок")
                flag=False
                break
    
    except KeyboardInterrupt:
        pass 
    #except SyntaxError:
    #    print("SyntaxError")
    #except IndexError:
    #    print("IndexError")
    #except ValueError:
    #    print("ValueError")
    #except UnboundLocalError:
    #    print("Возникла ошибка")
    #except TypeError:
    #    print("TypeError")                 