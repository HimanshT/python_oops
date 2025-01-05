class simpleclass:
    companyname = "PA Networks"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, str):
        return cls(str.split("-")[0], str.split("-")[1])


# Simple way to initialize class
c1 = simpleclass("good", 100000)
print(f"{c1.name}  {c1.salary}")

# if i want to run costructor with diff parameters
str = "hima-19293949"
c2 = simpleclass.fromstr(str)
print(f"{c2.name}  {c2.salary}")


# we are using class methods as alternative constructors
