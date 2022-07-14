import re
#stephen.marquard@uct.ac.za
reqd_file = open('progrm8.txt')
for item in reqd_file:
    reqd_ids = re.findall('[a-z,.]+[@]+[a-z,.]+[a-z,.]',item)
    if reqd_ids != []:
        print(reqd_ids)