# class Menu:
#     """fill in class definition here"""
# m = Menu()
# m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

'''idly 10
vada 20'''
class Menu:
    def __add__(food,num):
        orders=()
        return orders
m = Menu()
m = m + ("idly", 10) + ("vada", 20) 
print(m)
