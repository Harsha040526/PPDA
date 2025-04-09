import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"3Salary_Data.csv")
plt.scatter(df['YearsExperience'], df['Salary'])
plt.ylabel('YearsExperience')
plt.xlabel('Index')
plt.legend()
plt.show()
sns.scatterplot(x = df['Salary'], y = df['YearsExperience'])
plt.show()