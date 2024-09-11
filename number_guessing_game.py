
import random


random_number = random.randint(1, 50)
while True:
    try:
        guess = int(input('Enter a number between 1 and 50 > '))
        if guess == random_number:
            print("Congratulations you guessed the number")
            break
        elif guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    except ValueError:
        print("Enter a valid number")
