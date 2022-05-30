reqdlist = []
senders = dict()
text_name = input("Enter the name of file: ")
if text_name == "p":
    text_exe = open('progrm8.txt')
    for lines in text_exe:
        if lines.startswith('From '):
            words = lines.split()
            if words[1] not in senders:
                senders[words[1]] = 1
            else:
                senders[words[1]] += 1
for tpl in senders:
    reqdlist.append((senders[tpl],tpl))
reqdlist.sort()
print(reqdlist[-1])
