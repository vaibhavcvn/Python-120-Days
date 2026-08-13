try:
    import matplotlib.pyplot as plt

    months = ["January", "February", "March", "April", "May"]
    sales = [120, 150, 180, 140, 200]

    plt.plot(months, sales, marker="o")

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.show()

except ImportError:
    print("Matplotlib is not installed.")
