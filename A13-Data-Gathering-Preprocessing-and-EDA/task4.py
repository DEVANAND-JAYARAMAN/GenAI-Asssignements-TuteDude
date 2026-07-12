# task4.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("superstore_final_dataset.csv", encoding="unicode_escape")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("Dataset Loaded Successfully")

# Task 9 - Bivariate Analysis

print("\n==============================")
print("Task 9 - Bivariate Analysis")
print("==============================")

# Scatter Plot
plt.figure(figsize=(7,5))
plt.scatter(df["sales"], df["profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(7,5))
corr = df[["sales", "profit", "quantity", "discount"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

# Bar Plot
plt.figure(figsize=(7,5))
sns.barplot(data=df, x="category", y="sales", estimator=sum)

plt.title("Category vs Sales")
plt.show()

# Box Plot
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="category", y="sales")

plt.title("Category vs Sales")
plt.show()

# Violin Plot
plt.figure(figsize=(7,5))
sns.violinplot(data=df, x="category", y="sales")

plt.title("Category vs Sales Violin Plot")
plt.show()

# Regression Plot
plt.figure(figsize=(7,5))
sns.regplot(data=df, x="sales", y="profit")

plt.title("Sales vs Profit Regression")
plt.show()

# Pair Plot
sns.pairplot(df[["sales", "profit", "quantity", "discount"]])

plt.show()

# Task 10 - Insights

print("\n==============================")
print("Task 10 - Insights")
print("==============================\n")

print("1. Sales and Profit have a positive relationship.")
print("\n2. Technology category has higher sales compared to other categories.")
print("\n3. Some orders have negative profit.")
print("\n4. Sales column contains a few outliers.")
print("\n5. The dataset has very few missing values and duplicate rows.")
print("\nTask 9 and Task 10 completed successfully.")