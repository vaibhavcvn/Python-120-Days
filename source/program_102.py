try:
    import numpy as np

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print("Matrix:")
    print(matrix)

    print("Shape:", matrix.shape)
    print("Rows:", matrix.shape[0])
    print("Columns:", matrix.shape[1])

except ImportError:
    print("NumPy is not installed.")
