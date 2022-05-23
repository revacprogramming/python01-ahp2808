# Loops & Iterators
#program for calc. count and avg of input values
count = 0
sum = 0
try:
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        sum += int(num)
        count += 1
    print(count,sum,sum/count)
except ValueError :     
    print('invalid entry')

#program for largest and smallest values
numbers = []
try:
    while True:
        num = input('Enter the number:')
        numbers.append(int(num))
        if num == "done":
            break
except ValueError:
    print("Process ended")
print(numbers)
numbers.sort()
print(numbers)
print(f'largest number is {numbers[-1]}')
print(f'smallest number is {numbers[0]}')

