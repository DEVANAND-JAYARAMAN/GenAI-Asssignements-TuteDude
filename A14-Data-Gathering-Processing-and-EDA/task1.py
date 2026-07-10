#this file task1.py will cover the task1,2,3 as given in the google doc for the assignment
import pandas as pd
import os

# Task 1 : Creating New Features

if os.path.exists("superstore_final_dataset.csv"):
    df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")
    # Change column names
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    # Create new features
    df["total_sales"] = df["sales"] * df["quantity"]
    df["profit_ratio"] = df["profit"] / (df["sales"] + 1)
    print("New Features Added")
    print(df[["sales", "quantity", "total_sales", "profit", "profit_ratio"]].head())

else:
    print("Dataset not found")

# Task 2 : Date & Text Features

if os.path.exists("superstore_final_dataset.csv"):

    df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    # Convert date column
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Extract date values
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["day"] = df["order_date"].dt.day

    # Text feature
    df["product_length"] = df["product_name"].str.len()

    print("\nDate Features")
    print(df[["order_date", "year", "month", "day"]].head())

    print("\nText Feature")
    print(df[["product_name", "product_length"]].head())
else:
    print("Dataset not found")

# Task 3 : One Hot Encoding

if os.path.exists("superstore_final_dataset.csv"):

    df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    # Convert category columns
    a = pd.get_dummies(df,columns = ["category", "region", "segment"])
    print("\nEncoded Data")
    print(a.head())

else:
    print("Dataset not found")