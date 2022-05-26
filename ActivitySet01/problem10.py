# Dictionaries
#filename = "dataset/mbox-short.txt"
num_of_days = dict()
file_name = input("Enter name of file: ")
if file_name == 'p':
    file_exe = open('progrm8.txt')
    for lines in file_exe:
        if lines.startswith("From "):
            words = lines.split()
            if words[2] not in num_of_days:
                num_of_days[words[2]] = 1
            else:
                num_of_days[words[2]] += 1
print(num_of_days)

senders_emails = dict()
file_name = input("Enter the name of file: ")
if file_name == 'p':
    file_exe = open('progrm8.txt')
    for lines in file_exe :
        if lines.startswith('From '):
            words = lines.split() 
            if words[1] not in senders_emails:
                senders_emails[words[1]] = 1
            else:
                senders_emails[words[1]] += 1
print(senders_emails)
print(len(senders_emails))
