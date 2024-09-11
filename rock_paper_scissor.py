import random

choices = ('r', 'p', 's')
while True:
    user_choice = input('Choose from (r/p/s): ')
    if user_choice not in choices:
        print("Enter a valid number")
    comp_choice = random.choices(choices)
    print(f'You chose {user_choice}')
    print(f'Computer chose {comp_choice}')

    if user_choice == comp_choice:
        print('Tie!')
    elif (user_choice == 'r' and comp_choice == 's') or (user_choice == 's' and comp_choice == 'p') or (user_choice == 'p' and comp_choice == 'r'):
        print('You win!')
    else:
        print('You lost')
    should_continue = input('Continue (y/n): ').lower()
    if should_continue == 'n':
        break
