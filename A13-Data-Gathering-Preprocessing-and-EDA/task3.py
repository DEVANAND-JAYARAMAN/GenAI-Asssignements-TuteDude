# task3.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("superstore_final_dataset.csv", encoding="unicode_escape")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("Dataset Loaded Successfully")
print(df.head())

# Task 7 - Feature Preparation
print("\n==============================")
print("Task 7 - Feature Preparation")
print("==============================\n")

# One-Hot Encoding
df_encoded = pd.get_dummies(df,columns=["category", "region", "segment"],drop_first=True)

# Select Target Column
target = df_encoded["sales"]
features = df_encoded.drop(columns=["sales"])

print("Target Column : Sales")
print("Reason : I selected Sales as the target column because it is a numerical column that can be predicted using the remaining features")

print("Target Column : Profit")
print("Reason : Profit depends on sales, discount, quantity and other features.\n")

print("Features Shape :", features.shape)
print("Target Shape :", target.shape)

print("\nEncoded Dataset")
print(df_encoded.head())

# Task 8 - Univariate Analysis
print("\n==============================")
print("Task 8 - Univariate Analysis")
print("==============================")

# Histogram
plt.figure(figsize=(7,5))
plt.hist(df["sales"], bins=20)
plt.title("Sales Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Histogram + KDE
plt.figure(figsize=(7,5))
sns.histplot(df["sales"], kde=True)
plt.title("Sales Distribution")
plt.show()

# Count Plot
plt.figure(figsize=(7,5))
sns.countplot(data=df, x="category")
plt.title("Category Count")
plt.show()

# Box Plot
plt.figure(figsize=(6,5))
sns.boxplot(y=df["sales"])
plt.title("Sales Boxplot")
plt.show()

# Violin Plot
plt.figure(figsize=(6,5))
sns.violinplot(y=df["sales"])
plt.title("Sales Violin Plot")
plt.show()

# Bar Plot
category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(7,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(category_sales.values,labels=category_sales.index,autopct="%1.1f%%")
plt.title("Category Sales Share")
plt.show()

print("\nObservation:")
print("- Sales values are not evenly distributed.")
print("- Some sales values are much higher than others.")
print("- Technology category contributes a large share of sales.")
print("- Boxplot shows a few outliers in Sales.")
print("- Category distribution is balanced.")
print("\nTask 7 and Task 8 completed successfully.")