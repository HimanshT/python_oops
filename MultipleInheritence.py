class Family:
    def __init__(self, familyname):
        self.familyname = familyname

    def show(self):
        print("this is family name")


class Parents:
    def __init__(self, name, property_given):
        self.lastname = name
        self.property = property_given


class Child(Family, Parents):
    def __init__(self, familyname, name, property_given):
        Family.__init__(self, familyname)
        Parents.__init__(self, name, property_given)

    def show(self):
        print(f"FamilyName : {self.familyname} Property: {self.property}")


him = Child("Gupta", "Shubh", 126)

him.show()
print(Child.mro())  # useful method to list details for a class on what it will call
