numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Index is outside the list.")

except ValueError:
    print("Please enter a valid index.")
