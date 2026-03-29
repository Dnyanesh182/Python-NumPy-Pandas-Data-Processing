# UC8 – Apply arithmetic operations and modify DataFrame columns dynamically

import pandas as pd


class DataProcessing:

    def pandas_arithmetic_modification(self):
        data = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Price": [100, 200, 150],
            "Quantity": [2, 3, 4]
        }

        df = pd.DataFrame(data)
        print("Original DataFrame:\n", df)

        # Arithmetic operation (new column)
        df["Total"] = df["Price"] * df["Quantity"]
        print("\nAfter Adding Total Column:\n", df)

        # Modify existing column
        df["Price"] = df["Price"] + 10
        print("\nAfter Updating Price:\n", df)

        # Apply function (e.g., discount)
        df["Discounted_Total"] = df["Total"].apply(lambda x: x * 0.9)
        print("\nAfter Applying Discount:\n", df)

        # Multiple column operation
        df["Final_Amount"] = df["Discounted_Total"] + 50
        print("\nFinal DataFrame:\n", df)


def main():
    dp = DataProcessing()
    dp.pandas_arithmetic_modification()


if __name__ == "__main__":
    main()