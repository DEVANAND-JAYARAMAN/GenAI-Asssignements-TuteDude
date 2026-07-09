price_dict ={"Ferrari": 10000000,"Lamborghini": 12000000,"Porsche": 9000000,"Bugatti": 35000000,"Rolls Royce": 45000000,"Bentley": 30000000 }

price_dict["BMW"] = 8000000
price_dict["Ferrari"] = 11000000
product_name = "Porsche"

if product_name in price_dict:
    del price_dict[product_name]
else:
    print("Product not found")

total =sum(price_dict.values())
average= total/len(price_dict)
print("Average Price:", average)

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)
print("Highest Price of Product:", max_product, "-", price_dict[max_product])
print("Lowest Price of the Product:", min_product, "-", price_dict[min_product])