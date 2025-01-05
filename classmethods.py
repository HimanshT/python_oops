# Instance vs class variables

"""
A class method is a type of method that is bound to the class
and not the instace of class. if operates on the class as whole,
rather than on a specific instance of class.
defines with @classmethod decorater, followed by fn def
first argument is cls.
Direct access to create the class rether than instance
"""


class simpleclass:
    companyname = "PA Networks"

    def __init__(self, a):
        self.name = a

    def fn(self):
        print(f"{self.name}")

    @classmethod
    def changecompany(cls, newCompany):
        cls.companyname = newCompany


c1 = simpleclass("himanshu")
c1.fn()
c1.changecompany("youtube")
print(f"{c1.companyname}")
