from math import log2

def choice1(text):
    choice_charact = int(input("Выберите номер характеристики:\n1.Вероятность появления символа\n2.Вероятность появления биграммы\n3.Вероятность появления триграммы\n4.Энтропия текста\n"))
    if choice_charact == 1:
        sim = input("Введите искомый символ\n")
        p = ver(sim, text, 1)
        print('Вероятность равна: ',p)
    elif choice_charact == 2:
        flag = True
        while flag:
            sim = input("Введите искомую биграмму\n")
            if len(sim)!=2:
                print('Ведите только 2 символа')
            else:
                p = ver(sim, text, 2)
                print('Вероятность равна: ',p)
                flag = False
    elif choice_charact == 3:
        flag = True
        while flag:
            sim = input("Введите искомую триграмму\n")
            if len(sim)!=3:
                print('Ведите только 3 символа')
            else:
                p = ver(sim, text, 3)
                print('\nВероятность равна: ',p)
                flag = False
    elif choice_charact == 4:
        print('Энтропия равна: ', entrop(text))
    else:
        print('Выберите необходимую характеристику')

def open_text():
    flag = True
    while flag:
        try:
            way = input('Введите путь к тексту:\n')
            if  way.endswith('txt'):
                with open(way, "r", encoding="utf-8") as text_file:
                    text = []
                    for line in text_file:
                        if line.endswith('\n'):
                            line = line.rstrip('\n')
                        text.extend([line])
                    if len(text)!=0:
                        flag = False
                        break
                    else:
                        print("Пустой файл")
            else:
                print('Введите путь к файлу типа txt')
        except Exception:
            print("Возникла ошибка в открытии файла")
    return text

def ver(sim, text, g):
    n = 0
    m = 0
    for stroka in text:
        i = 0
        while i+g <= len(stroka):
            if stroka[i:i+g]==sim:
                m+=1
            i+=1
            n+=1
    
    #if len(text)>1:
    #    for k in range(len(text)-1):
    #        a = text[k]
    #        b = text[k+1]
    #        for l in range(1, g):
    #            if a[len(a)-l:]+b[:g-l]==sim:
    #                m+=1
    # 
    
    print(m)               
    return m/n

def entrop(text):
    h = 0
    alf = []
    for stroka in text:
        for i in stroka:
            if i in alf:
                pass
            else:
                alf.append(i)
                p = ver(i, text, 1)
                h-= p*log2(p)
    #for i in alf:
    #    print(i)
    return h

def main():
    choice_txt = int(input("1.Ввести текст\n2.Выбрать путь:\n"))
    for i in range(3):
        if choice_txt==1:
            text = []
            flag = True
            while flag:
                text.extend([input("Введите текст\n")])
                if len(text[0])==0:
                    print('Введите текст')
                else:
                    flag=False
            break
        elif choice_txt==2:
            text = open_text()
            break
        else:
            print('Ошибка ввода')
    choice1(text)

if __name__ == '__main__':
    main()