def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
b = float(input("Enter second number: "))

result = calculator(a, b, operation)

print("Result:", result)
