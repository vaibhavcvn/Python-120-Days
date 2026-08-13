try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78]
    }

    df = pd.DataFrame(data)

    sorted_df = df.sort_values("Marks", ascending=False)

    print("Students sorted by marks:")
    print(sorted_df)

except ImportError:
    print("Pandas is not installed.")
