import numpy as np

array1 = np.array([1,2,3,4])

array2 = np.array([5,6,7,8])

userinput = input("Do you want to subtract or add? ")

if userinput == "Add":
    array3 = array1 + array2
    print(array3)
elif userinput == "Subtract":
    array3 = array1 - array2
    print(array3)