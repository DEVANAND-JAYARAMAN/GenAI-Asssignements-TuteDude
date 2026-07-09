import numpy as np

array1 = np.arange(1, 11)
array2 = np.arange(1, 10).reshape(3, 3)
array3 = np.array([10, 20, 30, 40, 50])

print("Array 1")
print(array1)
print("Shape :", array1.shape)
print("Data Type :", array1.dtype)

print("----------------------")

print("Array 2")
print(array2)
print("Shape :", array2.shape)
print("Data Type :", array2.dtype)

print("----------------------")

print("Array 3")
print(array3)
print("Shape :", array3.shape)
print("Data Type :", array3.dtype)