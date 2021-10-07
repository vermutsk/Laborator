def open_text():
    flag = True
    while flag:
        try:
            way = input('Введите путь к тексту:\n')
            if  way.endswith('txt'):
                with open(way, "r", encoding="utf-8") as text_file:
                    text = []
                    for line in text_file:
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

def text_to_bits(text, encoding='utf-8'):
    with open('encode.txt', "w", encoding="utf-8") as encode_file:
        for stroka in text:
            bits = bin(int.from_bytes(stroka.encode(encoding), 'big'))[2:]
            encode_file.write(bits.zfill(8 * ((len(bits) + 7) // 8)) + '\n')
    print('Успешно зашифровано')

def text_from_bits(encoding='utf-8'):
    try:
        with open('encode.txt', "r", encoding="utf-8") as text_file:
            text = []
            for line in text_file:
                text.extend([line])
        with open('decode.txt', "w", encoding="utf-8") as decode_file:
            for stroka in text:
                stroka = stroka.rstrip('\n')
                txt = int(stroka, 2)
                print(txt)
                decode_file.write(txt.to_bytes((txt.bit_length() + 7) // 8, 'big').decode(encoding) or '\0')
        print('Успешно расшифровано')
    except Exception:
        print("Возникла ошибка в открытии файла")


def main():
    flag = True
    while flag:
        choice1  = int(input('1.Кодирование\n2.Декодирование\n3.Выход\nВыберите номер действия: '))
        if choice1==1:
            choice_txt = int(input("1.Ввести текст\n2.Выбрать путь:\n"))
            for i in range(3):
                if choice_txt==1:
                    text = []
                    flag = True
                    while flag:
                        text.extend([input("Введите текст\n")])
                        if len(text[0])==0:
                            print('Введите текст\n')
                        else:
                            flag=False
                    break
                elif choice_txt==2:
                    text = open_text()
                    break
                else:
                    print('Ошибка ввода')
            if len(text)>0:
                text_to_bits(text)
        elif choice1==2:
            text_from_bits()
        elif choice1 == 3:
            flag = False
        else:
            print('Ошибка ввода')
        

if __name__ == '__main__':
    main()