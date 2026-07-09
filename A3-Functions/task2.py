def factorial(n):
    if n<0:
        print("Negative number")
        return
    if (n==0 or n==1):
        return 1
    return n * factorial(n - 1)
print(factorial(5))  #function's parameter will be set to 5
print(factorial(0)) #0 will be passed
print(factorial(-3)) #Negative number, so it will return the negative number