#######################################################################
### Problem 1
#######################################################################

# Apply all eligible benefits to the customer's order.
# A customer can qualify for more than one benefit at the same time.

cart_total = 120
is_member = True
is_holiday = True

if is_member:
    print("Member benefit: free shipping.")

if is_holiday:
    print("Holiday benefit: free gift wrap.")

if cart_total > 100:
    print("Large order benefit: priority handling.")

print("Thank you for shopping with us!")


# Explaination Comment
'''
The core error with this problem was that using elif meant that only a single
user benifit could be applied at any time. Instead of the multiple benifits
they were eligible to recieve. I corrected this by seperating them into
their own if statements.
'''


################################################################################
### Problem 2
################################################################################

# Calculate employee bonus.  Employees must have worked 3 or more
# years.  Rating of 4 or above get $1000, ratings 3 or above get a
# $500 bonus and less than 3 get no bonus.

years_worked = 5
performance_rating = 4  # Rating from 1 (poor) to 5 (excellent)
bonus = 0

if years_worked >= 3:
    if performance_rating >= 4:
        bonus += 1000

    if performance_rating >= 3:
        bonus += 500
        print(f"Your bonus is ${bonus}")

    else:
        print("No bonus for poor performance")

elif years_worked < 3:
    print("Employees with less than 3 years do not qualify for bonuses")


# Explaination Comment
'''
There were a couple of errors in this problem. First the years worked logic
was incorrectly excluding people with 3 years worked from bonuses. Corrected
by switching the if years_worked to >=. Also added assignment logic to each
of the bonus tiers so they apply cumulatively. Also moved the bonus print
statement so that it is inside the bonus logic. Similarly I lets the
bonus logic as seperate statements. So that they can apply repeatedly.
'''