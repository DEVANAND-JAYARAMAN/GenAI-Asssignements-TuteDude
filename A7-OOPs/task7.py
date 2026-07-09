class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_value(self):
        total = 0
        for product in self.products:
            total = total + product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product.name, "-", product.price)

class Store:
    def __init__(self, name):
        self.store_name = name
        self.inventory = Inventory()

    def show_summary(self):
        print("Store :", self.store_name)
        print("Total Products :", len(self.inventory.products))
        print("Total Value :", self.inventory.get_total_value())

store = Store("Electro World")

product1 = Product("Laptop", 60000)
product2 = Product("Mouse", 800)
product3 = Product("Keyboard", 1500)

store.inventory.add_product(product1)
store.inventory.add_product(product2)
store.inventory.add_product(product3)

store.inventory.show_all_products()
store.show_summary()
print("Combined Price :", product1 + product2)