import numpy as np

# Slicing numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1[2:5]) # [3 4 5] as normal Python
print(np1[2: ]) # [3 4 5 6 7 8 9] till the end
print(np1[-3:-1]) # [7 8] - indicates till the end
print(np1[2:5:2]) # [3 5] with steps("2")
print(np1[::2]) # [1 3 5 7 9] Steps on the entire array

# 2d arrays
np2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(np2[1, 2]) # 8 it takes the element in position 2 of the second array(position 1)
print(np2[0:1, 1:3]) # [[2 3]] - Slices Row 0 to 1 and Columns 1 to 3
print(np2[0:2, 1:3]) # [[2 3] [7 8]] - Slices Rows 0 to 2 and Columns 1 to 3 from BOTH rows
