try:
    import matplotlib.pyplot as plt

    subjects = ["Math", "Python", "Statistics", "DBMS"]
    marks = [85, 92, 78, 88]

    plt.bar(subjects, marks)

    plt.title("Subject Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.show()

except ImportError:
    print("Matplotlib is not installed.")
