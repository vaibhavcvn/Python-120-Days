try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78]
    }

    df = pd.DataFrame(data)

    df["Result"] = df["Marks"].apply(
        lambda marks: "Pass" if marks >= 40 else "Fail"
    )

    print(df)

except ImportError:
    print("Pandas is not installed.")
