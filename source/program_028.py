text = input("Enter a string: ")

result = ""

for char in text:
    if char != " ":
        result += char

print("Without spaces:", result)
