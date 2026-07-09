class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.__price=price
        self.category =category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price=new_price

    def get_info(self):
        print(self.name)
        print(self.__price)
        print(self.category)

product = Product("Laptop",60000,"Electronics")
print("Old Price :",product.get_price())

product.set_price(58000)
print("New Price :",product.get_price())