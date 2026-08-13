try:
    import numpy as np

    numbers = np.array([10, 20, 30, 40, 50])

    print("Original:", numbers)
    print("Add 5:", numbers + 5)
    print("Multiply by 2:", numbers * 2)
    print("Square:", numbers ** 2)

except ImportError:
    print("NumPy is not installed.")
