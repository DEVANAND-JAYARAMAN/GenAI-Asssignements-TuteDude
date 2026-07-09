import numpy as np

sales = np.array([1200,1500,900,2000,1800,1700,1600])

print("Total Weekly Sales is:", np.sum(sales))
average = np.mean(sales)

print("Average Daily Sales :", average)

print("Highest Sales :", np.max(sales))
print("Lowest Sales :", np.min(sales))
print("Standard Deviation :", np.std(sales))

print("Sales Above Average")
print(sales[sales > average])