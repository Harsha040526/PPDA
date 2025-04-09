import numpy as np
arr_3 = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [1., 3., 5.]])
arr_tranp = arr_3.transpose()
print("Original matrix:\n", arr_3)
print("Transpose matrix:\n", arr_tranp)
# Try:
arr_3.shape
arr_3.T
arr_3.T.shape
