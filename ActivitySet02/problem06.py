''' Output:
    idly 10
    vada 20'''

class Menu:
    def add(self,name,amount):
        return name,amount
    def show(self):
        print(Menu.add)
m = Menu()  # Menu is a class
m.add("idli", 10)
m.add("vada", 20)
m.show()
