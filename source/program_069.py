def multiplication_table(number, limit=10):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))

multiplication_table(number)
