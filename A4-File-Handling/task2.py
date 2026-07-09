with open("sales_data.txt", "r") as file:
    data = file.read()

print("Using read():")
print(data)

with open("sales_data.txt", "r") as file:
    first_line = file.readline()

print("Using readline():")
print(first_line)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = []
for line in lines:
    sales.append(int(line.strip()))

print("Using readlines():")
print(sales)