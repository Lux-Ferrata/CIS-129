## The original program correctly created a "total_pay" variable with 
## both regular and bonus pay added together. But then over wrote that 
## correct code with a second declaration only using the "regular_pay"
## amount. Causing the final total pay message to not inclued "bonus".



# Total pay should be the regular pay plus any bonus earned.
regular_pay = 800
bonus = 100

total_pay = regular_pay + bonus

print(f"Total pay: ${total_pay}")