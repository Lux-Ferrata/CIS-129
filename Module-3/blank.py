# Kevin Fanning
# CIS129
# 05 Oct 2026
# In class activity


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Welcome to a basic Caesar Cipher program!")

while True:
    print("Do you want to (E)encrypt or (D)ecrypt")
    response = input().lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'dycrypt'
        break
    print("Please enter the letter e or d, nothing else.")

while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input().upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print("TEST: can we get to this point?") # TODO: Delete this test print.

print("Enter the message to {}.".format(mode))
message = input().upper()
translated = ""