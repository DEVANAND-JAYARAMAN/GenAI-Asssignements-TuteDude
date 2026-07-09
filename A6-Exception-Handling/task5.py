cart = []
while True:
    value = input("Enter Price (q to quit) : ")
    if value == "q":
        break

    try:
        price = float(value)
        if price < 0:
            raise ValueError("Negative price is not allowed")
        cart.append(price)

    except ValueError as e:
        print(e)

print("Total Items :",len(cart))
print("Total Bill :",sum(cart))