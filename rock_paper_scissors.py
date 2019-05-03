from random import randint

RPS_LIST = ["ROCK", "PAPER", "SCISSORS"]
CHOICES_DICT = {"R": "ROCK", "P": "PAPER", "S": "SCISSORS"}
user_name = input("Please enter your name:")

QT_MSG = 'It was nice beating you'
WTF_MSG = 'WTF Dude...'

while True:
    
    user_choice = input("\nHey " + user_name + ", please choose R, P, or S:").upper()
    
    if user_choice not in CHOICES_DICT:
        print(WTF_MSG)
        continue

    if user_choice == 'Q':
        print(QT_MSG)
        exit()

  
    user_choice = CHOICES_DICT[user_choice]
    cpu_choice = RPS_LIST[randint(0, 2)]

    print('You chose "' + user_choice + '" and the computer chose "' + cpu_choice + '"\n')

    if user_choice == cpu_choice:
        print('{} Ties!'.format(user_name))

    elif (user_choice == 'ROCK' and cpu_choice == 'SCISSORS') or \
    	(user_choice == 'PAPER' and cpu_choice == 'ROCK') or \
    	(user_choice == 'SCISSORS' and cpu_choice == 'PAPER'):
        print('{} Wins!'.format(user_name))
        
      
    elif (user_choice == 'ROCK' and cpu_choice == 'PAPER') or \
    	(user_choice == 'PAPER' and cpu_choice == 'SCISSORS') or \
    	(user_choice == 'SCISSORS' and cpu_choice == 'ROCK'):
      	print('{} Loses!'.format(user_name))
      	
        
      
        
      
        
        
       
