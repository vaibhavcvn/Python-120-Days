class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student = Student("Apoorv", 85)

print("Marks:", student.get_marks())

student.set_marks(92)

print("Updated marks:", student.get_marks())
