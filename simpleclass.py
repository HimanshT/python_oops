class Person:
    name = "himanshu"
    occupation = "software Developer"
    networth = 70

    def fn(self):
        print(
            f"{self.name} who is a {self.occupation}. His net worth is {self.networth}"
        )


a = Person()
b = Person()
a.fn()
b.name = "shubhi"
b.fn()
