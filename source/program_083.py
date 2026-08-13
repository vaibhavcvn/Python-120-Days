try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid number.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")
