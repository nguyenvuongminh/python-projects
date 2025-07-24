import random
## HAND DATA
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Indexing hands
hand = [rock, paper, scissors]

# Input the user's hand & print out
deal = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(hand[deal] + '\n')

# Generating the computer's hand & print out
res = random.randint(0,2)
print('Computer chose:\n')
print(hand[res] + "\n")

# Determining results
if deal == res: # Same hand
    print("You draw")
elif deal == 0: # If user deals a hammer
    if res == 1: # If the computer deals a paper
        print('You lose')
    elif res == 2: # If the computer deals scissors
        print('You win')
elif deal == 1: # If user deals a paper
    if res == 0: # If the computer deals a hammer
        print('You win')
    elif res == 2: # If the computer deals scissors
        print('You lose')
elif deal == 2: # If user deals scissors
    if res == 0: # If the computer deals a hammer
        print('You lose')
    elif res == 1: # If the computer deals a paper
        print('You win')
