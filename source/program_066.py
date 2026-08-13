def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [15, 42, 8, 91, 23, 67]

print("Numbers:", numbers)
print("Largest:", find_largest(numbers))
