def bitstring(str_text: str):
    res = ''.join(format(ord(i), 'b').zfill(8) for i in str_text)
    return res

def stringbit(str_text: str):
    res = ''
    while len(str_text)!=0:
        bit_str = 0
        for i in range(0, 8):
            if str_text[i]=='1':
                bit_str += pow(2, 7-i)
        res += ''.join(format(chr(int(bit_str))))
        str_text = str_text[8:]
    return res

def parsing_file(file_name:str):
    vord_dict = dict()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            vord_dict[line[0]] = line[1]
    return vord_dict

def BASE64_en(res: str):
    res = bitstring(res)
    ravno_to_end = 0
    for_test_24 = len(res)
    while for_test_24 % 24 != 0:
        res = res + '0'
        ravno_to_end += 1
        for_test_24 = len(res)
    translate_symbols = parsing_file("table64.txt")
    encrypted_str=''
    while len(res) != 0:
        bit_str = ''
        for i in range(0, 6):
            bit_str = bit_str + res[i]
        res = res[6:]
        i = len(res)
        encrypted_str=encrypted_str+translate_symbols[bit_str]
    ravno_to_end=int(ravno_to_end/8)
    for i in range(ravno_to_end):
        encrypted_str=encrypted_str+'='
    with open("encrypted_64.txt", 'w', encoding='utf-8') as encryptfile:
        encryptfile.write(encrypted_str)

def BASE32_en(res:str):
    res=bitstring(res)
    zero=0
    for_test_40=len(res)
    if for_test_40%5==3:
        zero=6
    elif for_test_40%5==1:
        zero=4
    elif for_test_40%5==4:
        zero=3
    elif for_test_40%5==2:
        zero=1
    if for_test_40%40!=0:
        while for_test_40%5!=0:
            res=res+'0'
            for_test_40=len(res)
    translate_symbols=parsing_file('table32.txt')
    encrypted_str = ''
    while len(res)!=0:
        bit_str = ''
        for i in range(5):
            bit_str=bit_str+res[i]
        res=res[5:]
        encrypted_str=encrypted_str+translate_symbols[bit_str]
    for i in range(zero):
        encrypted_str=encrypted_str+'='
    with open("encrypted_32.txt", 'w', encoding='utf-8') as encryptfile:
        encryptfile.write(encrypted_str)

def BASE64_de(res:str):
    j = res.count('=')
    res = res[0:len(res)-j]
    translate_symbols = parsing_file("table64.txt")
    decrypted_str = ''
    while len(res)!=0:
        str0 = res[0]
        res=res[1:]
        for key, value in translate_symbols.items():
            if value==str0:
                decrypted_str=decrypted_str+key
                break
    j*=8
    decrypted_str = decrypted_str[0:len(decrypted_str)-j]
    decrypted_str = stringbit(decrypted_str)
    with open("decrypted_64.txt", 'w', encoding='utf-8') as decryptfile:
        decryptfile.write(decrypted_str)

def BASE32_de(res:str):
    j = res.count('=')
    res = res[0:len(res)-j]
    translate_symbols = parsing_file("table32.txt")
    decrypted_str = ''
    while len(res)!=0:
        str0 = res[0]
        res=res[1:]
        for key, value in translate_symbols.items():
            if value==str0:
                decrypted_str=decrypted_str+key
                break
    if j==6:
        mod=3
    elif j==4:
        mod=1
    elif j==3:
        mod=4
    elif j==2:
        mod=2
    while len(decrypted_str)%5!=mod:
        for_test_24 = len(decrypted_str)-1
        decrypted_str = decrypted_str[0:for_test_24]
    decrypted_str = stringbit(decrypted_str)
    with open("decrypted_32.txt", 'w', encoding='utf-8') as decryptfile:
        decryptfile.write(decrypted_str)

#....................MENU....................#
def choose_file():
    flag = True
    while flag:
        fileway = input("Enter way for file: \n")
        try:
            if fileway.endswith(f".txt"):
                flag = False
                return fileway
            else:
                print("Error file type")
        except Exception:
            print("Error way")

def choose_text():
    flag1 = True
    while flag1:
        choose2 = int(input("Input text from - file\consol (1\\2)\n"))
        if choose2 == 1:
            fileway = choose_file()
            with open(fileway, 'r',  encoding="utf-8") as file:
                res = ''
                for line in file:
                    res += line
            return res
        elif choose2 == 2:
            res = input("Enter text\n")
            return res
        else:
            print("Error")

def choose_encrypt(res:str):
    choose1=int(input("Create choose - Base64\Base32 (64\\32)\n"))
    if choose1==64:
        BASE64_en(res)
    elif choose1==32:
        BASE32_en(res)
    else:
        print("Error")

def choose_decrypt(res:str):
    choose1=int(input("Create choose - Base64\Base32 (64\\32)\n"))
    if choose1==64:
        BASE64_de(res)
    elif choose1==32:
        BASE32_de(res)
    else:
        print("Error")

choose = int(input("What do we do? - encrypt\decrypt (1\\2)\n"))
if choose==1:
    res = choose_text()
    choose_encrypt(res)
elif choose==2:
    fileway = choose_file()
    with open(fileway, 'r', encoding="utf-8") as decryptfile:
        res = ''
        for line in decryptfile:
            res += line
    choose_decrypt(res)
