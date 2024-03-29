# cook your dish here
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        
class Customer(User):
        def __init__(self,name,phone,email,address,money):
            self.wallet = money
            self.__order = None
            self.due_amount = 0
            super().__init__(name,phone,email,address)
        
        @property
        def order(self):
            return self.__order
        
        @order.setter            
        def order(self,order):
            self.__order = order
        
        def place_order(self,order):
            self.order = order
            self.bill_due += order.bill
            print(f"{self.name} place an order with its bill {order.bill}")
        
        def eat_food(self,order):
            print(f'{self.name} item food {order.items}')
        
        def pay_for_order(self,amount):
            pass
        def give_tip(self,amount):
            pass
        
        def write_review(self,stars):
            pass
        
        
        
class Employee(User):
        def __init__(self,name,phone,email,address,salary, starting_date, department):
            super().__init__(name,phone,email,address)
            self.salary = salary
            self.starting_date = starting_date
            self.department = department
            self.due = salary
        
        def receive_salary(self):
            self.due = 0            
        
class Chef(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department,cooking_item):
        super().__init__(name,phone,email,address,salary,starting_date,department)
        self.cooking_item = cooking_item
        
class Server(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department):
        self.tips_earned = 0
        super().__init__(name,phone,email,address,salary,starting_date,department)
    
    def take_order(self,order):
        pass
    
    def transfer_order(self,order):
        pass
    
    def serve_food(self,order):
        pass
    
    def receive_tips(self,amount):
        self.tips_earned += amount
        
        
class Manager(Employee):
    def __init__(self,name,phone,email,address,salary,starting_date,department):
        self.tips_earned = 0
        super().__init__(name,phone,email,address,salary,starting_date,department)


        
        
        
        
        
        
        
        