import pandas as pd


df = pd.read_csv("experience.csv")


print("Content of the CSV file:")
print(df)


rows, columns = df.shape
print(f"\nTotal Rows: {rows}, Total Columns: {columns}")


print(f"\nLength of the dataframe: {len(df)}")


print("\nFirst 2 rows of the dataframe:")
print(df.head(2))
