import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("superstore_final_dataset.csv", encoding = "unicode_escape")

print("\n<--------------- Task 1 --------------->")

sns.relplot(data =df,x ="Sales",y= "Profit",hue ="Category")
plt.show()

sns.relplot(data = df,x = "Sales",y = "Profit",hue = "Category",kind = "scatter")
plt.show()

print("\n<--------------- Task 2 --------------->")

sns.lineplot(data =df,x="Sales",y="Profit")
plt.title("Line Plot")
plt.show()

sns.lineplot(data = df,x = "Sales",y = "Profit",marker = "o")

plt.title("Scatter Style Line Plot")
plt.show()

sns.relplot(data = df,x = "Sales",y = "Profit",col = "Category")
plt.show()

print("\n<--------------- Task 3 --------------->")

sns.histplot(df["Sales"])
plt.title("Histogram")
plt.show()

sns.kdeplot(df["Sales"])
plt.title("KDE Plot")
plt.show()

sns.rugplot(df["Sales"])
plt.title("Rug Plot")
plt.show()

sns.histplot(df["Sales"],kde = True)
plt.title("Histogram with KDE")
plt.show()

print("\n<--------------- Task 4 --------------->")
sns.histplot(data = df,x = "Sales",y = "Profit")
plt.title("Bivariate Histogram")
plt.show()

sns.kdeplot(data = df,x = "Sales",y = "Profit",fill = True)
plt.title("Bivariate KDE Plot")
plt.show()

print("\n<--------------- Task 5 --------------->")

sns.pairplot(df[["Sales", "Profit", "Quantity", "Discount"]])
plt.show()

correlation = df[["Sales", "Profit", "Quantity", "Discount"]].corr()

sns.heatmap(correlation,annot = True)
plt.title("Correlation Heatmap")
plt.show()

print("\n<--------------- Task 6 --------------->")

sns.barplot(data = df,x = "Category",y = "Sales")
plt.title("Bar Plot")
plt.show()

sns.boxplot(data = df,x = "Category",y = "Sales")
plt.title("Box Plot")
plt.show()

sns.violinplot(data = df,x = "Category",y = "Sales")
plt.title("Violin Plot")
plt.show()

sns.countplot(data = df,x = "Category")
plt.title("Count Plot")
plt.show()

print("\n<--------------- Task 7 --------------->")

sns.regplot(data = df,x = "Sales",y = "Profit")
plt.title("Regression Plot")
plt.show()

sns.lmplot(data = df,x = "Sales",y = "Profit",hue = "Category")
plt.show()

print("\n<--------------- Task 8 --------------->")

facet = sns.FacetGrid(df,col = "Category")
facet.map(plt.scatter, "Sales", "Profit")
plt.show()

sns.relplot(data = df,x = "Sales",y = "Profit",hue = "Category")
plt.show()

sns.catplot(data = df,x = "Category",y = "Sales",kind = "bar")
plt.show()

sns.displot(data = df,x = "Sales",kde = True)
plt.show()