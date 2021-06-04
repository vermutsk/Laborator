import Stribog as STR
import SHA
from random import randint

def n_iteration(M,method):
    Hm=M
    n=randint(2,100)
    HM_list=list()
    if method==1:
        for i in range(1,n):
            Hm=SHA.sha512(Hm)
            HM_list.append(Hm)
    elif method==2:
        for i in range(1,n):
            Hm=STR(Hm,512)
            HM_list.append(Hm)
    with open("HnList.txt","w") as txt:
        strin=""
        for i in HM_list:
            strin=strin+i+"\n"
        if method==1:
            strin = strin + "SHA 0"
        elif method==2:
            strin = strin + "STR 0"
        txt.write(strin)


def autoriz(KeyWord):
    with open("HnList.txt","r") as txt:
        hash_list=txt.read().split("\n")
    type=hash_list[-1].split()
    type_hash=type[0]
    num_enters=int(type[1])
    if num_enters>=len(hash_list)-5:
        choose=input("Need generate new password. Do it now?\nYes or No?\n>>")
        if "Yes"==choose:
            n_iteration()
        elif "No"==choose:
                pass
    Hm = KeyWord
    if type_hash == "SHA":
        for i in range(0, int(num_enters)+1):
            Hm = SHA.sha512(Hm)
        #if num_enters==0 or num_enters==1:
        #    Hm = SHA.sha512(Hm)
    elif type_hash == "STR":
        for i in range(1, int(num_enters)+1):
            Hm = STR(Hm, 512)
        #if num_enters==0 or num_enters==1:
        #    Hm = SHA.sha512(Hm)
    if Hm ==hash_list[num_enters]:
        print("Success")
        with open("HnList.txt", "w") as txt:
            strin = ""
            for i in hash_list:
                strin = strin + i + "\n"
            if type_hash == "SHA":
                strin = strin + "SHA "+str(num_enters+1)
            elif type_hash == "STR":
                strin = strin + "STR "+str(num_enters+1)
            txt.write(strin)
            return Hm
    else:
            print("bad try")
            return False

def main():
    chse=input("If u need create password - press 1\nIf u need autoriz - press 2\n")
    if chse=="1":
        M=input("Enter key word please\n>> ")
        Choose=input("SHA or Stribog?\n1 - SHA\n2 - STR\n>> ")
        n_iteration(M,int(Choose))
        print("Password generate completed")
    elif chse=="2":
        M = input("Enter key word please\n>> ")
        i = autoriz(M)
        return M

if __name__ == '__main__':
    main()
    