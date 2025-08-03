### NOTES
# Description: This code will be able to:
# - Encrypt a code, with the shifting number be user's input
# - Decrypt a code, with the shifting number ber the user's input
# - Future devs: Add user interface, add response for invalid cases.
# Written by Minh Nguyen, August 1st, 2025.
###****************************************************************

### ALPHABET
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

switch = 'ON'

### ENCRYPTING FUNCTION
def encrypt(alphabet, original_code, shifting_number, final_code):
    for letter in original_code:
        index = alphabet.index(letter)
        if (index + shifting_number) > 26:
            new_letter = alphabet[index + shifting_number - 26]
        else:
            new_letter = alphabet[index + shifting_number - 26]
        final_code.append(new_letter)

### DECRYPTING FUNCTION
def decrypt(alphabet, original_code, shifting_number, final_code):
    for letter in original_code:
        index = alphabet.index(letter)
        new_letter = alphabet[index - shifting_number]
        final_code.append(new_letter)

### THE LOOP
while switch == 'ON':
    selection = input('What do you want to do, encrypt or decrypt?\n')
    code = input('Please enter your code:\n')
    original_code = list(code)
    final_code = []
    shifting_number = int(input('Please enter your desired shifting number:\n'))

    if selection == 'encrypt':
        encrypt(alphabet, original_code, shifting_number, final_code)
        print(''.join(final_code))
    elif selection == 'decrypt':
        decrypt(alphabet, original_code, shifting_number, final_code)
        print(''.join(final_code))

    resume = input('Do you want to continue? Please type "yes" or "no".\n')

    if resume == 'yes':
        switch = 'ON'
    else:
        print('Thanks for using the tool!')
        switch = 'OFF'





