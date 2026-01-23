import numpy as np

# View
np1 = np.array([0, 1, 2, 3, 4, 5])
np2 = np1.view() # np2 is just a window to np1 (Shared Memory)

print(np1)
print(np2)

np1[0] = 41 # Changing original

print(np1)
print(np2) # View is also changed because they are connected

# Copy
np1 = np.array([0, 1, 2, 3, 4, 5])
np2 = np1.copy() # Creates a new independent array (New Memory)

print(np1)
print(np2)

np2[0] = 41 # Changing the copy

print(np1) # Original remains the same (Safe)
print(np2) # Only copy is changed