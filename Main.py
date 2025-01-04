#Data Science
# Process, Analyse, Interpret, Predict

import numpy as np #numpy stands for numerical py - work with arrays (set of numbers (could be string, but most common are numbers))

sample_list = [1,2,3,4]
print(type(sample_list))

#Converting lists to arrays using np.array

sample_numpy = np.array(sample_list)
print(type(sample_numpy)) # if it comes with 'ndarray' that is n-dimensional array

name = "Dju"
print(type(name))

#Creating an array using np.array

a = np.array([10, 20, 30])# + 100, see next comment below
print(type(a))

#Arrays can perform arithmetic operation
a = a + 100
print(a)

# Homogenous - only ONE type of data permitted
# b = np.array([1,2,3],"Diego")
# print(type(b))
# print(b)

# Creating an array of all 1s and 0s (this method only works for 1 and 0)

c = np.zeros(10)
print(c)

d = np.ones(5)
print(d)

#making decimal numbers in the array

e = np.array([1,2,3,4,5,],dtype = "f")
print(e)

# Making Multi-Dimensional arrays

f = np.array([[1,2],[3,4]])
print(f)

# All the minimini brackets need to have the same number of values

# g = np.array([[1,2],[3]])
# print(g)

# Array Specs

h = np.array([[1,2],[3,4]])

print(h)

print("Array Dimension:",h.ndim) # 1D, 2D, 3D, etcetera
print("Number of rows & columns:",h.shape) # number of rows and columns
print("Number of elements:",h.size) # number of elements
print("Array size:",h.nbytes,"bytes") # Size in bytes, eg. 4 bytes