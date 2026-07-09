products=["Ferrari", "Lamborghini", "Porsche", "Bugatti", "Rolls Royce", "Bentley"]
categories= ["Sports Car","Sports Car","Sports Car","Speed Car","Luxury Car","Luxury Car"]
price_dict ={"Ferrari": 10000000,"Lamborghini": 12000000,"Porsche": 9000000,"Bugatti": 35000000,"Rolls Royce": 45000000,"Bentley": 30000000}

catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:",catalog)
category_to_products ={}

for i in range(len(products)):
    category =categories[i]
    product =products[i]

    if category in category_to_products:
        category_to_products[category].append(product)
    else:
        category_to_products[category] = [product]

print("Category to Products:")
print(category_to_products)

max_count = 0
max_category = ""

for category in category_to_products:
    if len(category_to_products[category]) > max_count:
        max_count = len(category_to_products[category])
        max_category = category

print("Category with Maximum Products:", max_category)
print("Products in that Category:")
for product in category_to_products[max_category]:
    print(product)