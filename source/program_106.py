try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78]
    }

    df = pd.DataFrame(data)

    print("Average marks:", df["Marks"].mean())
    print("Highest marks:", df["Marks"].max())
    print("Lowest marks:", df["Marks"].min())

except ImportError:
    print("Pandas is not installed.")
