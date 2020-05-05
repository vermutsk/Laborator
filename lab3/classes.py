class Choice():
    def __init__(self, choice1):
        self.choice1=choice1
    def crypt_choice(self, **args):
        if self.choice1==1 or self.choice1==2 or self.choice1==3:
            if self.choice1==1:
                self.crypt='шифр замены'
            elif self.choice1==2:
                self.crypt='шифр перестановки'
            elif self.choice1==3:
                self.crypt='шифр гамирования'
        else:
            print(self.choice1, "Ошибка")
class Ways():
    def __init__(self, way):
        self.way=way
    def file_way(self, **args):
        if self.way.endswith(".txt"):
            text_filename=self.way
            print(text_filename)
        else:
            print("Неправильный формат файла")

class Ways1():
    def __init__(self, key):
        self.key=key
    def file_way1(self, **args):
        if self.key.endswith(".key"):
            key_filename=self.key
            print(key_filename)
        else:
            print("Неправильный формат файла")

class Open_files(Choice, Ways1):
    key_list=[]
    def __init__(self, crypt, key_filename):
        self.key_filename=key_filename
        self.crypt=crypt
    def open_file(self, **args):
        with open(self.key_filename, "r", encoding="utf-8") as key_file:
            for line in key_file:
                key_str=line.rstrip('\n')
                self.key_list.append(key_str)
                if self.key_list[0]==self.crypt:
                    print(self.crypt)
                else:
                    print("Неправильный файл ключа")
