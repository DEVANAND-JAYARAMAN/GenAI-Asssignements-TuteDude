A13 - GenAI

Files
- task1.py, task2.py, task3.py, task4.py, A13_GenAI_Notebook.ipynb
- products.json, superstore_final_dataset.csv, tmdb_movies.csv
Dataset and API sources
- Kaggle Superstore dataset: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- TMDB API endpoint used: https://api.themoviedb.org/3/movie/popular

Setup:

Install the required libraries:

pip install pandas numpy matplotlib seaborn requests

Set your TMDB key before running task2.py.

How to run

Run the files in order:

python task1.py
python task2.py
python task3.py
python task4.py

The plotting scripts save figures into the eda_outputs folder so the analysis can be reviewed even in a non-interactive environment.


This assignment helped me to practice reading data from CSV, JSON, SQLite, and an API, then cleaning and analyzing it with pandas. I also learned why environment variables are important for API keys, and I now understand how to turn raw dataset observations into specific, measurable EDA insights instead of generic comments

im not gonna share the env file. the env file contains the environmental vriavles of tmdb. api key. so im not gonna share it. go to the https://www.themoviedb.org/settings/api login first and then create the api key and use it

dont hardcore it. keep it in secrets or .env and then load from there. hardcoding is not a good practice


