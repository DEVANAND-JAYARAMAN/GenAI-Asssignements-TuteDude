#this file task3.py will cover the task numbers such as 7,8,9 as given in the google doc for the assignment
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Task 7 : Preprocessing Pipeline

df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

a = ["profit", "quantity", "discount"]
b = ["category", "region", "segment"]
c = Pipeline([("scaler", StandardScaler())])
d = Pipeline([("encoder", OneHotEncoder())])
e = ColumnTransformer([("num", c, a),("cat", d, b)])
f = e.fit_transform(df)

print("Pipeline Output")
print(f)

# Task 8 : Full ML Pipeline

df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

x = df[["profit", "quantity", "discount", "category", "region", "segment"]]
y = df["sales"]

a = ["profit", "quantity", "discount"]
b = ["category", "region", "segment"]
c = ColumnTransformer([("num", StandardScaler(), a),("cat", OneHotEncoder(), b)])
d = Pipeline([("preprocessing", c),("model", LinearRegression())])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)
d.fit(x_train, y_train)
e = d.predict(x_test)
print("\nPredicted Sales")
print(e[:10])

# Task 9 : Pipeline Benefits

print("\n1. Why pipelines are important?")
print("Pipelines combine preprocessing and model training in one place.")
print("\n2. What problems do pipelines solve?")
print("They avoid repeating the same preprocessing steps and reduce mistakes.")
print("\n3. Manual preprocessing vs Pipeline")
print("Manual preprocessing is done step by step. Pipelines automate all the steps together.")