#!/usr/bin/python3

from random import *

print('Do you want to play a game? Type Y for yes/Type N for no')

yesOrNo = input()

guess_taken = 0

random_number = (randint(1, 10))
#random_number = str(5)

if yesOrNo =='Y' or yesOrNo == 'y':
    print('Try and find the random number between 1 and 10')
    print('You only have 3 guesses')

    while guess_taken < 3:

        guess = int(input('Enter your guess now: '))

        guess_taken = guess_taken + 1

        if guess > random_number:
            print('Your guess is too high.')

        if guess < random_number:
            print('Your guess is too low.')

        if guess == random_number:
            break


    if guess == random_number:
        print('You did it! The correct number was: '+ str(random_number))

    if guess != random_number:
        print('Sorry, you ran out guesses. The random number was: '+str(random_number))

elif yesOrNo =='N' or yesOrNo == 'n':
    print('Okay, have a nice day!')

else:
    print('You entered something other than Y or N. This game is ending.')


