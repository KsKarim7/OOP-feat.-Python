# cook your dish here
from menu import Pizza,Burger,Menu,Drinks
from restaurant import Restaurant
from users import Chef,Server,Customer,Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza("Peperoni Pizza",450,'large',['meatball','onion'])
    menu.add_menu_items('pizza',pizza_1)
    pizza_2 = Pizza("Lasagnia Pizza",650,'large',['potato','shrimp'])
    menu.add_menu_items('pizza',pizza_2)
    pizza_3 = Pizza("Mushroom Pizza",350,'medium',['mashroom','tomato','oliveOil'])
    menu.add_menu_items('pizza',pizza_3)
    
    
    #burgir
    burger_1 = Burger("Naga Burger", 320, 'chicken', ['Extra Spice','sausage','red chili'])
    menu.add_menu_items("burger",burger_1)
    burger_2 = Burger("Beef Burger", 420, 'beef', ['Medium Spice','Onions','Mayo'])
    menu.add_menu_items("burger",burger_2)
    
    # drink
    coke = Drinks('Coke',40,True)
    menu.add_menu_items("drinks",coke)
    sprite = Drinks('Sprite',35,True)
    menu.add_menu_items("drinks",sprite)
    coffee = Drinks('Mocha Coffee',90,False)
    menu.add_menu_items("drinks",coffee)
    
    
    
    #show menu
    # menu.show_menu()
    
    restau = Restaurant('Delulu Food Ghor',1500,menu)
    
    
    # add add_employee
    manager = Manager("Raju", +8801, 'raju@tarc.com','Savar', 1500, "Octobar 26 2023",'core')
    restau.add_employee('manager',manager)
    chef = Chef("Fakruddin",+8802,"fakruddin@yahoo.com","bailey road", 2500,'Jan 1,2023',"Chef","almost everything")
    restau.add_employee("chef",chef)
    server = Server("Amader Server",+8803,'amdrServer@bailey.com','chipa goli',300, '27 march 2024','server')
    restau.add_employee('server',server)
    
    #show employees
    # restau.show_employees()

    #customer
    # customer 1 placing an order
    customer_1 = Customer('Speed', 6, 'ishow@khan.com', "chicago", 100000)
    order_1 = Order(customer_1, [pizza_3, coke, burger_1, pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    restau.add_order(order_1)
    # customer one paying for order_1
    restau.receive_payment(order_1, 20000, customer_1)

    print('Revenue and Balance after first customer payment: ', restau.revenue, restau.balance)

    # customer 2 placing an order
    customer_2 = Customer('Sakib Al Hasan', 6, 'king@khan.com', "banani", 100000)
    order_2 = Order(customer_2, [pizza_1, burger_2, burger_1, pizza_2, coffee])
    customer_2.pay_for_order(order_2)
    restau.add_order(order_2)
    
    # customer payment
    restau.receive_payment(order_2, 10000, customer_2)

    print('Revenue and Balance after second customer payment: ', restau.revenue, restau.balance)

    #pay rent
    restau.pay_expense(restau.rent,"Rent")
    print('After paying rent : ', restau.revenue, restau.balance, restau.expense)

    restau.pay_salary(manager)
    print(f"After paying manager's salary : , {restau.revenue}, {restau.balance}, {restau.expense}")

    
# calling main function
if __name__ == '__main__':
    main()