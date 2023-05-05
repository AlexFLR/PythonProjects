import random


def guess_the_number(x):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number:
                 guess = int(input(f'Guess a numver between 1 and {x}: '))
                 if guess < random_number:
                         print('Sorry, guess again.Too low.')
                 elif guess > random_number:
                         print('Sorry, guess again.Too high.')

        print(f'U have guessed.The number was  {random_number} indeed.')        

range = int(input('What guess range do u want?'))

guess_the_number(range)


        