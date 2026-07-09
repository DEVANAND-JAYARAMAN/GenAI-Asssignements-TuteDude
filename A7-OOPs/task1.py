class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
        print("Name :",self.name)
        print("Price :",self.price)
        print("Category :",self.category)

product1 = Product("Laptop", 55000, "Electronics")
product2 = Product("Mouse", 800, "Accessories")

product1.get_info()
print()
product2.get_info()