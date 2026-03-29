# UC5 – Reshape and split NumPy arrays for structured data transformation

import numpy as np


class DataProcessing:

    def numpy_reshape_split(self):
        # Create array
        arr = np.array([1, 2, 3, 4, 5, 6])

        print("Original Array:", arr)

        # Reshape to 2D
        reshaped = arr.reshape(2, 3)
        print("Reshaped (2x3):\n", reshaped)

        # Flatten back to 1D
        flattened = reshaped.flatten()
        print("Flattened:", flattened)

        # Split array
        split_arr = np.split(arr, 3)
        print("Split into 3 parts:", split_arr)


def main():
    dp = DataProcessing()
    dp.numpy_reshape_split()


if __name__ == "__main__":
    main()