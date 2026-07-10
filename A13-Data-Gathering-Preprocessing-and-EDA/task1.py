from pathlib import Path
import json
import sqlite3

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "superstore_final_dataset.csv"
JSON_PATH = BASE_DIR / "products.json"
SQLITE_PATH = BASE_DIR / "sample.db"


def load_csv_data():
	# Step 1: load the main CSV and check its basic structure.
	print("Task 1: Loading the CSV dataset")
	try:
		df = pd.read_csv(CSV_PATH, encoding="unicode_escape")
	except FileNotFoundError:
		print(f"CSV file not found: {CSV_PATH}")
		return None
	except Exception as exc:
		print(f"Could not read the CSV file: {exc}")
		return None

	print("Shape of Dataset:", df.shape)
	print("\nColumn Names:")
	print(df.columns)
	print("\nFirst 5 Rows:")
	print(df.head())
	print("\nLast 5 Rows:")
	print(df.tail())
	print("\nDataset Information:")
	df.info()
	print("\nSummary Statistics:")
	print(df.describe(include="all"))
	print("\nMissing Values:")
	print(df.isnull().sum())
	return df


def ensure_products_json():
	# Step 2: make the JSON demo self-contained if the file is missing.
	if JSON_PATH.exists():
		return

	sample_products = [
		{"Product": "Laptop", "Price": 65656, "Category": "Electronics"},
		{"Product": "Keyboard", "Price": 1555, "Category": "Accessories"},
		{"Product": "Mouse", "Price": 579, "Category": "Accessories"},
		{"Product": "Monitor", "Price": 25639, "Category": "Electronics"},
	]

	try:
		JSON_PATH.write_text(json.dumps(sample_products, indent=4), encoding="utf-8")
		print(f"Created fallback JSON file at {JSON_PATH}")
	except OSError as exc:
		print(f"Could not create fallback JSON file: {exc}")


def load_json_data():
	print("\nTask 2: Loading the JSON file")
	ensure_products_json()

	try:
		json_df = pd.read_json(JSON_PATH)
	except FileNotFoundError:
		print(f"JSON file not found: {JSON_PATH}")
		return None
	except Exception as exc:
		print(f"Could not read the JSON file: {exc}")
		return None

	print("Products Data:")
	print(json_df)
	return json_df


def load_sqlite_data():
	print("\nTask 3: Loading data from SQLite")
	employees = [
		(1, "John", "HR", 35000),
		(2, "David", "Sales", 42000),
		(3, "Alice", "IT", 55000),
		(4, "Sam", "Finance", 47000),
		(5, "Emma", "Marketing", 39000),
	]

	connection = None
	try:
		connection = sqlite3.connect(SQLITE_PATH)
		cursor = connection.cursor()
		cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS employees(
				id INTEGER PRIMARY KEY,
				name TEXT,
				department TEXT,
				salary INTEGER
			)
			"""
		)

		# Clear old demo rows so reruns stay readable.
		cursor.execute("DELETE FROM employees")
		cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)
		connection.commit()

		employee_df = pd.read_sql_query("SELECT * FROM employees", connection)
		print("Employee Details:")
		print(employee_df)
		return employee_df
	except sqlite3.Error as exc:
		print(f"SQLite error: {exc}")
		return None
	finally:
		if connection is not None:
			connection.close()


def main():
	load_csv_data()
	load_json_data()
	load_sqlite_data()


if __name__ == "__main__":
	main()