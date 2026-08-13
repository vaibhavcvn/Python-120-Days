products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Headphones": 2000,
    "Keyboard": 1500
}

total = 0

for product, price in products.items():
    print(product, ":", price)
    total += price

print("Total cost:", total)
