import numpy as np

# Filtering numpy arrays with boolean index lists
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = [False, True, False, True, False, True, False, True, False, True]

result = np1[x]

print("Original:", np1)
print("filtered:", result)