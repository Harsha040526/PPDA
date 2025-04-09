import pandas as pd
data_x = pd.Series([0, 1, 2, 3, 4, 5])
data_y = pd.Series([0, 1, 4, 9, 16, 25])
df = pd.DataFrame({'x_value': data_x, 'square(x)': data_y})
print(df)