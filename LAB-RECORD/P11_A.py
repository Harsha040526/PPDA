import pandas as pd
df = pd.read_csv(r"3Salary_Data.csv")
df

from sklearn.model_selection import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_data1 = pd.DataFrame(scaled_data, columns=df.columns)
scaled_data1