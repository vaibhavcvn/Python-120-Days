try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Math": [85, 72, 91, 78],
        "Python": [92, 80, 88, 90],
        "Statistics": [78, 75, 95, 82]
    }

    df = pd.DataFrame(data)

    df["Average"] = df[["Math", "Python", "Statistics"]].mean(axis=1)

    df["Result"] = df["Average"].apply(
        lambda x: "Pass" if x >= 40 else "Fail"
    )

    print(df)

except ImportError:
    print("Pandas is not installed.")
