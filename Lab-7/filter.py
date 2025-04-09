import pandas as pd
# Create a DataFrame from a dictionary
data = {'Name': ['Ram', 'Robert','Rahim'],
'Age': [25, 30, 35],
'City': ['Ayodya', 'Chennai', 'Delhi']}
df = pd.DataFrame(data)

# Boolean values
print(df["Age"]>25,"\n")

# Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print(filtered_df,"\n")

# Filter only whose Age is 25
filtered_df = df[df["Age"].isin([35])]
print(filtered_df)
