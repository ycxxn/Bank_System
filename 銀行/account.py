class Account:
    def __init__(self,number,name):
        self.__number=number
        self.__name=name
        self.total=0
    
    def getNum(self):
        return self.__number

    def getName(self):
        return self.__name

    def deposit(self,money):
        self.total+=money
        

a=Account("123","Chiu")
a.deposit(1000)
print(a.total)