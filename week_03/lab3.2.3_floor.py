# lab3.2.3_floor.py
# floors a number - takes a float and outputs an int rounded number 
# Author: Faolán Hamilton

#the difference between this function, and the previous absolute is this one allows for negative number 
#output, and will round to a whole number whereas absolute will output decimal places


import math

number_to_floor = float(input("Enter a float number, e.g. 3.5: "))
floored_number = math.floor (number_to_floor)
print ('{} floored is {}' .format (number_to_floor, floored_number))

