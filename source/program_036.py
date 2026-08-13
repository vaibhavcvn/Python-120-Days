numbers = [10, 20, 30, 20, 40, 20, 50]

value = int(input("Enter value to search: "))

if value in numbers:
    print("Value found")
    print("Occurrences:", numbers.count(value))
else:
    print("Value not found")
