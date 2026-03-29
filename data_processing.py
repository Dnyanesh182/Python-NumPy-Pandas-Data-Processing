# UC3 – Perform mathematical operations on NumPy arrays using vectorized computations

import numpy as np


class DataProcessing:

    def numpy_vectorized_operations(self):
        arr1 = np.array([10, 20, 30, 40])
        arr2 = np.array([1, 2, 3, 4])

        print("Array 1:", arr1)
        print("Array 2:", arr2)

        # Arithmetic operations
        print("Addition:", arr1 + arr2)
        print("Subtraction:", arr1 - arr2)
        print("Multiplication:", arr1 * arr2)
        print("Division:", arr1 / arr2)

        # Scalar operations
        print("Add 5:", arr1 + 5)
        print("Multiply by 2:", arr1 * 2)

        # Built-in functions
        print("Sum:", np.sum(arr1))
        print("Mean:", np.mean(arr1))
        print("Min:", np.min(arr1))
        print("Max:", np.max(arr1))
        print("Square Root:", np.sqrt(arr1))


def main():
    dp = DataProcessing()
    dp.numpy_vectorized_operations()


if __name__ == "__main__":
    main()