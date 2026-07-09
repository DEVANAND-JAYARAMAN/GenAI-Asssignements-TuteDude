import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax

print("Math Module")
print(math_utils.add(20,10))
print(math_utils.subtract(20,10))
print(square(8))

print("\nString Module")
text = "python programming language"
print(string_utils.capitalize_words(text))
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))

print("\nPackage Functions")
print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))

prices = [100,200,300, 400]
total = calculate_total(prices)
print("Total :",total)
print("After Tax :", apply_tax(total))