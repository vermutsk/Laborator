er=0
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
                choice1=int(input("\nУправление аккаунтом\n \n1) Создать аакаунт\
                    \n2) Аутентифицироваться\n3) Удалить аккаунт\
                    \n4)Изменить ключ шифрования\n5)Вернуться в главное меню\nВыбор: "))
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
                    pass
                elif choice1==2:
                    pass
                elif choice1==3:
                    '''нужны права доступа'''
                    pass
                elif choice1==4:
                    '''нужны права доступа'''
                    pass       

        elif choice==2:
            '''нужны права доступа'''
            er=0    
            while flag2:
                choice1=int(input("\nРабота с заметками:\n \n1) Создать заметку\
                    \n2) Изменить заметку\n3) Удалить заметку\
                    \\n4) Удалить все заметки\n5) Получить список заметок\
                    \n6)Вернуться в главное меню\nВыбор: "))
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
                    '''нужны права доступа'''
                    pass
                elif choice1==2:
                    '''нужны права доступа'''
                    pass
                elif choice1==3:
                    '''нужны права доступа'''
                    pass
                elif choice1==4:
                    '''нужны права доступа'''
                    pass 
                elif choice1==5:
                    '''нужны права доступа'''
                    pass
                                 

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