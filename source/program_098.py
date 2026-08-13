import re

text = input("Enter text: ")

numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)
