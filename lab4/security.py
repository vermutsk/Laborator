import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Cipher._mode_eax import EaxMode

def publick():
    with open('rsa_public.pem','r',encoding='utf-8') as pub_key:
        file=pub_key.read()
    file=file.encode("utf-8")
    return file

def private():
    with open('private_rsa_key.bin','r',encoding='utf-8') as priv_key:
        file=priv_key.read()
    file=file.encode("utf-8")
    return file

def publick_ordinary(way:str):
    way_new=os.path.join(way,"rsa_public.pem")
    with open(way_new,'r',encoding='utf-8') as pub_key:
        file=pub_key.read()
    file=file.encode("utf-8")
    return file

def private_ordinary(way:str):
    way_new=os.path.join(way,"Keys","private_rsa_key.bin")
    with open(way_new,'r',encoding='utf-8') as priv_key:
        file=priv_key.read()
    file=file.encode("utf-8")
    return file

def check_password(hashed_password:str, user_password:str):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def hash_password(password:str):
    salt ="zakharchenko.dvfu@.ru"
    salt_b=b"zakharchenko.dvfu@.ru"
    return hashlib.sha256(salt_b + password.encode('utf-8')).hexdigest() + ':' + salt


def generate_keys(way:str):
    code = 'booooooobs'
    key = RSA.generate(1024)

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
 

def security_files(way:str,name_file:str):
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

        cipher_aes: EaxMode = AES.new(session_key, AES.MODE_EAX)# type: ignore
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
   
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)


def security_sys_files(name_file:str):
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

        cipher_aes: EaxMode = AES.new(session_key, AES.MODE_EAX)# type: ignore
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
   
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)



def decode_files(way:str,name_file:str):
    code = 'booooooobs'
    with open(name_file, 'rb') as fobj:
        private_key = RSA.import_key(
            private_ordinary(way),
             passphrase=code
         )
        
        enc_session_key, nonce, tag, ciphertext = [
            fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]
      
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes: EaxMode = AES.new(session_key, AES.MODE_EAX,nonce)# type: ignore
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    with open(name_file,'wb') as out_file:
        out_file.write(data)


def decode_sys_files(name_file:str):
    code = 'booooooobs'
    with open(name_file, 'rb') as fobj:
        private_key = RSA.import_key(
            private(),
             passphrase=code
         )
        
        enc_session_key, nonce, tag, ciphertext = [
            fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]
      
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes: EaxMode = AES.new(session_key, AES.MODE_EAX,nonce)# type: ignore
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    with open(name_file,'wb') as out_file:
        out_file.write(data)

