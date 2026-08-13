def sum_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print("Sum:", sum_numbers(10, 20, 30))
print("Sum:", sum_numbers(5, 10, 15, 20, 25))
