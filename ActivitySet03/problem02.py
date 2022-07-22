from fractions import Fraction
def inp():
    x=input('enter the no. of unit fractions: ')
    return int(x)

def inp_fract(x):
    fract=[]
    str = input('Enter denominators of unit fraction: ')
    str1 = str.split()
    for y in str1:
        fract.append(int(y))
    if len(fract)>x | len(fract)<x :
        print('')    
    return fract

def sum_of_fract(fract):
    sum = 0
    str=''
    for x in fract:
        sum+= Fraction(1,x)
        str += f'{Fraction(1,x)} + '
    str = str.removesuffix('+ ')
    str += f'= {sum}'
    return str 

def main():
    no_of_Egyp_fract = inp()
    list_of_denom=inp_fract(no_of_Egyp_fract)
    Sum_of_Egyp_fract = sum_of_fract(list_of_denom)
    print(Sum_of_Egyp_fract)
if __name__ == '__main__':
    main()
'''
input : 2
    10 20
output :
1/10+1/20=3/20
'''        