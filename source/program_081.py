try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid input. Please enter a number.")
