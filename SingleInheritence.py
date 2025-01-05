class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def details(self):
        print("These are school details")


class Section(School):
    def __init__(self, name, students):
        School.__init__(self, name, location="Palampur")
        self.students = students

    def details(self):
        print(f"{self.name} {self.students}")


s1 = Section("Lal Murli school", 50)
s1.details()
print(s1.location)
print(s1.name)
