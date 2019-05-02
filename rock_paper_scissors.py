from random import randint
from sys import exit

RPS_LIST = ["rock", "paper", "scissors"]
CHOICES_DICT = {"r": "rock", "p": "paper", "s": "scissors", "q": "quit"}
USER_NAME = input("Type Players Name:")

while True:
    raw_user_choice = input("\n\n Hey " + USER_NAME + ", please choose r, p, or s:")

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
        print('Tie!\n')

    elif user_choice == 'rock' and cpu_choice == 'scissors':
        print('You Win!\n')

    elif user_choice == 'rock' and cpu_choice == 'paper':
        print('You Lose!\n')

    elif user_choice == 'paper' and cpu_choice == 'rock':
        print('You Win!\n')

    elif user_choice == 'paper' and cpu_choice == 'scissors':
        print('You Lose!\n')

    elif user_choice == 'scissors' and cpu_choice == 'rock':
        print('You Lose!\n')

    elif user_choice == 'scissors' and cpu_choice == 'paper':
        print('You Win!\n')
