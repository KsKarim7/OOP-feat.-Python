# Write down 4 differences between the class method and static method with proper examples.

# Class Method: Has access to class attributes and can modify then.Uses cls as the first parameter.They are defined using @classmethod decorator.Class methods can be overridden in subclasses, and they will behave like regular instance methods in the subclass.

# Static Method: Doesn't have access to class attributes. Doesn't have any default parameter and behaves like a usual function.They are defined using @staticmethod decorator.Static methods, on the other hand, cannot be overridden in subclasses and will behave the same way as they do in the base class.


class myClass:
    var = 10

    @classmethod
    def class_method(cls):
        cls.var += 1
        print(cls.var)

    @staticmethod
    def static_method():
        print("Static Method")

class sub_class:
    sub_var = 12

    @classmethod
    def subClass_method(cls):
        print(cls.sub_var)

    @staticmethod
    def subStatic_method():
        print("Static Method")