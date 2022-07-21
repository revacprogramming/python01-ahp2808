#s=system;d=database;u=username;p=password
def get_cs() :
    cs= input("enter the values: ")
    return cs 

def cs_to_lot(cs) :
    tup_list = []
    for value in cs:
        value = cs.split(';')
    for ele in value:
        word = ele.split('=')
        tup =(word[1],word[0])
        tup_list.append(tup)
    return tup_list

def main() :
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)

if __name__ == '__main__':
    main()