file_name = "sample.txt"

with open(file_name, "a") as file:
    file.write("\nThis line was added later.")

print("Content appended successfully.")
