# task1.py

import pandas as pd
import sqlite3
import json
# Task 1 - Load Data from CSV
print("Task 1 - Load CSV Dataset\n")

df = pd.read_csv("superstore_final_dataset.csv", encoding="unicode_escape")
print("Shape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

# Task 2 - Load Data from JSON
print("\n==============================")
print("Task 2 - Load JSON File")
print("==============================\n")
with open("products.json", "r") as file:
    products = json.load(file)
json_df = pd.DataFrame(products)
print(json_df)

# Task 3 - Load Data from SQLite

print("\n==============================")
print("Task 3 - SQLite Database")
print("==============================\n")
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER)""")
cursor.execute("DELETE FROM employees")

employees = [
    (1, "John", "HR", 35000),
    (2, "David", "Sales", 42000),
    (3, "Alice", "IT", 55000),
    (4, "Sam", "Finance", 47000),
    (5, "Emma", "Marketing", 39000)]

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)",employees)
conn.commit()
employee_df = pd.read_sql_query("SELECT * FROM employees",conn)

print(employee_df)
conn.close()
print("\nTask 1, Task 2 and Task 3 completed successfully.")