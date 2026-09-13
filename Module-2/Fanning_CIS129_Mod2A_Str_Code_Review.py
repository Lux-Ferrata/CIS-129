## The Original program's "upper" string method was missing its parensthesis.

username = "ada_lovelace"
print(f"Welcome, {username.upper()}!")

#############################################################################

## The original program, correctly used the "strip" string method. But then
## did not assign the output of that method to a variable. So the original
## unlcleaned input was still being passed to the print function.

# The cleaned username should print with no surrounding spaces: >ada<
raw_username = "   ada   "

cleaned_username = raw_username.strip()

print(f">{cleaned_username}<")

#############################################################################

## The orginal program had used single quotes to surround the string, and
## included a single quoute in the string. This resulted in only the word
## "it" being quouted properly. The most pythonic way to fix this is to use
## double quotes, though you could also have escaped the interior single quote

message = "It's a great day to learn Python"
print(message)

