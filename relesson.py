# oop объект оринтирования программирования
# 1.абстракуция
# 2.полиформизм
# 3.наследования
# 4.инкасулация

# создания класса

class car:
    
    def __init__(self,brand,model,year):
        self.a = brand
        self.b =model
        self.c =year
        
    def info(self):
        return f"{self.a} {self.b} {self.c}"
    
    
    
a = input("brand")
b =input("model")
c =input("year")
myCar =car(a,b,c) 


print(myCar.info())
        
        
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,ammount):
        self.__balance += ammount
        
    def getBalance(self):
        return self.__balance
    
a = int(input("a::::"))
b = int(input("b:::::"))
# print(type(a))
# print(type(b))
# c = a + b
# print(c)
accaunt = BankAccount(a)
accaunt.deposit(b)
print(accaunt.getBalance())







class laptop:
    def __init__(self,brand,model,price):
        self.a = brand
        self.b = model
        self.c = price
        
        
    def info(self):
        return f"{self.a} {self.b} {self.c}"
    
    
    
a = input("brand")
b = input("model")
c = input("chip")
mylaptop = laptop(a,b,c)





        
        