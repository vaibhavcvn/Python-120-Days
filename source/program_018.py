number = int(input("Enter a number: "))

print("Factors:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
