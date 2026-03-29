# UC6 – Create and manage Pandas Series and DataFrames from different data sources

import pandas as pd


class DataProcessing:

    def pandas_series_dataframe(self):
        # Series
        series = pd.Series([10, 20, 30, 40])
        print("Series:\n", series)

        # DataFrame from dictionary
        data = {
            "Name": ["Alice", "Bob"],
            "Age": [25, 30]
        }
        df_dict = pd.DataFrame(data)
        print("\nDataFrame from Dictionary:\n", df_dict)

        # DataFrame from list of records
        records = [
            {"Name": "John", "Age": 28},
            {"Name": "Jane", "Age": 32}
        ]
        df_list = pd.DataFrame(records)
        print("\nDataFrame from List:\n", df_list)

        # Read CSV
        try:
            df_csv = pd.read_csv("data.csv")
            print("\nDataFrame from CSV:\n", df_csv.head())
        except FileNotFoundError:
            print("\nCSV file not found (data.csv)")

        # Read JSON
        try:
            df_json = pd.read_json("data.json")
            print("\nDataFrame from JSON:\n", df_json.head())
        except FileNotFoundError:
            print("\nJSON file not found (data.json)")


def main():
    dp = DataProcessing()
    dp.pandas_series_dataframe()


if __name__ == "__main__":
    main()