def inp():
    x=input('Enter the total no. of strings: ')
    return int(x)

def inp_str():
    l=int(input('Enter the length of the string: '))
    str = input("Enter the string with specified length: ")
    if len(str) >l | len(str)<l :
        print('Enter string with specified length only')
    return str

def verifpal(r):
    x=len(r)-1
    r2 = ''
    while x>=0 :
        r2+=f'{r[x]}'
        x-=1
    if (r)==r2:
            return(r)

def list_of_str(str):   #returns list with string broke in increasing order of elements 
    pals=''
    pls3=[]
    for x in str:
        pals+=x
        if len(pals)>=3:
            pls3.append(pals)
    return pls3

def list_of_pals(str):
    pls6=[]
    for x in str:
        pls5=[]
        pls5.append(list_of_str(str))
        str=str.removeprefix(x)
        for x in pls5:
            for D in x:
                if verifpal(D)!= None:
                    pls6.append(verifpal(D))
    return pls6

def main():
    x = inp()
    z=0
    while z<x:
        str = inp_str()
        reqdpals=list_of_pals(str)
        print(reqdpals)
        for X in reqdpals:
            print(str.index(X,str[X])+1,X)
        z+=1
try:
    main()
except ValueError:
    print('Invalid input bro')
except TypeError:
    print('PROCESS OVER BRO')