try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78]
    }

    df = pd.DataFrame(data)

    passed = df[df["Marks"] >= 40]

    print("Students who passed:")
    print(passed)

except ImportError:
    print("Pandas is not installed.")
