import random

#returns eiter 'rock', 'paper', or 'scissors'
def get_computes_choice():


#random numer between 1 and 3
    random_number = random.randint(1, 3)

#create a dictionary with 3 items and valuses being the tool
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}

#We are getting the corresponding value 
    computers_choice = options[random_number]

    return computers_choice

def get_user_input():
    user_input = input(f'Enter rock/paper/scissors: ')

    user_input = user_input.lower()

    return user_input

def get_result(user_pick, computer_pick):

    if computer_pick == user_pick:
        return 'draw'

    elif user_pick == 'paper' and computer_pick == 'rock':
        return 'win'

    elif user_pick == 'rock' and computer_pick == 'scissors':
        return 'win'

    elif user_pick == 'scissors' and computer_pick == 'paper':
        return 'win'

    else:
        return 'lose'



computer_pick = get_computes_choice()
while True:
    users_pick = get_user_input()
    if users_pick in ['rock', 'paper', 'scissors']:
        break 
result = get_result(users_pick, computer_pick)

print(f"Computer's pick: {computer_pick}")
print(f'Your pick: {users_pick}')
print(f'You {result}')

