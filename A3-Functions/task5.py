prices= [100, 250, 400, 1200, 50, 2000, 850]
greater= list(filter(lambda x : x>500,prices))
smaller =list(filter(lambda x : x <=500,prices))
print("prices greater than 500:",greater)
print("prices less than or equal to 500:",smaller)