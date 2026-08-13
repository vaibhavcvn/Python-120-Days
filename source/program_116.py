try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya", "Karan"],
        "Marks": [85, 72, 91, 78, 88]
    }

    df = pd.DataFrame(data)

    highest = df.loc[df["Marks"].idxmax()]
    lowest = df.loc[df["Marks"].idxmin()]

    print("Highest scorer:")
    print(highest)

    print("\nLowest scorer:")
    print(lowest)

except ImportError:
    print("Pandas is not installed.")
