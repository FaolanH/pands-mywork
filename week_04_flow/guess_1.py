#guess_1.py 
#prompt user to guess a number, the program should keep prompting until correct
#Author: Faolán Hamilton

number_to_guess = 32

guess = int(input("Please guess the number (hint: it is whole/positive): "))
while guess != number_to_guess:
    print ("Incorrect!")
    guess = int(input("Please guess again: "))

print ("Correct! The number was", number_to_guess)