import os
import math
import timeit
from sys import argv
import multiprocessing as mp

def atkin(limit: int, number: int):
    print(f"{number} процесс начал работу")
    way = f"{number}.txt"
    status = f"{number} процесс завершил работу"
    i=number
    sieve = [False] * (limit+1)
    for x in range(i, int(math.sqrt(limit)) + 1, 3):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and n % 5 != 0 and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 5 != 0 and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 5 != 0 and n % 12 == 11:
                sieve[n] = not sieve[n]
    with open(way, "w", encoding='utf-8') as file_atkin:
        for x in sieve:
            string = str(x) + '\n'
            file_atkin.write(string)
    print(status + '\n')

def read_files():
    print("start read 1")
    with open('1.txt','r',encoding='utf-8') as file_1:
        first_read = file_1.read()
        list_1 = first_read.split("\n")
    print("start read 2")
    with open('2.txt','r',encoding='utf-8') as file_2:
            first_read = file_2.read()
            list_2 = first_read.split("\n")
    print("start read 3")
    with open('3.txt','r',encoding='utf-8') as file_3:
        first_read = file_3.read()
        list_3 = first_read.split("\n")
    list_123=[False]*len(list_1)
    len_list=len(list_1)
    for i in range(0,len_list):
        if list_1[i]=="False":
            a=False
        else: a=True
        if list_2[i]=="False":
            b=False
        else: b=True
        if list_3[i]=="False":
            c=False
        else: c=True
        list_123[i]=(a+b+c)%2
    list_4=[False]*len(list_123)
    for index, x in enumerate(list_123):
        if x==1:
            list_4[index]=index
    for x in range(5, int(math.sqrt(len(list_123)))):
        if list_4[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                list_4[y] = False
    way = os.getcwd()
    os.unlink(os.path.join(way, "1.txt"))
    os.unlink(os.path.join(way, "2.txt"))
    os.unlink(os.path.join(way, "3.txt"))
    return list_4

if __name__ == '__main__':
    try:
        if int(argv[1]) > 0:
            pass
        elif int(argv[1]) < 0 or int(argv[1]) == 0:
            raise Exception
        else:
            raise Exception
        limit = int(argv[1])
        with mp.Pool(processes=3) as pool:
            p = pool.starmap(atkin,iterable=[[limit, 1],[limit, 2],[limit, 3]],)
        time_list = read_files()
        while len(time_list)>limit:
            time_list.pop()
        result=list()
        for index, elem in enumerate(time_list):
            if elem is not False:
                result.append(elem)
        result.sort()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for i in result:
                str0 = ''+str(i)+"\n"
                file.write(str0)
        print(f"Время работы:{timeit.default_timer()}сек\n")
    except FileNotFoundError:
        pass
    except Exception:
        print("Ошибка")
    except BaseException:
        print("^C")
