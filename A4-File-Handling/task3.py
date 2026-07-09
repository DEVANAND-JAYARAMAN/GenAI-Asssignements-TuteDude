new_sales = [5000, 2500, 1700]
with open("sales_data.txt", "a") as file:
    for amount in new_sales:
        file.write(str(amount) + "\n")

with open("sales_data.txt", "r") as file:
    print(file.read())