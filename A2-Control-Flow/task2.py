orders =[1200, 2500, 800, 1750, 3000]

total_revenue=0
discount_orders =0
print("Order  Discount  Final Amount")

for amount in orders:
    if amount >=2000:
        discount=15
    elif amount>=1500:
        discount =10
    elif amount >=1000:
        discount=7
    else:
        discount=0
    final = amount- (amount * discount / 100)
    print(amount,"   ", str(discount) + "%", "   ", final)
    total_revenue= total_revenue + final
    if discount >0:
        discount_orders =discount_orders + 1

print("\nTotal Revenue :", total_revenue)
print("Orders with Discount :", discount_orders)