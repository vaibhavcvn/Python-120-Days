import json

student = {
    "name": "Apoorv",
    "age": 20,
    "branch": "AI & Data Science"
}

json_data = json.dumps(student, indent=4)

print(json_data)
