choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
from  classes import Choice, Open_files, Ways, Ways1
choice=Choice(choice1)
choice.crypt_choice()

way=input("Введите путь к файлу текста: ")
ways=Ways(way)
ways.file_way()

key=input("Введите путь к файлу ключа: ")
ways1=Ways1(key)
ways1.file_way1()

open_files=Open_files()
open_files.open_file()
