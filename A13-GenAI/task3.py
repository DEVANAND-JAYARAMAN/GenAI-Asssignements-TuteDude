import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 7 : Feature Preparation

df = pd.read_csv("superstore_final_dataset.csv", encoding= "unicode_escape")

# Rename column names

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# Convert categorical columns using One-Hot Encoding

encoded_df = pd.get_dummies(df, columns = ["category", "region", "segment"])
# Select target column

target = encoded_df["sales"]

# Remove target column from features

features = encoded_df.drop("sales", axis = 1)
print("Features")
print(features.head())

print("\nTarget")
print(target.head())

# Task 8 : Univariate Analysis

# Histogram
plt.figure(figsize = (8,5))
plt.hist(df["sales"], bins = 20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Histogram with KDE

sns.histplot(df["sales"], kde = True)
plt.title("Sales Histogram with KDE")
plt.show()

# KDE Plot

sns.kdeplot(df["sales"])
plt.title("Sales KDE Plot")
plt.show()

# Count Plot

sns.countplot(data = df, x = "category")
plt.title("Category Count")
plt.show()

# Box Plot

sns.boxplot(y = df["sales"])
plt.title("Sales Box Plot")
plt.show()

# Violin Plot

sns.violinplot(y = df["sales"])
plt.title("Sales Violin Plot")
plt.show()

# Pie Chart

category_sales = df.groupby("category")["sales"].sum()
plt.pie(category_sales.values,labels = category_sales.index,autopct = "%1.1f%%")
plt.title("Category Sales Share")
plt.show()

# Bar Chart

plt.bar(category_sales.index, category_sales.values)
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()