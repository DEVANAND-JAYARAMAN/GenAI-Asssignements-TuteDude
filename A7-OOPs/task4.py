class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class Laptop(Product):
    def get_info(self):
        print("Laptop :", self.name,"-",self.price)

class Mobile(Product):
    def get_info(self):
        print("Mobile:",self.name,"-",self.price)

items = [
    Laptop("Dell",60000),
    Mobile("Samsung", 25000),
    Laptop("HP",50000),
    Mobile("OnePlus",30000)
]
for item in items:
    item.get_info()