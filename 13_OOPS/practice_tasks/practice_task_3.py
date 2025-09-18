"""
Practice Task 3:
Create a class Student with:

Private attribute __marks

Method set_marks() to assign marks

Method get_marks() to retrieve marks

Validate in set_marks() that marks are between 0 and 100

"""


class Student:

    def __init__(self, name, marks=0):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        if marks in range(0, 101):
            self.__marks = marks
        else:
            print("marks are not in range of 0 and 100")

    def get_marks(self):
        return self.__marks


s = Student("Akhil")
s.set_marks(73)
print(s.get_marks())
