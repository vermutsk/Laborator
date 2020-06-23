import os
import glob
import subprocess 
from sys import platform
from time import sleep
import security as sec

def create_note(dir_name:str):
    flag = 0
    while flag < 3:
        try:
            way_note = sys_prog(dir_name)
            note_file = open(way_note,'x', encoding='utf-8')
            note_file.close()
            print("Заметка создана")
            flag = 3
            break
        except FileExistsError:
            flag +=1
            print("Заметка с таким именем уже существует")
        except Exception:
            flag +=1
            pass          

def change_note(dir_name:str):
    flag = 0
    while flag < 3:
        try:
            way = os.getcwd()
            way_note = sys_prog(dir_name)
            start_file(way_note)
            way_note = way_note.replace('\\','\\\\')
            subprocess.call(f'notepad "{way_note}"')
            sec.security_files(way, way_note)
            print("Заметка изменена")
            flag = 3
            break
        except FileNotFoundError:
            flag +=1
            print("Заметка не найдена")
        except Exception:
            flag +=1
            print("Kosyak")    
        
def delete_note(dir_name:str):
    flag = 0
    while flag < 3:
        try:
            way_note = sys_prog(dir_name)
            os.remove(way_note)
            print("Заметка удалена")
            flag = 3
            break 
        except FileNotFoundError:
            flag +=1
            print("Заметка не найдена")
        except Exception:
            flag +=1
            pass

def delete_all_notes(dir_name:str):
    way = os.getcwd()
    os.chdir(dir_name)
    files = glob.glob('*.txt')
    for f in files:
        try:
            os.unlink(f)
        except OSError:
            print("Ошибка")
    print("Успешно")
    os.chdir(way)

def list_notes(dir_name:str):
    way = os.getcwd()
    os.chdir(dir_name)
    files = glob.glob('*.txt')
    for f in files:
        f = f.rstrip('.txt')
        print(f)
    print("Успешно")
    os.chdir(way)

def sys_prog(dir_name:str):
    if platform == "linux" or platform == "linux2":
        slash = '/'
    elif platform == "win32" or platform == "win64":
        slash = '\\'
    way = os.getcwd()
    name_note = input("Введите название заметки:\n")
    way_note = f'{way}{slash}{dir_name}{slash}{name_note}.txt'
    return way_note

def start_file(way_note:str):
    try:
        sec.decode_sys_files(way_note)
    except Exception:
        sec.security_sys_files(way_note)
        sec.decode_sys_files(way_note)

    

