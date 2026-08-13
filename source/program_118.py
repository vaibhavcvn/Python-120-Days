try:
    import pandas as pd

    data = {
        "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
        "Price": [55000, 25000, 30000, 2000, 1500],
        "Quantity": [2, 5, 3, 10, 8]
    }

    df = pd.DataFrame(data)

    df["Total"] = df["Price"] * df["Quantity"]

    print(df)

    print("\nTotal revenue:", df["Total"].sum())

except ImportError:
    print("Pandas is not installed.")
