### NOTES
# Description: This code will be able to:
# - Encrypt a code, with the shifting number be user's input
# - Decrypt a code, with the shifting number ber the user's input
# I'll probably code the back-end first.
# Written by Minh Nguyen, August 1st, 2025.
###****************************************************************

### SETUP
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
selection = input('What do you want to do, encrypt or decrypt?\n')
final_code = []

### ENCRYPTING FUNCTION
def encrypt(alphabet, original_code, shifting_number, final_code):
    for letter in original_code:
        index = original_code.index(letter)
        new_letter = alphabet[index + shifting_number]
        final_code.append(new_letter)

### DECRYPTING FUNCTION
def encrypt(alphabet, original_code, shifting_number, final_code):
    for letter in original_code:
        index = original_code.index(letter)
        new_letter = alphabet[index + shifting_number]
        final_code.append(new_letter)

### ENCRYPTING CASE
code = input('Please enter your code:\n')
original_code = list(code)
shifting_number = int(input('Please enter your desired shifting number:\n'))


