import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])

x = np.where(np1 == 3)
print(x[0]) # [ 2 10]

y = np.where(np1 < 3)
print(y[0]) # [0 1]