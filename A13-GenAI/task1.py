import pandas as pd
import sqlite3

# Task 1 : Load Data from CSV

# Load the CSV file
df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

print("Shape of Dataset :", df.shape)
print("\nColumn Names :")
print(df.columns)

print("\nFirst 5 Rows :")
print(df.head())

print("\nLast 5 Rows :")
print(df.tail())

print("\nDataset Information :")
df.info()
print("\nSummary Statistics :")
print(df.describe())
print("\nMissing Values :")
print(df.isnull().sum())

# Task 2 : Load Data from JSON

json_df = pd.read_json("products.json")
print("\nProducts Data :")
print(json_df)

# Task 3 : Load Data from SQLite
# Connect to SQLite database using the sqlite3.connect("file_name")
connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

# Create employees table
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,name TEXT,department TEXT,salary INTEGER)""")

# Remove old records if the program is run again
cursor.execute("DELETE FROM employees")

# Insert sample records
employees = [    (1, "John", "HR", 35000),(2, "David", "Sales", 42000),(3, "Alice", "IT", 55000),(4, "Sam", "Finance", 47000),(5, "Emma", "Marketing", 39000)]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)",employees)
connection.commit()

# Read data using SQL query
employee_df = pd.read_sql_query("SELECT * FROM employees", connection)

print("\nEmployee Details :")
print(employee_df)
connection.close()