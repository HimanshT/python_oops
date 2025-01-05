# a self is an argument that is always passes
class simpleclass:
    def __init__(self, a, b):
        self.name = a
        self.occupation = b

    def fn(self):
        print(f"{self.name}")


a = simpleclass(
    "good", "should"
)  # here we are passing three arguments , python passes ( self, 'good', 'should')
a.fn()

# Default constructor in python
# when the constructor doesn't accept any arguments from the object and has only one argument , self, in the constructor
# __init__(self):
