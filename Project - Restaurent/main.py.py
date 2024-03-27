# cook your dish here
from menu import Pizza,Burger,Menu,Drinks
from restaurent import Restaurent
from restaurent import Restaurent
from Users import chef,customer,server,customer,manager

def main():
    menu = Menu()
    pizza_1 = Pizza("Peperoni Pizza",450,'large',['meatball','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza("Lasagnia Pizza",650,'large',['potato','shrimp'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza("Mushroom Pizza",350,'medium',['mashroom','tomato','oliveOil'])
    menu.add_menu_item('pizza',pizza_3)
    
    
    #burgir
    burger_1 = Burger("Naga Burger", 320, 'chicken', ['Extra Spice','sausage','red chili'])
    menu.add_menu_item("burger",burger_1)
    burger_2 = Burger("Beef Burger", 420, 'beef', ['Medium Spice','Onions','Mayo'])
    menu.add_menu_item("burger",burger_2)
    
    # drink
    coke = Drinks('Coke',40,True)
    menu.add_menu_item("drinks",coke)
    spite = Drinks('Sprite',35,True)
    menu.add_menu_item("drinks",sprite)
    coffee = Drinks('Mocha Coffee',90,False)
    menu.add_menu_item("drinks",sprite)
    
    
    
    #show menu
    menu.show_menu()
    
    restau = Restaurent('Delulu Food Ghor',1500,menu)
    
    
    # add add_employee
    manager = manager("Raju", +880, 'raju@tarc.com','Savar', 1500, "Octobar 26 2023",'core')
    restau.add_employee('manager',manager)
    chef = chef("Fakruddin",+880,"fakruddin@yahoo.com","bailey road", 2500,'Jan 1,2023',"Chef","almost everything")
    restau.add_employee("chef",chef)
    server = Server("Amader Server",+880,'amdrServer@bailey.com','chipa goli',300, '27 march 2024','server')
    restau.add_employee('server',server)
    
    #show employeed
    restau.show_employees()
    
# calling main function
if __name__ == '__main__':
    main()