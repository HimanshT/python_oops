"""
operator overloading is a feature in python that allows developers to redefind
the behaviour of mathematical and comparison operators for custom 
data types
"""


class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i + {self.j}j"

    def __add__(self, x):
        self.x1 = self.i + x.i
        self.x2 = self.j + x.j
        return f"{self.x1}i + {self.x2}j"


v1 = Vector(3, 5)
print(v1)

v2 = Vector(6, 7)
print(v2)

# now let's say we want to add two vector.
print(v1 + v2)  # it will be returned as string
# therefore to return as string, you can send it as
"""
def __add__(self,x):
return Vector(,)
"""


# diff operator work in different way

# __add__ , __sub__ , __mul__ , __truediv__ , __lt__
