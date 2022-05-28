# Lists
#filename = "dataset/romeo.txt"
file_name = input("Enter name of file: ")
uniques=[ ]
if file_name == 'romeo.txt':
    file_exe = open('progrm9.txt')
    for line in file_exe:
        uniq = line.split()
        for word in uniq:
            if not(word in uniques):
                uniques.append(word)
uniques.sort()
print(len(uniques))
print(uniques)
MBOX=[]
count = 0
file_name = input("Enter name of file: ")
if file_name == 'p':
    file_exe = open('progrm8.txt')
    for lines in file_exe:
        if lines.startswith("From ")  :
            senders = lines.split(" ")
            print(senders[1])
            count += 1
print(f"there were {count} lines having From as a starting word.")