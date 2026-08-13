class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)


student = Student("Apoorv", "AI & Data Science")
student.display()
