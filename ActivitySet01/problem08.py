# Files // filename = "dataset/mbox-short.txt"
file_name = input("Enter name of file: ")
if file_name == 'progrm8.txt':
    file_exe = open('progrm8.txt')
    for lines in file_exe:
        capitalized = lines.upper()
        print(capitalized)
else:
    print("Invalid file name")
file_exe.close()
