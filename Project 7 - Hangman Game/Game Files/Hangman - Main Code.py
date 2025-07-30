### Importing files
import hangman_art
import hangman_words
import random

### Opening banner & introduction
print(hangman_art.logo)
print('Welcome to hangman!')

### Selecting a word, generate blanks & an array for the word (for comparing purpose)
word_list = hangman_words.word_list
word_index = random.randint(0,len(word_list)-1)
word = word_list[word_index] # The word

word_array = list(word) # Word array

blank = [] # Generating the blanks
for i in range(0,len(word)):
    blank.append('_')

### Printing the blanks
print(''.join(blank))
life_count = 7

### The loop
while life_count > 0:
    answer = 'wrong'
    guess = input('Please guess a letter:\n')
    # Comparing the guessed letter to the word's letters
    for i in word_array:
        if guess == i:
            index = word_array.index(i) # Since Python counts from 0.
            blank[index] = guess
            answer = 'correct'

    # Correct case
    if answer == 'correct':
        if life_count < 7:
            print(hangman_art.stages[life_count])
        print('Correct guess.\n')
        print(f'Remaining lives: {life_count}/7')
        print(''.join(blank))

    # Wrong case
    else:
        life_count -= 1
        print(hangman_art.stages[life_count])
        print('Wrong guess.\n')
        print(f'Remaining lives: {life_count}/7')
        print(''.join(blank))

    # Winning case
    if blank == word_array:
        print("YOU WON THE GAME! YOU SAVED A MAN FROM DYING!")

    # Losing case
    if life_count == 0:
        print('Oh dear. You lost.')
        print(f'The correct word is {word}')