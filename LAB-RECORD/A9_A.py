import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('3Salary_Data.csv')

print(data.head())

if 'Experience' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Experience'], kde=True, bins=20, color='blue')
    plt.title('Distribution of Employee Experience')
    plt.xlabel('Years of Experience')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("The column 'Experience' is not found in the dataset. Please check the column names.")