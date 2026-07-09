prices = {
    "Mouse" :500,
    "Keyboard" :800,
    "Monitor":7000,
    "Pendrive":400,
    "Web-Camera": 5000
}
discount =float(input("Enter Discount Percentage : "))
with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    for product in prices:
        original= prices[product]
        final =original - (original * discount / 100)

        file.write(product + " | " + str(original) + " | " + str(final) + "\n")

with open("discount_report.txt", "r") as file:
    print(file.read())