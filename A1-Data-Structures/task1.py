products=["Ferrari","Lamborghini","Porsche","Bugatti","Rolls Royce","Bentley"]
sample_products = ("Ferrari", "10000000", "Sports Car")

print("Second Product: ", products[1])
print("Last Product: ", products[-1])

products.append("BMW")
products.append("BenZ")

print("Products after adding new items are: ", products)
temp_products=list(sample_products)
temp_products[1]= "20000000"
temp_sample_products=tuple(temp_products)

print("Product after updation is: ", temp_sample_products)




