class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name},{self.price},{self.category})"

    def __add__(self, other):
        return self.price + other.price

product1 =Product("Laptop", 60000, "Electronics")
product2 =Product("Mouse", 800, "Accessories")

print(product1)
print(product2)
print("Combined Price :", product1 + product2)