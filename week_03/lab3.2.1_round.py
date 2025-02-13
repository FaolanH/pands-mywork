# lab3.2.1_round.py
# Built-in functions with numbers - take in a float and output an int rounded up or down
# Author: Faolán Hamilton

#round to the nearest even number, e.g. 4.5 rounds to 4 but 5.5. rounds to 6, approximation not accurate
number_to_round = float(input("Enter a float number, e.g. 3.5: "))
rounded_number = round(number_to_round)
print ('{} rounded is {}' .format (number_to_round, rounded_number))

#the quotes must be around the text you want displayed when printed