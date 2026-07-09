with open("products.txt","w") as file:
    for i in range(3):
        product = input("Enter Product Name : ")
        price = input("Enter Product Price : ")
        file.write(product + " | " + price + "\n")

with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())