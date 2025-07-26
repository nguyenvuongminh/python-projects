### NOTES ###
# Description: This code ask the user for the number of letters, numbers, and symbol
# they want in their passcode. It will then generate a passcode fulfilling such conditions,
# with the characters arranged randomly.
# Written by Minh Nguyen.
#********************************************************************#
### CHARACTERS DATABASE ###
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

### WELCOME STATEMENTS & USERS INPUT ###
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### MAIN CODE ###
import random

password = []
# This will add the required numbers of letters, numbers, and symbol (each selected randomly) to the password array
for letter in range(1, nr_letters + 1):
    letter_index = random.randint(0,len(letters)-1)
    password.append(letters[letter_index])
for number in range(1, nr_numbers + 1):
    number_index = random.randint(0, len(numbers)-1)
    password.append(numbers[number_index])
for symbol in range(1, nr_symbols + 1):
    symbol_index = random.randint(0,len(symbols)-1)
    password.append(symbols[symbol_index])

# This will shuffle the password array so that the characters are arranged randomly
random.shuffle(password)

print(''.join(password)) # This will print the password array as a spaceless string

