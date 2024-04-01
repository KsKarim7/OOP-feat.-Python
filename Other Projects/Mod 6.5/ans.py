# answer no.1

def ans_one():
    print("Thought inheritance another class is used in a class which enhances reusability of code/class, extends and modifies the behavior defined in another class. New created class is called base class, superclass or parent class")

# For example

# Base class
class Vehicle:
  def move(self,name):
    print(f"Moving {name}")

# Derived class
class Motorcycle(Vehicle):
  def use_kickstand(self):
    print("Using kickstand")


# answer no.2
def ans_two():
    return f"Encapsulation is the process of bundling the data and the functions that operate on that data into a single unit, called a class. The idea to hide the implementation details of the class and expose only a minimal interface to the user.
    And Access modifiers are used to control the visibility of the class members (variables or methods) and restrict them to access. Some access modifiers are: Public Access modifier, private access modifier and protected access modifier"


class Geek:
      
     # public access modifiers: available for all
     def __init__(self, name, age):
           
           # public data members 
           self.geekName = name
           self.geekAge = age

class Student:
    
     # protected data members, only available to the derived or child classes
     _name = None
     _roll = None
     _branch = None

class Geek:
    
     # private members: only accessible within the class, it is the most secure access modifier
     __name = None
     __roll = None
     __branch = None
 
     def __init__(self, name, roll, branch):  
          self.__name = name
          self.__roll = roll
          self.__branch = branch