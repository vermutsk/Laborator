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

class Open_file():
    key_list=[]
    def open_file(self, key_filename, **args):
        with open(key_filename, "r", encoding="utf-8") as key_file:
            for line in key_file:
                key_str=line.rstrip('\n')
                self.key_list.append(key_str)
                if self.key_list[0]==choice.crypt:
                    print(choice.crypt)
                else:
                    print("Неправильный файл ключа")
