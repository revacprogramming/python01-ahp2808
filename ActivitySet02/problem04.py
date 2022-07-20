reqd_data = ['system','database','username','passwd']
def get_cs() :
    cs = input("Enter the connected string: ")
    return cs
def cs_to_lot(cs) :
    tupl_list = []
    n=0
    while n<len(reqd_data) :
        tupl_list.append((reqd_data[n],cs[n]))
        n +=1
    return tupl_list
def lot_to_cs(lot) :
    n=0
    cs=''
    while n< 4 :
        element = lot[n]
        cs += (f'{element[0]} = {element[1]}; ')
        n += 1
    return cs
def main() :
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
    cs = lot_to_cs(lot)
    print(cs)
main()