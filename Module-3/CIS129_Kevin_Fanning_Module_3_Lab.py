###########################################################################
###### ASCII is only being used due to the limited audiance. ##############
###########################################################################


###########################################################################
###### Introductory Sequence
###########################################################################

# Instantiating some variables and displaying a welcome screen and
# the item menu. early_End controls wether the the final screen
# shows the receipt or an error message.

early_End = False

first_Item_Number = None
first_Item_Quantity = None
first_Item_Sub_Total = None

second_Item_Number = None
second_Item_Quantity = None
second_Item_Sub_Total = None

third_Item_Number = None
third_Item_Quantity = None
third_Item_Sub_Total = None

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
''')

print()

print('''
Welcome to the the Fintastic Commissary!

You may choose from the following items.

Item                     Price
---------------------------------------
- 1. Lemon               $5.50
- 2. Lime                $6.00
- 3. Orange              $0.50
- 4. Grapefruit          $3.00
- 5. Citron              $9.00
---------------------------------------
''')

item_1_Price = 5.50
item_2_Price = 6.00
item_3_Price = 0.50
item_4_Price = 3.00
item_5_Price = 9.00


###########################################################################
### Core Program loop based on item number
###########################################################################

# I wrapped the whole program in a if statement so that the user is
# prompted for the appropriate number of items. The menus for two and
# three items are copies of the menus for 1 with simple variable name
# changes, so I will mostly annotate the 1 item menu with only key
# differences noted in the others.

number_Of_Items = int(input("How many items would you like to buy?\n1 - 3: "))

###########################################################################
###### One Item Menu
###########################################################################

if number_Of_Items == 1:
    print("1 items")
    print()

    first_Item_Number = int(input("What item number would you like? "))
    first_Item_Quantity = int(input("How many of that item would you like? "))
    print()

# This if statement is just so the user get a well formatted sub-total
# with a english name instead of just an item number. I thought it
# added a lot to useability to be able to easily confirm that you
# added the correct item.

    if first_Item_Number == 1:
        first_Item_Sub_Total = item_1_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 2:
        first_Item_Sub_Total = item_2_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Lime(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 3:
        first_Item_Sub_Total = item_3_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 4:
        first_Item_Sub_Total = item_4_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    else:
        first_Item_Sub_Total = item_5_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

###########################################################################
###### Two Items Menu
###########################################################################

elif number_Of_Items == 2:
    print("2 items")

    first_Item_Number = int(input("What item number would you like? "))
    first_Item_Quantity = int(input("How many of that item would you like? "))
    print()

    if first_Item_Number == 1:
        first_Item_Sub_Total = item_1_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 2:
        first_Item_Sub_Total = item_2_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Limes(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 3:
        first_Item_Sub_Total = item_3_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 4:
        first_Item_Sub_Total = item_4_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    else:
        first_Item_Sub_Total = item_5_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

# The only real difference here is that I am adding the previous
# subtotal amount to the new items. Same applies for the three
# item menu.

    second_Item_Number = int(input("What item number would you like? "))
    second_Item_Quantity = int(input("How many of that item would you like? "))
    print()

    if second_Item_Number == 1:
        second_Item_Sub_Total = item_1_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 2:
        second_Item_Sub_Total = item_2_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Lime(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 3:
        second_Item_Sub_Total = item_3_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 4:
        second_Item_Sub_Total = item_4_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    else:
        second_Item_Sub_Total = item_5_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

###########################################################################
###### Three Items Menu
###########################################################################

elif number_Of_Items == 3:
    print("3 items")

    first_Item_Number = int(input("What item number would you like? "))
    first_Item_Quantity = int(input("How many of that item would you like? "))
    print()

    if first_Item_Number == 1:
        first_Item_Sub_Total = item_1_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 2:
        first_Item_Sub_Total = item_2_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Limes(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 3:
        first_Item_Sub_Total = item_3_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    elif first_Item_Number == 4:
        first_Item_Sub_Total = item_4_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    else:
        first_Item_Sub_Total = item_5_Price * first_Item_Quantity

        print(f"You have added {first_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${first_Item_Sub_Total:.2f}")
        print()

    second_Item_Number = int(input("What item number would you like? "))
    second_Item_Quantity = int(input("How many of that item would you like? "))
    print()

    if second_Item_Number == 1:
        second_Item_Sub_Total = item_1_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 2:
        second_Item_Sub_Total = item_2_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Lime(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 3:
        second_Item_Sub_Total = item_3_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    elif second_Item_Number == 4:
        second_Item_Sub_Total = item_4_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    else:
        second_Item_Sub_Total = item_5_Price * second_Item_Quantity

        print(f"You have added {second_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total):.2f}")
        print()

    third_Item_Number = int(input("What item number would you like? "))
    third_Item_Quantity = int(input("How many of that item would you like? "))
    print()

    if third_Item_Number == 1:
        third_Item_Sub_Total = item_1_Price * third_Item_Quantity

        print(f"You have added {third_Item_Quantity} Lemon(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total):.2f}")
        print()

    elif third_Item_Number == 2:
        third_Item_Sub_Total = item_2_Price * third_Item_Quantity

        print(f"You have added {third_Item_Quantity} Lime(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total):.2f}")
        print()

    elif third_Item_Number == 3:
        third_Item_Sub_Total = item_3_Price * third_Item_Quantity

        print(f"You have added {third_Item_Quantity} Orange(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total):.2f}")
        print()

    elif third_Item_Number == 4:
        third_Item_Sub_Total = item_4_Price * third_Item_Quantity

        print(f"You have added {third_Item_Quantity} Grapefruit(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total):.2f}")
        print()

    else:
        third_Item_Sub_Total = item_5_Price * third_Item_Quantity

        print(f"You have added {third_Item_Quantity} Citron(s) to your cart.")
        print(f"Your current subtotal is ${(first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total):.2f}")
        print()


else:

# I felt pretty happy about this use of early_End. I know its simple, but
# being able to skip the receipt screen when the user enter an invalid
# item number really made this feel a bit more like an actual program
# to me instead of just a script.

    early_End = True
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠋⠉⠉⠙⠻⢿⣿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⠻⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣷⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣠⣤⣶⣶⣾⣿⣿⣿⢿⣿⣷⣦⣄⠀⠀⠙⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡿⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⠿⠛⠛⣏⠉⠉⢻⡄⠀⢹⠉⠛⣿⣧⡀⠀⠈⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠁⠀⠀⠀⢀⣤⣾⣿⣿⠿⠋⠉⣿⡀⠀⠀⢸⣦⠀⢸⣷⠀⢸⣧⠀⣿⠙⣿⡄⠀⠈⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠃⠀⠀⢀⣴⣿⣿⡿⠋⠹⣦⡀⠀⢿⣿⣆⠀⣿⣿⣇⣿⣿⣦⣿⣿⣄⣿⡇⣿⢻⡀⠀⠘⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⢠⣿⣿⠟⠁⢢⡀⠀⣿⣿⣦⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⢀⣧⠀⠀⢹⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⣾⣿⠛⣆⠀⠘⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⣿⡇⠀⠹⣿⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠈⢿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⢿⡗⣦⣄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⢸⣇⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠻⢿⣿⡷⠈⢿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣧⠀⠀⢿⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢻⣿⣿⡇⠀⠀⢻⠇⠀⠀⢿⠙⡟⢻⣉⡿⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡀⠀⠈⢷⣽⣿⣿⣿⣿⣿⣿⡏⠻⣿⣿⠀⠀⠙⢿⣇⣀⣤⣬⣤⣤⣤⡤⠶⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣧⠀⠈⠙⠂⣠⣴⠿⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠘⣿⣿⣿⣿⡌⠛⠆⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠹⣿⡻⢄⣙⡴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠚⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣷⣮⣛⠿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡀⠀
⠀⠀⠀⢀⣀⣠⣶⣾⣿⡿⠿⠛⠿⢿⣿⣿⣷⣾⣥⣄⣀⣀⣀⣀⣀⣀⠀⢀⣠⣶⣄⡀⢤⣀⣀⣀⣀⣤⣴⣶⣿⣿⣿⣿⠿⢿⣿⣿⣿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀
⠈⠉⠉⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⠛⣉⣤⣾⣿⣿⣿⣿⣿⣦⣀⠉⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠉⠛⠻⠿⠿⢿⣿⣿⣿⣶⣶⣶⣶⠶⠶⠶⠚⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⣿⣿⣿⠿⠛⠉⠉⠛⠻⢿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠴⠶⠿⠿⠿⠛⠛⠋⠉⠀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠶⢶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    print("Invalid number of items")


###########################################################################
###### Final Receipt Section
###########################################################################

# I actually had a lot of trouble with this section, getting the
# receipt to only print as many lines as I actually used was a bit
# frustrating. But the if not None sequence was a pretty good fix.
# it only shows how the line if the line was given a non-None value

if early_End is False:
    print('''
Item                                  Price
---------------------------------------------
- 1. Lemon                            $5.50
- 2. Lime                             $6.00
- 3. Orange                           $0.50
- 4. Grapefruit                       $3.00
- 5. Citron                           $9.00
---------------------------------------------
    ''')
    print()
    print("Your final recipt.")
    print("Item Number        Quantity         Sub Total")
    print("---------------------------------------------")
    if first_Item_Number is not None:
        print(f"-  {first_Item_Number}                  {first_Item_Quantity}               ${first_Item_Sub_Total:.2f}")
    if second_Item_Number is not None:
        print(f"-  {second_Item_Number}                  {second_Item_Quantity}               ${second_Item_Sub_Total:.2f}")
    if third_Item_Number is not None:
        print(f"-  {third_Item_Number}                  {third_Item_Quantity}               ${third_Item_Sub_Total:.2f}")
    print()
    print()

    if third_Item_Number is not None:
        tax_added = ((first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total) * 0.05)
    elif second_Item_Number is not None:
        tax_added = ((first_Item_Sub_Total + second_Item_Sub_Total) * 0.05)
    else:
        tax_added = (first_Item_Sub_Total * 0.05)

    print(f"Total Tax:                            ${tax_added:.2f}")

    if third_Item_Number is not None:
        final_Total = (first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total + ((first_Item_Sub_Total + second_Item_Sub_Total + third_Item_Sub_Total) * 0.05))
    elif second_Item_Number is not None:
        final_Total = (first_Item_Sub_Total + second_Item_Sub_Total + ((first_Item_Sub_Total + second_Item_Sub_Total) * 0.05))
    else:
        final_Total = (first_Item_Sub_Total +(first_Item_Sub_Total * 0.05))

    print(f"Final Total:                          ${final_Total:.2f}")

else:
    pass





