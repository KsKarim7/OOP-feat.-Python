from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,email,password):
        print("\nPlease Sign Up to your account:")
        self.__email = email
        self.__password = password

    def login(self,email,password):
        if(self.__email == email and self.__password == password ):
            print("Successfully logged in you account!")

class Customer(Account):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.obj = Sellers()
    def see_products(self):
        for k,v in self.obj.products.items():
            print(f"There are {v} numbers of {k} are available.")
    def place_order(self,item):
        if(item not in self.obj.products):
            print("Selected item is not available in the inventory!")
        else:
            Sellers.products[item] -= 1
            print("Your order has been placed successfully!")
        

class Sellers(Account):
    products = {}
    def __init__(self, email, password):
        super().__init__(email, password)
    def publish_products(self,item):
        if(item not in Sellers.products):
            Sellers.products[item] = 1
        else:
            Sellers.products[item] += 1

obj = Account()
    