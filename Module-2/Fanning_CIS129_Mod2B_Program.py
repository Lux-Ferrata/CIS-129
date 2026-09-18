'''
The lack of logical operators forces this program to assume a compliant, and knowledgeable user acting in good faith.
As such I do not attempt any form of error handling, or user constaints / input cleaning.
I find this frustrating, and ultimately have kind of just assumed that the goal is that they must buy any
quantity of 3 unique items, and that makes this feel a lot more senseible.
'''

print('''


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀



Greetings and Welcome to the Fintastic Shopping Center.

          You are REQUIRED to buy 3 items.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

'''
I have grouped each item processing into blocks 
where possible to keep logic locally located
'''

###############################################################################
# Item 1
###############################################################################

item_1_Name = input("Please enter the name of your first item: ")
item_1_Quantity = int(input("Please enter the quantity of that item: "))
item_1_Price = float(input("Please enter the price of that item: $"))
item_1_Cost = item_1_Price * item_1_Quantity
item_1_Subtotal = (item_1_Cost * 0.05) + item_1_Cost

# Even though its not strictly needed, I wrapped this in a float to indicate
# that its output MUST remain a float or else it will break other parts of the 
# program to other maintainers. A normal comment might be.
 
# Variable is used in fstrings and must be a float 
cart_subtotal = float(item_1_Subtotal)

print()
print()
print()

print(f"Your cart currently has {item_1_Quantity} of {item_1_Name}, at a price of ${item_1_Price:.2f} each. ")
print(f"Your current cart subtotal including tax is ${cart_subtotal:.2f}")


print()
print()
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

###############################################################################
# Item 2
###############################################################################

item_2_Name = input("Please enter the name of your second item: ")
item_2_Quantity = int(input("Please enter the quantity of that item: "))
item_2_Price = float(input("Please enter the price of that item: $"))
item_2_Cost = item_2_Price * item_2_Quantity
item_2_Subtotal = (item_2_Cost * 0.05) + item_2_Cost

# Variable is used in fstrings and must be a float 
cart_subtotal = float(item_1_Subtotal + item_2_Subtotal)

print()
print()
print()

print(f"Your cart currently has {item_1_Quantity} of {item_1_Name}, at a price of ${item_1_Price:.2f} each, and ")
print(f"{item_2_Quantity} of {item_2_Name}, at a price of ${item_2_Price:.2f} each.")
print(f"Your current cart subtotal including tax is ${cart_subtotal:.2f}")


print()
print()
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

###############################################################################
# Item 3
###############################################################################

item_3_Name = input("Please enter the name of your third item: ")
item_3_Quantity = int(input("Please enter the quantity of that item: "))
item_3_Price = float(input("Please enter the price of that item: $"))
item_3_Cost = item_3_Price * item_3_Quantity
item_3_Subtotal = (item_3_Cost * 0.05) + item_3_Cost

# Variable is used in fstrings and must be a float 
cart_subtotal = float(item_1_Subtotal + item_2_Subtotal + item_3_Subtotal)

print()
print()
print()

print(f"Your cart is now full.")
print(f"Your final total including tax is ${cart_subtotal:.2f}")
print()
print()
print("You bought the following items.")
print(f"Item 1: {item_1_Quantity} {item_1_Name}, at ${item_1_Cost:.2f}")
print(f"Item 2: {item_2_Quantity} {item_2_Name}, at ${item_2_Cost:.2f}")
print(f"Item 1: {item_3_Quantity} {item_3_Name}, at ${item_3_Cost:.2f}")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

###############################################################################
# Reciept
###############################################################################


print()
print()
print()
print('''
             Have a Fintastic day!


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠄⠀⠀⠀⣠⡶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⢤⠀⢤⠹⡌⠃⠀⠂⠀⠀⠀⠀⠀⠀⣠⠃⠘⣇⠀⠀⠁⠈⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠳⠼⠃⠢⠦⠙⠙⠀⠀⠀⠀⠀⢀⣤⠖⡧⠐⠚⠙⠳⠤⢀⢀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣄⣄⡀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢠⣾⠫⠇⠀⠀⠰⠒⠂⠀⠀⠈⠒⣭⣿⡧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⡅⠐⠐⠻⠶⠶⠖⠋⣉⡿⠃⠀⠀⠀⠀⠹⢿⣇⣆⣀⣠⡀⠔⢾⣿⠋⠈⠙⢝⣾⠿⢹⣟⢶⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⢧⡀⠀⠄⢠⣆⣌⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢆⠀⢱⠀⠀⠀⠀⠈⠀⠀⠉⢺⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⣇⢀⠀⠉⠳⠷⣿⣦⣤⣴⣶⡄⠀⣀⠀⠀⡀⣠⣄⣀⣀⡙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠓⣀⠤⣤⡀⠀⠀⢀⠀⣀
⠀⠀⠀⡏⠘⣻⣷⠶⠶⣲⣬⣬⣥⣤⠄⣀⣤⠼⠟⠋⠉⠁⠀⠉⠉⠟⠛⠻⢶⣤⡀⠀⠀⠀⡀⢤⣄⠀⠀⠉⠚⠛⠓⠒⠟⠋⠀
⠀⠀⠀⣿⣷⠋⠀⠀⠀⠀⠀⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠢⡀⠀⠙⠙⠊⠠⠲⣢⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣁⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠀⠀⠀⠀⠤⠳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')