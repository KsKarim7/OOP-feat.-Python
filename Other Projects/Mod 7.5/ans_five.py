# Explain the difference between inheritance and composition with proper examples.


# In OOP, both inheritance and composition are mechanisms for building relationships between classes, but they way of approaching the relation is different.

# Inheritance: It is an "is-a" relationship, where a class (subclass or derived class) inherits the properties and behaviors of another class (superclass or parent class). It is a parent-child relationship. It promotes code reuse and establishing a hierarchical relation.


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Moving at {} mph".format(self.speed))

class Car(Vehicle):
    def __init__(self, speed, car_type):
        super().__init__(speed)
        self.car_type = car_type

    def move(self):
        super().move()
        print("Car type is {}".format(self.car_type))

car = Car(50, "sedan")
car.move()


# Composition: Composition is a "has-a" relationship, where a class contains objects of other classes as attributes.It is a part-whole relationship, where a class is composed of other objects. Allows building complex objects by combining simpler ones. Enables flexibility as the behavior of the containing class is not directly tied to the behavior of the contained class.

class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()

car = Car()
car.start_car()
car.stop_car()