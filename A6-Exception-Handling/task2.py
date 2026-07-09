prices = [120, 350, "abc", 500, -200, 800]
total = 0

for item in prices:
    try:
        if type(item) == str:
            raise TypeError
        if item < 0:
            raise ValueError("Negative price not allowed")
        total = total + item
        print("Running Total :", total)

    except TypeError:
        print(item, "- Invalid price")

    except ValueError as e:
        print(e)