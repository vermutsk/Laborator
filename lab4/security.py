import os
import hashlib
import random
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Cipher._mode_eax import EaxMode
_iv = b'help_me_please__'

def _fill_random_bytes(bytes_str: bytes, length: int)-> bytes:
    while len(bytes_str) % length != 0: 
        symbol = bytes()
        if len(bytes_str) > 0:
            pos = random.randint(0, len(bytes_str))
            symbol = bytes_str[pos: pos + 1]
        bytes_str += symbol
    return bytes_str

def publick()->bytes:
    with open('rsa_public.pem','r',encoding='utf-8') as pub_key:
        file=pub_key.read()
    file1=file.encode("utf-8")
    return file1

def private()->bytes:
    with open('private_rsa_key.bin','r',encoding='utf-8') as priv_key:
        file=priv_key.read()
    file1=file.encode("utf-8")
    return file1

def publick_ordinary(way:str)->bytes:
    way_new=os.path.join(way,"rsa_public.pem")
    with open(way_new,'r',encoding='utf-8') as pub_key:
        file=pub_key.read()
    file1=file.encode("utf-8")
    return file1

def private_ordinary(way:str)->bytes:
    way_new=os.path.join(way, "private_rsa_key.bin")
    with open(way_new,'r',encoding='utf-8') as priv_key:
        file=priv_key.read()
    file1=file.encode("utf-8")
    return file1

def check_password(hashed_password:str, user_password:str)->bool:
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def hash_password(password:str)->str:
    salt ="eyafjallajokulll"
    salt_b=b"eyafjallajokulll"
    return hashlib.sha256(salt_b + password.encode('utf-8')).hexdigest() + ':' + salt

def generate_keys(way:str)->None:
    print("Генерация ключей...")
    code = 'helphelphe'
    key = RSA.generate(4096)

    encrypted_key = key.exportKey(
        passphrase=code, 
        pkcs=8, 
        protection="scryptAndAES128-CBC"
    )

    with open(os.path.join(way,'rsa_public.pem'), 'wb') as file_key:
        file_key.write(key.publickey().exportKey())
    security_sys_files(os.path.join(way,'rsa_public.pem')) 

    with open(os.path.join(way,'private_rsa_key.bin'), 'wb') as file_key: 
        file_key.write(encrypted_key)
    security_sys_files(os.path.join(way,'private_rsa_key.bin')) 

def security_files(way:str,name_file:str)->None:
    data: bytes=b''
    with open(name_file,'rb') as some_file:
        data=some_file.read()
    with open(name_file, 'wb') as out_file:

        recipient_key = RSA.import_key(
            publick_ordinary(way)
        )
        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        
        len_block = len(data).to_bytes(length=16, byteorder='big')
        data = len_block + data
        data = _fill_random_bytes(data, 16)
        
        cipher_aes = AES.new(session_key, AES.MODE_CBC, _iv)
        ciphertext = cipher_aes.encrypt(data)
        
        out_file.write(ciphertext)

def security_sys_files(name_file:str)->None:
    data:bytes=b''
    with open(name_file,'rb') as some_file:
        data=some_file.read()
    with open(name_file, 'wb') as out_file:
        recipient_key = RSA.import_key(
            publick()
            )
   
        session_key = get_random_bytes(16)
   
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        
        len_block = len(data).to_bytes(length=16, byteorder='big')
        data = len_block + data
        data = _fill_random_bytes(data, 16)
        
        cipher_aes = AES.new(session_key, AES.MODE_CBC, _iv)
        ciphertext = cipher_aes.encrypt(data)
        
        out_file.write(ciphertext)

def decode_files(way:str,name_file:str)->None:
    code = 'helphelphe'
    with open(name_file, 'rb') as fobj:
        private_key = RSA.import_key(
            private_ordinary(way),
             passphrase=code
         ) 
        enc_session_key, ciphertext = [
            fobj.read(x) for x in (private_key.size_in_bytes(), -1)
        ]  
        
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)  
        
        cipher_aes = AES.new(session_key, AES.MODE_CBC, _iv)

        data = cipher_aes.decrypt(ciphertext)
        size = int.from_bytes(data[:16], byteorder='big')
        data = data[16:size + 16]
    
    with open(name_file,'wb') as out_file:
        out_file.write(data)



def decode_sys_files(name_file:str)->None:
    code = 'helphelphe'
    with open(name_file, 'rb') as fobj:
        private_key = RSA.import_key(
            private(),
             passphrase=code
         )
        
        enc_session_key, ciphertext = [
            fobj.read(x) for x in (private_key.size_in_bytes(), -1)
        ]
      
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)  
        
        cipher_aes = AES.new(session_key, AES.MODE_CBC, _iv)

        data = cipher_aes.decrypt(ciphertext)
        size = int.from_bytes(data[:16], byteorder='big')
        data = data[16:size + 16]
    
    with open(name_file,'wb') as out_file:
        out_file.write(data)

