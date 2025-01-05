"""
The super() keyword in python is used to refer to the 
parent class. It is especially useful when a class inherits from
multiple parent classes and you want to call a method from one of the parent class

"""


class ParentClass:
    def parent_method(self):
        print("This is the parent method 1")


# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent2")


class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")
        super().parent_method()


co = ChildClass()
co.child_method()


class Employee:
    def __init__(self, name):
        self.name = name


class bench(Employee):
    def __init__(self, bench, name):
        self.bench = bench
        super().__init__(name)
