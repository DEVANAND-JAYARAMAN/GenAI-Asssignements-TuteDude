from pathlib import Path
import os

import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "superstore_final_dataset.csv"
TMDB_OUTPUT_PATH = BASE_DIR / "tmdb_movies.csv"


def load_tmdb_movies():
    # Step 1: use an environment variable instead of a hardcoded API key.
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        print("TMDB_API_KEY is not set, so the API download is being skipped.")
        return None

    url = "https://api.themoviedb.org/3/movie/popular"
    try:
        response = requests.get(
            url,
            params={"api_key": api_key, "language": "en-US", "page": 1},
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
        movies = payload.get("results", [])
    except requests.RequestException as exc:
        print(f"TMDB request failed: {exc}")
        return None
    except ValueError as exc:
        print(f"Could not decode TMDB response as JSON: {exc}")
        return None

    movie_list = []
    for movie in movies:
        movie_list.append(
            {
                "Title": movie.get("title"),
                "Release Date": movie.get("release_date"),
                "Rating": movie.get("vote_average"),
                "Popularity": movie.get("popularity"),
                "Language": movie.get("original_language"),
            }
        )

    movies_df = pd.DataFrame(movie_list)
    try:
        movies_df.to_csv(TMDB_OUTPUT_PATH, index=False)
        print(f"Saved TMDB data to {TMDB_OUTPUT_PATH}")
    except OSError as exc:
        print(f"Could not write tmdb_movies.csv: {exc}")

    print("TMDB Movies:")
    print(movies_df.head())
    return movies_df


def load_superstore_data():
    # Step 2: inspect the raw dataset before cleaning.
    try:
        df = pd.read_csv(CSV_PATH, encoding="unicode_escape")
    except FileNotFoundError:
        print(f"CSV file not found: {CSV_PATH}")
        return None
    except Exception as exc:
        print(f"Could not read the CSV file: {exc}")
        return None

    print("\nShape:", df.shape)
    print("\nData Types")
    print(df.dtypes)
    print("\nNumerical Columns")
    print(list(df.select_dtypes(include=["number"]).columns))
    print("\nCategorical Columns")
    print(list(df.select_dtypes(exclude=["number"]).columns))
    print("\nMissing Values")
    print(df.isnull().sum())
    print("\nSummary")
    print(df.describe())
    print("\nUnique Values")
    print(df.nunique())
    return df


def clean_superstore_data(df):
    # Step 3: basic cleaning with simple, explainable rules.
    print("\nTask 6: Data Cleaning")
    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns
    text_columns = cleaned_df.select_dtypes(exclude=["number"]).columns

    for column in numeric_columns:
        if cleaned_df[column].isna().any():
            cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].mean())

    for column in text_columns:
        if cleaned_df[column].isna().any():
            cleaned_df[column] = cleaned_df[column].fillna("Unknown")

    before_duplicates = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    removed_duplicates = before_duplicates - len(cleaned_df)

    cleaned_df.columns = cleaned_df.columns.str.lower().str.replace(" ", "_", regex=False)

    if "order_date" in cleaned_df.columns:
        cleaned_df["order_date"] = pd.to_datetime(cleaned_df["order_date"], errors="coerce")

    print(f"Removed duplicate rows: {removed_duplicates}")
    print("\nCleaned Dataset")
    print(cleaned_df.head())
    print("\nUpdated Column Names")
    print(list(cleaned_df.columns))
    print("\nMissing Values After Cleaning")
    print(cleaned_df.isnull().sum())
    return cleaned_df


def main():
    load_tmdb_movies()
    df = load_superstore_data()
    if df is not None:
        clean_superstore_data(df)


if __name__ == "__main__":
    main()