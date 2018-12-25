# The Numpy array is the fundamental data structure for scikit-learn, the package we'll be using to learn ML.

# General standard convention to import numpy in this format:
import numpy as np


# a numpy array
x = np.array([0, 1, 2, 3, 4])
# print(x)

# print the dimensions of the array
# print(x.ndim)
# print the shape of the array
# print(x.shape)

# create a 2-D array
y = np.array([[0, 1, 2], [3, 4, 5]])
# a 2x3 array, notice the entire array is enclosed with in an extra pair of brackets [ ]

print(y.ndim)
print(y.shape)

# the above was manual ways of creating arrays, numpy has functions for automatically creating arrays. Common arrays
# 1) A Matrix of ones:
a = np.ones((3, 3))
# remember that (3, 3) is a tuple. a 3x3 matrix filled with ones.

# 2) A matrix of zeros:
b = np.zeros((2, 2))
# once again (2,2) is a tuple.

# 3) The identity matrix:
c = np.eye(3)
# a 3x3 identity matrix

# 4) Specified diagonal:
d = np.diag(np.array([1, 2, 3, 4]))
print(d)

# randomly generate numbers using numpy
e = np.random.rand(4)
# this is a standard uniform distribution
print(e)
