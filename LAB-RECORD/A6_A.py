import numpy as np

# Create a 3x3 numpy array with random integers between 1 and 20
array = np.random.randint(1, 21, size=(3, 3))
print("Original Array:\n", array)

# Calculate the mean of the array
mean = np.mean(array)
print("\nMean of Array:", mean)

# Replace all elements less than 10 with 0
array[array < 10] = 0
print("\nModified Array:\n", array)