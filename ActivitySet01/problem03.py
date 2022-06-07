def in_put() :
	hrs,rate = input("Enter the hours and rate : ").split()
	return hrs,rate

def computepay(hrs,rate) :
	payment = (float(hrs))*(float(rate))
	return payment

def extra_pay(hrs,rate) :
		extra_payment = computepay(hrs,rate) + ((float(hrs))-40)*(float(rate)*0.5)
		return extra_payment

def main() :
	hrs,rate = in_put()
	computepay(hrs,rate)
	if float(hrs)>40:
		extra_pay(hrs,rate)	
		print(f'The payment for Employee is {extra_pay(hrs,rate)}')
	else:
		print(f'The payment for Employee is {computepay(hrs,rate)}')

try:
	main()
except ValueError:
	print("Invalid input.Numeric entry only in the form of 'hours rate'")