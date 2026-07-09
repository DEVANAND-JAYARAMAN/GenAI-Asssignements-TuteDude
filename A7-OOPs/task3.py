class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(self.name)
        print(self.price)
        print(self.category)

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        print("Name :", self.name)
        print("Price :", self.price)
        print("Category :", self.category)
        print("Warranty :", self.warranty_years, "Years")

obj = ElectronicProduct("Laptop", 65000, "Electronics", 2)
obj.get_info()