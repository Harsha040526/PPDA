import pandas as pd
data = {'Name': ['Ram', 'Robert','Rahim'],
'Age': [25, 30, 35],
'City': ['Ayodya', 'Chennai', 'Delhi']}
df = pd.DataFrame(data)

# Access a column
print(df["Name"],"\n")
# Accessing a row by label
print(df.loc[0],"\n")
# Access a row by index
print(df.iloc[1],"\n")
# Access a specific cell
print(df.at[0, "Age"],"\n")
# Slicing
print(df[1:3],"\n")

print(df.iloc[1],"\n")

print(df.at[2,"City"])
