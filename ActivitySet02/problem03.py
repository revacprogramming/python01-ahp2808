reqd_data = ['system','database','username','password']
def get_cs() :
    cs= input("enter the values: ")
    return cs 
def cs_to_lot(cs) :
    tupl_list = []
    n=0
    while n<len(reqd_data) :
        tupl_list.append((reqd_data[n],cs[n]))
        n+=1
    return tupl_list
def main() :
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
if __name__ == '__main__':
    main() 