# UC2 – Work with multi-dimensional NumPy arrays for matrix-based computations

import numpy as np


class DataProcessing:

    def numpy_2d_operations(self):
        # Create 2D arrays
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])

        print("Matrix 1:\n", matrix1)
        print("Matrix 2:\n", matrix2)

        # Access element
        print("Element at (0,1):", matrix1[0][1])

        # Addition
        print("Addition:\n", matrix1 + matrix2)

        # Element-wise multiplication
        print("Element-wise Multiplication:\n", matrix1 * matrix2)

        # Matrix multiplication
        print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))

        # Transpose
        print("Transpose:\n", matrix1.T)


def main():
    dp = DataProcessing()
    dp.numpy_2d_operations()


if __name__ == "__main__":
    main()