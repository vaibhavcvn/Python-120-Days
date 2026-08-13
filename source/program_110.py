try:
    import pandas as pd

    df = pd.read_csv("students.csv")

    print("Student data:")
    print(df)

except FileNotFoundError:
    print("students.csv was not found.")

except ImportError:
    print("Pandas is not installed.")
