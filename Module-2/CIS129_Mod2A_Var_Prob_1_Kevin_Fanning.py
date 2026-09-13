## The original program displayed a syntax error due to the incorrect
## inclusion of an underscore in the fstring variable name. Eg sub_total
## Which did not match the previously declared variable.


item_price = 8.50
shipping = 4.00
subtotal = item_price + shipping
print(f"Your subtotal is ${subtotal}")
