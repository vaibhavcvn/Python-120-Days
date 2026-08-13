import random

balance = 1000

print("Simple Bank Simulation")
print("Starting balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("Thank you for using the bank simulation.")
        break

    else:
        print("Invalid option.")
