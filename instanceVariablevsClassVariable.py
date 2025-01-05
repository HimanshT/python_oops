# Instance vs class variables

"""
Class variables are defined at the class level and 
are shared among all instances of the class . They are defined
outside of any method and are usually used to store info
that is common to all instances of the class.
"""


class simpleclass:
    companyname = "PA Networks"  # this is a class variable
    noofemployees = 1

    def __init__(self, a):
        self.name = a
        self.raisevalue = 1.25  # this is an instance variable
        self.noofemployees += 1

    def fn(self):
        print(f"{self.name}")
        print(f"{self.noofemployees}")


c1 = simpleclass("himanshu")
c1.fn()

# if there is instance variable , then they will refer to it else will refer to class variable
