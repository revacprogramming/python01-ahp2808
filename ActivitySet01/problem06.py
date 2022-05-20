# Loops & Iterators
count = 0
sum = 0
while True:
    num = input("Enter a number: ")
    # if ( type(num)==int or num == "done" ) == False :
    #     print('invalid entry')
    if num == "done":
        break
    sum += int(num)
    count += 1

print(count,sum,sum/count)

