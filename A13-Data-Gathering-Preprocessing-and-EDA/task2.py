# task2.py

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Task 4 - TMDB API Mini Project

print("Task 4 - TMDB API\n")
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
url = "https://api.themoviedb.org/3/movie/popular"
params = {"api_key": api_key,"language": "en-US","page": 1}

response = requests.get(url, params=params)
data = response.json()
movies = []
for movie in data["results"]:
    movies.append({
        "Title": movie["title"],
        "Release Date": movie["release_date"],
        "Rating": movie["vote_average"],
        "Popularity": movie["popularity"],
        "Language": movie["original_language"]})

movies_df = pd.DataFrame(movies)

print("\nPopular Movies\n")
print(movies_df.head())

movies_df.to_csv("tmdb_movies.csv", index=False)

print("\ntmdb_movies.csv created successfully.")

# Task 5 - Understanding the Data
print("\n==============================")
print("Task 5 - Understanding the Data")
print("==============================\n")

df = pd.read_csv("superstore_final_dataset.csv", encoding="unicode_escape")

print("Dataset Shape:")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nNumerical Columns")
print(df.select_dtypes(include="number").columns.tolist())

print("\nCategorical Columns")
print(df.select_dtypes(exclude="number").columns.tolist())

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary Statistics")
print(df.describe(include="all"))

print("\nDuplicate Rows:", df.duplicated().sum())

# Task 6 - Data Cleaning
print("\n==============================")
print("Task 6 - Data Cleaning")
print("==============================\n")

# Fill missing numerical values
num_cols = df.select_dtypes(include="number").columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing categorical values
cat_cols = df.select_dtypes(exclude="number").columns

for col in cat_cols:
    df[col] = df[col].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df.columns = (df.columns.str.lower().str.replace(" ", "_"))

# Fix date columns
if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"])

if "ship_date" in df.columns:
    df["ship_date"] = pd.to_datetime(df["ship_date"])

print("Cleaning completed.\n")
print(df.head())
print("\nColumn Names")
print(df.columns)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nFinal Shape")
print(df.shape)
print("\nTask 4, Task 5 and Task 6 completed successfully.")