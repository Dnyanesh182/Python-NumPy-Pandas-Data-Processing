# UC7 – Perform DataFrame slicing, filtering, and column selection operations

import pandas as pd


class DataProcessing:

    def pandas_slicing_filtering(self):
        data = {
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Age": [25, 30, 35, 28],
            "Salary": [50000, 60000, 70000, 55000]
        }

        df = pd.DataFrame(data)
        print("Original DataFrame:\n", df)

        # Column selection
        print("\nSelect 'Name' column:\n", df["Name"])

        # Multiple columns
        print("\nSelect Name and Salary:\n", df[["Name", "Salary"]])

        # Row slicing
        print("\nFirst two rows:\n", df[0:2])

        # Filtering
        print("\nAge > 28:\n", df[df["Age"] > 28])

        # Combined filtering + column selection
        print("\nFiltered Names (Salary > 55000):\n", df[df["Salary"] > 55000]["Name"])


def main():
    dp = DataProcessing()
    dp.pandas_slicing_filtering()


if __name__ == "__main__":
    main()