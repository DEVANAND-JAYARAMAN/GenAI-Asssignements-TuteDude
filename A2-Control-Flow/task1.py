order_amount = int(input("Enter Order Amount: "))

if order_amount>=2000:
    discount =15
elif order_amount>=1500:
    discount= 10
elif order_amount>= 1000:
    discount=7
else:
    discount =0

discount_amount= (order_amount * discount) /100
final_amount =order_amount -discount_amount
print("Discount :", str(discount) +"%")
print("Final Amount :", final_amount)