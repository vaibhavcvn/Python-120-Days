def calculate(a, b):
    return a + b, a - b, a * b, a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition, subtraction, multiplication, division = calculate(a, b)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
