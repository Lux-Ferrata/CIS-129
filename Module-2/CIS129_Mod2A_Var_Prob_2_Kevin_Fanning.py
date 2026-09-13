## The original program included a syntax error caused by the variable
## "people" being assigned a value of the output on the "input" function,
## and then having that value be used as part of a mathematical operation.
## The out put of "input" is a string by defualt, so it needs to be type 
## cast to a float to be used for maths.

people = int(input("How many people are sharing the bill? "))
bill_total = 60.00

share = bill_total / people

print(f"Each person pays ${share}")