orders =[]

while True:
    print("\n1. Add Order")
    print("2. Show Orders")
    print("3. Quit")
    choice =input("Enter your choice : ")

    if choice =="1":
        amount =int(input("Enter Order Amount : "))
        orders.append(amount)
    elif choice == "2":
        total = 0
        if len(orders) == 0:
            print("No orders available.")
        else:
            for amount in orders:

                if amount >= 2000:
                    discount = 15
                elif amount >= 1500:
                    discount = 10
                elif amount >= 1000:
                    discount = 7
                else:
                    discount = 0

                final = amount - (amount * discount / 100)
                print("Order :", amount, " Final :", final)
                total = total + final
            print("Total :", total)

    elif choice == "3":
        print("You quit program")
        break

    else:
        print("Invalid Choice")
        continue