import random

#Creating the function for getting the computers input and it will returns either 'rock', 'paper', or 'scissors'
def get_computes_choice():


#random number between 1 and 3
    random_number = random.randint(1, 3)

#create a dictionary with 3 items and values being the tool
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}

#We are getting the corresponding value 
    computers_choice = options[random_number]

    return computers_choice

# Creating the function for getting the users input 
def get_user_input():
    user_input = input(f'Enter rock/paper/scissors: ')

    user_input = user_input.lower()

    return user_input

# creating the function for getting the results of the computers and users picks
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


# Start the code with getting the computers pick calling the get_computer_choice function
computer_pick = get_computes_choice()

# Run the code until we have a valid pick from the user using the get_user_input function
while True:
    users_pick = get_user_input()
    if users_pick in ['rock', 'paper', 'scissors']:
        break 

# This will call the get_results function and compare the computer and users choice to see who wins
result = get_result(users_pick, computer_pick)


# print the computers and users inputs and print who the winner is. 
print(f"Computer's pick: {computer_pick}")
print(f'Your pick: {users_pick}')
print(f'You {result}')

