def in_put() :
	x = float(input("enter the number: "))
	return x
	
def add(a,b) :
    return a+b
	
def output(a,b,sum) :
    print(f"{a} + {b} = {sum}")
	
def main():
	a = in_put()
	b = in_put()
	sum = add(int(a),int(b))
	output(a,b,sum)

if __name__ == '__main__' :
    main()