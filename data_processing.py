# UC1 – Create and Manipulate 1D NumPy Arrays

import numpy as np


class DataProcessing:

    def numpy_1d_operations(self):
        # Create 1D array
        arr = np.array([10, 20, 30, 40, 50])
        print("Original Array:", arr)

        # Access element
        print("First Element:", arr[0])

        # Modify element
        arr[1] = 25
        print("Updated Array:", arr)

        # Mathematical operations (vectorized)
        print("Array + 5:", arr + 5)
        print("Array * 2:", arr * 2)

        # Built-in functions
        print("Sum:", np.sum(arr))
        print("Mean:", np.mean(arr))
        print("Max:", np.max(arr))


def main():
    dp = DataProcessing()
    dp.numpy_1d_operations()


if __name__ == "__main__":
    main()