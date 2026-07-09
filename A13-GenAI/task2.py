import pandas as pd
import requests
# Task 4 : Load Data from TMDB API

api_key = "fea516c366ad73f57dbc951bef5513ac"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"

response = requests.get(url)
movies = response.json()["results"]
movie_list = []

for movie in movies:
    movie_list.append({"Title": movie["title"],"Release Date": movie["release_date"],
        "Rating": movie["vote_average"],"Popularity": movie["popularity"],"Language": movie["original_language"]})

movies_df = pd.DataFrame(movie_list)
movies_df.to_csv("tmdb_movies.csv", index = False)

print("TMDB Movies")
print(movies_df.head())

# Task 5 : Understanding the Data
df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")
print("\nShape :", df.shape)

print("\nData Types")
print(df.dtypes)

print("\nNumerical Columns")
print(df.select_dtypes(include = ["int64", "float64"]).columns)

print("\nCategorical Columns")
print(df.select_dtypes(include = ["object"]).columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary")
print(df.describe())

print("\nUnique Values")
print(df.nunique())

# Task 6 : Data Cleaning

# Fill missing values
number_columns = df.select_dtypes(include = ["int64", "float64"]).columns

for column in number_columns:
    df[column] = df[column].fillna(df[column].mean())

text_columns = df.select_dtypes(include = ["object"]).columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Remove duplicate rows

df = df.drop_duplicates()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# Convert order_date to datetime

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nCleaned Dataset")
print(df.head())

print("\nUpdated Column Names")
print(df.columns)