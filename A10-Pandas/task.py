import pandas as pd

# -------------------- Task 1 --------------------

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print("<-----------------------------------Task 1------------------------------------------>")

print(series)
print("Index :", series.index)
print("Data Type :", series.dtype)

print("First Element :", series[0])
print("Last Two Elements")
print(series[-2:])

# -------------------- Task 2 --------------------

print("\n-----------------------------------Task 2------------------------------------------>")

print("Add 5")
print(series + 5)

print("Subtract 2")
print(series - 2)

print("Multiply by 1.05")
print(series * 1.05)

print("Divide by 2")
print(series / 2)

# -------------------- Task 3 --------------------

print("\n<-----------------------------------Task 3------------------------------------------>")

print("Maximum :", series.max())
print("Minimum :", series.min())
print("Sum :", series.sum())
print("Mean :", series.mean())

passed = series.apply(lambda x : x >= 70)

print("Passed")
print(passed)

print("Students Passed :", passed.sum())

# -------------------- Task 4 --------------------

students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks" : [78, 85, 90, 66, 72],
    "Subject" : ["Math", "Math", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print("\n<-----------------------------------Task 4------------------------------------------>")

print(df.head(3))

print(df.tail(2))

print("Shape :", df.shape)

print("Columns :", df.columns)

# -------------------- Task 5 --------------------

print("\n<-----------------------------------Task 5------------------------------------------>")

print(df.info())

print(df.describe())

print(df.head())

print(df.tail())

sorted_df = df.sort_values("Marks", ascending = False)

sorted_df = sorted_df.reset_index(drop = True)

print(sorted_df)

# -------------------- Task 6 --------------------

print("\n<-----------------------------------Task 6------------------------------------------>")

print("Marks > 75")
print(df[df["Marks"] > 75])

print("Math Students")
print(df[df["Subject"] == "Math"])

average = df["Marks"].mean()

print("Above Average")
print(df[df["Marks"] > average])

print("Failed Students")
print(df[df["Marks"] < 70])

# -------------------- Task 7 --------------------

print("\n<-----------------------------------Task 7------------------------------------------>")

print(df.groupby("Subject")["Marks"].mean())

print(df.groupby("Subject")["Marks"].count())

print(df.groupby("Subject")["Marks"].max())

# -------------------- Task 8 --------------------

df.plot(x = "Name", y = "Marks", kind = "bar", title = "Student Marks")

df["Marks"].plot(kind = "line", title = "Marks Line Graph")

df["Marks"].plot(kind = "hist", title = "Marks Histogram")

# -------------------- Task 9 --------------------

sales = {
    "Day" : ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Revenue" : [1200, 1500, 900, 2000, 1800]
}

sales_df = pd.DataFrame(sales)

print("\n<-----------------------------------Task 9------------------------------------------>")

print("Total Revenue :", sales_df["Revenue"].sum())

print("Average Revenue :", sales_df["Revenue"].mean())

highest = sales_df.loc[sales_df["Revenue"].idxmax()]

print("Highest Revenue Day")
print(highest)

average = sales_df["Revenue"].mean()

print("Revenue Above Average")
print(sales_df[sales_df["Revenue"] > average])

sales_df.plot(x = "Day", y = "Revenue", kind = "line", title = "Revenue by Day")