products =["Ferrari", "Lamborghini", "Porsche", "Bugatti", "Rolls Royce", "Bentley"]
categories =["Sports Car","Sports Car","Sports Car","Speed Car","Luxury Car","Luxury Car"]
categories_set = set(categories)

print("Categories:", categories_set)

categories_set.add("SUV")
categories_set.add("Sports Car")

print("Categories after adding new category:", categories_set)
print("Is Luxury Car available:", "Luxury Car" in categories_set)
print("Total Unique Categories is:", len(categories_set))