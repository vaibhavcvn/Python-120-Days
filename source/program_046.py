student = {
    "name": "Apoorv",
    "age": 20,
    "branch": "AI & Data Science"
}

key = input("Enter the key to search: ")

if key in student:
    print("Value:", student[key])
else:
    print("Key not found")
