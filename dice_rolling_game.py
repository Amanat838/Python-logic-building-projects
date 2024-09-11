import random


counter = 0
while True:

    choice = input('Roll the dice (y/n)').lower()
    if counter >= 5:
        print("Maximum attempts")
        break
    if choice == 'y':
        random_numbers = (random.randint(1, 6), random.randint(1, 6))
        print(random_numbers)
        counter = counter+1
    elif choice == 'n':
        print("Exiting the game")
        break
    else:
        print("Press y to start the game")
