import pandas as pd
import matplotlib.pyplot as plt

# loading the superstore dataset, unicode_escape handles special characters in the csv
df = pd.read_csv("superstore_final_dataset.csv")

#Task 1: Line Plot
print("\n<----------------Task 1---------------->")
# converting Order Date column from string to actual datetime so we can extract month
df["Order Date"] = pd.to_datetime(df["Order Date"])

# extracting month number like 1,2,3 and month name from the date
df["Month"] = df["Order Date"].dt.month_name()
df["MonthNum"] = df["Order Date"].dt.month

# groupby both month number and name, using that we can sort by number
monthly_sales = df.groupby(["MonthNum", "Month"])["Sales"].sum()

# sorting by MonthNum puts months in calendar order (1=Jan, 2=Feb, ...)
monthly_sales = monthly_sales.sort_index(level="MonthNum")

# we only need the month names for the x-axis labels
month_names = [name for (_, name) in monthly_sales.index]
sales_values = monthly_sales.values
plt.figure(figsize=(10, 5))

# plotting month names on x-axis and total sales on y-axis, marker="o" adds dots at each point
plt.plot(month_names, sales_values, marker="o")
plt.title("Sales Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Task 2: Scatter Plot
print("\n<--------------- Task 2 --------------->")
plt.figure(figsize=(8, 5))

# each dot = one order row, x = how much was sold and act as x-asix, y = how much profit was made and act as y-axix
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

#Task 3: Bar Plot 
print("\n<--------------- Task 3 --------------->")

# summing sales per category to get one value per category
category_sales = df.groupby("Category")["Sales"].sum()

# vertical chart - bar chart
plt.figure(figsize=(7, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category Wise Sales (Vertical)")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# horizontal chart using the barh method/function
plt.figure(figsize=(7, 5))
plt.barh(category_sales.index, category_sales.values)
plt.title("Category Wise Sales (Horizontal)")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.show()

#Task 4:

print("\n<--------------- Task 4 --------------->")
# filtering the dataframe by category and grouping each slice by Region separately
regions = sorted(df["Region"].unique())

furniture = df[df["Category"] == "Furniture"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)
office = df[df["Category"] == "Office Supplies"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)
technology = df[df["Category"] == "Technology"].groupby("Region")["Sales"].sum().reindex(regions, fill_value=0)

# using range() to get numeric positions for bars since we can't place 3 bars at the same x position
x = range(len(regions))
width = 0.25  # each bar takes 0.25 units, so 3 bars fit side by side without overlapping

plt.figure(figsize=(8, 5))

# first group 
plt.bar(x, furniture, width=width, label="Furniture")

# second group
plt.bar([i + width for i in x], office, width=width, label="Office Supplies")

# third group
plt.bar([i + width * 2 for i in x], technology, width=width, label="Technology")

# centering the region labels under the middle bar of each group
plt.xticks([i + width for i in x], regions)  # regions is a plain list here
plt.title("Region Wise Category Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.legend()
plt.show()


#Task 5: Stacked Bar Chart
print("\n<--------------- Task 5 --------------->")
plt.figure(figsize=(8, 5))

# first category starts from 0 (no bottom needed)
plt.bar(regions, furniture, label="Furniture")

# second category starts from where furniture ended, so bottom=furniture
plt.bar(regions, office, bottom=furniture, label="Office Supplies")

# third category starts from where furniture + office ended
bottom_values = furniture + office
plt.bar(regions, technology, bottom=bottom_values, label="Technology")
plt.title("Region Wise Category Sales (Stacked)")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.legend()
plt.show()


#Task 6: Histogram

print("\n<--------------- Task 6 --------------->")
plt.figure(figsize=(8, 5))

# bins=20 splits the sales range into 20 equal intervals and counts how many orders fall in each
plt.hist(df["Sales"], bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Number of Orders")
plt.show()


#Task 7: Pie Chart - round chart
print("\n<--------------- Task 7 --------------->")
category_share = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6, 6))
plt.pie(category_share.values,labels=category_share.index,startangle=90)
plt.title("Category Wise Sales Share")
plt.show()
