import numpy as np

# .shape tell us how many dimensions it has
np1 = np.array([0, 1, 2, 3, 4, 5])
print(np1.shape) # 6, 6 items 1 dimension

np2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(np2.shape) # (2, 5) 2 rows and 5 columns

# We can reshape 1D to 2D/3D... using reshape
np3 = np1.reshape(2, 3)
print(np3) #[[0 1 2] [3 4 5]]
print(np3.shape) #(2, 3)

np4 = np1.reshape(1,3,2)
print(np4) #[[[0 1] [2 3] [4 5]]]
print(np4.shape) #(1, 3, 2)

# Flatten to 1D
np5 = np4.reshape(-1)
print(np5) #[0 1 2 3 4 5]
print(np5.shape) #(6,)