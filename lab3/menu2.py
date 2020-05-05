choice1=int(input("Выберите метод шифровки:\n1) Метод замены\n2) Метод перестановки\n3) Метод гамирования\n4) Вернуться в главное меню\nВыбор: "))
from  classes import Choice, Open_file
choice=Choice(choice1, crypt)
choice.crypt_choice()
way=input("Введите путь к файлу текста: ")
if way.endswith(".txt"):
    text_filename=way
else:
    print("Неправильный формат файла")
key=input("Введите путь к файлу ключа: ")
if key.endswith(".key"):
    key_filename=key

else:
    print("Неправильный формат файла")
open_file=Open_file(key_filename)
open_file.open_file()
