#guess_2.py
#let the user know how close they were with their guess
#Author: Faolán Hamilton

#attempt 1 = number_to_guess = 32

import random

number_to_guess = random.randint (1,50)

guess = int(input("Please guess the number (hint: it is a whole, positive number between 1-49): "))
while guess != number_to_guess:
    if guess <0 or guess >50:
        print ("Please enter a whole, positive number")
    
    elif guess < number_to_guess:
        print ("Incorrect, too low!")


    elif guess > number_to_guess:
        print ("Incorrect, too high!")

    guess = int(input("Please guess again: "))

print ("Just right! Yes, the number was", number_to_guess)