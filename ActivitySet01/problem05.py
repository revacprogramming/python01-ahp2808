# Functions

def computepay(h,r) :
    payment = float(h)*float(r)
    extra_payment = (float(h)-40)*(float(rate)*0.5)
    if float(h)>40:
        return payment+extra_payment
    return payment

hours = float(input('Enter the hours: '))
rate = float(input('Enter the rate: '))
p = computepay(hours,rate)
print(f'Pay {p}')