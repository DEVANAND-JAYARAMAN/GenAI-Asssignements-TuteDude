#this file tas2.py file cover the task numbers 4,5 and 6 as given in the google doc for the assignment

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# Task 4 : ColumnTransformer
df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

# Change column names

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# Select columns

a = ["profit", "quantity", "discount"]
b = ["category", "region", "segment"]
c = ColumnTransformer(transformers = [("num", "passthrough", a),("cat", OneHotEncoder(), b)])

d = c.fit_transform(df)
print("Column Transformer Output")
print(d)

# Task 5 : StandardScaler
df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

a = df[["profit", "quantity", "discount"]]
b = StandardScaler()
c = b.fit_transform(a)

print("\nStandard Scaler")
print(c[:5])
print("\nMean")
print(c.mean(axis = 0))
print("\nStandard Deviation")
print(c.std(axis = 0))

# Task 6 : MinMaxScaler

df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

a = df[["profit", "quantity", "discount"]]
b = MinMaxScaler()
c = b.fit_transform(a)

print("\nMin Max Scaler")
print(c[:5])
print("\nMinimum Value")
print(c.min(axis = 0))
print("\nMaximum Value")
print(c.max(axis = 0))