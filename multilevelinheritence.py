class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def details(self):
        print("These are school details")


class Section(School):
    def __init__(self, name, section_name, students):
        School.__init__(self, name, location="Palampur")
        self.students = students
        self.section_name = section_name

    def details(self):
        print(f"{self.name} {self.students}")


class Student(Section):
    def __init__(self, schoolname, sectionname, studentname, students):
        self.studentname = studentname
        Section.__init__(self, schoolname, sectionname, students)

    def details(self):
        print(
            f"The student {self.studentname} studies in school:{self.name} in section {self.section_name}"
        )


hima = Student("DPS", "E5", "balbeer", 70)
hima.details()
