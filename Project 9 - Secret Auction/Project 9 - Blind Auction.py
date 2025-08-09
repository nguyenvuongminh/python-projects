logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo + '\n')
other = 'yes'

bids = {}
highest_bid = 0

while other == 'yes':
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    other = input('Is there any other bidder? Type "yes" or "no". ')

    bids[name] = price

    if other == 'yes':
        print('\n'* 20)
    elif other == 'no':
        break

for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name

print(f'Congratulation {highest_bidder}! You have won the secret auction!')



