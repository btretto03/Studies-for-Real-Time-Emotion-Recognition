import numpy as np

# Math functions of numpy
np1  = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.sqrt(np1)) # Square root of each element
print(np.abs(np1)) # Absolute value of each element
print(np.exp(np1)) # Exponential(e^x) of each value

print(np.max(np1)) # 9
print(np.min(np1)) # 1
print(np.sign(np1)) # Returns -1 for neg, 0 for zero, 1 for pos
