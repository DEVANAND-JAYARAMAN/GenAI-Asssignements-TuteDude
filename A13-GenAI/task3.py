from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "superstore_final_dataset.csv"
OUTPUT_DIR = BASE_DIR / "eda_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_superstore_data():
	try:
		df = pd.read_csv(CSV_PATH, encoding="unicode_escape")
	except FileNotFoundError:
		print(f"CSV file not found: {CSV_PATH}")
		return None
	except Exception as exc:
		print(f"Could not read the CSV file: {exc}")
		return None

	df.columns = df.columns.str.lower().str.replace(" ", "_", regex=False)
	return df


def save_plot(filename):
	plot_path = OUTPUT_DIR / filename
	plt.tight_layout()
	plt.savefig(plot_path, dpi=150, bbox_inches="tight")
	plt.close()
	print(f"Saved plot: {plot_path}")


def prepare_features(df):
	# Step 1: turn categorical columns into numeric indicators.
	columns_to_encode = [column for column in ["category", "region", "segment"] if column in df.columns]
	encoded_df = pd.get_dummies(df, columns=columns_to_encode)

	if "sales" not in encoded_df.columns:
		print("The sales column is missing, so feature preparation stops here.")
		return None, None

	print("I am using sales as the target because it is the numeric outcome the later analysis compares against the other fields.")
	target = encoded_df["sales"]
	features = encoded_df.drop(columns=["sales"])

	print("Features")
	print(features.head())
	print("\nTarget")
	print(target.head())
	print(f"Encoded feature shape: {features.shape}")
	return features, target


def run_univariate_analysis(df):
	# Step 2: save a few single-variable plots for inspection.
	plt.figure(figsize=(8, 5))
	plt.hist(df["sales"], bins=20, color="#2a6f97")
	plt.title("Sales Distribution")
	plt.xlabel("Sales")
	plt.ylabel("Frequency")
	save_plot("task3_sales_histogram.png")

	plt.figure(figsize=(8, 5))
	sns.histplot(df["sales"], kde=True, color="#1d3557")
	plt.title("Sales Histogram with KDE")
	plt.xlabel("Sales")
	save_plot("task3_sales_histplot.png")

	plt.figure(figsize=(8, 5))
	sns.kdeplot(df["sales"], fill=True, color="#457b9d")
	plt.title("Sales KDE Plot")
	plt.xlabel("Sales")
	save_plot("task3_sales_kde.png")

	plt.figure(figsize=(8, 5))
	sns.countplot(data=df, x="category", order=df["category"].value_counts().index, color="#457b9d")
	plt.title("Category Count")
	plt.xlabel("Category")
	plt.ylabel("Count")
	save_plot("task3_category_count.png")

	plt.figure(figsize=(6, 5))
	sns.boxplot(y=df["sales"], color="#90be6d")
	plt.title("Sales Box Plot")
	plt.ylabel("Sales")
	save_plot("task3_sales_boxplot.png")

	plt.figure(figsize=(6, 5))
	sns.violinplot(y=df["sales"], color="#f4a261")
	plt.title("Sales Violin Plot")
	plt.ylabel("Sales")
	save_plot("task3_sales_violin.png")

	category_sales = df.groupby("category", as_index=False)["sales"].sum()
	plt.figure(figsize=(6, 6))
	plt.pie(category_sales["sales"], labels=category_sales["category"], autopct="%1.1f%%")
	plt.title("Category Sales Share")
	save_plot("task3_category_pie.png")

	plt.figure(figsize=(8, 5))
	plt.bar(category_sales["category"], category_sales["sales"], color="#e76f51")
	plt.title("Category Wise Sales")
	plt.xlabel("Category")
	plt.ylabel("Sales")
	save_plot("task3_category_bar.png")


def main():
	df = load_superstore_data()
	if df is None:
		return

	prepare_features(df)
	run_univariate_analysis(df)


if __name__ == "__main__":
	main()