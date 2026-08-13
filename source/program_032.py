numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    value = int(input(f"Enter number {i + 1}: "))
    numbers.append(value)

print("List:", numbers)
