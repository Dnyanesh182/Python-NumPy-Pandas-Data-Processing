# UC4 – Apply slicing and indexing techniques on NumPy arrays for data extraction

import numpy as np


class DataProcessing:

    def numpy_slicing_indexing(self):
        # 1D Array
        arr = np.array([10, 20, 30, 40, 50])

        print("Array:", arr)

        # Indexing
        print("First Element:", arr[0])
        print("Last Element:", arr[-1])

        # Slicing
        print("Slice (1:4):", arr[1:4])
        print("Every 2nd element:", arr[::2])

        # 2D Array
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

        print("Matrix:\n", matrix)

        # Indexing
        print("Element (1,2):", matrix[1][2])

        # Slicing rows
        print("First two rows:\n", matrix[0:2])

        # Slicing columns
        print("First column:", matrix[:, 0])

        # Sub-matrix
        print("Sub-matrix:\n", matrix[0:2, 1:3])


def main():
    dp = DataProcessing()
    dp.numpy_slicing_indexing()


if __name__ == "__main__":
    main()