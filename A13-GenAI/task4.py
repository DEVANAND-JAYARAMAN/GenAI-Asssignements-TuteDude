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


def build_bivariate_plots(df):
	# Step 1: pair the main measures so the relationships are visible.
	plt.figure(figsize=(8, 5))
	plt.scatter(df["sales"], df["profit"], alpha=0.4, color="#264653")
	plt.title("Sales vs Profit")
	plt.xlabel("Sales")
	plt.ylabel("Profit")
	save_plot("task4_sales_vs_profit.png")

	plt.figure(figsize=(8, 5))
	correlation = df[["sales", "profit", "quantity", "discount"]].corr()
	sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
	plt.title("Correlation Heatmap")
	save_plot("task4_correlation_heatmap.png")

	plt.figure(figsize=(8, 5))
	sns.barplot(data=df, x="category", y="sales", estimator="sum", errorbar=None, color="#457b9d")
	plt.title("Category vs Sales")
	plt.xlabel("Category")
	plt.ylabel("Sales")
	save_plot("task4_category_bar.png")

	plt.figure(figsize=(8, 5))
	sns.boxplot(data=df, x="category", y="sales", color="#a8dadc")
	plt.title("Category vs Sales Box Plot")
	plt.xlabel("Category")
	plt.ylabel("Sales")
	save_plot("task4_category_box.png")

	plt.figure(figsize=(8, 5))
	sns.violinplot(data=df, x="category", y="sales", color="#f4a261")
	plt.title("Category vs Sales Violin Plot")
	plt.xlabel("Category")
	plt.ylabel("Sales")
	save_plot("task4_category_violin.png")

	plt.figure(figsize=(8, 5))
	sns.regplot(data=df, x="sales", y="profit", scatter_kws={"alpha": 0.35}, line_kws={"color": "red"})
	plt.title("Regression Plot")
	save_plot("task4_sales_profit_regression.png")

	sample_df = df[["sales", "profit", "quantity", "discount"]].sample(n=min(1000, len(df)), random_state=42)
	pair_grid = sns.pairplot(sample_df, corner=True, diag_kind="hist")
	pair_grid.fig.suptitle("Pair Plot of Key Numeric Features", y=1.02)
	pair_grid.fig.savefig(OUTPUT_DIR / "task4_pairplot.png", dpi=150, bbox_inches="tight")
	plt.close(pair_grid.fig)
	print(f"Saved plot: {OUTPUT_DIR / 'task4_pairplot.png'}")


def print_insights(df):
	# Step 2: write the conclusions with numbers so they are easy to verify.
	sales_mean = df["sales"].mean()
	sales_median = df["sales"].median()
	sales_max = df["sales"].max()
	q1, q3 = df["sales"].quantile([0.25, 0.75])
	sales_iqr = q3 - q1
	sales_outlier_threshold = q3 + 1.5 * sales_iqr
	sales_outliers = int((df["sales"] > sales_outlier_threshold).sum())

	negative_profit_rows = int((df["profit"] < 0).sum())
	negative_profit_total = df.loc[df["profit"] < 0, "profit"].sum()

	correlation = df[["sales", "profit", "quantity", "discount"]].corr()
	category_profit = df.groupby("category")["profit"].sum().sort_values(ascending=False)
	state_sales = df.groupby("state")["sales"].sum().sort_values(ascending=False)
	sub_category_sales = df.groupby("sub-category")["sales"].sum().sort_values(ascending=False)
	missing_values = int(df.isna().sum().sum())
	duplicate_rows = int(df.duplicated().sum())
	high_discount_rows = int((df["discount"] >= 0.5).sum())

	print("\nTask 10: Insights")
	print(
		f"1. Sales is strongly right-skewed: mean {sales_mean:.2f}, median {sales_median:.2f}, max {sales_max:.2f}, and {sales_outliers} rows sit above the upper outlier threshold of {sales_outlier_threshold:.2f}."
	)
	print(
		f"2. Technology leads profit with {category_profit.iloc[0]:.2f}, followed by Office Supplies at {category_profit.iloc[1]:.2f}; Furniture is far behind at {category_profit.iloc[2]:.2f}."
	)
	print(
		f"3. Sales and profit move together moderately (correlation {correlation.loc['sales', 'profit']:.3f}), while discount is linked to lower profit (correlation {correlation.loc['discount', 'profit']:.3f})."
	)
	print(
		f"4. The dataset contains {negative_profit_rows} negative-profit orders, and those rows add up to {negative_profit_total:.3f} total profit loss."
	)
	print(
		f"5. California and New York are the strongest sales states at {state_sales.iloc[0]:.3f} and {state_sales.iloc[1]:.3f}; Phones and Chairs are the top sub-categories at {sub_category_sales.iloc[0]:.3f} and {sub_category_sales.iloc[1]:.3f}."
	)
	print(
		f"6. Data quality is clean at the row level with {missing_values} missing values and {duplicate_rows} duplicate rows, but {high_discount_rows} orders have discounts of 50 percent or more, which is a risk area for margin pressure."
	)


def main():
	df = load_superstore_data()
	if df is None:
		return

	build_bivariate_plots(df)
	print_insights(df)


if __name__ == "__main__":
	main()