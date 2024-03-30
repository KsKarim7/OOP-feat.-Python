from abc import ABC, abstractmethod

class Account(ABC):
    acc = {}
    def __init__(self,email,password):
        print("\nPlease Sign Up Log in to your account:")
        self.__email = email
        self.__password = password
    def signUp(self):
        Account.acc[self.__email] = self.__password
    def login(self,email,password):
        # if(self.__email == email and self.__password == password ):
        #     print("Successfully logged in you account!")
        flag = False
        if(email in Account.acc):
            if(Account.acc[email] == password):
                print("Login Successful! ")
                flag = True
                return flag
            else:
                print("Please enter the correct email or password")
                return flag
        else:
            print("No such account found with these credentials")
            return flag

class Customer(Account):
    def __init__(self, email, password):
        super().__init__(email,password)
        self.obj = Seller()
    def see_products(self):
        print("Following are the available products: ")
        for k,v in self.obj.products.items():
            print(f"{k} : {v}")
    def place_order(self,item):
        if(item not in self.obj.products):
            print("Selected item is not available in the inventory!")
        else:
            Seller.products[item] -= 1
            print("Your order has been placed successfully!")
            if(Seller.products[item] == 0):
                Seller.products.pop(item)
        

class Seller(Account):
    products = {}
    def __init__(self, email, password):
        super().__init__(email,password)
    def add_product(self,item,price):
        if(item not in Seller.products,quantity):
            Seller.products[item] = [1,price]
        else:
            Seller.products[item][0] += quantity
            Seller.products[item][1] = price
            

while(True):
    n = int(input("Press 1 for sign up as a Customer.\nPress 2 for sign up as a Seller.\nPress 3 for Login"))
    if(n == 1):
        mail = input("Enter you Email: ")
        pas = input("Enter you password: ")
        obj = Customer(mail,pas)
        obj.signUp()
        print("Your are now directed to the log in page,\n ----Please Login----\n")
        mail = input("Enter you Email: ")
        pas = input("Enter you password: ")
        flag = obj.login(mail,pas)
        if(flag == False):
            print("Your are returned to the Main Page")
            continue
        else:
            obj.see_products()
    elif(n == 2):
        mail = input("Enter you Email: ")
        pas = input("Enter you password: ")
        obj = Seller(mail,pas)
        obj.signUp()
        mail = input("Enter you Email: ")
        pas = input("Enter you password: ")
        print("Your are now directed to the log in page,\n ----Please Login----\n")
        flag = obj.login(mail,pas)
        
        if(flag == False):
            print("Your are returned to the Main Page")
            continue
        else:
            while(True):
                m = int(input("Press 1 to add products to the inventory.\nPress 2 for going back to the Main Page"))
                if(m == 1):
                    name = input("Enter product name: ")
                    price = int(input("Enter product price: "))
                    quantity = int(input("Enter product quantity: "))
                    obj.add_product(name,price,quantity)
                if(m == 2):
                    print("Your are returned to the Main Page")
                    continue  

    elif(n == 3):
        mail = input("Enter you Email: ")
        pas = input("Enter you password: ")
        # obj = Account(mail,pas)
        # obj.login(mail,pas)
        m = int(input("Your are now directed to the log in page,\n ----Please Login----\nPress 1 for Customer\nPress 2 for seller"))
        if(m == 1):
            obj = Customer(mail,pas)
            mail = input("Enter you Email: ")
            pas = input("Enter you password: ")
            flag = obj.login(mail,pas)
            if(flag == False):
                print("Your are returned to the Main Page")
                continue
            else:
                obj.see_products()
        else:
            mail = input("Enter you Email: ")
            pas = input("Enter you password: ")
            obj = Seller(mail,pas)
            flag = obj.login(mail,pas)
            if(flag == False):
                print("Your are returned to the Main Page")
                continue
            else:
                while(True):
                    m = int(input("Press 1 to add products to the inventory.\nPress 2 for going back to the Main Page"))
                    if(m == 1):
                        name = input("Enter product name: ")
                        price = int(input("Enter product price: "))
                        quantity = int(input("Enter product quantity: "))
                        obj.add_product(name,price,quantity)
                    if(m == 2):
                        print("Your are returned to the Main Page")
                        continue  


    