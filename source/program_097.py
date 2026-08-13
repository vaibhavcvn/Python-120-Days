import json

with open("student.json", "r") as file:
    student = json.load(file)

print("Student information:")

for key, value in student.items():
    print(key, ":", value)
