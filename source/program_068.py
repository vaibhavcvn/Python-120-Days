def remove_duplicates(numbers):
    result = []

    for number in numbers:
        if number not in result:
            result.append(number)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

print("Original:", numbers)
print("Without duplicates:", remove_duplicates(numbers))
