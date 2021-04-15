table64 = {'000000': 'A', '100000': 'g', '000001': 'B', '100001': 'h', '000010': 'C', '100010': 'i', '000011': 'D',
            '100011': 'j', '000100': 'E',
            '100100': 'k', '000101': 'F', '100101': 'l', '000110': 'G', '100110': 'm', '000111': 'H', '100111': 'n',
            '001000': 'I', '101000': 'o',
            '001001': 'J', '101001': 'p', '001010': 'K', '101010': 'q', '001011': 'L', '101011': 'r', '001100': 'M',
            '101100': 's', '001101': 'N',
            '101101': 't', '001110': 'O', '101110': 'u', '001111': 'P', '101111': 'v', '010000': 'Q', '110000': 'w',
            '010001': 'R', '110001': 'x',
            '010010': 'S', '110010': 'y', '010011': 'T', '110011': 'z', '010100': 'U', '110100': '0', '010101': 'V',
            '110101': '1', '010110': 'W',
            '110110': '2', '010111': 'X', '110111': '3', '011000': 'Y', '111000': '4', '011001': 'Z', '111001': '5',
            '011010': 'a', '111010': '6',
            '011011': 'b', '111011': '7', '011100': 'c', '111100': '8', '011101': 'd', '111101': '9', '011110': 'e',
            '111110': '+', '011111': 'f',
            '111111': '/', ' ': ' '}

table32 = {'00000': 'A', '00001': 'B', '00010': 'C', '00011': 'D', '00100': 'E', '00101': 'F', '00110': 'G',
            '00111': 'H', '01000': 'I',
            '01001': 'J', '01010': 'K', '01011': 'L', '01100': 'M', '01101': 'N', '01110': 'O', '01111': 'P',
            '10000': 'Q', '10001': 'R',
            '10010': 'S', '10011': 'T', '10100': 'U', '10101': 'V', '10110': 'W', '11010': '2', '10111': 'X',
            '11011': '3', '11000': 'Y',
            '11100': '4', '11001': 'Z', '11101': '5', '11110': '6', '11111': '7', ' ': ' '}


def Enter_message():
    while True:
        type_mes = input("Выбирите тип ввода сообщения:\n"
                        "1. Ввод с консоли\n"
                        "2. Ввод из файла формата txt\n"
                        ">>")
        if type_mes == '1':
            message = input("Вводить сообщение сюда\n"
                            ">>")
            break
        elif type_mes == '2':
            name_file = input("Вводить названия файла сюда\n"
                            ">>")
            with open(name_file, 'r') as file:
                message = file.read()
            break
        else:
            continue
    return message




def Text_to_ASCII_64(message):
    message_in_ASCII = ''
    bit_0_array = '00000000'
    for ch in message:
        c = bin(ord(ch))[2:]
        while len(c) != 8:
            c = '0' + c
        message_in_ASCII += c
    l_24 = (len(message_in_ASCII) % 24) % 7
    # print(len(message_in_ASCII), l_24)
    if l_24 == 2:
        message_in_ASCII += bit_0_array
    elif l_24 == 1:
        message_in_ASCII += bit_0_array * 2
    elif l_24 == 0:
        pass
    return message_in_ASCII, l_24  # l_24 параметр отвечающий за количиство ранво поле перевода по таблице: l_24 = 0 - 0 знако =, l_24 = 1 - 2 знака =, l_24 = 2 - 1 знак = .


def Text_to_ASCII_32(message):
    message_in_ASCII = ''
    for ch in message:
        c = bin(ord(ch))[2:]
        while len(c) != 8:
            c = '0' + c
        message_in_ASCII += c
    if not (len(message_in_ASCII)) % 40:
        return message_in_ASCII, 0
    else:
        N = len(message_in_ASCII) % 5
        rav = 0
        if N == 1:
            rav = 4
        elif N == 2:
            rav = 1
        elif N == 3:
            rav = 6
        elif N == 4:
            rav = 3

        while len(message_in_ASCII) % 5 != 0:
            message_in_ASCII = message_in_ASCII + '0'

        return message_in_ASCII, rav


def encrypted_BASE64(message_ASCII, num_rav):
    message_BASE64 = ''
    for elem in [message_ASCII[i:i + 6] for i in range(0, len(message_ASCII), 6)]:
        for key, value in table64.items():
            if elem == key:
                message_BASE64 += value
    if num_rav == 0:
        pass
    elif num_rav == 1:
        message_BASE64 += '=='
    elif num_rav == 2:
        message_BASE64 += '='
    return message_BASE64


def encrypted_BASE32(message_ASCII, num_rav):
    message_BASE32 = ''
    for elem in [message_ASCII[i:i + 5] for i in range(0, len(message_ASCII), 5)]:
        for key, value in table32.items():
            if elem == key:
                message_BASE32 += value
    if num_rav == 0:
        pass
    elif num_rav == 1:
        message_BASE32 = message_BASE32 + '=' * 1
    elif num_rav == 3:
        message_BASE32 = message_BASE32 + '=' * 3
    elif num_rav == 4:
        message_BASE32 = message_BASE32 + '=' * 4
    elif num_rav == 6:
        message_BASE32 = message_BASE32 + '=' * 6
    writh_file(message_BASE32, '32')
    return message_BASE32


def writh_file(message, format):
    name = input("Введите названия файла для шифрования:")
    name = name + '.' + format
    with open(name, 'w') as file:
        file.write(message)


def decrypted_BASE64(message_BASE64):
    message_ASCII = ''
    num_rav = 0
    for ch in message_BASE64:
        if ch == '=':
            num_rav += 1

    for i in range(num_rav):
        message_BASE64 = message_BASE64.rstrip('=')

    for ch in message_BASE64:
        for key, value in table64.items():
            if ch == value:
                message_ASCII += key

    for i in range(num_rav):
        message_ASCII = message_ASCII.rstrip('00000000')
    name_file = input("Введите имя файла для записи расшифровки:")
    name_file = name_file + '.txt'
    with open(name_file, 'w', encoding='utf-8') as file:
        for elem in [message_ASCII[i:i + 8] for i in range(0, len(message_ASCII), 8)]:
            ch = int(elem, 2)
            file.write(chr(ch))


def decrypted_BASE32(message_BASE32):
    def go_to_text(ASCII_text, file):
        for elem in [ASCII_text[i:i + 8] for i in range(0, len(ASCII_text), 8)]:
            ch = int(elem, 2)
            file.write(chr(ch))

    message_ASCII = ''
    num_rav = 0
    for ch in message_BASE32:
        if ch == '=':
            num_rav += 1
    print(num_rav)

    for i in range(num_rav):
        message_BASE32 = message_BASE32.rstrip('=')

    for ch in message_BASE32:
        for key, value in table32.items():
            if ch == value:
                message_ASCII += key
    name_file = input("Введите имя файла для записи расшифровки:")
    name_file = name_file + '.txt'
    with open(name_file, 'w') as file:
        if num_rav == 0:
            go_to_text(message_ASCII, file)
        elif num_rav == 6:
            message_ASCII = message_ASCII.rstrip('00')
            go_to_text(message_ASCII,file)
        elif num_rav ==4:
            message_ASCII = message_ASCII.rstrip('0000')
            go_to_text(message_ASCII,file)
        elif num_rav == 3:
            message_ASCII = message_ASCII.rstrip('0')
            go_to_text(message_ASCII,file)
        elif num_rav == 1:
            message_ASCII = message_ASCII.rstrip('000')
            go_to_text(message_ASCII, file)




def read_file(format):
    name = input("Введите название файла для расшифровки:")
    name = name + '.' + format
    with open(name, 'r') as file:
        message_BASE = file.read()
    return message_BASE


def main():
    en_de = input("Главное меню:\n"
                  "1. Ззашифровать.\n"
                  "2. Расшифровать.\n"
                  ">>")
    if en_de == '1':
        type = input("Выберети формат шифрования:\n"
                     "1. BASE 64\n"
                     "2. BASE 32\n"
                     ">>")
        if type == '1':
            message_ASCII_64, rav = Text_to_ASCII_64(Enter_message())
            H = encrypted_BASE64(message_ASCII_64, rav)
            print(H)
        elif type == '2':
            message_ASCII_32, rav = Text_to_ASCII_32(Enter_message())
            H = encrypted_BASE32(message_ASCII_32, rav)
            print(H)
        else:
            print('Error')

    elif en_de == '2':

        type = input("Выбирите формат дешифрования:\n"
                     "1. BASE 64\n"
                     "2. BASE 32\n"
                     ">>")
        if type == '1':

            text_BASE64 = read_file('64')
            decrypted_BASE64(text_BASE64)


        elif type == '2':

            text_BASE32 = read_file('32')
            decrypted_BASE32(text_BASE32)

        else:
            print('Error')

    else:
        print('Error')


if __name__ == '__main__':
    while True:
        main()