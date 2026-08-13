try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78],
        "Branch": ["AIDS", "CSE", "AIDS", "CSE"]
    }

    df = pd.DataFrame(data)

    result = df.groupby("Branch")["Marks"].mean()

    print("Average marks by branch:")
    print(result)

except ImportError:
    print("Pandas is not installed.")
