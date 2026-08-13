file_name = "sample.txt"

with open(file_name, "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))

for line in lines:
    print(line.strip())
