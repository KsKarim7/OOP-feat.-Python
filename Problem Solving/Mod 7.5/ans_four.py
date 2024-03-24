# Write what are getter and setter with proper examples

# Getter: getter methods are used to retrieve data or value of a private or protected attribute


class Getter:
    def __init__(self) -> None:
        self.__value = 007

    def get_value(self):
        return self.__value

obj = Getter()
print(obj.get_value())


# Setter: setter methods are used to modify the value of a private or protected attribute.

class Setter:
    def __init__(self):
        self.__value = 0  

    def set_value(self, new_value):
        self.__value = new_value
        
    def get_value(self):
        return self.__value

obj = Setter()
obj.set_value(10)
print(obj.get_value())  # Output: 10