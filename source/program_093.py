from datetime import datetime

date_string = input("Enter date (YYYY-MM-DD): ")

date = datetime.strptime(date_string, "%Y-%m-%d")

print("Formatted date:", date.strftime("%d-%m-%Y"))
print("Year:", date.year)
print("Month:", date.month)
print("Day:", date.day)
