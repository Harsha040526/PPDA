import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"5ds_salaries.csv")
df.columns
df.skew(numeric_only = True)
df.kurt(numeric_only = True)
sns.histplot(df["salary"])
plt.show()
sns.histplot(df["salary"], kde = True)
plt.show()
sns.displot(df["salary"])