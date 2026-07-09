import numpy as np

data = np.array([[10,20,30],[40,50,60],[70,80,90]])

print("Row Sum")
print(np.sum(data, axis = 1))

print("Column Sum")
print(np.sum(data, axis = 0))

print("Minimum")
print(np.min(data))

print("Maximum")
print(np.max(data))

print("Mean")
print(np.mean(data))