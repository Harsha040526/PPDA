import numpy as np
# Create a 1D array with 12 elements
arr = np.arange(24) # [0, 1, 2, ..., 11]
# Reshape into a 3x4 array
reshaped_arr = arr.reshape(6, 4)
print("Original Array (1D):\n", arr)
print("Reshaped Array (3x4):\n", reshaped_arr)
# Reshape into a 2x3x4 array (2 layers, 3 rows, 4 columns)
reshaped_arr_3D = arr.reshape(2, 3, 4)
print("Reshaped Array (2x3x4):\n", reshaped_arr_3D)
