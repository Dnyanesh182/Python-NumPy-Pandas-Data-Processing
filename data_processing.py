# UC10 – Perform aggregation and group-by operations for data analysis and summarization

import pandas as pd


class DataProcessing:

    def pandas_groupby_aggregation(self):
        data = {
            "Department": ["IT", "HR", "IT", "HR", "Finance"],
            "Employee": ["A", "B", "C", "D", "E"],
            "Salary": [50000, 40000, 60000, 45000, 70000]
        }

        df = pd.DataFrame(data)
        print("Original DataFrame:\n", df)

        # GroupBy with sum
        print("\nSalary Sum by Department:\n", df.groupby("Department")["Salary"].sum())

        # GroupBy with mean
        print("\nAverage Salary by Department:\n", df.groupby("Department")["Salary"].mean())

        # GroupBy with count
        print("\nEmployee Count by Department:\n", df.groupby("Department")["Employee"].count())

        # Multiple aggregations
        print("\nMultiple Aggregations:\n",
              df.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"]))


def main():
    dp = DataProcessing()
    dp.pandas_groupby_aggregation()


if __name__ == "__main__":
    main()