try:
    numerator = int(input("Enter Numerator : "))
    denominator = int(input("Enter Denominator : "))
    result = numerator / denominator

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Denominator cannot be zero.")

else:
    print("Result :", result)

finally:
    print("Operation Complete")