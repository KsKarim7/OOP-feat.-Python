class Product():
    def __init__(self) -> None:
        self.item = ""
        # self.item_list = []
    def my_product(self,item):
        self.item = item

class Shop(Product):
    products = []
    def __init__(self, item) -> None:
        self.item = item
        super().__init__()
    def add_product(self):
        Shop.products.append(super().my_product(self.item))
    def buy_product(self,name):
        for i in Shop.products:
            if(i.item == name):
                print("Order Proceeded")

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.products = []

#     def add_product(self, product):
#         if isinstance(product, Product):
#             self.products.append(product)
#         else:
#             raise ValueError("Invalid product type. Expected Product, but got {}".format(type(product).__name__))

#     def __str__(self):
#         return "{}'s products: {}".format(self.name, ', '.join(product.name for product in self.products))

# # Example usage:
# my_shop = Shop('My Shop')
# my_product = Product('My Product', 10.0)
# my_shop.add_product(my_product)
# print(my_shop)