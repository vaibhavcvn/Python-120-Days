class Employee:
    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)


employee1 = Employee("Apoorv", 40000)
employee2 = Employee("Rahul", 35000)

employee1.display()
print()
employee2.display()
