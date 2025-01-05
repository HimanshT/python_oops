class Employee:
    def __init__(self, x, y):
        self.name = x
        self.occupation = y

    def show(self):
        print(f"my name is {self.name} and my work is {self.occupation}")


hi = Employee("shubh", "software engineer")
hi.show()


class InheritedClass(Employee):
    def show1(self):
        print(f"my name is {self.name} and my work is {self.occupation}")


ht = InheritedClass("x", "jhadu pocha krne wala")

ht.show1()

# Types of Inheritence
# 1. Single Inheritence
# 2. Multiple Inheritence
# 3. Multilevel Inheritence
# 4. Hierarchical Inheritence
# 5. Hybrid Inheritence
