import os
import glob
import random
import security as sec
from typing import Tuple

def create_akk()->None:
    flag = True
    er=0
    while flag:
        try:    
            way = os.getcwd()
            bd_way = os.path.join(way, 'bd.txt')
            if os.path.exists(bd_way):
                start_file(bd_way)
                flag1 = 0
                while flag1 == 0:
                    log_list=[]
                    login = input("Введите логин\n")
                    with open(bd_way, "r", encoding="utf-8") as bd_file:
                        for line in bd_file:
                            login1, hash_salt, access = line.split('|')
                            log_list.append(login1)
                            if login == login1:
                                print("Данный логин уже занят") 
                    if log_list.count(login) < 1:
                        bd_file = open(bd_way, "a", encoding="utf-8")
                        str0, dir_name = write_bd(login)
                        bd_file.write(str0)
                        bd_file.close()
                        flag1 = 1
                    er+=1
                    if er > 2:
                        print("Слишком много попыток")
                        flag = False
                        break
            else:
                login = input("Введите логин\n")
                with open(bd_way, "x", encoding="utf-8") as bd_file:
                    str0, dir_name = write_bd(login)
                    bd_file.write(str0)                        
            sec.security_sys_files(bd_way)
            dir_way = os.path.join(way, dir_name)
            sec.generate_keys(dir_way)
            print("Аккаунт успешно создан")
            flag = False
            break
        except Exception:
            print("Ошибка") 

def write_bd(login:str)->Tuple[str, str]:
    password = input("Введите пароль\n")
    hash_salt = sec.hash_password(password)
    flag = True
    while flag:
        try:
            dir_name = str(random.randint(0, 1000))
            os.mkdir(dir_name)
            flag = False
            break
        except Exception:
            pass
    str0 = f'{login}|{hash_salt}|{dir_name}\n'
    return str0, dir_name       

def authentication()->str:
    try:
        flag = 0
        way = os.getcwd()
        bd_way = os.path.join(way, 'bd.txt')
        flag = start_file(bd_way)
        if flag == 3:
            print("Создайте аккаунт")
            access = ''
            return access
        while flag < 3:
            login = input("\nВведите логин\n")
            flag += 1
            with open(bd_way,'r', encoding='utf-8') as bd_file:
                for line in bd_file:
                    line = line.rstrip('\n')
                    login1, hash_salt, access = line.split('|')
                    if login == login1:
                        i=0
                        while i != 3:
                            password = input("Введите пароль\n")
                            if sec.check_password(hash_salt, password):
                                print("Успешно")
                                i = 2
                                sec.security_sys_files(bd_way)
                                return access
                            else:
                                print("Неверный пароль")
                                i+=1
                            if i == 3:
                                print("Слишком много попыток")
            if login != login1:
                print("Данный пользователь не найден")
            if flag == 3:
                print("Слишком много попыток")        
    except FileNotFoundError:
        sec.security_sys_files(bd_way)
        print("Создайте аккаунт")
    except Exception:
        sec.security_sys_files(bd_way)
        print("Ошибка")
    assert False

def delete_akk(access:str)->None:
    way = os.getcwd()
    bd_way = os.path.join(way, 'bd.txt')
    start_file(bd_way)
    dir_way = os.path.join(way, access)
    try:
        str0 = ''
        i = 0
        while i < 2:
            with open(bd_way,'r', encoding='utf-8') as bd_file:
                for line in bd_file:
                    line1 = line.rstrip('\n')
                    login1, hash_salt, access1 = line1.split('|')
                    if access == access1:
                        line = ''
                    str0 = str0 + line
            if len(str0) > 1:
                with open(bd_way,'w', encoding='utf-8') as new_bd_file:
                    new_bd_file.write(str0)
                sec.security_sys_files(bd_way)
                i = 3
                break
            else:                
                os.remove(bd_way)
                i = 3
                break
        files = os.listdir(dir_way)
        for f in files:
            del_way = os.path.join(dir_way, f)
            try:
                os.remove(del_way)
            except OSError:
                print("Ошибка")
        os.rmdir(dir_way)
        print("Успешно")
    except Exception:
        sec.security_sys_files(bd_way)
        i+=1
        print("Ошибка удаления")
    
def change_keys(access:str)->None:
    way = os.getcwd()
    dir_way = os.path.join(way, access)
    os.chdir(access)
    files = glob.glob('*.txt')
    for f in files:
        note_way = os.path.join(dir_way, f)
        try:
            sec.decode_files(way, note_way)
        except Exception:
            sec.security_files(way, note_way)
            sec.decode_files(way, note_way)
    os.chdir(way)
    os.remove(os.path.join(dir_way, 'private_rsa_key.bin'))
    os.remove(os.path.join(dir_way, 'rsa_public.pem'))
    sec.generate_keys(dir_way)
    os.chdir(access)
    files = glob.glob('*.txt')
    for f in files:
        note_way = os.path.join(dir_way, f)
        try:
            sec.security_files(way, note_way)
        except OSError:
            print("Ошибка")
    print("Ключ шифрования успешно изменен")
    os.chdir(way) 
    
def start_file(bd_way:str)->int:
    try:
        sec.decode_sys_files(bd_way)
        flag = 0
    except FileNotFoundError:
        flag = 3
    except Exception:
        sec.security_sys_files(bd_way)
        sec.decode_sys_files(bd_way)
        flag = 0
    return flag

