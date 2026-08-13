import json

student = {
    "name": "Apoorv",
    "age": 20,
    "branch": "AI & Data Science"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")
