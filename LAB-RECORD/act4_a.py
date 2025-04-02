import pandas as pd

# Read the CSV file (Replace 'experience.csv' with your actual file name)
df = pd.read_csv("experience.csv")

# Display the last 3 rows only
print("Last 3 rows of the dataframe:")
print(df.tail(3))

# Display the description and information of the dataframe
print("\nDescription of the dataframe:")
print(df.describe())

print("\nInformation about the dataframe:")
print(df.info())

# Display the column names
print("\nColumn names:")
print(df.columns.tolist())
