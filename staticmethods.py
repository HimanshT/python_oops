# static methods are basically functions that are inside the class but we can call them like normal functions
# we just want to ship it with class but we want to acess them normally without creating an object


class Employee:
    def __init__(self, x, y):
        self.name = x
        self.occupation = y

    def show(self):
        print(f"my name is {self.name} and my work is {self.occupation}")

    @staticmethod
    def look(x, y):
        print(f"my name is {x} and my work is {y}")


Employee.look("x", "y")

# Static methods have a very clear use-case. When we need some functionality not w.r.t an Object but w.r.t the complete class, we make a method static. This is pretty much advantageous when we need to create Utility methods as they aren’t tied to an object lifecycle usually. Finally, note that in a static method, we don’t need the self to be passed as the first argument.
