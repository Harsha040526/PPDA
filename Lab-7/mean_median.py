import numpy as np
import pandas as pd
data = [10, 12, 13, 11, 12, 14, 10] # Example dataset without outliers
data_with_outlier = [10, 12, 13, 11, 12, 14, 10, 100] # Add an extreme outlier

# Calculate mean and median for both cases
mean_without_outlier = np.mean(data)
median_without_outlier = np.median(data)
mean_with_outlier = np.mean(data_with_outlier)
median_with_outlier = np.median(data_with_outlier)

# Print results
print(f"Mean without outlier: {mean_without_outlier:.2f}")
print(f"Median without outlier: {median_without_outlier:.2f}")
print(f"Mean with outlier: {mean_with_outlier:.2f}")
print(f"Median with outlier: {median_with_outlier:.2f}")