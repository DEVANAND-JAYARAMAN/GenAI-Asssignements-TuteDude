with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = []
for line in lines:
    sales.append(int(line.strip()))

total =sum(sales)
highest= max(sales)
lowest= min(sales)
average= total /len(sales)

print("Total Sales :", total)
print("Highest Sale :", highest)
print("Lowest Sale :", lowest)
print("Average Sale :", average)