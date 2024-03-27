# cook your dish here
# cook your dish here
class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.cooking_time = 15
        
class Burger(Food):
    def __init__(self,name,price,meat,ingredients):
        super().__init__(name,price)
        self.meat = meat
        self.ingredients = ingredients
        
class Pizza(Food):
    def __init__(self,name,price,size,topings):
        super().__init__(name,price)
        self.size = size
        self.topings = topings
        
class Burger(Food):
    def __init__(self,name,price,isCold = True):
        super().__init__(name,price)
        self.isCold = isCold
    
# composition    
class Menu:
    def __init__():
        self.pizzas = []
        self.burgers = []
        self.drinks = []
    
    def add_menu_items(self,item_type,item):
        if(item_type == 'pizza'):
            self.pizzas.append(item)
        elif(item_type == 'burger'):
            self.burger.append(item)
        elif(item_type == 'drinks'):
            self.drinks.append(item)
            
    def remove_pizza(self,pizza):
        if pizza in slef.pizzas:
            self.pizzas.remove(pizza)
            
    def show_menu(self):
        for pizza in self.pizzas:
            print(f"name: {pizza.name} price{pizza.price}")
        for b in self.burders:
            print(f"name: {b.name} price{b.price}")
        for d in self.drinks:
            print(f"name: {d.name} price{d.price}")
