try:
    import pandas as pd

    data = {
        "Name": ["Apoorv", "Rahul", "Sneha", "Riya"],
        "Marks": [85, 72, 91, 78]
    }

    df = pd.DataFrame(data)

    df.to_csv("students.csv", index=False)

    print("CSV file created successfully.")

except ImportError:
    print("Pandas is not installed.")
