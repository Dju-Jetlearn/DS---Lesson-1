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

#Arrays can perform arithmetic operation

a = np.array([10, 20, 30]) + 100
print(type(a))

#or

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

# g = np.array([[1,2],[3]]) THIS IS BAD
# print(g)

# Array Specs

h = np.array([[1,2],[3,4]])

print(h)

print("Array Dimension:",h.ndim) # 1D, 2D, 3D, etcetera
print("Number of rows & columns:",h.shape) # number of rows and columns
print("Number of elements:",h.size) # number of elements
print("Array size:",h.nbytes,"bytes") # Size in bytes, eg. 4 bytes

i = np.arange(1,101)
print(i)

j = np.arange(1,100,2)
print(j)

k = np.arange(2,101,2)
print(k)

l = np.random.randint(1,10)
print(l)

m = np.random.permutation(np.arange(1,11))
print("permutation : ", m)

n = np.random.rand(1,20) # generates 20 random numbers from 0 to 1
print(n)

o = np.arange(1,26).reshape(5,5) # 5 no.1 = rows, 5 no.2 = columns
print(o)

p = np.arange(1,37).reshape(1,36)
q = np.arange(1,37).reshape(2,18)
r = np.arange(1,37).reshape(3,12)
s = np.arange(1,37).reshape(4,9)
t = np.arange(1,37).reshape(6,6)
u = np.arange(1,37).reshape(9,4)
v = np.arange(1,37).reshape(12,3)
w = np.arange(1,37).reshape(18,2)
x = np.arange(1,37).reshape(36,1)

print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)
print(w)
print(x)

y = np.random.permutation(np.arange(1,101))
print(y)

z = np.sort(y)
print(z)