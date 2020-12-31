# This Student is used for get and set objects
import random

# Using slots to speed up stuff
class StudentSlots:

    grade = 8
    __slots__ = ['first_name', 'last_name']

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student:

    grade = 8
    __slots__ = [first_name, last_name]

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # def __str__(self):
    #     return f"Student: {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Student({self.first_name!r}, {self.last_name!r})"

    @property
    def name(self):
        print("Getter for the name")
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name):
        print("Setter for the name")
        self.first_name, self.last_name = name.split()

    @property
    def ager(self):
        self.age = random.randint(10, 100)
        print("Getter for age")
        return f"Age is {self.age}"

    @ager.setter
    def ager(self, ager):
        print("Setter for the age")
        self.age = ager

    # Here we are instantiating using convenience initializing
    @classmethod
    def from_dict(cls, name_info):
        fname = name_info["first_name"]
        lname = name_info["last_name"]
        return cls(fname, lname)

    # Here we are using staticmethods to create a statistic thing
    @staticmethod
    def show_duties():
        return "Study, Play, Sleep"





new_stud = Student("John", "Smith")
print(Student.grade)
print(new_stud.grade)
cls_student = Student.from_dict({"first_name":"kl", "last_name":"yal"})
print(type(cls_student))
# print(new_stud.name)
# new_stud.name = "Jonny Brochure"
# print(new_stud.ager)
# new_stud.ager = random.randint(10, 1000)


