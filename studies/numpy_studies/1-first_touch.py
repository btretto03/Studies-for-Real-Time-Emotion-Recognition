import numpy as np # Commom to import as np

# Creating a np array
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1) # [0 1 2 3 4 5 6 7 8 9]
print(np1.shape) # As we use len in Python we can use shape in with np -> (10,)

# Automatic complete
np2 = np.arange(10)
print(np2) # [0 1 2 3 4 5 6 7 8 9]

np3 = np .arange(0, 10, 2) # We can determinate the begging(0), the end(10) and the step(2)
print(np3) # [0 2 4 6 8]

np4 = np.zeros(10) # Create an array full of zeros(strings 0. not int)
print(np4) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

np5 = np.zeros((2, 10)) # Create 2 dimentional with 10 zeros each
print(np5) # Saída: [[0. 0. ... 0.] [0. 0. ... 0.]]

np6 = np.full((10), 6) # If you want to use another number not 0 we can create an array like this
print(np6) # [6 6 6 6 6 6 6 6 6 6]

np7 = np.full((2, 10), 6) # Multidimentional with another number, in this case (6)
print(np7)

my_list = [1, 2, 3, 4, 5] # We can convert python lists in np arrays
np8 = np.array(my_list)
print(np8)
print(np[8]) # We can use this notation
