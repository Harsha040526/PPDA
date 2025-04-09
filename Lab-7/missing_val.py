import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4],
'B': [5, np.nan, 7, 8],
'C': [9, 10, 11, np.nan]}
df = pd.DataFrame(data)
print(df,"\n")

# Drop rows with missing values
df.fillna(0, inplace=True) # Modify df directly
print(df,"\n") # Print the modified DataFrame

# Fill missing values with the mean of the column
df["C"].fillna(df["C"].mean(), inplace=True)
print(df)