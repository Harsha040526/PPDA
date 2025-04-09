import numpy as np

# Create two 3x3 numpy arrays with random integers between 1 and 10
array1 = np.random.randint(1, 11, size=(3, 3))
array2 = np.random.randint(1, 11, size=(3, 3))

print("Array 1:\n", array1)
print("\nArray 2:\n", array2)

# Perform matrix subtraction
subtraction_result = array1 - array2
print("\nMatrix Subtraction Result:\n", subtraction_result)

# Perform element-wise division
division_result = np.divide(array1, array2, where = array2 != 0)
print("\nElement-wise Division Result:\n", division_result)