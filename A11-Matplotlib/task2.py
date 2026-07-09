import pandas as pd
import matplotlib.pyplot as plt

# it loads the dataset independently so it can be run without task1.py
df = pd.read_csv("superstore_final_dataset.csv")

#Task 2: Scatter Plot 

print("\n<----------------Task 2---------------->")

plt.figure(figsize=(8, 5))

# scatter plot shows if any relationship between two columns
plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


#Task 3: Bar Plot 

print("\n<----------------Task 3---------------->")

# groupby Category and sum Sales to get total sales per category
category_sales = df.groupby("Category")["Sales"].sum()

# vertical bar chart
plt.figure(figsize=(7, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category Wise Sales (Vertical)")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# horizontal bar chart - barh flips the axes compared to bar
plt.figure(figsize=(7, 5))
plt.barh(category_sales.index, category_sales.values)
plt.title("Category Wise Sales (Horizontal)")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.show()


#Task 4: Multiple Bar Chart

print("\n<----------------Task 4---------------->")
# filtering by category first and then grouping each slice by Region separately to achive the task
regions = sorted(df["Region"].unique())

furniture = df[df["Category"] == "Furniture"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)
office = df[df["Category"] == "Office Supplies"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)
technology = df[df["Category"] == "Technology"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)

x = range(len(regions))
width = 0.25

plt.figure(figsize=(8, 5))

plt.bar(x, furniture, width=width, label="Furniture")
plt.bar([i + width for i in x], office, width=width, label="Office Supplies")
plt.bar([i + width * 2 for i in x], technology, width=width, label="Technology")

# tick labels placed at center
plt.xticks([i + width for i in x], regions)

plt.title("Region Wise Category Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.legend()
plt.show()

# ─── Task 5: Stack Bar

print("\n<--------------- Task 5 --------------->")
plt.figure(figsize=(8, 5))

# stacking works by passing the previous bar's values as the bottom of the next bar, through this, it will work
plt.bar(regions, furniture, label="Furniture")
plt.bar(regions, office, bottom=furniture, label="Office Supplies")

plt.bar(regions, technology, bottom=furniture + office, label="Technology")
plt.title("Region Wise Category Sales after Stacking is")

plt.xlabel("Region:")
plt.ylabel("Total Sales:")
plt.legend()
plt.show()

#Task 6: Histogram

print("\n<---------------Task 6--------------->")
plt.figure(figsize=(8, 5))

# histogram groups shows how many values fall in each bin
plt.hist(df["Sales"], bins=20)
plt.title("Sales Distribution:")
plt.xlabel("Sales Amount:")
plt.ylabel("Number of Orders")
plt.show()

#Task 7: Pie Chart 

print("\n<----------------Task 7---------------->")
category_share = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6, 6))
plt.pie(category_share.values,labels=category_share.index,autopct="%1.1f%%",startangle=90)
plt.title("Category Wise Sales Share")
plt.show()
