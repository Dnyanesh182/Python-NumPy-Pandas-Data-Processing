# UC9 – Handle missing and duplicate data with cleaning techniques in DataFrames

import pandas as pd
import numpy as np


class DataProcessing:

    def pandas_data_cleaning(self):
        data = {
            "Name": ["Alice", "Bob", "Charlie", "Alice"],
            "Age": [25, np.nan, 35, 25],
            "Salary": [50000, 60000, None, 50000]
        }

        df = pd.DataFrame(data)
        print("Original DataFrame:\n", df)

        # Detect missing values
        print("\nMissing Values:\n", df.isnull())

        # Fill missing values
        df["Age"].fillna(df["Age"].mean(), inplace=True)
        df["Salary"].fillna(0, inplace=True)
        print("\nAfter Filling Missing Values:\n", df)

        # Remove duplicates
        df_cleaned = df.drop_duplicates()
        print("\nAfter Removing Duplicates:\n", df_cleaned)


def main():
    dp = DataProcessing()
    dp.pandas_data_cleaning()


if __name__ == "__main__":
    main()