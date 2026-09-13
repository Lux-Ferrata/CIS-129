## The original program displayed a syntax error due to the incorrect
## inclusion of an underscore in the fstring variable name. Eg sub_total
## Which did not match the previously declared variable.


item_price = 8.50
shipping = 4.00
subtotal = item_price + shipping
print(f"Your subtotal is ${subtotal}")

##################################################################################

## The original program included a syntax error caused by the variable
## "people" being assigned a value of the output on the "input" function,
## and then having that value be used as part of a mathematical operation.
## The out put of "input" is a string by defualt, so it needs to be type 
## cast to a float to be used for maths.

people = int(input("How many people are sharing the bill? "))
bill_total = 60.00

share = bill_total / people

print(f"Each person pays ${share}")

######################################################################################

## The original program correctly created a "total_pay" variable with 
## both regular and bonus pay added together. But then overwrote that 
## correct code with a second declaration only using the "regular_pay"
## amount. Causing the final total pay message to not include "bonus".



# Total pay should be the regular pay plus any bonus earned.
regular_pay = 800
bonus = 100

total_pay = regular_pay + bonus

print(f"Total pay: ${total_pay}")
