A13 - GenAI

Files

- task1.py, task2.py, task3.py, task4.py
- products.json, superstore_final_dataset.csv, tmdb_movies.csv

What each file does

- task1.py loads the Superstore CSV, loads JSON data into a DataFrame, and demonstrates SQLite read/write with a small employee table.
- task2.py pulls popular movies from TMDB using an environment variable, then performs understanding and cleaning steps on the Superstore dataset.
- task3.py prepares features with one-hot encoding and creates univariate plots for sales and category distribution.
- task4.py creates bivariate plots and prints the final insights with numerical evidence.

Dataset and API sources
- Kaggle Superstore dataset: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- TMDB API endpoint used: https://api.themoviedb.org/3/movie/popular

Setup:

Install the required libraries:

pip install pandas numpy matplotlib seaborn requests

Set your TMDB key before running task2.py.

PowerShell:
$env:TMDB_API_KEY = "your_tmdb_key_here"

How to run

Run the files in order:

python task1.py
python task2.py
python task3.py
python task4.py

The plotting scripts save figures into the eda_outputs folder so the analysis can be reviewed even in a non-interactive environment.

What I Learnt:

This assignment helped me to practice reading data from CSV, JSON, SQLite, and an API, then cleaning and analyzing it with pandas. I also learned why environment variables are important for API keys, and I now understand how to turn raw dataset observations into specific, measurable EDA insights instead of generic comments

