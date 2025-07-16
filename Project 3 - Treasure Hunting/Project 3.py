print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You stopped by a crossroad. Which direction do you want to go?\nType "left" or "right"\n')
if direction == 'left':
    print('As you turned left, you definitely did not fall into any booby trap, or any hole.\n')
    print('After a few long hours, you stopped in front of a huge castle. An old man walked by and whisper in your ear:\n')
    print('"The castle is just a poor decoy. The treasure actually lies under the lake over there."\n')
    action = input("Would you swim down the lake, give it a minute to think, or do anything else? Type 'swim' or 'wait'.\n")
    if action == 'wait':
        print('After waiting, you saw a bunch of trout underneath the lake. You choose not to swim, but to pick a door.')
        door = input('There are three doors: red, yellow, and blue. Which one would you choose?\n')
        if door == 'Yellow':
            print('You found the treasure! You win!')
        else:
            print('Behind the door, there is a giant troll. If you think this is not game over, tell it to the car-sized club the troll is holding.')
            print('Better luck next time!')
    else:
        print('You are attacked by a bunch of trout the moment you touched the water.\n')
        print("If this doesn't kill you, I don't know what would. Better luck next time!")
else:
    print('As you move forward in your chosen direction, you unknowingly stepped on a booby trap, which you have been avoiding. Luck is not on your side this time, though: You fell into the Hole of Despair!\n')
    print('Game over. Better luck next time!')

