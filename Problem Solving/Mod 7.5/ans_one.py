# Write what is meant by operator overloading and method overriding with examples.

# -- These concepts are related to polymorphism, allows objects to behave differently on context. 
# Operator Overloading: It refers to the ability to define custom behavior for build-in operators(+,-,/,*). By overloading operators we can define how objects of a class will respond to certain operations.

class overloadingOperators:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y 
        self.z = z
    def __add__(self,other):
        return (self.x + self.y) ** other.z
    
obj1 = overloadingOperators(2,4,5)
obj2 = overloadingOperators(3,2,5)
print(obj1 + obj2)


# Method Overriding: Two different methods with same name (in subclass and superclass)  that each perform different class. Here, subclass or child class method will override parent's one.


class MP:
    def make_decision(self):
        print("There will be two percent tax in each shipment")

class CM(MP):
    def make_decision(self):
        print("There will be 2.5% tax in each shipment")

decision = CM()
CM.make_decision()



