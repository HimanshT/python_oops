"""
Redefine a method in the derived class.
"""


class ParentClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class BaseClass(ParentClass):
    def __init__(self, r):
        self.r = r
        super().__init__(r, r)

    def area(self):
        return 3.14 * super().area()


bc = BaseClass(6)
print(bc.area())
