import numpy as np
from NorthStar import north_west

import numpy as np

# Create a 2D array
arr = np.array([[5, 3, 8],
                [2, 7, 4],
                [6, 1, 9]])

# Find the indices of the minimum element
i, j = np.unravel_index(np.argmin(arr), arr.shape)

print("Indices of the minimum element:")
print(i, j)

a = np.array([[1, 2]])
b = np.array([[4],
              [5]])
print(a + b)

assert north_west(np.array([140, 180, 160]), np.array([[2, 3, 4, 2, 4],
                                                       [8, 4, 1, 4, 1],
                                                       [9, 7, 3, 7, 2]]), np.array([60, 70, 120, 130, 100])) == 1380


