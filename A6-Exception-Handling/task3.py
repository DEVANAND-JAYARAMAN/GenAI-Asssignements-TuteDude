def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    print("Valid Age")

try:
    age = int(input("Enter Age : "))
    check_age(age)

except ValueError as e:
    print(e)