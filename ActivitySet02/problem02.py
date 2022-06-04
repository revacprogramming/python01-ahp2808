# def main():
#     a, b = input_two_numbers()
#     sum = add(a, b)
#     output(a, b, sum)
# if __name__ == '__main__': main()
def add(a,b) :
    return a+b
def output(a,b,sum) :
    print(f"{a} + {b} = {sum}")
def main():
    a, b = input("enter the numbers").split()
    sum = add(int(a),int(b))
    output(a,b,sum)
if __name__ == '__main__' :
    main()