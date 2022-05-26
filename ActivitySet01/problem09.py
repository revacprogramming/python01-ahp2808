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
