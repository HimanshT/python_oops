# public access in python
# 1. By default everything is public in python


class Employee:
    def __init__(self, x, y):
        self.name = x
        self.__occupation = y  # if you add __ before a variable then it becomes private

    def show(self):
        print(f"my name is {self.name} and my work is {self.occupation}")


e1 = Employee("a", "b")

# print(e1.__occupation)  cannot be accessed directly
# can be accessed indirectly in this way  , name mangling


# Name mangling

# A technique used to protect class-private and superclass-private attributes
# from being accidently overwritten by subclasses. Names of class-private and superclass-private
# atributes are transfromed by the addition of a single leading underscore and a double
# leading underscore respectively
print(e1._Employee__occupation)


# protected access modifier is done by a single underscore before word : _variable
