import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 9 : Bivariate Analysis
# Load the dataset

df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

# Rename column names

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# Scatter Plot

plt.figure(figsize = (8,5))
plt.scatter(df["sales"], df["profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# Correlation Heatmap

correlation = df[["sales","profit","quantity","discount"]].corr()
sns.heatmap(correlation, annot = True)
plt.title("Correlation Heatmap")
plt.show()

# Bar Plot

sns.barplot(data = df,x = "category",y = "sales")
plt.title("Category vs Sales")
plt.show()

# Box Plot

sns.boxplot(data = df,x = "category",y = "sales")
plt.title("Category vs Sales")
plt.show()

# Violin Plot

sns.violinplot(data = df,x = "category",y = "sales")
plt.title("Category vs Sales")
plt.show()

# Regression Plot

sns.regplot(data = df,x = "sales",y = "profit")
plt.title("Regression Plot")
plt.show()

# Pair Plot

sns.pairplot(df[["sales","profit","quantity","discount"]])
plt.show()

# Task 10 : Insights

# Insight 1
# Most orders have the lower sales values.
# Insight 2
# Technology category contributes more to thetotal sales.
# Insight 3
# There is a positive relationship between thesales and profit.
# Insight 4
# Some products have high sales but low profit.
# Insight 5
# The dataset contains very few missing values and is suitable for analysis.