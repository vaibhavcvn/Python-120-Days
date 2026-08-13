def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("Average:", calculate_average(numbers))
