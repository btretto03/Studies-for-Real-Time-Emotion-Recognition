import numpy as np

# 1D array, as normal Python
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for x in np1:
    print(x)

# 2D
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
for x in np2:
    for y in x:
        print(y)

# 3D
np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
for x in np3:
    #print(x)
    for y in x:
        #print(y)
        for z in y:
            print(z)
# For n dimention we need n loops

# We can use np.nditer() to save from writing all those loops
for x in np.nditer(np3):
    print(x)