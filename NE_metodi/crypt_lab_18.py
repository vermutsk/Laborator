import SHA
import Stribog
import crypt_lab_14 as lab14
import crypt_lab_17 as lab17
import gen_simple as gs
import random
import json
import os

def new_g(w: str, p: int):
    g = SHA.sha512(w)
    g = int(g, 16)
    g = g % p
    return g


def main():
    flag = True
    while flag:
        acc = lab14.main()
        if acc != False and acc != None:
            flag = False
    #print(acc)
    if acc != False:
        print('Пользователь А в системе')
        w = acc
        p = gs.gen_simple(16)
        g = new_g(w, p)
        key_check = lab17.modul_main(p, g)
        if key_check:
            pass
        else:
            print('Ошибка доступа')
            return -1
    else:
        exit()


if __name__ == '__main__':
    main()