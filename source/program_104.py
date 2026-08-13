try:
    import numpy as np

    numbers = np.array([12, 7, 25, 4, 18, 30, 9])

    print("Original:", numbers)
    print("Sorted:", np.sort(numbers))
    print("Mean:", np.mean(numbers))
    print("Median:", np.median(numbers))
    print("Standard deviation:", np.std(numbers))

except ImportError:
    print("NumPy is not installed.")
