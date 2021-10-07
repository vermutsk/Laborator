def block(way, gamm):
    flag = True
    while flag:
        try:
            with open(way, "r", encoding="utf-8") as text_file:
                text = []
                g = text_file.read().rstrip('\n')
                while len(g)%len(gamm)!=0:
                    g+=' '
                while len(g)!=0:
                    text.append(g[:len(gamm)])
                    g = g[len(gamm):]
                if len(text)!=0:
                    flag = False
                    break
                else:
                    print("Пустой файл")
                flag = False
        except Exception:
            print("Возникла ошибка в открытии файла")
    return text

def text_to_bits(i, encoding='utf-8'):
    bits = bin(int.from_bytes(i.encode(encoding), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8'):
    str = int(bits, 2)
    text = str.to_bytes((str.bit_length() + 7) // 8, 'big').decode(encoding)
    return text

def encrypt(text, gamm, a):
    characters = list(map(chr, range(32, 256)))
    alphabet = []
    for i in characters:
        g = i.decode('utf-8')
        alphabet.append(g)
    cipher = ""
    print(len(characters))
    for block in text:
        for elem in block:
            print(elem)
            c=(characters.index(elem)+characters.index(gamm[block.index(elem)]))%len(characters)
            cipher=cipher+characters[c]
    with open('encodeVernem.txt', "w", encoding="utf-8") as encode_file:
        encode_file.write(cipher)

def decrypt():
    pass

def main():
    flag = True
    while flag:
        choice1  = int(input('1.Кодирование\n2.Декодирование\n3.Выход\nВыберите номер действия: '))
        if choice1==1:
            flag1 = True
            while flag1:
                way = input("1.Введите путь: к файлу:\n")
                if  way.endswith('txt'):
                    flag1 = False
                    break
                else:
                    print('Введите путь к файлу типа txt')
            gamm = input("Ввeдите гамму: ")
            g = []
            for i in range(len(gamm)):
                g.append(text_to_bits(gamm[i]))
            text = block(way, g)
            if len(text)>0:
                encrypt(text, g, 256)
        elif choice1==2:
            decrypt()
        elif choice1 == 3:
            flag = False
        else:
            print('Ошибка ввода')
        

if __name__ == '__main__':
    main()