import numpy as np
import pandas as pd
from numpy import random as ra



#############
### NUMPY ###
#############



# ARRAYS #
print("ARRAYS:\n\n")

# 1D array:
np_array_1d = np.array([1, 2, 4, 9, 16, 25])

print("1D ARRAY:\n")
print(np_array_1d)
print("Type:", type(np_array_1d))
print("Dimension:", np_array_1d.ndim)    # ndim stands for "n" dimension.
print("\n\n")

# 2D array:
np_array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    # Arrays must be a consistent shape.

print("2D ARRAY:\n")
print(np_array_2d)
print("Type:", type(np_array_2d))
print("Dimensions:", np_array_2d.ndim)
print("Shape:", np_array_2d.shape)
print("\n\n")

#3D array:
np_array_3d = np.array([
    [[10, 11], [14, 15]],
    [[9, 8], [7, 6]],
    [[18, 8], [15, 16]],
    [[29, 38], [17, 66]],
])

print("3D ARRAY:\n")
print(np_array_3d)
print("Type:", type(np_array_3d))
print("Dimensions:", np_array_3d.ndim)
print("Shape:", np_array_3d.shape)
print("\n\n")

# 0D array:
np_array_0d = np.array(42)    # )D arrays use round brackets only

print("0D ARRAY:\n")    # A 0D array acts like a scalar value.
print(np_array_0d)
print("Type:", type(np_array_0d))
print("Dimensions:", np_array_0d.ndim)
print("Shape:", np_array_0d.shape)
print("\n\n\n")

# Indexing and slicing:
print("INDEXING AND SLICING:\n")
print("3rd element of the 1D array:", np_array_1d[2])
print("2nd row, 3rd element of the 2d array:", np_array_2d[1, 2])    # Row first, element second.
print("1st row, last element of the 2d array:", np_array_2d[0, -1])
print("3rd row, first 2 elements of the 2d array:", np_array_2d[2, 0:2])
print("\n\n\n")

# Reshaping:
array_1 = np.array([1, 2, 3, 2, 4, 6, 3, 6, 9, 4, 8, 12])
array_reshaped = array_1.reshape(4, 3)

print("RESHAPING ARRAYS:\n")
print("Original array\n:", array_1)
print("\nReshaped 4x3:\n", array_reshaped)
print("\nReshaped ?x4:\n", array_1.reshape(-1, 4))    # When the number of dimensions is unknown.
print("\nReshaped 2x?:\n", array_1.reshape(2, -1))
print("\nReshaped 6x?:\n", array_1.reshape(6, -1))

# Flattening an array:
print("\n\n\nFLATTENING ARRAYS:\n")
print("Flattened 3d array:", np_array_3d.reshape(-1))



