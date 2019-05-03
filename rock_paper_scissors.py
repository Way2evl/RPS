from random import randint
from sys import exit

RPS_LIST = ["rock", "paper", "scissors"]
CHOICES_DICT = {"r": "rock", "p": "paper", "s": "scissors", "q": "quit"}
user_name = input("Please enter your name:")

while True:
    raw_user_choice = input("\n\n Hey " + user_name + ", please choose r, p, or s:")

    # let them quit
    if raw_user_choice == 'q':
        print('It was nice beating you')
        exit()
    
    if raw_user_choice not in CHOICES_DICT:
        print("WTF dude...\n\n")
        continue
        
    user_choice = CHOICES_DICT[raw_user_choice]  # r -> rock
    cpu_choice = RPS_LIST[randint(0, 2)]    # 0 -> rock

    print('You chose "' + user_choice + '" and the computer chose "' + cpu_choice + '"')

    if user_choice == cpu_choice:
        print('{} Ties!'.format(user_name))

    elif (user_choice == 'rock' and cpu_choice == 'scissors') or \
    	(user_choice == 'paper' and cpu_choice == 'rock') or \
    	(user_choice == 'scissors' and cpu_choice == 'paper'):
        print('{} Wins!'.format(user_name))
      
    elif (user_choice == 'rock' and cpu_choice == 'paper') or \
    	(user_choice == 'paper' and cpu_choice == 'scissors') or \
    	(user_choice == 'scissors' and cpu_choice == 'rock'):
      	print('{} Loses!'.format(user_name))
