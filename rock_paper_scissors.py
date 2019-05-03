from random import randint

ROCK = 'Rock'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
RPS_LIST = [ROCK, PAPER, SCISSORS]
CHOICES_DICT = {"R": ROCK, "P": PAPER, "S": SCISSORS}

# UI elements
user_name = input("Please enter your name:")
QT_MSG = 'It was nice beating you'
WTF_MSG = 'WTF Dude...'
CHOOSE_MSG = "\nHey {}, please choose R, P, or S:"
CHOSE_MSG = 'You chose "{}" and the computer chose "{}"\n'
WIN_MSG = '{} Wins!'
LOSE_MSG = '{} Loses!'
TIE_MSG = '{} Ties!'


while True:

    user_choice = input(CHOOSE_MSG.format(user_name)).upper()

    if user_choice == 'Q':
        print(QT_MSG)
        exit()

    if user_choice not in CHOICES_DICT:
        print(WTF_MSG)
        continue

    user_choice = CHOICES_DICT[user_choice]
    cpu_choice = RPS_LIST[randint(0, 2)]  

    print(CHOSE_MSG.format(user_choice, cpu_choice))
    if user_choice == cpu_choice:
        print(TIE_MSG.format(user_name))

    elif ((user_choice == ROCK and cpu_choice == SCISSORS) or
          (user_choice == PAPER and cpu_choice == ROCK) or
          (user_choice == SCISSORS and cpu_choice == PAPER)):
        print(WIN_MSG.format(user_name))

    elif ((user_choice == ROCK and cpu_choice == PAPER) or
          (user_choice == PAPER and cpu_choice == SCISSORS) or
          (usr_choice == SCISSORS and cpu_choice == ROCK)):
      	print(LOSE_MSG.format(user_name))
