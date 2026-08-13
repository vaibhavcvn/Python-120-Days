students = {
    "Apoorv": 85,
    "Rahul": 72,
    "Sneha": 91,
    "Riya": 78
}

highest_student = max(students, key=students.get)

print("Highest scorer:", highest_student)
print("Marks:", students[highest_student])
