import numpy as np
import pandas as pd
# Create a Series from a list
data = [1, 3, 5, np.nan, 6]
s = pd.Series(data)
print(s)
# print(type(data[0]))